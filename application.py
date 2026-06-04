from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

# host = "localhost"
# port = "5432"
# user = "postgres"
# password = "1234567890-=qwertyuiop[]"
# db = "main"

load_dotenv()

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DB = os.getenv("DB")

db_uri = f"postgresql+pg8000://{USER}:{PASSWORD}@{HOST}/{DB}"
# ????????? ???????????(engine)
engine = create_engine(db_uri)

# ????????? ?????(session) ?? ?????? ???????????(engine)
Session = sessionmaker(bind=engine)  # ???? ? ?????????? ??????????? ?? ???? ?????
session = Session()  # ????????? ?????

# ????????? ??????? ? ???? ?????

metadata = MetaData()
metadata.reflect(bind=engine)

tables = metadata.tables
print(list(tables.keys()))


def show_doctors_specializations(session):
    query = """
        SELECT d.surname, s.name
        FROM doctorsspecializations ds
        JOIN doctors d ON ds.doctorid = d.id
        JOIN specializations s ON ds.specializationid = s.id
    """

    result = session.execute(text(query))

    for row in result:
        print(row)


show_doctors_specializations(session)


def show_doctors_salaries(session):
    query = """
        SELECT d.surname,
               (d.salary + COALESCE(d.allowance, 0)) AS salary
        FROM doctors d
        WHERE d.on_vacation = FALSE
    """

    result = session.execute(text(query))

    for row in result:
        print(row)


def show_wards_by_department(session, department_id):
    query = """
        SELECT w.name
        FROM wards w
        WHERE w.departmentid = :department_id
    """

    result = session.execute(text(query), {"department_id": department_id})

    for row in result:
        print(row)


show_wards_by_department(session, 1)


def show_donations_by_month(session, month, year):
    query = """
        SELECT d.name,
               s.name,
               dn.amount,
               dn.date
        FROM donations dn
        JOIN departments d ON dn.departmentid = d.id
        JOIN sponsors s ON dn.sponsorid = s.id
        WHERE EXTRACT(MONTH FROM dn.date) = :month
          AND EXTRACT(YEAR FROM dn.date) = :year
    """

    result = session.execute(text(query), {"month": month, "year": year})

    for row in result:
        print(row)


show_donations_by_month(session, 6, 2026)

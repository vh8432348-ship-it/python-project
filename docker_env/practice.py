import time
from settings import settings

while True:
    print(f"app_name = {settings.app_name}", flush=True)
    print(f"filename = {settings.filename}", flush=True)
    print(f"login = {settings.login}", flush=True)
    print(f"password = {settings.password}", flush=True)
    print("-" * 30, flush=True)

    time.sleep(2)

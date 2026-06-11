from redis import Redis


class SocialApp:
    def __init__(self):
        self.server = Redis(
            host="localhost",
            port=6379,
            db=0,
            decode_responses=True,
        )
        self.current_user = None

    def _get_cred_key(self, user_name):
        return f"credential:{user_name}"

    def _get_info_key(self, user_name):
        return f"personal_info:{user_name}"

    def _get_friends_key(self, user_name):
        return f"friends:{user_name}"

    def _get_story_key(self, user_name, story_name):
        return f"story:{user_name}:{story_name}"

    def signup(self, user_name, password):
        key = self._get_cred_key(user_name)

        if self.server.exists(key):
            print("Користувач вже існує")
            return

        self.server.set(key, password)
        print("Користувача зареєстровано")

    def login(self, user_name, password):
        key = self._get_cred_key(user_name)

        if not self.server.exists(key):
            print("Користувача не існує")
            return

        true_password = self.server.get(key)

        if true_password != password:
            print("Невірний пароль")
            return

        self.current_user = user_name
        print("Вхід успішний")

    def add_info(self, name, age, city):
        if self.current_user is None:
            print("Не залогінено")
            return

        key = self._get_info_key(self.current_user)

        data = {"name": name, "age": age, "city": city}
        self.server.hset(key, mapping=data)

        print("Інформацію додано")

    def get_info(self):
        if self.current_user is None:
            print("Не залогінено")
            return

        key = self._get_info_key(self.current_user)
        print(self.server.hgetall(key))

    def add_friend(self, friend):
        if self.current_user is None:
            print("Не залогінено")
            return

        if not self.server.exists(self._get_cred_key(friend)):
            print("Користувача не знайдено")
            return

        self.server.sadd(self._get_friends_key(self.current_user), friend)
        self.server.sadd(self._get_friends_key(friend), self.current_user)

        print("Друг доданий")

    def get_friends(self):
        if self.current_user is None:
            print("Не залогінено")
            return

        print(self.server.smembers(self._get_friends_key(self.current_user)))

    def add_story(self, story_name, content):
        if self.current_user is None:
            print("Не залогінено")
            return

        key = self._get_story_key(self.current_user, story_name)

        if self.server.exists(key):
            print("Такий пост вже існує")
            return

        self.server.set(key, content)
        print("Пост додано")


class MuseumApp:
    def __init__(self):
        self.server = Redis(
            host="localhost",
            port=6379,
            db=0,
            decode_responses=True,
        )
        self.current_user = None

    def _get_cred_key(self, user_name):
        return f"credential:{user_name}"

    def _get_exhibit_key(self, exhibit_id):
        return f"exhibit:{exhibit_id}"

    def _get_people_key(self, person_id):
        return f"person:{person_id}"

    def _get_exhibit_people_key(self, exhibit_id):
        return f"exhibit_people:{exhibit_id}"

    def _get_person_exhibits_key(self, person_id):
        return f"person_exhibits:{person_id}"

    def signup(self, user_name, password):
        key = self._get_cred_key(user_name)

        if self.server.exists(key):
            print("Користувач існує")
            return

        self.server.set(key, password)
        print("Користувача створено")

    def login(self, user_name, password):
        key = self._get_cred_key(user_name)

        if not self.server.exists(key):
            print("Не знайдено")
            return

        if self.server.get(key) != password:
            print("Невірний пароль")
            return

        self.current_user = user_name
        print("Вхід успішний")

    def add_exhibit(self, exhibit_id, title, type_, description):
        key = self._get_exhibit_key(exhibit_id)

        if self.server.exists(key):
            print("Вже існує")
            return

        data = {"id": exhibit_id, "title": title, "type": type_, "description": description}
        self.server.hset(key, mapping=data)

        print("Експонат додано")

    def get_all_exhibits(self):
        print([self.server.hgetall(k) for k in self.server.keys("exhibit:*")])

    def add_person(self, person_id, name, role):
        key = self._get_people_key(person_id)

        data = {"id": person_id, "name": name, "role": role}
        self.server.hset(key, mapping=data)

        print("Людину додано")


    def link_person_to_exhibit(self, exhibit_id, person_id):
        self.server.sadd(self._get_exhibit_people_key(exhibit_id), person_id)
        self.server.sadd(self._get_person_exhibits_key(person_id), exhibit_id)

        print("Зв'язок створено")

    def get_books_only(self):
        print([
            self.server.hgetall(k)
            for k in self.server.keys("exhibit:*")
            if self.server.hgetall(k).get("type") == "book"
        ])


if __name__ == "__main__":
    # SOCIAL TEST
    social = SocialApp()
    social.signup("John", "123")
    social.login("John", "123")
    social.add_info("John Doe", 20, "Kyiv")
    social.add_friend("John")

    social.add_story("python", "Python is cool")


    museum = MuseumApp()
    museum.signup("admin", "123")
    museum.login("admin", "123")

    museum.add_exhibit(1, "Book", "book", "Great book")
    museum.add_person(1, "Tolstoy", "writer")
    museum.link_person_to_exhibit(1, 1)

    museum.get_all_exhibits()
    museum.get_books_only()
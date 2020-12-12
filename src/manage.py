from src.fetch import Fetcher
from src.controller import Controller
from src.parse import Parser


class Manager:
    def __init__(self):
        self.fetcher = Fetcher()
        self.controller = Controller()
        self.parser = Parser()
        self.register_user = self.controller.load_user()

    def update_user_info(self, name):
        user_history = self.fetcher.user_history(name)
        user = self.parser.from_user_history_to_user(user_history, name)
        if self.controller.load_user():
            self.controller.clear_table("user")
        self.controller.save_user(user)

    def update_contests_info(self):
        if self.controller.load_contests_info():
            self.controller.clear_table("contests_info")
        contests_info = self.fetcher.contests_information()
        self.controller.save_contests_info(contests_info)

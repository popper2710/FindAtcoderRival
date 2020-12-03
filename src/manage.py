from src.fetch import Fetcher
from src.controller import Controller
from src.parse import Parser


class Manager:
    def __init__(self):
        self.fetcher = Fetcher()
        self.controller = Controller()
        self.parser = Parser()

    def update_user_info(self, name):
        user_history = self.fetcher.user_history(name)
        user = self.parser.from_result_to_user(user_history[0])
        for result in user_history:
            user.add_contest_result(result)
        if self.controller.load_user():
            self.controller.clear_table("user")
        self.controller.save_user(user)

    def update_contests_info(self):
        if self.controller.load_contests_info():
            self.controller.clear_table("contests_info")
        contests_info = self.fetcher.contests_information()
        self.controller.save_contests_info(contests_info)

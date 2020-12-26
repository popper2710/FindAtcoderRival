from src.fetch import Fetcher
from src.controller import Controller
from src.parse import Parser

from collections import defaultdict


class Manager:
    def __init__(self):
        self.fetcher = Fetcher()
        self.controller = Controller()
        self.parser = Parser()
        self.register_user = self.controller.load_user()

    def find_rivals(self, rival_cond):
        if self.register_user is None:
            raise Exception("[ERROR] User is not registered")
        user_results = defaultdict(list)
        for contest_result in self.register_user.contest_results:
            contest_standing = self.fetcher.contest_standings(contest_result.contestName)
            for fetch_result in contest_standing:
                result = self.parser.from_result_to_result(fetch_result)
                user_results[result.username].append(result)

        for (_, v) in user_results:
            if self._eval_rival(v, rival_cond):
                user = self.parser.from_result_to_user(v[0])
                for result in v:
                    user.add_contest_result(result)
                self.controller.save_rivals(user)

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

    def _eval_rival(self, result):
        pass

from src.fetch import Fetcher
from src.controller import Controller
from src.parse import Parser
from src.rival_cond import RivalCond

from collections import defaultdict


class Manager:
    def __init__(self):
        self.fetcher = Fetcher()
        self.controller = Controller()
        self.parser = Parser()
        self.register_user = self.controller.load_user()
        self.rival_cond = RivalCond()

    def find_rivals(self):
        if self.register_user is None:
            raise Exception("[ERROR] User is not registered")
        user_results = defaultdict(list)
        for contest_result in self.register_user.contest_results:
            contest_standing = self.fetcher.contest_standings(contest_result.contestName)
            for fetch_result in contest_standing:
                result = self.parser.from_result_to_result(fetch_result)
                user_results[result.username].append(result)

        for (_, v) in user_results:
            if self._eval_rival(v):
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

    def set_rival_cond(self, rival_cond):
        self.rival_cond = rival_cond

    def _eval_rival(self, results):
        results.sort(key=lambda result: result.contest_start_time, reverse=True)
        rival_rate = results[0].new_rating
        if rival_rate < self.register_user.current_rating - self.rival_cond.lower_rate_limit \
                or rival_rate > self.register_user.current_rating + self.rival_cond.upper_rate_limit:
            return False

        for rival_result in results:
            for user_result in self.register_user.contest_results:
                if rival_result.contestName == user_result.contestName \
                    and not (- self.rival_cond.lower_rate_limit <= rival_result.ranking - user_result.ranking \
                             <= self.rival_cond.upper_rate_limit):
                    return False
        return True

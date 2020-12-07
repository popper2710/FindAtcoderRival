import datetime
from src import config


class User:
    username = ""
    current_rating = -1
    contest_results = []
    last_updated = datetime.datetime.now()

    def to_dict(self):
        return {
            "username": self.username,
            "current_rating": self.current_rating,
            "contest_results": {r.contest_name: r.to_dict() for r in self.contest_results},
            "last_updated": self.last_updated.strftime(config.DATE_FORMAT)
        }

    def add_contest_result(self, contest_result):
        if self.username == contest_result.username:
            self.contest_results.append(contest_result)
        else:
            raise ValueError("Invalid Argument: username is not equal")

    def update_current_rating(self):
        latest_contests = sorted(self.contest_results, key=lambda x: x.contest_start_time,reverse=True)
        for i in latest_contests:
            if i.new_lating > 0:
                self.current_rating = i.new_lating
                break

    def __eq__(self, other):
        return self.username == other.username and self.last_updated == other.last_updated

    def __ne__(self, other):
        return not self.__eq__(other)



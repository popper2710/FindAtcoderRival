import datetime

from src import config


class ContestResult:
    contestName = ""
    username = ""
    new_rating = -1
    contest_start_time = -1
    elapsed_time = -1

    def to_dict(self):
        return {
            "contestName": self.contestName,
            "username": self.username,
            "new_rating": self.new_rating,
            "start_time": self.contest_start_time,
            "elapsed_time": self.elapsed_time
        }

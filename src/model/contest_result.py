import datetime

from src import config


class ContestResult:
    contestName = ""
    username = ""
    new_rating = -1
    ranking = -1
    contest_start_time = -1
    elapsed_time = -1

    def to_dict(self):
        return {
            "contestName": self.contestName,
            "username": self.username,
            "new_rating": self.new_rating,
            "ranking": self.ranking,
            "contest_start_time": self.contest_start_time,
            "elapsed_time": self.elapsed_time
        }

    @staticmethod
    def from_dict(result_dict):
        result = ContestResult()
        result.contestName = result_dict["contestName"]
        result.username = result_dict["username"]
        result.new_rating = result_dict["new_rating"]
        result.ranking = result_dict["ranking"]
        result.contest_start_time = result_dict["contest_start_time"]
        result.elapsed_time = result_dict["elapsed_time"]
        return result

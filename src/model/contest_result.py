import datetime

from src import config


class ContestResult:
    contestName = ""
    performance = -1
    new_rating = -1
    end_time = datetime.datetime.now()

    def to_dict(self):
        return {
            "contestName": self.contestName,
            "performance": self.performance,
            "new_rating": self.new_rating,
            "end_time": self.end_time.strftime(config.DATE_FORMAT)
        }

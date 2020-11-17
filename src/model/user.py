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

    def __eq__(self, other):
        return self.username == other.username and self.last_updated == other.last_updated

    def __ne__(self, other):
        return not self.__eq__(other)



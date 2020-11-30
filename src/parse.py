from datetime import datetime

from src import model


class Parser:
    @staticmethod
    def from_result_to_user(fetch_result):
        user = model.User()
        user.username = fetch_result['UserScreenName']
        user.last_updated = datetime.now()
        return user

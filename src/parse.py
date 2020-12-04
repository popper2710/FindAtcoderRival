from datetime import datetime

from src import model, controller


class Parser:
    def __init__(self):
        contests_info = controller.Controller().load_contests_info()
        self.contests_info = {info['id']: info for info in contests_info}

    @staticmethod
    def from_result_to_user(fetch_result):
        user = model.User()
        user.username = fetch_result['UserScreenName']
        user.last_updated = datetime.now()
        return user

    def from_result_to_result(self, fetch_result):
        result = model.ContestResult()
        first_task = fetch_result['TaskResults'].keys()[0]
        result.contestName = first_task.rsplit("_", 1)[0]
        result.username = fetch_result['UserScreenName']
        result.new_rating = fetch_result["Rating"]
        result.contest_start_time = self.contests_info[result.contestName]
        result.elapsed_time = fetch_result["TotalResult"]["Elapsed"]
        return result


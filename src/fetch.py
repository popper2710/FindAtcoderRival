import sys

import requests


class Fetcher:
    def __init__(self):
        self.atcoder_url = "https://atcoder.jp"

    def contest_standings(self, contest_name: str):
        rank_url = f"{self.atcoder_url}/contests/{contest_name}/standings/json"
        res = requests.get(rank_url)
        return res.json()

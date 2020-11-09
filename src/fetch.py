import os
import pickle

import requests
from bs4 import BeautifulSoup


class Fetcher:
    def __init__(self):
        self.atcoder_url = "https://atcoder.jp"

    def contest_standings(self, contest_name: str):
        rank_url = f"{self.atcoder_url}/contests/{contest_name}/standings/json"
        headers = {"Content-Type": "application/json"}
        res = requests.get(rank_url, headers=headers)
        return res.json()

    def login(self, username: str, password: str):
        login_url = f"{self.atcoder_url}/login"
        client = requests.session()
        r = client.get(login_url)
        soup = BeautifulSoup(r.content, 'html.parser')
        csrf_token = soup.select_one('input[name="csrf_token"]')["value"]
        params = {"username": username,
                  "password": password,
                  "csrf_token": csrf_token}
        client.post(login_url, params=params)
        cookies = client.cookies
        if not os.path.exists("../data/config"):
            os.mkdir("../data/config")
        with open("../data/config/session.pkl", "wb") as f:
            pickle.dump(cookies, f)
        return True

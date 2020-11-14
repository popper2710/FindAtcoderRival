import os
import sys
import pickle

import requests
from bs4 import BeautifulSoup

from src import config


class Fetcher:
    def __init__(self):
        self.atcoder_url = "https://atcoder.jp"
        self.config_path = config.PROJECT_ROOT + "/data/config/"
        self.session_filename = "session.pkl"
        self.is_login = True
        if not self.__check_session():
            self.logout()
            self.is_login = False

    def contest_standings(self, contest_name: str):
        if not self.is_login:
            sys.stderr.write("[ERROR] please login to use")
            sys.exit(1)
        rank_url = f"{self.atcoder_url}/contests/{contest_name}/standings/json"
        headers = {"Content-Type": "application/json"}
        res = requests.get(rank_url, headers=headers, cookies=self.__load_cookies())
        return res.json()

    def login(self, username: str, password: str):
        if not self.is_login:
            return False

        login_url = f"{self.atcoder_url}/login"
        client = requests.session()
        r = client.get(login_url)
        params = {"username": username,
                  "password": password,
                  "csrf_token": self.__extract_csrf_token(r.content)}
        client.post(login_url, params=params)
        cookies = client.cookies
        self.__save_cookies(cookies)
        return True

    def __check_session(self):
        try:
            settings_url = f"{self.atcoder_url}/settings"
            r = requests.get(settings_url, cookies=self.__load_cookies())
            return r.status_code == 200

        except Exception:
            return False

    def logout(self):
        if not self.is_login:
            return False
        logout_path = self.atcoder_url + "/logout"
        client = requests.session()
        r = client.get(self.atcoder_url)
        params = {"csrf_token": self.__extract_csrf_token(r.content)}
        client.post(logout_path, params=params)
        os.remove(self.config_path + self.session_filename)
        return True

    def __load_cookies(self):
        with open(self.config_path + self.session_filename, "rb") as f:
            return pickle.load(f)

    def __save_cookies(self, cookies):
        if not os.path.exists(self.config_path):
            os.mkdir(self.config_path)
        with open(self.config_path + self.session_filename, "wb") as f:
            pickle.dump(cookies, f)

    @staticmethod
    def __extract_csrf_token(content):
        soup = BeautifulSoup(content, 'html.parser')
        csrf_token = soup.select_one('input[name="csrf_token"]')["value"]
        return csrf_token

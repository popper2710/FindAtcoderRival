import os
import pickle

import requests
from bs4 import BeautifulSoup

from src import config


class Fetcher:
    def __init__(self, username="", password=""):
        self.atcoder_url = "https://atcoder.jp"
        self.config_path = config.PROJECT_ROOT + "/data/config/"
        self.session_filename = "session.pkl"
        self.is_login = False
        if self.__check_session():
            self.is_login = True
        else:
            self.logout()
            if self.login(username, password):
                self.is_login = True

    def contest_standings(self, contest_name: str):
        rank_url = f"{self.atcoder_url}/contests/{contest_name}/standings/json"
        headers = {"Content-Type": "application/json"}
        res = requests.get(rank_url, headers=headers, cookies=self.__load_cookies())
        res_dict = res.json()
        res_dict["ContestName"] = contest_name
        return res_dict

    def user_history(self, username: str):
        history_url = f"{self.atcoder_url}/users/{username}/history/json"
        headers = {"Content-Type": "application/json"}
        res = requests.get(history_url, headers=headers)
        return res.json()

    @staticmethod
    def contests_information():
        atcoder_problems_url = "https://kenkoooo.com/atcoder/resources/contests.json"
        res = requests.get(atcoder_problems_url)
        return res.json()

    def login(self, username: str, password: str):
        if self.is_login:
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

    def logout(self):
        if not self.is_login:
            return False
        logout_path = self.atcoder_url + "/logout"
        client = requests.session()
        r = client.get(self.atcoder_url)
        params = {"csrf_token": self.__extract_csrf_token(r.content)}
        client.post(logout_path, params=params)
        if os.path.exists(self.config_path + self.session_filename):
            os.remove(self.config_path + self.session_filename)
        self.is_login = False
        return True

    def __load_cookies(self):
        with open(self.config_path + self.session_filename, "rb") as f:
            return pickle.load(f)

    def __save_cookies(self, cookies):
        if not os.path.exists(self.config_path):
            os.mkdir(self.config_path)
        with open(self.config_path + self.session_filename, "wb") as f:
            pickle.dump(cookies, f)

    def __check_session(self):
        try:
            if not os.path.exists(self.config_path + self.session_filename):
                return False
            settings_url = f"{self.atcoder_url}/settings"

            r = requests.get(settings_url, cookies=self.__load_cookies())
            return r.status_code == 200

        except Exception:
            return False

    @staticmethod
    def __extract_csrf_token(content):
        soup = BeautifulSoup(content, 'html.parser')
        csrf_token = soup.select_one('input[name="csrf_token"]')["value"]
        return csrf_token

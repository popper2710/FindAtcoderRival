import os

from tinydb import TinyDB, Query

from src import config

TABLE_LIST = ['rivals', 'user']


class Controller:
    def __init__(self):
        self.data_path = config.PROJECT_ROOT + "/data/"
        if not os.path.exists(self.data_path):
            os.mkdir(self.data_path)
        self. db = TinyDB(self.data_path + "db.json")
        self.table = dict()
        for table_name in TABLE_LIST:
            self.table["table_name"] = self.db.table(table_name)

    def save_rivals(self, rivals):
        self.table["rivals"].insert(rivals)

    def save_user(self, user):
        self.table["user"].insert(user)

    def load_rivals(self):
        query = Query()
        res = self.table["rivals"].search(query.rivals.exists())
        return res

    def load_user(self):
        query = Query()
        res = self.table["user"].search(query.user.exists())
        return res

    def clear_db(self):
        self.db.purge()







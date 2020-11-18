import os

from src import config


class Controller:
    def __init__(self):
        self.user_data_path = config.PROJECT_ROOT + "/data/user"
        if not os.path.exists(self.user_data_path):
            os.mkdir(self.user_data_path)
        


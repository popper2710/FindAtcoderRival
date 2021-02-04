import os
import datetime

PROJECT_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../")
DATE_FORMAT = "%Y-%m-%dT%H:%M:%s+09:00"

UPDATE_INTERVAL = datetime.timedelta(days=3)

import configparser
import os.path

class DevConfig:
    def __init__(self):
        try:
            self.db_config = configparser.ConfigParser()
            config_path=os.path.join(os.path.dirname(__file__),'devconfig.properties')
            self.db_config.read(config_path)
            self.connect_db("dev")
        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(e)

    def connect_db(self, dev):
        try:
            host = self.db_config.get(dev, 'host')
            user = self.db_config.get(dev, 'user')
            password = self.db_config.get(dev, 'password')
            db = self.db_config.get(dev, 'database')
            return host, user, password, db
        except ConnectionError as e:
            print(e)
        except Exception as e:
            print(e)
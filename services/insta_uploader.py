import sys, os
from . import config

# --- Importing customized instabot lib ---
from pathlib import Path
path_root = f'{Path(__file__).parents[1]}/lib'
print(path_root)
sys.path.append(str(path_root))
from instabot import Bot
# --- ---

def upload_post(self):
    bot = Bot()
    instaUsername = config.INSTA_USERNAMES[self.environment]
    instaPassword = os.environ[config.INSTA_PASSWORD_KEYS[self.environment]]
    bot.login(username = instaUsername, password = instaPassword)
    bot.upload_photo(config.FINISHED_IMG_PATH, self.caption)
    self.logger.info("Img Upload Success")
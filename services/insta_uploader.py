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
    print(self.insta_username)
    print(self.insta_password)
    bot.login(username = self.insta_username, password = self.insta_password)
    bot.upload_photo(config.FINISHED_IMG_PATH, self.caption)
    self.logger.info("Img Upload Success")
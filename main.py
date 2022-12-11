import sys, json
import logging
import logging.handlers
import os
from PIL import Image, ImageFont, ImageDraw


# --- Importing customized instabot lib ---
from pathlib import Path
path_root = f'{Path(__file__).parents[0]}/lib'
sys.path.append(str(path_root))
from lib.instabot import Bot
# --- ---


# --- Setting up Logging ---
logFileName = "status.log"
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    logFileName,
    maxBytes = 1024 * 1024,
    backupCount = 2,
    encoding = "utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)
# --- ---


# --- Loading Inputs ---
payload = json.loads(sys.argv[1])
logger.info(f"Payload: { payload }")
try:
    instaPassword = os.environ["INSTA_PASSWORD"]
except KeyError:
    instaPassword = "Instagram password not available!"
# --- ---


# --- Generating Image ---
imgPath = "./assets/img/prep.jpg"
img = Image.open(imgPath)
fontUrl = "./assets/font/LeagueSpartan-Bold.ttf"
font = ImageFont.truetype(fontUrl, 100)
finalImgName = "completed.jpg"

draw = ImageDraw.Draw(img)
imgText = "Test GH Actions #2"
draw.text((22, 880), imgText, (256, 256, 256), font = font)
img.save(finalImgName)
logger.info("Img Generation Success")
# --- ---


# --- Upload image on Instagram ---
bot = Bot()
instaUsername = "ipuranklist"
bot.login(username = instaUsername, password = instaPassword)

caption = "This is a test post. No actual results released.\n\n 16-11-22: Exam (Dec. 2021) Revised Result for M.Tech. (CSE), Enrol. No. 00516404820\n\n16-11-22: Exam (July 2022) Result for B.TECH(CE), 2nd Sem"
bot.upload_photo(finalImgName, caption)
logger.info("Img Upload Success")
# --- ---
from services import config
from services.logger import init_logger
from services.load_inputs import load_inputs
from services.img_generator import generate_image
from services.insta_uploader import upload_post


# --- Uncomment these for local testing ---
# import os
# os.environ['INSTA_PASSWORD'] = 'asdf'
# os.environ['INSTA_PASSWORD_DEV'] = 'asdf1'
# --- ---

class IPURInstaBot(object):
    def __init__(self):
        self.logger = init_logger()
        self.environment = config.ENV_DEVELOPMENT
        self.entry_type = None
        self.caption = None
        self.insta_username = None
        self.insta_password = None

    def main(self):
        load_inputs(self)
        if (self.entry_type != config.ENTRY_TYPE_CIRCULAR):
            generate_image(self)
            upload_post(self)


# --- EXECUTE MAIN ---
if __name__ == '__main__':
    ipur_insta_bot = IPURInstaBot()
    ipur_insta_bot.main()
# --- ---
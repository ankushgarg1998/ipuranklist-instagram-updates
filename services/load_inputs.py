import json, os, sys
from . import config

def load_inputs(self):
    payload = json.loads(sys.argv[1])
    self.environment = payload[config.ENVIRONMENT]
    self.entry_type = payload[config.ENTRY_TYPE]
    self.caption = payload[config.MESSAGE]
    self.logger.info(f'Payload: { self.environment } - { self.entry_type }')
    self.insta_username = config.INSTA_USERNAMES[self.environment]
    insta_password_key = config.INSTA_PASSWORD_KEYS[self.environment]
    try:
        self.insta_password = os.environ[insta_password_key]
    except KeyError:
        self.logger.info('Instagram password not available!')
        raise
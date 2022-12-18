# --- BASIC CONFIGS ---
ENVIRONMENT = 'environment'
ENTRY_TYPE = 'entryType'
MESSAGE = 'message'

ENV_DEVELOPMENT = 'development'
ENV_PRODUCTION = 'production'
# --- --- 


# --- INSTAGRAM CONFIGS ---
INSTA_USERNAMES = {
    ENV_DEVELOPMENT: 'ipur_test_account',
    ENV_PRODUCTION: 'ipuranklist'
}
INSTA_PASSWORD_KEYS = {
    ENV_DEVELOPMENT: 'INSTA_PASSWORD_DEV',
    ENV_PRODUCTION: 'INSTA_PASSWORD'
}
# --- --- 


# --- IMAGE CONFIGS ---
TOTAL_IMAGES = 11
IMG_PATH_PREFEIX = './assets/img/'
FONT_PATH = './assets/font/LeagueSpartan-Bold.ttf'
FINISHED_IMG_PATH = './assets/img/completed.jpg'

TITLE_TEXT_FONT_SIZE = 180
TITLE_TEXT_POSITION = (50, 500)
TITLE_TEXT_COLOR = (256, 256, 256)
TITLE_TEXT_LINE_SPACING = 20
TITLE_TEXTS = {
        'result': 'new\nresults\nout.',
        'datesheet': 'new\ndatesheets\nout.',
        'circular': 'new\ncirculars\nout.',
    }

SUBTITLE_TEXT_FONT_SIZE = 70
SUBTITLE_TEXT_POSITION = (50, 975)
SUBTITLE_TEXT_COLOR = (256, 222, 89)
SUBTITLE_TEXT = 'details in caption.'
# --- --- 

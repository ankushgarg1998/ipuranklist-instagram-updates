from PIL import Image, ImageFont, ImageDraw
from . import config

def generate_image(self):
    # Draw Image
    img = Image.open(config.IMG_PATH)
    draw = ImageDraw.Draw(img)
    
    # Add Title
    font = ImageFont.truetype(config.FONT_PATH, config.TITLE_TEXT_FONT_SIZE)
    draw.text(config.TITLE_TEXT_POSITION, config.TITLE_TEXTS.get(self.entry_type), config.TITLE_TEXT_COLOR, font = font, spacing = config.TITLE_TEXT_LINE_SPACING)
    
    # Add Subtitle
    font = ImageFont.truetype(config.FONT_PATH, config.SUBTITLE_TEXT_FONT_SIZE)
    draw.text(config.SUBTITLE_TEXT_POSITION, config.SUBTITLE_TEXT, config.SUBTITLE_TEXT_COLOR, font = font)
    
    # Save Image
    img.save(config.FINISHED_IMG_PATH)
    self.logger.info("Img Generation Success")
    return config.FINISHED_IMG_PATH
from PIL import ImageFont

PATH = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono'

Bold = ImageFont.truetype(f"{PATH}-Bold.ttf", 10)
BoldSmall = ImageFont.truetype(f"{PATH}-Bold.ttf", 9)
Medium = ImageFont.truetype(f"{PATH}.ttf", 10)
Huge = ImageFont.truetype(f"{PATH}-Bold.ttf", 35)

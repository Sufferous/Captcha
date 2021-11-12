import os
import math
import string
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont

height = 100
width = 300

def generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(175, 255))

def generate_captcha(size=6):
    arr = np.random.randint(low = 0, high = 255, size = (height, width, 3))

    im = Image.fromarray(arr.astype('uint8'))
    im.save("background.jpg")
    # get an image
    with Image.open("background.jpg").convert("RGBA") as base:

        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", base.size, (255,255,255,0))

        # get a drawing context
        d = ImageDraw.Draw(txt)

        x = 10

        # draw captcha with slight opacity variation and y position
        code = generator(size=size)

        for letter in code:
            fnt = ImageFont.truetype("code_new_roman.otf", random.randint(65, 85))
            d.text((x,random.randint(20, 30)), letter, font=fnt, fill=(0,0,0,random.randint(175, 255)))
            x += random.randint(30, 40)
        for i in range(random.randint(4,6)):
            extra_noise = [(random.randint(0, 25), random.randint(20, height - 20)), (random.randint(150, width), random.randint(0, height))]
            d.line(extra_noise, fill=random_color(), width=random.randint(1, 3))

        out = Image.alpha_composite(base, txt)

        try:
            os.remove("captcha.png")
        except:
            pass
        os.remove("background.jpg")
        out.save("captcha.png")

        print(code)
        return code

generate_captcha()

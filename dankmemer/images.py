from io import BytesIO
from datetime import datetime
from os import listdir

from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance, ImageFilter
from wand import image as wandimage

from .textutils import render_text_with_emoji, wrap, auto_text_size
from . import skew, noisegen, gm
from random import randint, choice
from math import ceil

from redbot.core.data_manager import bundled_data_path


def abandon(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/abandon.bmp")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/verdana.ttf", size=24)
    canv = ImageDraw.Draw(base)
    render_text_with_emoji(self, base, canv, (25, 413), wrap(font, text, 320), font, "black")

    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def aborted(self, avatar):
    base = Image.open(f"{bundled_data_path(self)}/images/aborted.bmp")
    img1 = Image.open(avatar).convert("RGBA").resize((90, 90))
    base.paste(img1, (390, 130), img1)
    base = base.convert("RGB")

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def affect(self, avatar):
    avatar = Image.open(avatar).resize((200, 157)).convert("RGBA")
    base = Image.open(f"{bundled_data_path(self)}/images/affect.bmp").convert("RGBA")

    base.paste(avatar, (180, 383, 380, 540), avatar)
    base = base.convert("RGB")

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def armor(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/armor.bmp").convert("RGBA")
    # We need a text layer here for the rotation
    font, text = auto_text_size(
        text, ImageFont.truetype(f"{bundled_data_path(self)}/fonts/sans.ttf"), 207, font_scalar=0.8
    )
    canv = ImageDraw.Draw(base)

    render_text_with_emoji(self, base, canv, (34, 371), text, font=font, fill="Black")
    base = base.convert("RGB")

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def ballon(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/balloon.bmp").convert("RGBA")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/sans.ttf")
    canv = ImageDraw.Draw(base)

    text = text.split(", ")

    if len(text) != 2:
        text = ["Separate the items with a", "comma followed by a space"]

    balloon, label = text

    balloon_text_1_font, balloon_text_1 = auto_text_size(balloon, font, 162)
    balloon_text_2_font, balloon_text_2 = auto_text_size(balloon, font, 170, font_scalar=0.95)
    balloon_text_3_font, balloon_text_3 = auto_text_size(balloon, font, 110, font_scalar=0.8)
    label_font, label_text = auto_text_size(label, font, 125)

    render_text_with_emoji(
        self, base, canv, (80, 180), balloon_text_1, font=balloon_text_1_font, fill="Black"
    )
    render_text_with_emoji(
        self, base, canv, (50, 530), balloon_text_2, font=balloon_text_2_font, fill="Black"
    )
    render_text_with_emoji(
        self, base, canv, (500, 520), balloon_text_3, font=balloon_text_3_font, fill="Black"
    )
    render_text_with_emoji(self, base, canv, (620, 155), label_text, font=label_font, fill="Black")
    base = base.convert("RGB")

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def bed(self, avatars):
    base = Image.open(f"{bundled_data_path(self)}/images/bed.bmp").convert("RGBA")
    avatar = Image.open(avatars[0]).resize((100, 100)).convert("RGBA")
    avatar2 = Image.open(avatars[1]).resize((70, 70)).convert("RGBA")
    avatar_small = avatar.copy().resize((70, 70))
    base.paste(avatar, (25, 100), avatar)
    base.paste(avatar, (25, 300), avatar)
    base.paste(avatar_small, (53, 450), avatar_small)
    base.paste(avatar2, (53, 575), avatar2)
    base = base.convert("RGBA")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def bongocat(self, avatar):
    base = Image.open(f"{bundled_data_path(self)}/images/bongocat.bmp").convert("RGBA")
    avatar = Image.open(avatar).resize((750, 750)).convert("RGBA")

    avatar.paste(base, (0, 0), base)
    avatar = avatar.convert("RGBA")

    b = BytesIO()
    avatar.save(b, format="png")
    b.seek(0)
    return b


def boo(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/boo.bmp").convert("RGBA")
    # We need a text layer here for the rotation
    canv = ImageDraw.Draw(base)

    text = text.split(", ")

    if len(text) != 2:
        text = ["Separate the items with a", "comma followed by a space"]

    first, second = text

    first_font, first_text = auto_text_size(
        first,
        ImageFont.truetype(f"{bundled_data_path(self)}/fonts/sans.ttf"),
        144,
        font_scalar=0.7,
    )
    second_font, second_text = auto_text_size(
        second,
        ImageFont.truetype(f"{bundled_data_path(self)}/fonts/sans.ttf"),
        144,
        font_scalar=0.7,
    )

    canv.text((35, 54), first_text, font=first_font, fill="Black")
    canv.text((267, 57), second_text, font=second_font, fill="Black")
    base = base.convert("RGB")

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def brain(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/brain.bmp")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/verdana.ttf", size=30)

    if len(text.split(",")) < 4:
        a, b, c, d = "you need, four items, for this, command (split by commas)".split(",")
    else:
        a, b, c, d = text.split(",")[:4]

    a, b, c, d = [wrap(font, i, 225).strip() for i in [a, b, c, d]]

    canvas = ImageDraw.Draw(base)
    canvas.text((15, 40), a, font=font, fill="Black")
    canvas.text((15, 230), b, font=font, fill="Black")
    canvas.text((15, 420), c, font=font, fill="Black")
    canvas.text((15, 610), d, font=font, fill="Black")

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def brazzers(self, avatar):
    avatar = Image.open(avatar).convert("RGBA")
    base = Image.open(f"{bundled_data_path(self)}/images/brazzers.bmp")
    aspect = avatar.width / avatar.height

    new_height = int(base.height * aspect)
    new_width = int(base.width * aspect)
    scale = new_width / avatar.width
    size = (int(new_width / scale / 2), int(new_height / scale / 2))

    base = base.resize(size).convert("RGBA")

    # avatar is technically the base
    avatar.paste(base, (avatar.width - base.width, avatar.height - base.height), base)
    avatar = avatar.convert("RGBA")

    b = BytesIO()
    avatar.save(b, format="png")
    b.seek(0)
    return b


def byemom(self, avatar, text, username):
    base = Image.open(f"{bundled_data_path(self)}/images/mom.bmp")
    avatar = Image.open(avatar).convert("RGBA").resize((70, 70), resample=Image.BICUBIC)
    avatar2 = avatar.copy().resize((125, 125), resample=Image.BICUBIC)
    text_layer = Image.new("RGBA", (350, 25))
    bye_layer = Image.new("RGBA", (180, 51), (255, 255, 255))
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/arial.ttf", size=20)
    bye_font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/arimobold.ttf", size=14)
    canv = ImageDraw.Draw(text_layer)
    bye = ImageDraw.Draw(bye_layer)
    username = username or "Tommy"
    msg = "Alright {} im leaving the house to run some errands".format(username)

    text = wrap(font, text, 500)
    msg = wrap(font, msg, 200)

    render_text_with_emoji(self, text_layer, canv, (0, 0), text, font=font, fill="Black")
    render_text_with_emoji(self, bye_layer, bye, (0, 0), msg, font=bye_font, fill=(42, 40, 165))
    text_layer = text_layer.rotate(24.75, resample=Image.BICUBIC, expand=True)

    base.paste(text_layer, (350, 443), text_layer)
    base.paste(bye_layer, (150, 7))
    base.paste(avatar, (530, 15), avatar)
    base.paste(avatar2, (70, 340), avatar2)
    base = base.convert("RGBA")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def cancer(self, avatar):
    base = Image.open(f"{bundled_data_path(self)}/images/cancer.bmp").convert("RGBA")
    avatar = Image.open(avatar).resize((100, 100)).convert("RGBA")

    base.paste(avatar, (351, 200), avatar)
    base = base.convert("RGBA")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def changemymind(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/changemymind.bmp").convert("RGBA")
    # We need a text layer here for the rotation
    text_layer = Image.new("RGBA", base.size)
    font, text = auto_text_size(
        text, ImageFont.truetype(f"{bundled_data_path(self)}/fonts/sans.ttf"), 310
    )
    canv = ImageDraw.Draw(text_layer)

    render_text_with_emoji(self, text_layer, canv, (290, 300), text, font=font, fill="Black")

    text_layer = text_layer.rotate(23, resample=Image.BICUBIC)

    base.paste(text_layer, (0, 0), text_layer)
    base = base.convert("RGB")

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def cheating(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/cheating.bmp")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/medium.woff", size=26)
    canv = ImageDraw.Draw(base)
    try:
        me, classmate = text.replace(" ,", ",", 1).split(",", 1)
    except ValueError:
        me = "aight thx"
        classmate = "yo dude, you need to split the text with a comma"
    me = wrap(font, me, 150)
    classmate = wrap(font, classmate, 150)
    render_text_with_emoji(self, base, canv, (15, 300), me[:50], font=font, fill="White")
    render_text_with_emoji(self, base, canv, (155, 200), classmate[:50], font=font, fill="White")

    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def citation(self, text):
    text = text.replace(", ", ",").split(",")
    if len(text) != 3:
        text = [
            "M.O.A. CITATION",
            "You must have 3 arguments split by comma",
            "PENALTY ASSESSED - WRONG IMAGE",
        ]
    base = Image.open(f"{bundled_data_path(self)}/images/citation.bmp")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/bmmini.ttf", size=16)
    canv = ImageDraw.Draw(base)
    text_0 = wrap(font, text[0], 320)
    text_1 = wrap(font, text[1], 320)
    canv.text((20, 10), text_0, font=font)
    canv.text((20, 45), text_1, font=font)
    size = canv.textsize(text[2], font=font)
    new_width = (base.width - size[0]) / 2
    canv.text((new_width, 130), text[2], font=font, align="center")
    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def confusedcat(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/confusedcat.bmp")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/medium.woff", size=36)
    canv = ImageDraw.Draw(base)
    try:
        ladies, cat = text.replace(" ,", ",", 1).split(",", 1)
    except ValueError:
        ladies = "Dank Memer"
        cat = "People who forget to split text with a comma"
    ladies = wrap(font, ladies, 510)
    cat = wrap(font, cat, 510)
    render_text_with_emoji(self, base, canv, (5, 5), ladies[:100], font=font, fill="Black")
    render_text_with_emoji(self, base, canv, (516, 5), cat[:100], font=font, fill="Black")

    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


# SOMETHING IS WRONG HERE
def corporate(self, avatars):
    base = Image.open(f"{bundled_data_path(self)}/images/corporate.jpg")
    img1 = Image.open(avatars[0]).convert("RGBA").resize((512, 512), Image.LANCZOS)
    try:
        img2 = Image.open(avatars[1]).convert("RGBA").resize((512, 512), Image.LANCZOS)
    except IndexError:
        img2 = img1

    img1 = skew.skew(img1, [(208, 44), (718, 84), (548, 538), (20, 446)])

    img2 = skew.skew(img2, [(858, 112), (1600, 206), (1312, 666), (634, 546)], resolution=1400)

    base.paste(img1, (0, 0), img1)
    base.paste(img2, (0, 0), img2)

    base = base.resize((base.width // 2, base.height // 2))

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def cry(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/cry.bmp")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/tahoma.ttf", size=20)
    canv = ImageDraw.Draw(base)

    text = wrap(font, text, 180)
    render_text_with_emoji(self, base, canv, (382, 80), text, font=font, fill="Black")

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def dab(self, avatar):
    base = Image.open(f"{bundled_data_path(self)}/images/dab.bmp").convert("RGBA")
    avatar = Image.open(avatar).resize((500, 500)).convert("RGBA")
    final_image = Image.new("RGBA", base.size)

    # Put the base over the avatar
    final_image.paste(avatar, (300, 0), avatar)
    final_image.paste(base, (0, 0), base)

    b = BytesIO()
    final_image.save(b, format="png")
    b.seek(0)
    return b


def deepfry(self, avatar):
    avatar = Image.open(avatar).resize((400, 400)).convert("RGBA")

    # noinspection PyPep8
    joy, hand, hundred, fire = [
        Image.open(f"{bundled_data_path(self)}/images/deepfry_{asset}.bmp")
        .resize((100, 100))
        .rotate(randint(-30, 30))
        .convert("RGBA")
        for asset in ["joy", "ok-hand", "100", "fire"]
    ]

    avatar.paste(joy, (randint(20, 75), randint(20, 45)), joy)
    avatar.paste(hand, (randint(20, 75), randint(150, 300)), hand)
    avatar.paste(hundred, (randint(150, 300), randint(20, 45)), hundred)
    avatar.paste(fire, (randint(150, 300), randint(150, 300)), fire)

    noise = avatar.convert("RGB")
    noise = noisegen.add_noise(noise, 25)
    noise = ImageEnhance.Contrast(noise).enhance(randint(5, 20))
    noise = ImageEnhance.Sharpness(noise).enhance(17.5)
    noise = ImageEnhance.Color(noise).enhance(randint(-15, 15))

    b = BytesIO()
    noise.save(b, format="png")
    b.seek(0)
    return b


def delete(self, avatar):
    base = Image.open(f"{bundled_data_path(self)}/images/delete.bmp").convert("RGBA")
    avatar = Image.open(avatar).resize((195, 195)).convert("RGBA")

    base.paste(avatar, (120, 135), avatar)
    base = base.convert("RGBA")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def disability(self, avatar):
    avatar = Image.open(avatar).resize((175, 175)).convert("RGBA")
    base = Image.open(f"{bundled_data_path(self)}/images/disability.bmp").convert("RGBA")

    base.paste(avatar, (450, 325), avatar)
    base = base.convert("RGBA")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def doglemon(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/doglemon.bmp")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/medium.woff", size=30)
    canv = ImageDraw.Draw(base)
    try:
        lemon, dog = text.replace(" ,", ",", 1).split(",", 1)
    except ValueError:
        lemon = "Text that is not seperated by comma"
        dog = "Dank Memer"
    lemon = wrap(font, lemon, 450)
    dog = wrap(font, dog, 450)
    render_text_with_emoji(self, base, canv, (850, 100), lemon[:180], font=font, fill="Black")
    render_text_with_emoji(self, base, canv, (500, 100), dog[:200], font=font, fill="White")

    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def door(self, avatar):
    base = Image.open(f"{bundled_data_path(self)}/images/door.bmp").convert("RGBA")
    avatar = Image.open(avatar).resize((479, 479)).convert("RGBA")
    final_image = Image.new("RGBA", base.size)

    # Put the base over the avatar
    final_image.paste(avatar, (250, 0), avatar)
    final_image.paste(base, (0, 0), base)
    final_image = final_image.convert("RGBA")

    b = BytesIO()
    final_image.save(b, format="png")
    b.seek(0)
    return b


def egg(self, avatar):
    base = (
        Image.open(f"{bundled_data_path(self)}/images/egg.bmp").resize((350, 350)).convert("RGBA")
    )
    avatar = Image.open(avatar).resize((50, 50)).convert("RGBA")

    base.paste(avatar, (143, 188), avatar)
    base = base.convert("RGBA")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def emergencymeeting(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/emergencymeeting.bmp")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/medium.woff", size=33)
    canv = ImageDraw.Draw(base)
    if len(text) >= 140:
        text = text[:137] + "..."
    text = wrap(font, text, 750)
    render_text_with_emoji(self, base, canv, (0, 0), text, font=font, fill="Black")

    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def excuseme(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/excuseme.bmp")

    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/sans.ttf", size=40)
    canv = ImageDraw.Draw(base)
    text = wrap(font, text, 787)
    render_text_with_emoji(self, base, canv, (20, 15), text, font=font, fill="Black")

    base = base.convert("RGB")

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


# TODO put some MAX_WIDTH
def expanddong(self, text):
    text = text[:500]
    lines = ceil((len(text) * 128) / 1920) + 1
    base = Image.new("RGBA", (1920, lines * 128), (255, 255, 255, 0))
    line = 0
    pos = 0
    chars = dict()
    for i in listdir(f"{bundled_data_path(self)}/images/expanddong"):
        if i.endswith(".bmp"):
            chars[i[0]] = Image.open(f"{bundled_data_path(self)}/images/expanddong/{i}")
    for word in text.split(" "):
        if 15 - pos <= len(word):
            pos = 0
            line += 1
        for char in word:
            char = char.lower()
            if chars.get(char):
                base.paste(chars[char], (pos * 128, line * 128))
            pos += 1
        pos += 1
        if pos >= 15:
            pos = 0
            line += 1

    base = base.convert("RGBA")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def expandingwwe(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/expandingwwe.jpg")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/verdana.ttf", size=30)

    text = text.replace(", ", ",")

    if len(text.split(",")) < 5:
        (
            a,
            b,
            c,
            d,
            e,
        ) = "you need, five items, for this, command, (split by commas)".split(",")
    else:
        a, b, c, d, e = text.split(",", 4)

    a, b, c, d, e = [wrap(font, i, 225).strip() for i in [a, b, c, d, e]]

    canvas = ImageDraw.Draw(base)
    canvas.text((5, 5), a, font=font, fill="Black")
    canvas.text((5, 205), b, font=font, fill="Black")
    canvas.text((5, 410), c, font=font, fill="Black")
    canvas.text((5, 620), d, font=font, fill="Black")
    canvas.text((5, 825), e, font=font, fill="Black")

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def facts(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/facts.bmp")
    # We need to create an image layer here for the rotation
    text_layer = Image.new("RGBA", base.size)
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/verdana.ttf", size=25)
    canv = ImageDraw.Draw(text_layer)

    text = wrap(font, text, 400)
    render_text_with_emoji(self, text_layer, canv, (90, 600), text, font=font, fill="Black")
    text_layer = text_layer.rotate(-13, resample=Image.BICUBIC)
    base.paste(text_layer, (0, 0), text_layer)

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def failure(self, avatar):
    base = Image.open(f"{bundled_data_path(self)}/images/failure.bmp").convert("RGBA")
    avatar = Image.open(avatar).resize((215, 215)).convert("RGBA")

    base.paste(avatar, (143, 525), avatar)
    base = base.convert("RGBA")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def fakenews(self, avatar):
    base = Image.open(f"{bundled_data_path(self)}/images/fakenews.bmp").convert("RGBA")
    avatar = Image.open(avatar).resize((400, 400)).convert("RGBA")
    final_image = Image.new("RGBA", base.size)

    # Put the base over the avatar
    final_image.paste(avatar, (390, 0), avatar)
    final_image.paste(base, (0, 0), base)
    final_image = final_image.convert("RGBA")

    b = BytesIO()
    final_image.save(b, format="png")
    b.seek(0)
    return b


def farmer(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/farmer.jpg")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/verdana.ttf", size=24)
    canv = ImageDraw.Draw(base)

    clouds, farmertext = text.replace(", ", ",").split(",", 1)

    if len(clouds) >= 150:
        clouds = clouds[:147] + "..."

    if len(farmertext) >= 100:
        farmertext = farmertext[:97] + "..."
    render_text_with_emoji(self, base, canv, (50, 300), wrap(font, clouds, 580), font, "white")
    render_text_with_emoji(self, base, canv, (50, 825), wrap(font, farmertext, 580), font, "white")

    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def fedora(self, avatar):
    base = Image.open(f"{bundled_data_path(self)}/images/fedora.bmp").convert("RGBA")
    avatar = Image.open(avatar).resize((275, 275)).convert("RGBA")
    final_image = Image.new("RGBA", base.size)

    # Put the base over the avatar
    final_image.paste(avatar, (112, 101), avatar)
    final_image.paste(base, (0, 0), base)

    b = BytesIO()
    final_image.save(b, format="png")
    b.seek(0)
    return b


def floor(self, avatar, text):
    base = Image.open(f"{bundled_data_path(self)}/images/floor.bmp").convert("RGBA")
    avatar = Image.open(avatar).resize((45, 45)).convert("RGBA")
    avatar2 = avatar.copy().resize((23, 23))
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/sans.ttf", size=22)
    canv = ImageDraw.Draw(base)

    text = wrap(font, text, 300)
    render_text_with_emoji(self, base, canv, (168, 36), text, font=font, fill="Black")

    base.paste(avatar, (100, 90), avatar)
    base.paste(avatar2, (330, 90), avatar2)
    base = base.convert("RGBA")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def fuck(self, text):
    text = text.replace(", ", ",").split(",")
    if len(text) != 2:
        text = ["me not using commas", "you must split the lines with a comma"]
    base = Image.open(f"{bundled_data_path(self)}/images/fuck.jpg")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/verdana.ttf", size=24)
    canv = ImageDraw.Draw(base)
    render_text_with_emoji(self, base, canv, (200, 600), wrap(font, text[0], 320), font, "white")
    render_text_with_emoji(self, base, canv, (750, 700), wrap(font, text[1], 320), font, "white")

    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def garfield(self, avatar, text):

    base = Image.open(f"{bundled_data_path(self)}/images/garfield_garfield.png").convert("RGB")
    no_entry = (
        Image.open(f"{bundled_data_path(self)}/images/garfield_no_entry.png")
        .convert("RGBA")
        .resize((224, 224), Image.LANCZOS)
    )
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/arial.ttf", size=28)
    avatar = Image.open(avatar).resize((192, 192), Image.LANCZOS).convert("RGBA")
    avatar2 = avatar.copy().resize((212, 212), Image.LANCZOS).convert("RGBA")

    base.paste(avatar, (296, 219), avatar)
    base.paste(no_entry, (280, 203), no_entry)
    base.paste(avatar2, (40, 210), avatar2)

    draw = ImageDraw.Draw(base)
    render_text_with_emoji(self, base, draw, (15, 0), wrap(font, text, base.width), font, "black")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def gay(self, avatar):
    img1 = Image.open(avatar).convert("RGBA")
    img2 = Image.open(f"{bundled_data_path(self)}/gay/gay.bmp").convert("RGBA").resize(img1.size)
    img2.putalpha(128)
    img1.paste(img2, (0, 0), img2)
    img1 = img1.convert("RGB")

    b = BytesIO()
    img1.save(b, format="png")
    b.seek(0)
    return b


def godwhy(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/godwhy.png").resize(
        (1061, 1080), Image.LANCZOS
    )
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/verdana.ttf", size=24)
    canv = ImageDraw.Draw(base)

    if len(text) >= 127:
        text = text[:124] + "..."

    render_text_with_emoji(self, base, canv, (35, 560), wrap(font, text, 370), font, "black")

    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def goggles(self, avatar):
    img1 = Image.open(avatar).convert("RGBA")
    base = Image.open(f"{bundled_data_path(self)}/images/goggles.jpg").convert("RGBA")
    img1 = skew.skew(img1, [(32, 297), (171, 295), (180, 456), (41, 463)])
    base.paste(img1, (0, 0), img1)
    base = base.resize((base.width, int(base.height / 1.5)), Image.LANCZOS).convert("RGB")

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def hitler(self, avatar):
    base = Image.open(f"{bundled_data_path(self)}/images/hitler.bmp")
    img1 = Image.open(avatar).convert("RGBA").resize((140, 140))
    base.paste(img1, (46, 43), img1)
    base = base.convert("RGB")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def humansgood(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/humansgood.bmp").convert("RGBA")
    # We need a text layer here for the rotation
    font, text = auto_text_size(
        text, ImageFont.truetype(f"{bundled_data_path(self)}/fonts/sans.ttf"), 125, font_scalar=0.7
    )
    canv = ImageDraw.Draw(base)
    render_text_with_emoji(self, base, canv, (525, 762), text, font, "black")
    base = base.convert("RGB")

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def inator(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/inator.jpg")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/verdana.ttf", size=24)
    canv = ImageDraw.Draw(base)
    render_text_with_emoji(self, base, canv, (370, 0), wrap(font, text, 340), font, "black")
    vowels = ["i", "y", "e", "a", "u", "o"]
    for vowel in vowels:
        if text.endswith(vowel):
            ending = "nator"
            break
    else:
        ending = "inator"
    render_text_with_emoji(
        self, base, canv, (370, 380), wrap(font, text + ending, 335), font, "black"
    )
    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def invert(avatar):
    avatar = Image.open(avatar)
    if avatar.mode == "RGBA":
        r, g, b, a = avatar.split()
        rgb_image = Image.merge("RGB", (r, g, b))
        inverted = ImageOps.invert(rgb_image)
        r, g, b = inverted.split()
        avatar = Image.merge("RGBA", (r, g, b, a))
    else:
        avatar = avatar.convert("RGB")
        avatar = ImageOps.invert(avatar)

    avatar = avatar.convert("RGBA")
    b = BytesIO()
    avatar.save(b, format="png")
    b.seek(0)
    return b


def ipad(self, avatar):
    white = Image.new("RGBA", (2048, 1364), 0x00000000)
    base = Image.open(f"{bundled_data_path(self)}/images/ipad.png")
    img1 = Image.open(avatar).convert("RGBA").resize((512, 512), Image.LANCZOS)

    img1 = skew.skew(img1, [(476, 484), (781, 379), (956, 807), (668, 943)])
    white.paste(img1, (0, 0), img1)
    white.paste(base, (0, 0), base)
    white = white.convert("RGBA").resize((512, 341), Image.LANCZOS)

    b = BytesIO()
    white.save(b, format="png")
    b.seek(0)
    return b


def jail(self, avatar):
    overlay = Image.open(f"{bundled_data_path(self)}/images/jail.bmp").resize((350, 350))
    base = Image.open(avatar).convert("LA").resize((350, 350))
    base.paste(overlay, (0, 0), overlay)

    base = base.convert("RGBA")
    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def justpretending(self, text):
    text = text.replace(", ", ",").split(",")
    if len(text) != 2:
        text = ["you should add two things split by commas", "idiot"]
    base = Image.open(f"{bundled_data_path(self)}/images/justpretending.jpg")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/verdana.ttf", size=24)
    canv = ImageDraw.Draw(base)
    render_text_with_emoji(self, base, canv, (678, 12), wrap(font, text[0], 320), font, "black")
    render_text_with_emoji(self, base, canv, (9, 800), wrap(font, text[1], 100), font, "black")
    render_text_with_emoji(self, base, canv, (399, 808), wrap(font, text[1], 100), font, "black")
    render_text_with_emoji(self, base, canv, (59, 917), wrap(font, text[1], 100), font, "black")
    render_text_with_emoji(self, base, canv, (425, 910), wrap(font, text[1], 100), font, "black")

    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def keepurdistance(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/keepurdistance.png")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/MontserratBold.ttf", size=24)
    canv = ImageDraw.Draw(base)

    text = text.upper()

    if len(text) >= 30:
        text = text[:27] + "..."
    render_text_with_emoji(self, base, canv, (92, 660), wrap(font, text, 440), font, "white")

    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def kimborder(self, avatar):
    base = Image.open(f"{bundled_data_path(self)}/images/kimborder.png")
    white = Image.new("RGBA", (base.width, base.height), 0x00000000)
    img1 = Image.open(avatar).convert("RGBA")
    img1 = img1.resize((img1.width, img1.height), Image.LANCZOS)

    img1 = skew.skew(img1, [(0, 402), (476, 413), (444, 638), (0, 638)])
    white.paste(img1, (0, 0), img1)
    white.paste(base, (0, 0), base)
    white = white.convert("RGBA").resize((base.width, base.height), Image.LANCZOS)

    b = BytesIO()
    white.save(b, format="png")
    b.seek(0)
    return b


def knowyourlocation(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/knowyourlocation.bmp").convert("RGBA")
    # We need a text layer here for the rotation
    canv = ImageDraw.Draw(base)

    text = text.split(", ")

    if len(text) != 2:
        text = ["Separate the items with a", "comma followed by a space"]

    top, bottom = text

    top_font, top_text = auto_text_size(
        top, ImageFont.truetype(f"{bundled_data_path(self)}/fonts/sans.ttf"), 630
    )
    bottom_font, bottom_text = auto_text_size(
        bottom, ImageFont.truetype(f"{bundled_data_path(self)}/fonts/sans.ttf"), 539
    )
    render_text_with_emoji(self, base, canv, (64, 131), top_text, top_font, "black")
    render_text_with_emoji(self, base, canv, (120, 450), bottom_text, bottom_font, "black")
    base = base.convert("RGB")

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def laid(self, avatar):
    base = Image.open(f"{bundled_data_path(self)}/images/laid.bmp").convert("RGBA")
    avatar = Image.open(avatar).resize((115, 115)).convert("RGBA")
    final_image = Image.new("RGBA", base.size)

    # Put the base over the avatar
    final_image.paste(avatar, (512, 360), avatar)
    final_image.paste(base, (0, 0), base)
    final_image.convert("RGBA")

    b = BytesIO()
    final_image.save(b, format="png")
    b.seek(0)
    return b


def lick(self, text):
    text = text.replace(", ", ",").split(",")
    if len(text) != 2:
        text = ["Dank Memer", "People who do not split with a comma"]
    base = Image.open(f"{bundled_data_path(self)}/images/lick.jpg")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/verdana.ttf", size=24)
    canv = ImageDraw.Draw(base)
    render_text_with_emoji(self, base, canv, (80, 200), wrap(font, text[0], 220), font, "white")
    render_text_with_emoji(self, base, canv, (290, 240), wrap(font, text[1], 320), font, "white")

    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def madethis(self, avatars):
    base = Image.open(f"{bundled_data_path(self)}/images/madethis.bmp").convert("RGBA")
    avatar = Image.open(avatars[0]).resize((130, 130)).convert("RGBA")
    avatar2 = Image.open(avatars[1]).resize((111, 111)).convert("RGBA")
    base.paste(avatar, (92, 271), avatar)
    base.paste(avatar2, (422, 267), avatar2)
    base.paste(avatar2, (406, 678), avatar2)
    base.paste(avatar2, (412, 1121), avatar2)
    base = base.convert("RGBA")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def magik(self, avatar, text):
    try:
        img = wandimage.Image(file=avatar)
    except Exception as e:
        raise Exception(f"The image could not be loaded: {e}")

    if img.animation:
        img = img.convert("png")
    img.transform(resize="400x400")

    try:
        multiplier = int(text)
    except ValueError:
        multiplier = 1
    else:
        multiplier = max(min(multiplier, 10), 1)

    img.liquid_rescale(
        width=int(img.width * 0.5),
        height=int(img.height * 0.5),
        delta_x=0.5 * multiplier,
        rigidity=0,
    )
    img.liquid_rescale(
        width=int(img.width * 1.5),
        height=int(img.height * 1.5),
        delta_x=2 * multiplier,
        rigidity=0,
    )

    b = BytesIO()
    img.save(file=b)
    b.seek(0)
    img.destroy()
    return b


def master(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/master.bmp").convert("RGBA")
    text = text.split(",")
    if len(text) == 3:
        a, b, c = text
    else:
        a, b, c = ("you need 3 items", "for this command", "split by commas")
    font, text1 = auto_text_size(
        a, ImageFont.truetype(f"{bundled_data_path(self)}/fonts/sans.ttf"), 250, font_scalar=0.2
    )
    font, text2 = auto_text_size(b, font, 250, font_scalar=0.3)
    font, text3 = auto_text_size(c, font, 300, font_scalar=0.2)
    canv = ImageDraw.Draw(base)
    text_layer = Image.new("RGBA", base.size)
    tilted_text = ImageDraw.Draw(text_layer)

    canv.text((457, 513), text1, font=font, fill="White")
    tilted_text.text((350, 330), text2, font=font, fill="White")
    canv.text((148, 151), text3, font=font, fill="White")

    text_layer = text_layer.rotate(8, resample=Image.BICUBIC)

    base.paste(text_layer, (0, 0), text_layer)
    base = base.convert("RGB")

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


"""
    This endpoint works a bit differently from the other endpoints.
    This endpoint takes in top_text and bottom_text parameters instead of text.
    It also supports color and font parameters.
    Fonts supported are: arial, arimobold, impact, robotomedium, robotoregular, sans, segoeuireg, tahoma and verdana.
    Colors can be defined with HEX codes or web colors, e.g. black, white, orange etc. Try your luck ;)
    The default is Impact in white
"""


def meme(self, avatar, top_text, bottom_text, color, font, altstyle):
    img = Image.open(avatar).convert("RGBA")
    factor = int(img.height / 10)
    deffont = font or "impact"
    deffont = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/{deffont}.ttf", size=factor)
    draw = ImageDraw.Draw(img)
    defcolor = color or "white"

    def draw_text_with_outline(string, x, y):
        x = int(x)
        y = int(y)
        render_text_with_emoji(
            self, img, draw, (x - 2, y - 2), string, font=deffont, fill=(0, 0, 0)
        )
        render_text_with_emoji(
            self, img, draw, (x + 2, y - 2), string, font=deffont, fill=(0, 0, 0)
        )
        render_text_with_emoji(
            self, img, draw, (x + 2, y + 2), string, font=deffont, fill=(0, 0, 0)
        )
        render_text_with_emoji(
            self, img, draw, (x - 2, y + 2), string, font=deffont, fill=(0, 0, 0)
        )
        render_text_with_emoji(self, img, draw, (x, y), string, font=deffont, fill=defcolor)

    def draw_text(string, pos):
        string = string.upper()
        w, h = draw.textsize(string, deffont)  # measure the size the text will take

        line_count = 1
        if w > img.width:
            line_count = int(round((w / img.width) + 1))

        lines = []
        if line_count > 1:

            last_cut = 0
            is_last = False
            for i in range(0, line_count):
                if last_cut == 0:
                    cut = int((len(string) / line_count) * i)
                else:
                    cut = int(last_cut)

                if i < line_count - 1:
                    next_cut = int((len(string) / line_count) * (i + 1))
                else:
                    next_cut = len(string)
                    is_last = True

                # make sure we don't cut words in half
                if not next_cut == len(text) or not text[next_cut] == " ":
                    try:
                        while string[next_cut] != " ":
                            next_cut += 1
                    except IndexError:
                        next_cut = next_cut - 1

                line = string[cut:next_cut].strip()

                # is line still fitting ?
                w, h = draw.textsize(line, deffont)
                if not is_last and w > img.width:
                    next_cut -= 1
                    while string[next_cut] != " ":
                        next_cut -= 1

                last_cut = next_cut
                lines.append(string[cut : next_cut + 1].strip())

        else:
            lines.append(string)

        last_y = -h
        if pos == "bottom":
            last_y = img.height - h * (line_count + 1) - 10

        for i in range(0, line_count):
            w, h = draw.textsize(lines[i], deffont)
            x = img.width / 2 - w / 2
            y = last_y + h
            draw_text_with_outline(lines[i], x, y)
            last_y = y

    if altstyle:
        text_font = ImageFont.truetype(
            f'{bundled_data_path(self)}/fonts/{font or "arial"}.ttf', size=24
        )
        text = wrap(text_font, top_text or "TOP TEXT", img.width)
        text_img = Image.new("RGB", (img.width, 10000), "white")
        text_draw = ImageDraw.Draw(text_img)
        text_size = text_draw.textsize(text, text_font)
        new_image = Image.new("RGB", (img.width, img.height + text_size[1] + 10), "white")
        new_image.paste(img, (0, text_size[1] + 10))
        new_draw = ImageDraw.Draw(new_image)
        new_draw.text((0, 0), text, color or "black", text_font)
        img = new_image

    else:
        draw_text(top_text or "TOP TEXT", "top")
        draw_text(bottom_text or "BOTTOM TEXT", "bottom")

    b = BytesIO()
    img.save(b, format="png")
    b.seek(0)
    return b


def note(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/note.bmp").convert("RGBA")
    # We need a text layer here for the rotation
    text_layer = Image.new("RGBA", base.size)
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/sans.ttf", size=16)
    canv = ImageDraw.Draw(text_layer)

    text = wrap(font, text, 150)
    render_text_with_emoji(self, text_layer, canv, (455, 420), text, font=font, fill="Black")

    text_layer = text_layer.rotate(-23, resample=Image.BICUBIC)

    base.paste(text_layer, (0, 0), text_layer)
    base = base.convert("RGB")

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def nothing(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/nothing.bmp")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/medium.woff", size=33)
    canv = ImageDraw.Draw(base)
    text = wrap(font, text, 200)
    render_text_with_emoji(self, base, canv, (340, 5), text[:120], font=font, fill="Black")

    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def obama(self, avatar, usernames):
    base = Image.open(f"{bundled_data_path(self)}/images/obama.jpg")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/arimobold.ttf", size=36)
    canv = ImageDraw.Draw(base)

    avatar = Image.open(avatar).resize((200, 200), Image.LANCZOS).convert("RGBA")

    w, _ = canv.textsize(wrap(font, usernames[0], 400), font)

    base.paste(avatar, (120, 73), avatar)
    base.paste(avatar, (365, 0), avatar)

    render_text_with_emoji(
        self, base, canv, (int(210 - (w / 2)), 400), wrap(font, usernames[0], 400), font, "white"
    )
    render_text_with_emoji(
        self, base, canv, (int(470 - (w / 2)), 300), wrap(font, usernames[0], 400), font, "white"
    )

    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def ohno(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/ohno.bmp").convert("RGBA")
    font = ImageFont.truetype(
        f"{bundled_data_path(self)}/fonts/sans.ttf", size=16 if len(text) > 38 else 32
    )
    canv = ImageDraw.Draw(base)

    text = wrap(font, text, 260)
    render_text_with_emoji(self, base, canv, (340, 30), text, font=font, fill="Black")
    base = base.convert("RGB")

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def piccolo(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/piccolo.bmp")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/medium.woff", size=33)
    canv = ImageDraw.Draw(base)
    text = wrap(font, text, 850)
    render_text_with_emoji(self, base, canv, (5, 5), text[:300], font=font, fill="Black")

    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def plan(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/plan.bmp").convert("RGBA")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/sans.ttf", size=16)
    canv = ImageDraw.Draw(base)

    words = text.split(", ")

    if len(words) != 3:
        words = [
            "you need three items for this command",
            "and each should be split by commas",
            "Example: pls plan 1, 2, 3",
        ]

    words = [wrap(font, w, 120) for w in words]

    a, b, c = words

    render_text_with_emoji(self, base, canv, (190, 60), a, font=font, fill="Black")
    render_text_with_emoji(self, base, canv, (510, 60), b, font=font, fill="Black")
    render_text_with_emoji(self, base, canv, (190, 280), c, font=font, fill="Black")
    render_text_with_emoji(self, base, canv, (510, 280), c, font=font, fill="Black")
    base = base.convert("RGB")

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def presentation(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/presentation.bmp")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/verdana.ttf", size=24)
    canv = ImageDraw.Draw(base)
    text = wrap(font, text, 330)
    render_text_with_emoji(self, base, canv, (150, 80), text, font=font, fill="Black")

    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def quote(self, avatar, text, usernames):
    avatar = Image.open(avatar).resize((150, 150))
    base = Image.new("RGBA", (1500, 300))
    font_med = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/medium.woff", size=60)
    font_time = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/medium.woff", size=40)
    font_sb = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/semibold.woff", size=55)

    poly = Image.new("RGBA", avatar.size)
    pdraw = ImageDraw.Draw(poly)
    pdraw.ellipse([(0, 0), *avatar.size], fill=(255, 255, 255, 255))
    if poly.mode == "RGBA":
        r, g, b, a = poly.split()
        rgb_image = Image.merge("RGB", (r, g, b))
        inverted = ImageOps.invert(rgb_image)
        r, g, b = inverted.split()
        iv = Image.merge("RGBA", (r, g, b, a))
    else:
        iv = ImageOps.invert(poly)

    base.paste(avatar, (15, 75), mask=iv)

    words = Image.new("RGBA", base.size)
    canvas = ImageDraw.Draw(words)

    render_text_with_emoji(
        self, base, canvas, (230, 70), usernames[0], font=font_med, fill="White"
    )
    render_text_with_emoji(
        self, base, canvas, (230, 150), text, font=font_sb, fill=(160, 160, 160)
    )

    timestamp_left = 230 + canvas.textsize(usernames[0], font=font_med)[0] + 20
    render_text_with_emoji(
        self,
        base,
        canvas,
        (timestamp_left, 90),
        "Today at {}".format(datetime.utcnow().strftime("%H:%M")),
        font=font_time,
        fill=(125, 125, 125),
    )

    final = Image.alpha_composite(base, words)
    downscaled = final.resize((500, 100), Image.ANTIALIAS)
    downscaled = downscaled.convert("RGBA")

    b = BytesIO()
    downscaled.save(b, format="png")
    b.seek(0)
    return b


def radialblur(self, avatar):
    output = gm.radial_blur(Image.open(avatar), 15, "png")

    b = BytesIO(output)
    b.seek(0)
    return b


def rip(self, avatar):
    base = (
        Image.open(f"{bundled_data_path(self)}/images/rip.bmp").convert("RGBA").resize((642, 806))
    )
    avatar = Image.open(avatar).resize((300, 300)).convert("RGBA")

    base.paste(avatar, (175, 385), avatar)
    base = base.convert("RGBA")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def roblox(self, avatar):
    base = Image.open(f"{bundled_data_path(self)}/images/roblox.bmp").convert("RGBA")
    avatar = Image.open(avatar).resize((56, 74)).convert("RGBA")
    base.paste(avatar, (168, 41), avatar)

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def salty(self, avatar):
    avatar = Image.open(avatar).convert("RGBA").resize((256, 256))

    salt = (
        Image.open(f"{bundled_data_path(self)}/images/salt.bmp")
        .convert("RGBA")
        .resize((256, 256))
        .rotate(-130, resample=Image.BICUBIC)
    )

    blank = Image.new("RGBA", (256, 256))
    blank.paste(avatar, (0, 0), avatar)
    frames = []

    for i in range(8):
        base = blank.copy()
        if i == 0:
            base.paste(salt, (-125, -125), salt)
        else:
            base.paste(salt, (-135 + randint(-5, 5), -135 + randint(-5, 5)), salt)

        frames.append(base)

    b = BytesIO()
    frames[0].save(
        b,
        save_all=True,
        append_images=frames[1:],
        format="gif",
        loop=0,
        duration=20,
        optimize=True,
    )
    b.seek(0)
    return b


def satan(self, avatar):
    base = Image.open(f"{bundled_data_path(self)}/images/satan.bmp").convert("RGBA")
    avatar = Image.open(avatar).resize((195, 195)).convert("RGBA")
    final_image = Image.new("RGBA", base.size)

    # Put the base over the avatar
    final_image.paste(avatar, (200, 90), avatar)
    final_image.paste(base, (0, 0), base)
    final_image = final_image.convert("RGBA")

    b = BytesIO()
    final_image.save(b, format="png")
    b.seek(0)
    return b


def savehumanity(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/humanity.bmp").convert("RGBA")
    # We need a text layer here for the rotation
    text_layer = Image.new("RGBA", base.size)
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/sans.ttf", size=16)
    canv = ImageDraw.Draw(text_layer)

    text = wrap(font, text, 180)
    render_text_with_emoji(self, text_layer, canv, (490, 410), text, font=font, fill="Black")

    text_layer = text_layer.rotate(-7, resample=Image.BICUBIC)

    base.paste(text_layer, (0, 0), text_layer)
    base = base.convert("RGB")

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def screams(self, avatars):
    base = Image.open(f"{bundled_data_path(self)}/images/screams.bmp").convert("RGBA")
    avatar = Image.open(avatars[0]).resize((175, 175)).convert("RGBA")
    avatar2 = Image.open(avatars[1]).resize((156, 156)).convert("RGBA")
    base.paste(avatar, (200, 1), avatar)
    base.paste(avatar2, (136, 231), avatar2)
    base = base.convert("RGBA")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def shit(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/shit.bmp")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/segoeuireg.ttf", size=30)

    # We need a text layer here for the rotation
    text_layer = Image.new("RGBA", base.size)
    canv = ImageDraw.Draw(text_layer)

    text = wrap(font, text, 350)
    render_text_with_emoji(self, text_layer, canv, (0, 570), text, font=font, fill="Black")
    text_layer = text_layer.rotate(52, resample=Image.BICUBIC)

    base.paste(text_layer, (0, 50), text_layer)
    base = base.convert("RGB")

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def sickban(self, avatar):
    base = Image.open(f"{bundled_data_path(self)}/images/ban.bmp").convert("RGBA")
    avatar = Image.open(avatar).resize((400, 400)).convert("RGBA")
    base.paste(avatar, (70, 344), avatar)
    base = base.convert("RGBA")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def slap(self, avatars):
    base = (
        Image.open(f"{bundled_data_path(self)}/images/batslap.bmp")
        .resize((1000, 500))
        .convert("RGBA")
    )
    avatar = Image.open(avatars[1]).resize((220, 220)).convert("RGBA")
    avatar2 = Image.open(avatars[0]).resize((200, 200)).convert("RGBA")
    base.paste(avatar, (580, 260), avatar)
    base.paste(avatar2, (350, 70), avatar2)
    base = base.convert("RGB")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def slapsroof(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/slapsroof.bmp")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/medium.woff", size=33)
    canv = ImageDraw.Draw(base)
    suffix = " in it"
    text = wrap(font, text + suffix, 1150)
    render_text_with_emoji(self, base, canv, (335, 31), text, font=font, fill="Black")

    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def sneakyfox(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/sneakyfox.bmp")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/arimobold.ttf", size=36)
    canv = ImageDraw.Draw(base)
    try:
        fox, otherthing = text.replace(" ,", ",", 1).split(",", 1)
    except ValueError:
        fox = "Text that is not split with a comma"
        otherthing = "the bot"
    fox = wrap(font, fox, 500)
    otherthing = wrap(font, otherthing, 450)
    render_text_with_emoji(self, base, canv, (300, 350), fox[:180], font=font, fill="Black")
    render_text_with_emoji(self, base, canv, (670, 120), otherthing[:180], font=font, fill="Black")

    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def spank(self, avatars):
    base = Image.open(f"{bundled_data_path(self)}/images/spank.bmp").resize((500, 500))
    img1 = Image.open(avatars[0]).resize((140, 140)).convert("RGBA")
    img2 = Image.open(avatars[1]).resize((120, 120)).convert("RGBA")
    base.paste(img1, (225, 5), img1)
    base.paste(img2, (350, 220), img2)
    base = base.convert("RGBA")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def stroke(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/stroke.bmp")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/verdana.ttf", size=12)
    canv = ImageDraw.Draw(base)
    text = wrap(font, text, 75)
    render_text_with_emoji(self, base, canv, (272, 287), text, font=font, fill="Black")

    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def surprised(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/surprised.bmp").convert("RGBA")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/robotoregular.ttf", size=36)
    try:
        text1, text2 = text.replace(", ", ",").split(",")
    except ValueError:
        (
            text1,
            text2,
        ) = "tries to use surprised without splitting by comma,the command breaks".split(",")
    text1 = wrap(font, "me: " + text1, 650)
    text2 = wrap(font, "also me: " + text2, 650)
    canv = ImageDraw.Draw(base)
    render_text_with_emoji(self, base, canv, (20, 20), text1, font=font, fill="White")
    render_text_with_emoji(self, base, canv, (20, 140), text2, font=font, fill="White")
    base = base.convert("RGB")

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def sword(self, usernames, text):
    text = text.replace(", ", ",").split(",")
    if len(text) != 2:
        text = ["SPLIT BY", "COMMA"]
    base = Image.open(f"{bundled_data_path(self)}/images/sword.bmp")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/verdana.ttf", size=48)
    temp = Image.new("RGBA", (1200, 800), color=(0, 0, 0, 0))

    swordtext = wrap(font, text[0], 3000)
    food = wrap(font, text[1], 300)
    canv = ImageDraw.Draw(base)
    temp_draw = ImageDraw.Draw(temp)
    render_text_with_emoji(self, temp, temp_draw, (0, 0), swordtext, font=font, fill="White")
    temp = temp.rotate(-25, expand=1)
    render_text_with_emoji(self, base, canv, (330, 330), usernames[0], font=font, fill="White")

    base.paste(temp, (-30, 605), temp)

    size = canv.textsize(food, font=font)

    new_width = (base.width - size[0]) / 2

    render_text_with_emoji(self, base, canv, (new_width - 20, 830), food, font=font, fill="Black")

    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def theoffice(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/theoffice.png")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/verdana.ttf", size=28)
    canv = ImageDraw.Draw(base)

    left, right = text.replace(", ", ",").split(",", 2)

    render_text_with_emoji(self, base, canv, (125, 200), wrap(font, left, 200), font, "white")
    render_text_with_emoji(self, base, canv, (420, 250), wrap(font, right, 200), font, "white")

    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def thesearch(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/thesearch.bmp").convert("RGBA")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/sans.ttf", size=16)
    canv = ImageDraw.Draw(base)

    text = wrap(font, text, 178)
    render_text_with_emoji(self, base, canv, (65, 335), text, font=font, fill="Black")
    base = base.convert("RGB")

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def trash(self, avatar):
    avatar = Image.open(avatar).resize((483, 483)).convert("RGBA")
    base = Image.open(f"{bundled_data_path(self)}/images/trash.bmp").convert("RGBA")

    avatar = avatar.filter(ImageFilter.GaussianBlur(radius=6))
    base.paste(avatar, (480, 0), avatar)
    base = base.convert("RGBA")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def tweet(self, avatar, username0, username1, text):
    base = Image.open(f"{bundled_data_path(self)}/images/trump.bmp")
    avatar = Image.open(avatar).resize((98, 98)).convert("RGBA")
    font = ImageFont.truetype(
        f"{bundled_data_path(self)}/fonts/segoeuireg.ttf",
        size=50,
    )
    font2 = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/robotomedium.ttf", size=40)
    font3 = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/robotoregular.ttf", size=29)
    font4 = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/robotoregular.ttf", size=35)

    circle = Image.new("L", (20, 20), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, 20, 20), fill=255)
    alpha = Image.new("L", avatar.size, 255)
    w, h = avatar.size
    alpha.paste(circle.crop((0, 0, 10, 10)), (0, 0))
    alpha.paste(circle.crop((0, 10, 10, 10 * 2)), (0, h - 10))
    alpha.paste(circle.crop((10, 0, 10 * 2, 10)), (w - 10, 0))
    alpha.paste(circle.crop((10, 10, 10 * 2, 10 * 2)), (w - 10, h - 10))
    avatar.putalpha(alpha)

    base.paste(avatar, (42, 38), avatar)
    canv = ImageDraw.Draw(base)
    text2 = wrap(font2, username0, 1150)
    tag_raw = username1
    text3 = wrap(font3, f"@{tag_raw}", 1150)

    time = datetime.now().strftime("%-I:%M %p - %d %b %Y")
    retweets = "{:,}".format(randint(0, 99999))
    likes = "{:,}".format(randint(0, 99999))
    text4 = wrap(font3, time, 1150)
    text5 = wrap(font4, retweets, 1150)
    text6 = wrap(font4, likes, 1150)
    total_size = (45, 160)
    for i in text.split(" "):
        i += " "
        if i.startswith(("@", "#")):
            if total_size[0] > 1000:
                total_size = (45, total_size[1] + 65)
            render_text_with_emoji(self, base, canv, total_size, i, font=font, fill="#1b95e0")
            y = canv.textsize(i, font=font)
            total_size = (total_size[0] + y[0], total_size[1])
        else:
            if total_size[0] > 1000:
                total_size = (45, total_size[1] + 65)
            render_text_with_emoji(self, base, canv, total_size, i, font=font, fill="Black")
            y = canv.textsize(i, font=font)
            total_size = (total_size[0] + y[0], total_size[1])
    render_text_with_emoji(self, base, canv, (160, 45), text2, font=font2, fill="Black")
    render_text_with_emoji(self, base, canv, (160, 95), text3, font=font3, fill="Grey")
    render_text_with_emoji(self, base, canv, (40, 570), text4, font=font3, fill="Grey")
    render_text_with_emoji(self, base, canv, (40, 486), text5, font=font4, fill="#2C5F63")
    render_text_with_emoji(self, base, canv, (205, 486), text6, font=font4, fill="#2C5F63")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def ugly(self, avatar):
    base = Image.open(f"{bundled_data_path(self)}/ugly/ugly.bmp").convert("RGBA")
    avatar = Image.open(avatar).resize((175, 175)).convert("RGBA")
    base.paste(avatar, (120, 55), avatar)
    base = base.convert("RGBA")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def unpopular(self, avatar, text):
    avatar = Image.open(avatar).resize((666, 666)).convert("RGBA")
    base = Image.open(f"{bundled_data_path(self)}/images/unpopular_unpopular.bmp").convert("RGBA")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/semibold.woff", size=100)
    reticle = Image.open(f"{bundled_data_path(self)}/images/unpopular_reticle.bmp").convert("RGBA")
    temp = Image.new("RGBA", (1200, 800), color=(0, 0, 0, 0))
    avatar_square = Image.new(mode="RGBA", size=(360, 270), color=(0, 0, 0, 0))
    avatar_mono = avatar.resize((300, 310)).rotate(16, expand=1).convert("1")
    avatar_darkened = ImageEnhance.Brightness(avatar_mono.convert("RGB")).enhance(0.5)
    avatar_square.paste(avatar_darkened, (0, 0), avatar_mono)

    bigsize = (avatar.size[0] * 3, avatar.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(avatar.size, Image.ANTIALIAS)
    avatar.putalpha(mask)

    base.paste(avatar, (1169, 1169), avatar)
    face = avatar.resize((368, 368))
    base.paste(face, (140, 250), face)
    base.paste(reticle, (1086, 1086), reticle)
    base.paste(avatar_square, (-20, 1670), avatar_square)
    canv = ImageDraw.Draw(temp)
    wrapped = wrap(font, text, 1150)
    render_text_with_emoji(self, temp, canv, (0, 0), wrapped, font, "black")
    w = temp.rotate(1, expand=1)
    base.paste(w, (620, 280), w)
    base = base.convert("RGBA")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def violence(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/violence.jpg")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/arimobold.ttf", size=24)
    canv = ImageDraw.Draw(base)
    render_text_with_emoji(self, base, canv, (355, 0), wrap(font, text, 270), font, "black")

    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def violentsparks(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/violentsparks.bmp")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/medium.woff", size=36)
    canv = ImageDraw.Draw(base)
    try:
        me, sparks = text.replace(" ,", ",", 1).split(",", 1)
    except ValueError:
        sparks = "me"
        me = "Dank Memer being mad that I forgot to split my text with a comma"
    me = wrap(font, me, 550)
    sparks = wrap(font, sparks, 200)
    render_text_with_emoji(self, base, canv, (15, 5), me, font=font, fill="White")
    render_text_with_emoji(self, base, canv, (350, 430), sparks, font=font, fill="Black")

    base = base.convert("RGB")
    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def vr(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/vr.bmp").convert("RGBA")
    # We need a text layer here for the rotation
    font, text = auto_text_size(
        text, ImageFont.truetype(f"{bundled_data_path(self)}/fonts/sans.ttf"), 207, font_scalar=0.8
    )
    canv = ImageDraw.Draw(base)
    w, _ = canv.textsize(text, font)
    render_text_with_emoji(
        self, base, canv, (int((170 - (w / 2))), 485), text, font=font, fill="Black"
    )
    base = base.convert("RGB")

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def walking(self, text):
    base = Image.open(f"{bundled_data_path(self)}/images/walking.bmp")

    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/sans.ttf", size=50)
    canv = ImageDraw.Draw(base)
    text = wrap(font, text, 1000)
    render_text_with_emoji(self, base, canv, (35, 35), text, font=font, fill="black")

    base = base.convert("RGB")

    b = BytesIO()
    base.save(b, format="jpeg")
    b.seek(0)
    return b


def wanted(self, avatar):
    base = Image.open(f"{bundled_data_path(self)}/images/wanted.bmp").convert("RGBA")
    avatar = Image.open(avatar).resize((447, 447)).convert("RGBA")
    base.paste(avatar, (145, 282), avatar)

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def warp(self, avatar):
    implode = "-{}".format(str(randint(3, 15)))
    roll = "+{}+{}".format(randint(0, 256), randint(0, 256))
    swirl = "{}{}".format(choice(["+", "-"]), randint(120, 180))
    concat = ["-implode", implode, "-roll", roll, "-swirl", swirl]

    output = gm.convert(Image.open(avatar), concat, "png")

    b = BytesIO(output)
    b.seek(0)
    return b


def whodidthis(self, avatar):
    base = Image.open(f"{bundled_data_path(self)}/images/whodidthis.bmp")
    avatar = Image.open(avatar).resize((720, 405)).convert("RGBA")
    base.paste(avatar, (0, 159), avatar)
    base = base.convert("RGBA")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def whothisis(self, avatar, text):
    base = Image.open(f"{bundled_data_path(self)}/images/whothisis.bmp")
    avatar = Image.open(avatar).resize((215, 215)).convert("RGBA")
    font = ImageFont.truetype(f"{bundled_data_path(self)}/fonts/arimobold.ttf", size=40)
    base.paste(avatar, (523, 15), avatar)
    base.paste(avatar, (509, 567), avatar)
    base = base.convert("RGBA")

    canv = ImageDraw.Draw(base)
    render_text_with_emoji(self, base, canv, (545, 465), text, font=font, fill="White")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b


def youtube(self, avatar, text, username):
    avatar = Image.open(avatar).resize((52, 52)).convert("RGBA")
    name = username
    base = Image.open(f"{bundled_data_path(self)}/youtube/youtube.bmp").convert("RGBA")
    font = ImageFont.truetype(
        f"{bundled_data_path(self)}/fonts/robotomedium.ttf",
        size=17,
    )
    font2 = ImageFont.truetype(
        f"{bundled_data_path(self)}/fonts/robotoregular.ttf",
        size=17,
    )
    font3 = ImageFont.truetype(
        f"{bundled_data_path(self)}/fonts/robotoregular.ttf",
        size=19,
    )

    bigsize = (avatar.size[0] * 3, avatar.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(avatar.size, Image.ANTIALIAS)
    avatar.putalpha(mask)

    base.paste(avatar, (17, 33), avatar)
    canv = ImageDraw.Draw(base)
    op = wrap(font, name, 1150)
    size = canv.textsize(name, font=font)
    comment = wrap(font3, text, 550)
    num = randint(1, 59)
    plural = "" if num == 1 else "s"
    time = f"{num} minute{plural} ago"
    render_text_with_emoji(self, base, canv, (92, 34), op, font=font, fill="Black")
    render_text_with_emoji(self, base, canv, (100 + size[0], 34), time, font=font2, fill="Grey")
    render_text_with_emoji(self, base, canv, (92, 59), comment, font=font3, fill="Black")
    base = base.convert("RGBA")

    b = BytesIO()
    base.save(b, format="png")
    b.seek(0)
    return b

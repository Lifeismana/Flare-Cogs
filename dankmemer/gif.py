from io import BytesIO

from PIL import Image, ImageOps
from random import randint

from redbot.core.data_manager import bundled_data_path


def airpods(self, avatar):
    blank = Image.new("RGBA", (400, 128), (255, 255, 255, 0))
    avatar = Image.open(BytesIO(avatar)).convert("RGBA").resize((128, 128))
    left = Image.open(f"{bundled_data_path(self)}/images/airpods_left.gif")
    right = Image.open(f"{bundled_data_path(self)}/images/airpods_right.gif")
    out = []
    for i in range(0, left.n_frames):
        left.seek(i)
        right.seek(i)
        f = blank.copy().convert("RGBA")
        l = left.copy().convert("RGBA")
        r = right.copy().convert("RGBA")
        f.paste(l, (0, 0), l)
        f.paste(avatar, (136, 0), avatar)
        f.paste(r, (272, 0), r)
        out.append(f.resize((400, 128), Image.LANCZOS).convert("RGBA"))

    b = BytesIO()
    out[0].save(
        b,
        format="gif",
        save_all=True,
        append_images=out[1:],
        loop=0,
        disposal=2,
        optimize=True,
        duration=30,
        transparency=0,
    )
    b.seek(0)
    return b


def america(self, avatar):
    img1 = Image.open(BytesIO(avatar)).convert("RGBA").resize((480, 480))
    img2 = Image.open(f"{bundled_data_path(self)}/images/america.gif")
    img1.putalpha(128)

    out = []
    for i in range(0, img2.n_frames):
        img2.seek(i)
        f = img2.copy().convert("RGBA").resize((480, 480))
        f.paste(img1, (0, 0), img1)
        out.append(f.resize((256, 256)))

    b = BytesIO()
    out[0].save(
        b,
        format="gif",
        save_all=True,
        append_images=out[1:],
        loop=0,
        disposal=2,
        optimize=True,
        duration=30,
    )
    b.seek(0)
    return b


def communism(self, avatar):
    img1 = Image.open(BytesIO(avatar)).convert("RGBA").resize((300, 300))
    img2 = Image.open(f"{bundled_data_path(self)}/images/communism.gif")
    img1.putalpha(96)

    out = []
    for i in range(0, img2.n_frames):
        img2.seek(i)
        f = img2.copy().convert("RGBA").resize((300, 300))
        f.paste(img1, (0, 0), img1)
        out.append(f.resize((256, 256)))

    b = BytesIO()
    out[0].save(
        b,
        format="gif",
        save_all=True,
        append_images=out[1:],
        loop=0,
        disposal=2,
        optimize=True,
        duration=40,
    )
    img2.close()
    b.seek(0)
    return b


def dank(self, avatar):
    avatar = Image.open(BytesIO(avatar)).resize((320, 320)).convert("RGBA")

    horn = (
        Image.open("/images/dank_horn.bmp")
        .convert("RGBA")
        .resize((100, 100))
        .rotate(315, resample=Image.BICUBIC)
    )
    horn2 = ImageOps.mirror(horn.copy().resize((130, 130)).rotate(350, resample=Image.BICUBIC))
    hit = (
        Image.open(f"{bundled_data_path(self)}/images/dank_hit.bmp")
        .convert("RGBA")
        .resize((40, 40))
    )
    gun = (
        Image.open(f"{bundled_data_path(self)}/images/dank_gun.bmp")
        .convert("RGBA")
        .resize((250, 205))
    )
    faze = (
        Image.open(f"{bundled_data_path(self)}/images/dank_faze.bmp")
        .convert("RGBA")
        .resize((60, 40))
    )

    blank = Image.new("RGBA", (256, 256), color=(254, 0, 0))
    blank.paste(avatar, (-20, -20), avatar)
    # blank.paste(overlay, None, overlay)
    frames = []

    for i in range(8):
        base = blank.copy()
        if i == 0:
            base.paste(horn, (175, 0), horn)
            base.paste(horn2, (-60, 0), horn2)
            base.paste(hit, (90, 65), hit)
            base.paste(gun, (120, 130), gun)
            base.paste(faze, (5, 212), faze)
        else:
            base.paste(horn, (165 + randint(-8, 8), randint(0, 12)), horn)
            base.paste(horn2, (-50 + randint(-6, 6), randint(-2, 10)), horn2)
            base.paste(hit, (110 + randint(-30, 30), 55 + randint(-30, 30)), hit)
            base.paste(gun, (120, 130), gun)
            base.paste(faze, (12 + randint(-6, 6), 210 + randint(-2, 10)), faze)

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


def trigger(self, avatar):
    avatar = Image.open(BytesIO(avatar)).resize((320, 320)).convert("RGBA")
    triggered = Image.open(f"{bundled_data_path(self)}/images/triggered_triggered.bmp")
    tint = Image.open(f"{bundled_data_path(self)}/images/triggered_red.bmp").convert("RGBA")
    blank = Image.new("RGBA", (256, 256), color=(231, 19, 29))
    frames = []

    for i in range(8):
        base = blank.copy()

        if i == 0:
            base.paste(avatar, (-16, -16), avatar)
        else:
            base.paste(avatar, (-32 + randint(-16, 16), -32 + randint(-16, 16)), avatar)

        base.paste(tint, (0, 0), tint)

        if i == 0:
            base.paste(triggered, (-10, 200))
        else:
            base.paste(triggered, (-12 + randint(-8, 8), 200 + randint(0, 12)))

        frames.append(base)

    b = BytesIO()
    frames[0].save(
        b,
        save_all=True,
        append_images=frames[1:],
        format="gif",
        loop=0,
        duration=20,
        disposal=2,
        optimize=True,
    )
    b.seek(0)
    return b

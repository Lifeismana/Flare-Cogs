import uuid

from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, ColorClip
from moviepy.video.fx.rotate import rotate

from redbot.core.data_manager import bundled_data_path


def kowalski(self, text):
    name = f"{bundled_data_path(self)}/{uuid.uuid4().hex}.gif"

    clip = VideoFileClip(f"{bundled_data_path(self)}/images/kowalski.gif")
    text = TextClip(
        text,
        fontsize=36,
        method="caption",
        size=(245, None),
        align="West",
        color="black",
        stroke_color="black",
        stroke_width=1,
        font=f"{bundled_data_path(self)}/fonts/verdana.ttf",
    ).set_duration(clip.duration)
    text = text.set_position((340, 65)).set_duration(clip.duration)
    text = rotate(text, angle=10, resample="bilinear")

    video = CompositeVideoClip([clip, text]).set_duration(clip.duration)

    video.write_gif(name)
    clip.close()
    video.close()
    return name


def letmein(self, text):
    name = f"{bundled_data_path(self)}/{uuid.uuid4().hex}"
    name_mp4 = name + ".mp4"
    name_mp3 = name + ".mp3"
    if len(text) >= 400:
        text = text[:400] + "..."

    clip = VideoFileClip(f"{bundled_data_path(self)}/video/letmein.mp4")

    textclip = TextClip(
        txt=text,
        bg_color="White",
        fontsize=32,
        font=f"{bundled_data_path(self)}/fonts/verdana.ttf",
        method="caption",
        align="west",
        size=(clip.size[0], None),
    ).set_duration(clip.duration)

    color = ColorClip(
        (clip.size[0], textclip.size[1]), color=(255, 255, 255), ismask=False
    ).set_duration(clip.duration)

    video = CompositeVideoClip(
        [clip.set_position(("center", textclip.size[1])), color, textclip],
        size=(clip.size[0], textclip.size[1] + clip.size[1]),
    )

    video.write_videofile(name_mp4, threads=1, preset="superfast", verbose=False, temp_audiofile=name_mp3)
    clip.close()
    video.close()
    return name_mp4

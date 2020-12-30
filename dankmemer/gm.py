import subprocess


def convert(img_bytes, args: list, output_format: str):
    args = ["gm", "convert", "-"] + args + ["{}:-".format(output_format)]

    proc = subprocess.Popen(
        args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE
    )
    stdout, stderr = proc.communicate(img_bytes)
    return stdout


def radial_blur(img_bytes, degrees: int, output_format: str):
    args = [
        "convert",
        "-",
        "-rotational-blur",
        str(degrees),
        "{}:-".format(output_format),
    ]
    proc = subprocess.Popen(
        args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE
    )
    stdout, stderr = proc.communicate(img_bytes)
    return stdout

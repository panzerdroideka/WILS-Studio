from PIL import Image
from pathlib import Path


def export_youtube_shorts(input_file):

    target_width = 1440
    target_height = 2560
    target_ratio = target_width / target_height

    image = Image.open(input_file)

    width, height = image.size

    source_ratio = width / height

    if source_ratio > target_ratio:

        new_width = int(height * target_ratio)

        left = (width - new_width) // 2
        top = 0
        right = left + new_width
        bottom = height

    else:

        new_height = int(width / target_ratio)

        left = 0
        top = (height - new_height) // 2
        right = width
        bottom = top + new_height

    cropped = image.crop(
        (
            left,
            top,
            right,
            bottom,
        )
    )

    resized = cropped.resize(
        (
            target_width,
            target_height,
        ),
        Image.Resampling.LANCZOS,
    )

    output_file = (
        Path(input_file).stem
        + "_YT_SHORTS_1440x2560.png"
    )

    resized.save(output_file)

    print()
    print("Ferdig:")
    print(output_file)


if __name__ == "__main__":

    file_path = input(
        "Bildefil: "
    ).strip()

    export_youtube_shorts(file_path)

# crop_estimator.py

PROFILES = {
    "YouTube Shorts 9:16": 9 / 16,
    "Desktop 3200×1800": 16 / 9,
    "YouTube 4K": 16 / 9,
    "Album Cover": 1.0,
}


def crop_percent(width, height, target_ratio):

    source_ratio = width / height

    if abs(source_ratio - target_ratio) < 0.0001:
        return 0.0

    # Kilde bredere enn mål
    if source_ratio > target_ratio:

        required_width = height * target_ratio

        kept_fraction = required_width / width

        crop = (1.0 - kept_fraction) * 100

    # Kilde smalere enn mål
    else:

        required_height = width / target_ratio

        kept_fraction = required_height / height

        crop = (1.0 - kept_fraction) * 100

    return round(crop, 1)


def crop_status(crop):

    if crop <= 10:
        return "🟢 Lav"

    if crop <= 25:
        return "🟡 Moderat"

    if crop <= 40:
        return "🟠 Høy"

    return "🔴 Ekstrem"


def analyze_crop(width, height):

    results = []

    for profile_name, ratio in PROFILES.items():

        crop = crop_percent(
            width,
            height,
            ratio
        )

        results.append({
            "name": profile_name,
            "crop": crop,
            "status": crop_status(crop),
        })

    return results

# analyzer.py

PROFILES = {
    "YouTube Shorts 9:16": {
        "ratio": 9 / 16,
        "target": "2160 × 3840"
    },

    "Desktop 3200×1800": {
        "ratio": 16 / 9,
        "target": "3200 × 1800"
    },

    "YouTube 4K": {
        "ratio": 16 / 9,
        "target": "3840 × 2160"
    },

    "Album Cover": {
        "ratio": 1.0,
        "target": "3000 × 3000"
    }
}


def score_profile(image_ratio, profile_ratio):

    diff_percent = abs(
        image_ratio - profile_ratio
    ) / profile_ratio * 100

    score = max(0, round(100 - diff_percent))

    return score, diff_percent


def classify(score):

    if score >= 95:
        return "🟢 GRØNN"

    if score >= 80:
        return "🟡 GUL"

    if score >= 50:
        return "🟠 RØD"

    return "⛔ STOPP"


def analyze_image(width, height):

    image_ratio = width / height

    results = []

    for profile_name, profile in PROFILES.items():

        score, diff = score_profile(
            image_ratio,
            profile["ratio"]
        )

        results.append(
            {
                "name": profile_name,
                "score": score,
                "difference": diff,
                "target": profile["target"],
                "status": classify(score)
            }
        )

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    best = results[0]

    return best, results

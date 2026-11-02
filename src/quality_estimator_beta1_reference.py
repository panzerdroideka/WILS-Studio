# quality_estimator.py

PROFILES = {
    "YouTube Shorts 9:16": (1440, 2560),
    "Desktop 3200×1800": (3200, 1800),
    "YouTube 4K": (3840, 2160),
    "Album Cover": (3000, 3000),
}


def quality_status(scale_factor):

    if scale_factor >= 1.0:
        return "🟢 Ingen oppskalering"

    if scale_factor >= 0.8:
        return "🟢 Høy kvalitet"

    if scale_factor >= 0.6:
        return "🟡 God kvalitet"

    if scale_factor >= 0.4:
        return "🟠 Synlig kvalitetstap"

    return "🔴 Krever oppskalering"


def analyze_quality(width, height):

    results = []

    for profile_name, (target_w, target_h) in PROFILES.items():

        scale_x = width / target_w
        scale_y = height / target_h

        scale_factor = min(scale_x, scale_y)

        results.append({
            "name": profile_name,
            "status": quality_status(scale_factor),
            "factor": round(scale_factor, 2),
            "target": f"{target_w}×{target_h}",
        })

    return results

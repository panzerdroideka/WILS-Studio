WILS Studio
WILS Studio is a lightweight image analysis and export tool built in Python.

The project helps creators evaluate and prepare images for:

YouTube Shorts (9:16)
YouTube 4K
Desktop wallpapers
Album covers
Features
Profile Analysis
Analyzes an image and recommends the most suitable target format.

Crop Estimation
Calculates how much of the original image must be cropped to fit a target format.

Quality Estimation
Evaluates image quality after resizing and indicates when upscaling may be required.

Shorts Export
Automatically:

Crops to 9:16
Resizes to 1440×2560
Saves a finished YouTube Shorts image
Project Structure
main.py
GUI application

analyzer.py
Profile scoring and recommendations

crop_estimator.py
Crop calculations

quality_estimator.py
Quality evaluation

profiles.py
Central profile definitions

shorts_export.py
YouTube Shorts exporter
Requirements
pip install PyQt6 Pillow
Run GUI
python3 main.py
Export YouTube Shorts
python3 shorts_export.py
Current Status
Version: 1.0

The project currently supports:

Image analysis
Crop estimation
Quality estimation
YouTube Shorts export
Future versions may include additional export formats and image processing workflows.

Author
Wils / Panzerdroideka

This is the Way!


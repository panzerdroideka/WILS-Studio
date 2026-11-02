< WILS Studio >

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

This is the Way!

Author
Wils / Panzerdroideka

Here i present my first use of this tool!

The First publication with this graphics tool used to crop and Upscayl this image  and make it useful to a YouTube Short Album Cover-Art
<img width="1339" height="1730" alt="VåreBlaff_v3språk-218bpm" src="https://github.com/user-attachments/assets/18c7daf3-d19a-485a-9727-afb259763046" />

After using this Graphics tool on thise here picture i got this picture to my tune "Our Brief Encounters-Våre korte blaff"
<img width="1333" height="1747" alt="Screenshot_20261102_215828" src="https://github.com/user-attachments/assets/72957277-7cf3-4d28-96c2-e0c07ad3a16b" />

Wils@NorseDiscoveries


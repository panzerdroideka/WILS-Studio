import sys
from pathlib import Path

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QFileDialog,
    QLabel,
    QVBoxLayout,
    QGroupBox,
    QProgressBar,
)

from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from PIL import Image

from analyzer import analyze_image
from crop_estimator import analyze_crop


class WILSStudio(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("WILS Image Preparation Studio")
        self.resize(1100, 850)

        self.current_pixmap = None

        self.button = QPushButton("Velg bilde")
        self.button.clicked.connect(self.select_image)

        # ------------------------
        # BESTE MATCH
        # ------------------------

        self.best_match = QLabel(
            "Ingen fil valgt."
        )

        self.best_match.setWordWrap(True)

        best_group = QGroupBox("BESTE MATCH")

        best_layout = QVBoxLayout()
        best_layout.addWidget(self.best_match)

        best_group.setLayout(best_layout)

        # ------------------------
        # PROFILER
        # ------------------------

        self.profile_labels = []
        self.profile_bars = []

        profile_group = QGroupBox("PROFILER")

        profile_layout = QVBoxLayout()

        for _ in range(4):

            label = QLabel("-")

            bar = QProgressBar()
            bar.setRange(0, 100)

            self.profile_labels.append(label)
            self.profile_bars.append(bar)

            profile_layout.addWidget(label)
            profile_layout.addWidget(bar)

        profile_group.setLayout(profile_layout)

        # ------------------------
        # CROP ESTIMAT
        # ------------------------

        self.crop_labels = []

        crop_group = QGroupBox("CROP ESTIMAT")

        crop_layout = QVBoxLayout()

        for _ in range(4):

            label = QLabel("-")

            self.crop_labels.append(label)

            crop_layout.addWidget(label)

        crop_group.setLayout(crop_layout)

        # ------------------------
        # TEKNISKE DATA
        # ------------------------

        self.details = QLabel(
            "Ingen fil valgt."
        )

        self.details.setWordWrap(True)

        details_group = QGroupBox("TEKNISKE DATA")

        details_layout = QVBoxLayout()
        details_layout.addWidget(self.details)

        details_group.setLayout(details_layout)

        # ------------------------
        # FORHÅNDSVISNING
        # ------------------------

        self.preview_title = QLabel("")
        self.preview_title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.preview = QLabel("")
        self.preview.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        # ------------------------
        # LAYOUT
        # ------------------------

        layout = QVBoxLayout()

        layout.addWidget(self.button)

        layout.addWidget(best_group)
        layout.addWidget(profile_group)
        layout.addWidget(crop_group)
        layout.addWidget(details_group)

        layout.addWidget(self.preview_title)
        layout.addWidget(self.preview)

        self.setLayout(layout)

    def resizeEvent(self, event):

        super().resizeEvent(event)

        if self.current_pixmap:
            self.update_preview()

    def update_preview(self):

        if not self.current_pixmap:
            return

        scaled = self.current_pixmap.scaled(
            self.width() - 60,
            int(self.height() * 0.45),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

        self.preview.setPixmap(scaled)

    def select_image(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Velg bildefil",
            str(Path.home()),
            "Bilder (*.png *.jpg *.jpeg *.webp *.bmp *.tif *.tiff)"
        )

        if not file_path:
            return

        try:

            with Image.open(file_path) as img:
                width, height = img.size

            aspect = width / height

            if height > width:
                orientation = "Vertikal"
            elif width > height:
                orientation = "Horisontal"
            else:
                orientation = "Kvadratisk"

            best, rankings = analyze_image(
                width,
                height
            )

            crop_data = analyze_crop(
                width,
                height
            )

            self.best_match.setText(
                f"""
Profil: {best['name']}

Score: {best['score']}/100

Status: {best['status']}

Anbefalt mål:
{best['target']}
"""
            )

            for index, item in enumerate(rankings[:4]):

                self.profile_labels[index].setText(
                    item["name"]
                )

                self.profile_bars[index].setValue(
                    item["score"]
                )

            for index, item in enumerate(crop_data[:4]):

                self.crop_labels[index].setText(
                    f"{item['name']}  |  "
                    f"{item['status']}  |  "
                    f"{item['crop']} %"
                )

            self.details.setText(
                f"""
Fil:
{Path(file_path).name}

Oppløsning:
{width} × {height}

Orientering:
{orientation}

Aspect ratio:
{aspect:.4f}
"""
            )

            self.current_pixmap = QPixmap(file_path)

            self.preview_title.setText(
                "FORHÅNDSVISNING"
            )

            self.update_preview()

        except Exception as error:

            self.details.setText(
                f"Feil under analyse:\n{error}"
            )


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = WILSStudio()
    window.show()

    sys.exit(app.exec())

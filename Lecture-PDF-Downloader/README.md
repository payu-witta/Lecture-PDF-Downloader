# CS240 Lecture Downloader

This repository contains a simple Python script to automate the download of lecture PDFs from a course website.

## Features
Automatically downloads PDFs from a series of numbered URLs
Saves the files locally into a specified folder
Efficiently handles missing or inaccessible files

## Instructions

1. Clone this repository:
git clone https://github.com/payu-witta/Lecture-PDF-Downloader.git

2. Navigate into the project folder:
cd Lecture-PDF-Downloader

3. Install the required Python Library:
pip install -r requirements.txt

4. Update the `base_url` and `destination` variables in `download_lectures.py` to fit your use case:
```python
base_url = "https://example.com/lectures/lecture"
destination = r"C:\path\to\your\folder"

5. Run the script:
python download_lectures.py

## Notes
Ensure that the PDFs follow a pattern similar to lecture1.pdf, lecture2.pdf, ..., lecture33.pdf with some iterable
This script is intended for publicly accessible files only

## License
This project is licensed under the MIT License - see the LICENSE file for details

## Disclaimer
This script is intended for downloading publicly available files with proper authorization
Please ensure you have permission to download and use any content
"""
Lecture PDF Downloader
Downloads a series of PDFs automatically into a specified folder
One common example is to use this to download lecture PDFs from a certain domain
They are commonly in the same format each time, 
with a certain index changing successively each lecture

It is advantageous in reducing tedious work when downloading lecture PDFs
over a very large range

I used this program to download the Sp---- 20-- lecture slides for self-studying prior to the Fall 2025 semester at UMass Amherst
from Prof. Andrew Shiting Lan and Prof. Nic Herdon
for COMPSCI 2--: --------- ----- -----------
"""

# github.com/payu-witta/Lecture-PDF-Downloader

import os
import requests

def download_lectures(base_url, destination_folder, start=1, end=33):
    """_summary_
    Download lecture PDFs from base_url

    Args:
        base_url (str): Base URL without lecture number and extension.
        destination_folder (str): Folder to save downloaded files.
        start (int): Starting lecture number (inclusive). Defaults to 1.
        end (int): Ending lecture number (inclusive). Defaults to 33.
    """
    os.makedirs(destination_folder, exist_ok=True)
    
    for i in range(start, end + 1):
        url = f'{base_url}{i}.pdf'
        filename = f'lecture{i}.pdf'
        filepath = os.path.join(destination_folder, filename)
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
                
            print(f"Downloaded {filename}")
            
        except Exception as e:
            print(f"Failed to download {filename}: {e}")

if __name__ == "__main__":
    # Set your base URL and destination folder here
    base_url = "https://example.com/lectures/lecture" # <-- MODIFY THIS
    destination = r"C:\path\to\your\folder" # <-- MODIFY THIS
    download_lectures(base_url, destination)
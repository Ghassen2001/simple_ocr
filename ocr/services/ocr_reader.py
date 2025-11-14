# ocrapp/services/ocr_reader.py

import easyocr
from django.conf import settings
import os

# Load languages once (improves performance)
reader = easyocr.Reader(['fr', 'en'])
 # add what you need

def extract_text(image_path):
    """
    Returns list of text strings from the image.
    """
    results = reader.readtext(image_path, detail=0)
    return results


def extract_text_with_boxes(image_path):
    """
    Returns list of (bounding_box, text, confidence)
    """
    results = reader.readtext(image_path, detail=1)
    return results

import os
import time
import logging
from PIL import ImageGrab
from datetime import datetime

def take_screenshots(interval=1):
    """
    Takes screenshots every `interval` seconds and saves them in the 'screenshots' folder.
    """
    directory = "screenshots"
    if not os.path.exists(directory):
        os.makedirs(directory)

    try:
        while True:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(directory, f"screenshot_{timestamp}.png")
            screenshot = ImageGrab.grab()
            screenshot.save(filename)
            logging.info(f"Screenshot saved as {filename}")
            time.sleep(interval)
    except KeyboardInterrupt:
        logging.info("Stopped taking screenshots.")

# Example usage:
# take_screenshots(interval=1)
import os
import logging

# Configure logging to display debug-level messages with timestamps
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Create directories for storing audio recordings, screenshots, notes, and snippets if they don't already exist
directories = ["audiorecords", "screenshots", "notes", "snippets"]

for directory in directories:
    try:
        os.makedirs(directory, exist_ok=True)
        logging.info(f"Directory {directory} created or already exists.")
    except OSError as e:
        logging.error(f"Error creating directory {directory}: {e}")
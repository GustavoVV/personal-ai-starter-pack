import wave
import os
from datetime import datetime
from modules.constants import CHANNELS, FS
import logging
import json

def create_audio_file(recording):
    """
    Creates an audio file from the recording.
    """
    directory = "audiorecords"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(directory, f"audio_{timestamp}.wav")

    with wave.open(filename, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)
        wf.setframerate(FS)
        wf.writeframes(recording)

    file_size = os.path.getsize(filename)
    logging.debug(f"Audio file {filename} saved with size {file_size} bytes.")
    return filename

def save_interaction_to_file(transcription, response):
    """
    Saves the interaction (transcription and response) to a JSON file.
    """
    interaction = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "transcription": transcription,
        "response": response
    }

    directory = "interactions"
    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = os.path.join(directory, "interactions.json")

    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = json.load(file)
    else:
        data = []

    data.append(interaction)

    with open(filename, "w") as file:
        json.dump(data, file, indent=2)

    logging.debug(f"Interaction saved to {filename}")
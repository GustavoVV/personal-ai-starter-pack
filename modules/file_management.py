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

def save_interaction_to_file(transcription, response, folder="notes", filename="interactions"):
    """
    Save the transcription and response to a file.
    """
    if not os.path.exists(folder):
        os.makedirs(folder)

    file_path = os.path.join(folder, f"{filename}.json")

    interaction = {
        "timestamp": datetime.now().isoformat(),
        "transcription": transcription,
        "response": response
    }

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
    else:
        data = []

    data.append(interaction)

    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)
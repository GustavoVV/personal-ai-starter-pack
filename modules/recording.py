import time
import sounddevice as sd
import threading
import logging
import pyaudio
import numpy as np
import os
import wave
from datetime import datetime

def record_audio(duration, fs, channels):
    """
    Simple function to record audio from the microphone.
    Gives you DURATION seconds of audio to speak into the microphone.
    After DURATION seconds, the recording will stop.
    Hit enter to stop the recording at any time.
    """
    logging.info("Starting audio recording...")
    recording = sd.rec(
        int(duration * fs), samplerate=fs, channels=channels, dtype="int16"
    )

    def duration_warning():
        time.sleep(duration)
        if not stop_event.is_set():
            logging.warning("Record limit hit - your assistant won't hear what you're saying now. Increase the duration.")

    stop_event = threading.Event()
    warning_thread = threading.Thread(target=duration_warning)
    warning_thread.daemon = True  # Set the thread as daemon so it doesn't block program exit
    warning_thread.start()

    input("Press Enter to stop recording...")
    stop_event.set()
    sd.stop()

    logging.info("Recording complete.")
    return recording

def record_computer_audio(duration, fs, channels, threshold=500):
    """
    Function to record audio from the computer's output.
    Only saves the recording if there is significant audio activity.
    """
    logging.info("Starting computer audio recording...")
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=channels, rate=fs, input=True, frames_per_buffer=1024)

    frames = []
    silent_frames = 0

    for _ in range(0, int(fs / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)
        audio_data = np.frombuffer(data, dtype=np.int16)
        if np.max(audio_data) < threshold:
            silent_frames += 1

    stream.stop_stream()
    stream.close()
    p.terminate()

    if silent_frames < len(frames) * 0.9:  # Save only if less than 90% of the frames are silent
        logging.info("Significant audio detected, saving recording.")
        save_computer_audio(frames, fs, channels)
    else:
        logging.info("No significant audio detected, discarding recording.")

def save_computer_audio(frames, fs, channels):
    """
    Saves the recorded computer audio to a file.
    """
    directory = "audiosfrompc"
    if not os.path.exists(directory):
        os.makedirs(directory)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(directory, f"computer_audio_{timestamp}.wav")

    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))

    file_size = os.path.getsize(filename)
    logging.debug(f"Computer audio file {filename} saved with size {file_size} bytes.")

# Example usage:
# recording = record_audio(duration=10, fs=44100, channels=2)
# computer_audio = record_computer_audio(duration=10, fs=44100, channels=2)
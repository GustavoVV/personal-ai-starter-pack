import time
import sounddevice as sd
import threading
import logging

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
import os
import time
import logging
import subprocess
from datetime import datetime
from typing import List
from dotenv import load_dotenv
from modules.typings import Interaction
from modules.constants import DURATION, FS, CHANNELS, CONVO_TRAIL_CUTOFF, ASSISTANT_TYPE
from modules.recording import record_audio
from modules.file_management import create_audio_file, save_interaction_to_file
from modules.prompt_builder import build_prompt
from assistants.assistants import GroqElevenPAF, OpenAIPAF

# Configure logging to display debug-level messages with timestamps
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from .env file
load_dotenv()

def main():
    """
    Main function to run the personal AI assistant.
    """
    previous_interactions: List[Interaction] = []

    if ASSISTANT_TYPE == "OpenAIPAF":
        assistant = OpenAIPAF()
        logging.info("Initialized OpenAI Personal AI Assistant...")
    elif ASSISTANT_TYPE == "GroqElevenPAF":
        assistant = GroqElevenPAF()
        logging.info("Initialized Groq-ElevenLabs Personal AI Assistant...")
    else:
        raise ValueError(f"Invalid assistant type: {ASSISTANT_TYPE}")

    assistant.setup()

    while True:
        try:
            input("Press Enter to start recording...")
            recording = record_audio(duration=DURATION, fs=FS, channels=CHANNELS)

            filename = create_audio_file(recording)
            transcription = assistant.transcribe(filename)

            logging.info(f"Input Transcription: '{transcription}'")

            prompt = build_prompt(transcription, previous_interactions)
            response = assistant.think(prompt)

            logging.info(f"AI Assistant Response: '{response}'")

            assistant.speak(response)

            os.remove(filename)

            # Save interaction to file
            save_interaction_to_file(transcription, response)

            # Update previous interactions
            previous_interactions.append(Interaction(role="human", content=transcription))
            previous_interactions.append(Interaction(role="assistant", content=response))

            # Keep only the last CONVO_TRAIL_CUTOFF interactions
            if len(previous_interactions) > CONVO_TRAIL_CUTOFF:
                previous_interactions = previous_interactions[-CONVO_TRAIL_CUTOFF:]

            logging.info("Ready for next interaction. Press Ctrl+C to exit.")
        except KeyboardInterrupt:
            logging.info("Exiting the program.")
            break

if __name__ == "__main__":
    main()

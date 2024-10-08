# Windows executable creator
   pyinstaller my_assistant.spec

# Fast Personal AI Assistant
> Fast TTS & STT
>
> A quick start personal AI assistant framework using OpenAI, Groq, and ElevenLabs.

![own-your-ai](./img/own-your-ai.png)

## Setup

### Create and activate virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
  ```

- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

- Set up environment variables:
  ```bash
  cp .env.sample .env
  # Edit .env file and add your API keys
  ```
  `I recommend starting with the OpenAI assistant since you only need to set up the OpenAI API key.`.

- Run the main script:
  ```bash
  python main.py
  ```

- Press `Enter` to start recording, and `Enter` again to stop recording.

- Adjust the maximum duration of the recording in `constants.py: DURATION`

- Update configuration variables in `constants.py`
  - Tweak naming.
  - Update the prompt to your liking.
  - Update the assistant type to the one you want to use.

## Watch the walk through video
[CONTROL your Personal AI Assistant with GPT-4o mini & ElevenLabs](https://youtu.be/ikaKpfUOb0U)

## Resources
- https://console.groq.com/docs/speech-text
- https://console.groq.com/docs/libraries
- https://platform.openai.com/docs/guides/speech-to-text
- https://platform.openai.com/docs/guides/text-to-speech
- https://platform.openai.com/docs/api-reference/audio#audio/createTranscription-prompt
- https://openai.com/api/pricing/

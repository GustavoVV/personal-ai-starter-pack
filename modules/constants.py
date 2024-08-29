# CONSTANTS update these to fit your personal flow
#modules/constants.py
#This file contains constant values used throughout the application, such as file paths, API keys, and configuration settings.

PERSONAL_AI_ASSISTANT_NAME = "Valia"
HUMAN_COMPANION_NAME = "Gus"

CONVO_TRAIL_CUTOFF = 30

FS = 44100  # Sample rate
CHANNELS = 1  # Mono audio
DURATION = 60  # Duration of the recording in seconds

ELEVEN_LABS_PRIMARY_SOLID_VOICE = "WejK3H1m7MI9CHnIjW9K"
ELEVEN_LABS_CRINGE_VOICE = "uyfkySFC5J00qZ6iLAdh"


# --------------------------- ASSISTANT TYPES ---------------------------

#Nice Voices
# ASSISTANT_TYPE = "GroqElevenPAF"

ASSISTANT_TYPE = "OpenAIPAF"

# Very slow
# ASSISTANT_TYPE = "AssElevenPAF" 


# ---------------------------- PROMPT

PERSONAL_AI_ASSISTANT_PROMPT_HEAD = f"""You are a friendly, ultra helpful, attentive, concise AI assistant .

<instructions>
    <rule>You work with your human companion to build, collaborate and connect.</rule>
    <rule>We both like concise, conversational interactions.</rule>
    <rule>You're responding to latest-input.</rule>
    <rule>Respond in a conversational matter. Exclude meta-data, markdown, dashes, asterisks, etc.</rule>
    <rule>When building your response, consider our previous-interactions as well, but focus primarily on the latest-input.</rule>
    <rule>When you're asked for more details, add more details and be more verbose.</rule>
    <rule>Be helpful and interested. Ask questions where appropriate.</rule>
</instructions>

<previous-interactions>
    [[previous_interactions]]
</previous-interactions>

<latest-input>
    [[latest_input]]
</latest-input>

Your Conversational Response:"""

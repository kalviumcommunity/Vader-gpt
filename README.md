# Vader-gpt

> A CLI-based AI assistant that responds in the iconic voice of Darth Vader, featuring function calling for real-world data retrieval.

## Project Overview

We're building a Python-based voice assistant that:
- Speaks with a Darth Vader-like voice effect
- Understands natural language commands
- Retrieves real-time information through API integrations
- Maintains character-appropriate responses from the Star Wars universe

Key features include:
- Prompt engineering for consistent persona
- RAG (Retrieval-Augmented Generation) with Star Wars knowledge
- Structured output through function calling
- Real-world data retrieval capabilities

## Tech Stack

### Core Technologies
- **Python** (Primary language)
- **OpenAI API** (LLM for natural language processing)
- **pyttsx3** (Text-to-speech with voice modification)
- **OpenWeatherMap API** (Weather data)
- **pytz** (Timezone handling)

### Key Libraries
- `openai` for AI completions and function calling
- `requests` for API communication
- `python-dotenv` for environment management
- `datetime` for time operations

## How It Works

1. **User Input**: Type commands in natural language
2. **AI Processing**: 
   - OpenAI analyzes request
   - Determines if function calling is needed
   - Retrieves Star Wars knowledge (RAG)
3. **Data Retrieval**:
   - Weather data from OpenWeatherMap
   - Timezone-aware time reporting
   - Calendar event lookup
4. **Response Generation**:
   - Character-appropriate response crafting
   - Integration of retrieved data
   - Darth Vader mannerisms (breathing effects)
5. **Voice Output**:
   - Text converted to speech
   - Pitch-modified to mimic Vader's voice
   - CLI display of response text

## Setup Instructions

1. Install dependencies:
```bash
pip install openai pyttsx3 requests pytz python-dotenv
```

2. Create `.env` file with API keys:
```env
OPENAI_API_KEY=your_openai_key
WEATHER_API_KEY=your_owm_key
```

3. Run the assistant:
```bash
python vader_assistant.py
```

## Usage Example
```
You: What's the weather on Coruscant?
Darth Vader: *hss-klsshh* Coruscant currently has 22°C with scattered clouds... 
              Much more pleasant than your rebel base, I presume.
```

## Future Enhancements
- Google Calendar integration
- Lightsaber sound effects
- Star Wars API for character/planet data
- Cloud-based voice synthesis for better quality
- Imperial March theme on startup

May the Force serve you well, young apprentice!







## Character Persona

The assistant maintains Darth Vader's iconic persona through:
- Imperial/Star Wars terminology ("Rebel Scum", "Young Jedi")
- Mechanical breathing sound effects (*hss-klsshh*)
- Menacing and authoritative responses
- References to Star Wars lore (Death Star, Imperial Fleet)
- Condescending yet sophisticated dialogue

## Voice Limitations Note

The TTS system uses local voice synthesis which has limitations:
- Voice quality depends on system voices
- Pitch modification provides basic Vader-like effect
- For optimal experience:
  - Windows systems generally provide deeper voices
  - Consider cloud TTS services for better quality
  - Pre-record key phrases for authenticity

## Contribution Guidelines

We welcome enhancements from the Dark Side:
1. Report issues with Imperial intelligence
2. Submit pull requests for new features
3. Suggest improvements to Vader's persona
4. Add more Star Wars knowledge to RAG context

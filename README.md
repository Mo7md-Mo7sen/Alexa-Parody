# Alexa (Parody)

A simple voice assistant built with Python using speech recognition and text-to-speech engines.

## Remainder 
Never feel overwhelmed by how big systems work. Just like I did with my Alexa (parody), you can take the **"divide and conquer"** approach. Remember, Alexa is just a combination of software and some hardware! By breaking down the complexity into manageable parts, you can build your own version of a voice assistant. Each component, from voice recognition to text-to-speech, can be tackled individually, making the process approachable and fun.



## Features
- Play YouTube videos by topic
- Tell the current time
- Provide information on a person using Wikipedia
- Share a joke
- Respond to basic questions and comments

## Requirements
- Python 3.x
- `speech_recognition` library
- `pyttsx3` library
- `pywhatkit` library
- `wikipedia` library
- `pyjokes` library

## Usage
1. Clone the repository or download the code.
2. Run the script using Python:
   ```bash
   python alexa.py
3. Speak a command to Alexa (Parody), such as "Play music" or "What time is it?"
   
## Code Structure
It's organized into several functions:

- talk(text): speaks out the given text using the text-to-speech engine
- take_command(): listens for a voice command and processes it
- run_assistant(): processes the command and performs the appropriate action
- The main loop runs Alexa (Parody) in an infinite loop, listening for commands and responding accordingly.
  
## Customization
You can customize Alexa (Parody) by modifying the run_assistant() function to add new commands or actions.





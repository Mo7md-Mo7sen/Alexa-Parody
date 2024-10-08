import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize the speech recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set the voice (0 for male, 1 for female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    """Speak out the text using the speech engine."""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listen for a voice command and process it."""
    try:
        with sr.Microphone() as source:
            print("Listening for a command...")
            listener.adjust_for_ambient_noise(source)  # Adjusts for background noise
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:  # Trigger word is now 'Alexa (parody)'
                command = command.replace('alexa', '').strip()  # Remove 'alexa' from the command
                print(f"Command received: {command}")
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        print("Network error.")
        return ""
    return command

def run_alexa():
    """Process the command and perform the appropriate action."""
    command = take_command()

    if command:
        if 'play' in command:
            # Extract the topic by removing the word 'play' from the command
            topic = command.replace('play', '').strip()
            # Perform a YouTube search for the topic and play a random video
            if topic:  # Ensure that a topic was extracted
                talk(f"Searching YouTube for {topic} videos.")
                pywhatkit.playonyt(topic)  # This will search YouTube for random videos about the topic
            else:
                talk("Sorry, I didn't catch the topic. Please say it again.")
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f'The current time is {current_time}')
        elif 'who is' in command:
            person = command.replace('who is', '').strip()
            try:
                about = wikipedia.summary(person, sentences=1)
                talk(about)
                print(about)
            except wikipedia.exceptions.DisambiguationError:
                talk('Please be more specific, multiple entries found.')
            except wikipedia.exceptions.PageError:
                talk('Sorry, I could not find information on that person.')
        elif 'date' in command:
            talk('I prefer to keep it professional, thank you!')
        elif 'are you single' in command:
            talk('I am currently focused on learning, no time for relationships!')
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            talk(joke)
            print(joke)
        else:
            talk('Sorry, I didn’t catch that. Could you repeat it?')

# Run the assistant in a loop
while True:
    run_alexa()
    
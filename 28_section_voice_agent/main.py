import speech_recognition as sr

def main():
    r = sr.Recognizer()  #speech to text

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 2

        print("speak something...")
        audio = r.listen(source)

        print("Processing Audio...(STT)")
        try:
            stt = r.recognize_google(audio)
            print("You said: ", stt)
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio. Please speak clearly and try again.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

main()
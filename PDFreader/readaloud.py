import pyttsx3

class ReadAloud:
    def __init__(self, text):
        self.text = text
        self.read_aloud()

    def read_aloud(self):
        return pyttsx3.speak(self.text)



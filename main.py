import pyttsx3

if __name__ == '__main__':
    print('Welcome to Robo Pronouncer !')

engine = pyttsx3.init()

while True:
    x = input("Enter your word to pronounce  :")
    print("Please press e to exit ")
    if x == "e":
        engine.say('your system is closed')
        engine.runAndWait()
        break
    engine.say(x)
    engine.runAndWait()

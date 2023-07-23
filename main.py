import pyttsx3

if __name__ == '__main__':
    print("Welcome to intelligent speaker created by Muskan Agarwal")
    engine = pyttsx3.init()
    while True:
        start = input("What you want to say\n")

        engine.say(start)
        engine.runAndWait()
        g = input("Press z to discontinue")
        if g == 'x':
            print("Sorry Time's Up")
            break
import webbrowser
import random
import turtle
import time

def birthday_program():
    print("Happy Valentine's Day, my dearest!")
    print("Please choose an option:")
    print("1. Gift")
    print("2. Love")
    print("3. Dance")
    print("4. Super Gift")
    print("5. Interesting facts and romantic music")
    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        print("Please wait 10 seconds...")
        for i in range(10, 0, -1):
            print(f"{i} seconds left")
            time.sleep(1)
        print("How do you like the gift, my dearest?")
    elif choice == 2:
        print("Please wait 2 minutes...")
        total_time = 120
        for i in range(total_time, 0, -1):
            minutes, seconds = divmod(i, 60)
            print(f"{minutes} minutes and {seconds} seconds left")
            time.sleep(1)
        print("How are you, my dearest?")
    elif choice == 3:
        print("Starting the dance...")
        turtle.speed(0)
        turtle.bgcolor("black")
        turtle.penup()
        turtle.goto(0, 250)
        turtle.pendown()
        turtle.pencolor("pink")
        turtle.write("Happy Valentine's Day, my dearest!", font=("Arial", 40, "normal"), align="center")
        colors = ["red", "pink", "red", "orange", "magenta", "violet", "purple"]
        for i in range(100):
            turtle.pencolor(random.choice(colors))
            x = random.randint(-300, 300)
            y = random.randint(-300, 300)
            if abs(x) < 100 and abs(y) < 100:
                continue
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            turtle.write("\u2764", font=("Arial", 40, "normal"))
        time.sleep(7)
        webbrowser.open("https://youtu.be/DF3XjEhJ40Y")
        total_time = 120
        for i in range(total_time, 0, -1):
            minutes, seconds = divmod(i, 60)
            print(f"\n{minutes} minutes and {seconds} seconds left", end="\r")
            time.sleep(1)
        print("\nTime's up! Take a break, my dearest. You're all I have, kitty.")
    elif choice == 4:
        print("Wait, minicaaaa ;) ")
        total_time = 1500
        for i in range(total_time, 0, -1):
            minutes, seconds = divmod(i, 60)
            print(f"{minutes} minutes and {seconds} seconds left")
            time.sleep(1)
        print(
            "I have been preparing for this day for a long time. This day is yours, and you can do whatever you want. This is just the beginning of your day.")
    elif choice == 5:
        messages = [
            "() You make my life better and more interesting with every passing day",
            "() You're the light in my life, and I love you so much",
            "() You bring so much joy and happiness to my life, I'm so grateful for you",
            "() I love being with you and making memories together",
            "() You make every day a special one, just by being yourself",
            "() You're the missing piece of my life, and I'm so happy to have you",
            "() I love the way you smile and how you light up a room",
            "() You're the best thing that's ever happened to me, I love you more and more every day",
            "() You're my everything, and I'm so grateful to have you in my life",
            "() I love you more than words could ever express, you're my heart and soul",
            "() My love for you is as sweet as chocolate, and today I want to shower you with all my affection. Happy Valentine's Day!",
            "() I am the luckiest person in the world to have you as my sweetheart. Happy Valentine's Day, my love!",
            "() You light up my life like nobody else. Happy Valentine's Day, my darling!",
            "() Your love is my greatest treasure, and I am so grateful to have you by my side. Happy Valentine's Day!",
            "() You make every day feel like Valentine's Day with your endless love and affection. Happy Valentine's Day!",
            "() I thank God every day for bringing you into my life. Happy Valentine's Day, my love!",
            "() I am so lucky to have a love like yours that fills me with happiness and joy. Happy Valentine's Day!",
            "() You are my everything, my love. Happy Valentine's Day!",
            "() I cannot imagine my life without you, and I am so thankful to have you by my side. Happy Valentine's Day!",
            "() Your smile brightens my day, and your love warms my heart. Happy Valentine's Day!",
            "() You are the reason for my happiness and I am so grateful to have you as my Valentine. Happy Valentine's Day!",
            "() You are my rock, my best friend, and my soulmate. Happy Valentine's Day, my love!",
            "() Your love is a gift that I cherish every day, and today I want to celebrate it with all my heart. Happy Valentine's Day!",
            "() I am so blessed to have you in my life, and I will love you forever. Happy Valentine's Day!",
            "() You are my everything, and I will always love you. Happy Valentine's Day!",
            "() You bring so much joy and happiness into my life, and I am so grateful for your love. Happy Valentine's Day!",
            "() I love you more and more every day, and I am so happy to spend this special day with you. Happy Valentine's Day!",
            "() You are the most amazing person I have ever met, and I am so grateful for your love. Happy Valentine's Day!",
            "() Your love is a treasure that I will always hold close to my heart. Happy Valentine's Day!",
            "() You are my best friend, my soulmate, and my one true love. Happy Valentine's Day!",
            "() I am so grateful for every moment that we spend together, and I will love you forever. Happy Valentine's Day!",
            "() Your love is my greatest gift, and I am so lucky to have you as my Valentine. Happy Valentine's Day!",
            "() I am so blessed to have found you, and I will always cherish our love. Happy Valentine's Day!",
            "() You make every day feel like a special occasion, and I am so grateful for your love. Happy Valentine's Day!",
            "() You make every moment brighter with your love and affection. Happy Valentine's Day!",
            "() I am so lucky to have a love like yours that brings so much happiness into my life. Happy Valentine's Day!",
            "() You are my sunshine on a cloudy day, and I will always love you. Happy Valentine's Day!",
            "() I cannot imagine a life without you, and I am so grateful for your love. Happy Valentine's Day!",
            "() You are my everything, my love, and I am so thankful to have you by my side. Happy Valentine's Day!",
            "() Your love is my greatest adventure, and I cannot wait to see what the future holds. Happy Valentine's Day!",
        ]

        print("\nChoose a melody to turn on:")
        songs = [
            ["Это любовь", "Скриптонит"],
            ["Она с тобой", "Билли"],
            ["Ты и Я", "Xcho"],
            ["Про Любов?", "Скрябін"],
            ["ІНША ЛЮБОВ", "ENLEO"]
        ]
        for i, song in enumerate(songs):
            print(f"{i + 1}. {song[0]} by {song[1]}")

        song_choice = int(input("Enter your choice (1-5): "))
        if song_choice == 1:
            webbrowser.open("https://www.youtube.com/watch?v=tYXQb_-8FoY")
            print(f"Enjoy listening to '{songs[0][0]}' by {songs[0][1]}")
            print("\n".join(random.sample(messages, 30)))
        elif song_choice == 2:
            webbrowser.open("https://youtu.be/bQ9qLtPdAds")
            print(f"Enjoy listening to '{songs[1][0]}' by {songs[1][1]}")
            print("\n".join(random.sample(messages, 30)))
        elif song_choice == 3:
            webbrowser.open("https://youtu.be/ZwTW9ukCpyw")
            print(f"Enjoy listening to '{songs[2][0]}' by {songs[2][1]}")
            print("\n".join(random.sample(messages, 30)))
        elif song_choice == 4:
            webbrowser.open("https://youtu.be/mFl365yRumg")
            print(f"Enjoy listening to '{songs[3][0]}' by {songs[3][1]}")
            print("\n".join(random.sample(messages, 30)))
        elif song_choice == 5:
            webbrowser.open("https://www.youtube.com/watch?v=0o0iK-ufovM")
            print(f"Enjoy listening to '{songs[4][0]}' by {songs[4][1]}")
            print("\n".join(random.sample(messages, 30)))
        else:
            print("Invalid choice. Please try again.")


print(birthday_program())


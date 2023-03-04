from playsound import playsound
import time


def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"\rAlarm will sound in: {minutes_left:02d}:{seconds_left:02d}", end="")

    print("\n")
    playsound("/Users/marcik/Downloads/music.mp3")


minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)

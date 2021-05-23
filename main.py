import urllib
from playsound import playsound
import speech_recognition as sr
from datetime import datetime
import pyttsx3
import random
import pytz
import os
import urllib.request
import re
import youtube_dl


def ytsearch(song_name):
    tts("searching for " + song_name)
    song_name = song_name[5:]
    search_keyword = song_name.replace(" ", "")
    print(search_keyword)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print("https://www.youtube.com/watch?v=" + video_ids[0])
    downloader("https://www.youtube.com/watch?v=" + video_ids[0], song_name)


def speech():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
            return command
    except:
        pass


def downloader(url, song_name):
    ydl_opts = {
        'format': 'bestaudio/best',
        # 'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])
    play(song_name)


def play(song_name):
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")
    tts("playing " + song_name)
    playsound("song.mp3")
    os.remove("song.mp3")

	
def tts(string):
    engine = pyttsx3.init()
    engine.say(string)
    engine.runAndWait()


def time():
    tz_NY = pytz.timezone('America/Los_Angeles')
    datetime_NY = datetime.now(tz_NY)
    print(datetime_NY.strftime("%I:%M %p"))
    tts(datetime_NY.strftime("%I:%M %p"))


def main():
    quit = True
    discord = False
    while quit:
        try:
            phrase = speech()
            if 'hey Discord' in phrase or discord:
                if not discord:
                    tts("Yes?")
                discord = True
                if 'play' in phrase:
                    ytsearch(phrase)
                if 'time' in phrase:
                    time()
                if 'quit' in phrase:
                    tts("shutting down")
                    quit = False
        except:
            pass


if __name__ == "__main__":
    main()

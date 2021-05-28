from playsound import playsound
import speech_recognition as sr
from datetime import datetime
import pyttsx3
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
    tts("The time is " + datetime_NY.strftime("%I:%M %p"))

# Requires phrase recorded, then outputs just the command after hey discord
# Used to have bot output .commands
def dot_parse(str, sub):
    i = str.find(sub)
    if i != -1:
        return "." + str[i:]
    else:
        raise Exception('Command has an error')


def main():
    quit = True
    discord = False
    attempts = 0
    while quit:
        try:
            phrase = speech()
            if 'hey discord' in phrase or discord:
                if not discord:
                    tts("Yes?")
                discord = True
                if 'play' and 'random' in phrase:
                    #TODO: [STRETCH] find a random song
                    pass

                if 'play' in phrase:
                    ytsearch(phrase)


                if 'queue' in phrase:
                    #TODO: Queue the song
                    parsed_phrase = dot_parse(phrase, 'queue')
                    #TODO: Make bot type queue command
                    pass

                if 'pause' in phrase:
                    #TODO: Implement the Pause functionality
                    parsed_phrase = dot_parse(phrase, 'pause')
                    #TODO: Make bot type pause command
                    pass
                
                if 'resume' in phrase:
                    #TODO: continue / unplay the song
                    parsed_phrase = dot_parse(phrase, 'resume')
                    #TODO: Make bot type resume command
                    pass

                if 'stop' in phrase:
                    #TODO: stop the music.
                    parsed_phrase = dot_parse(phrase, 'stop')
                    #TODO: Make bot type stop command
                    pass

                if 'time' in phrase:
                    time()

                if 'quit' or 'leave' in phrase:
                    tts("shutting down")
                    parsed_phrase = dot_parse(phrase, 'leave')
                    #TODO: Make bot type leave
                    quit = False

            attempts = 0

        except:
            #TODO: What are possible excepts we can receive? 
            if attempts <= 3:
                tts("There's been an error. Please restart the bot.")
                quit = False
            else:
                tts("I couldn't understand that, please try again.")
            attempts += 1


if __name__ == "__main__":
    main()

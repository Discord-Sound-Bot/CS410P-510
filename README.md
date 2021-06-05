# Hey Discord
A personal assistant for Discord, created for CS410 / 510P Computers, Sound, and Music. 

Contributors: 

Noah Funderburgh [nof2@pdx.edu]

Alejandro Castaneda [cas29@pdx.edu]

Long Huynh [lonhuynh@pdx.edu]


## The Project Purpose
---
In a manner similar to "Hey Google" or "Alexa …" we introduce the concept of a Discord personal assistant.
This personal assistant will be able to play, pause, queue, and skip music.
The music will be provided by the youtube API.

## Intended Functionality
---
The point of this program is to provide a Discord Bot that utilizes the Speech Recognition open source library to manage music. 
After configuring and starting the Discord bot, the user is be able to say commands like 
"Hey Discord, Play 'Sad'"
"Hey Discord, Pause."

### Available Commands:
*help* : Provides a chat message with what commands are available for you to use.

*play 'song name'*: Plays [song name]. Finds the song from Youtube.

*queue 'song name'*: Queues [song name] to play after the next queued song (after the next song if there is no songs in the queue). 

*pause*: Pauses the current playing song.

*resume*: Unpauses the current playing song.

*time*: Provides the current time.

*skip*: Proceeds to the next played song.

*quit*: Leaves the voice channel

## Installation
---
1. Clone the repo. 
2. The machine you're using this with needs `ffmpeg`. If you do not have ffmpeg, check out this Youtube tutorial for [windows](https://www.youtube.com/watch?v=r1AtmY-RMyQ), or you can use `brew install ffmpeg` if you have Homebrew. If you can successfully run `ffmpeg` in the command prompt, you can proceed.
3. The bot requires an active Discord voice channel, as well as an account to run. If you don't have one, create an account at https://discord.com/brand-new
4. Then, connect to the [server](https://discord.gg/dCrRfbAZ6E ) provided by copying and pasting this link, and clicking 'Accept': https://discord.gg/dCrRfbAZ6E 
5. After joining the Discord link, join the voice channel by clicking on the #general voice chat (has the audio icon to the left of it).
6. Start the bot by running `python3 main.py`. 
7. In the #bot text channel, type .join so that the bot joins the voice channel with you, then type .listen to begin the 'listening' process.
8. Execute commands by beginning with "Hey Discord", followed by what command you're hoping for. Check above for available functionality.
9. The bot will exit after a few minutes of inactivity or if you say "Hey Discord, leave."

## Results
---
### What worked? What didn't? 
Our initial project proposal involved using CMU Sphinx to detect the speech and translate it into 'commands'. 
However, CMU Sphinx had incredibly low accuracy and performed incredibly slow. 

After diving a little into the rabbit hole, we decided to pivot towards the open source Speech Recognition library. 
Unsurpisingly, Google's model was incredibly accurate and provided the functionality that we were hoping to get.
Another problem we faced was Discord's API is very inconsistent with their audio issues.

Despite the constant advancement on their repository, it is still not in a stable version that we could use for this project. 
Instead, we decided to switch the bot to run locally, listening to the 'users' commands rather than the whole server's.

In the future, we would like to have it listen to Discord directly, so that more people can make use of the bot.
Unfortunately Discord.py doesn't support it yet, so we had to make do with listening to local audio instead.
 

# CS410 / 510
Noah Funderburgh [nof2@pdx.edu]
Alejandro Castaneda [cas29@pdx.edu]
Long Huynh [lonhuynh@pdx.edu]

## The Project Purpose
In a manner similar to "Hey Google" or "Alexa …" we introduce the concept of a Discord personal assistant.
This personal assistant will be able to play, pause, queue, and skip music.
The music will be provided by the youtube API.

## Intended Functionality
The point of this program is to provide a Discord Bot that utilizes the Speech Recognition open source library to manage music. 
After configuring and starting the Discord bot, the user should be able to say commands like 
"Hey Discord, Play 'Sad'"
"Hey Discord, Pause."

## Getting Started

To begin, you can start off by cloning the repo. In order for the program
to work you will need ffmpeg. If you already have ffmpeg then your set to go.
If not then here is a short youtube video on how to install it. 

https://www.youtube.com/watch?v=r1AtmY-RMyQ

If your able to type ffmpeg in command prompt and don't get errors then you have
successfully installed it.

After, installing ffmpeg you can just run main.py. The bot should start up and when the
bot is ready it will output "Bot is ready!".

In order for the bot to work propperly you will need to be in a discord voice channel.
The steps to do that are:
1. If you don't have a discord account you will have to make one https://discord.com/brand-new
2. Then put in this link in your browser https://discord.gg/dCrRfbAZ6E it will ask if you want to join the server, hit accept

After joining the Discord link, join the voice channel.
In the bot text channel, type .join so that the bot joins the same channel you're in. 
Then, type .listen and the bot will tell that it's listening.
You have to say hey discord then the command for it to work

Watch video to see how to run: 

## Results

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
 
## Speech Functions:
help

play 'song name'

queue 'song name'

pause

resume

time

skip

quit

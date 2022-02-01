import requests;
import discord;
from discord.ext import commands



bot = commands.Bot(command_prefix='!'); # command format: !command

# indicates that discord bot is connected
@bot.event
async def on_ready():
    print("Discord bot logged in!");

# simple hello command
@bot.command()
async def hello(context):
    username = context.message.author;  # user giving command
    await username.send("Greetings!");  # sends direct message to this user - remember await!

# weather command using weather api
@bot.command()
async def weather(content, city):
    username = content.message.author;
    
    base_url = "http://api.openweathermap.org/data/2.5/weather?q="; # base url
    complete_url = base_url + city + "&APPID=" + KEY;               # include data to send
    
    response = requests.get(complete_url);          # get request, store response object
    data     = response.json();                     # reponse data in JSON format
    weather  = data['weather'][0]['description']    # extract specific weather data
    
    await username.send(weather);   # send weather data to user

bot.run(TOKEN);
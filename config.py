import os

from sample_config import Var


class Development(Config):
  # get this values from my.telegram.org. 
  # 6 is just a placeholder. Fill your own api id & hash.
  APP_ID = 25742938
  API_HASH = "b35b715fe8dc0a58e8048988286fc5b6"

  # the name to display in your alive message.
  # If not filled anything then default value is LEGEND User.
  ALIVE_NAME = "AKSHIT User"

  # create any PostgreSQL database.
  # I recommend to use elephantsql and paste that link here
  DB_URI = "postgres://oaykvtmj:bsIGPV7wmId1x1CNH9eqxQVX5t25cHI3@manny.db.elephantsql.com/oaykvtmj"

  # After cloning the repo and installing requirements...
  # Do python string_session.py and fill the on screen prompts.
  # String session will be saved in your saved message of telegram.
  # Put that string here.
  AKSHIT_STRING = "1BZWaqwUAUD43K5aIkXqPBYANp7MOkRB81TplGCA85UrUjc-_CIuB7Cu92H8QudHb5ledoQhn66Hf5FEVpuNV4B7foaGjIOyuzA154wLhf79nFH5nDAr63qVu21TUaeRSQ39IGtmg4mqdd1TPwcDZocG6qnY8uJAsLHDYArvTzblNBJxL4dybniOvYhMaWtHc38Pi6AJdXjrkHM2SATQmaP7psmJQ9xdYKLruPmpH7Jl9FDAzpclUY25NV2YXpO5YhLSNJQOv6tPldqrTS-7R7Xp2EzBxJS4Joodc8NRymg_8HRIYs7n39PvZJwRVt1uwnSoCZ0snrdNOvVLnu_guQWDf0e0Uq2k="

  # Create a bot in @botfather and fill the following values with bot token and username.
  BOT_TOKEN = "7737579995:AAHzTgISMQhZuEasuOBEm6aTn5mqes-f0aQ" #token
  BOT_USERNAME = "badmunda" #username

  # Create a private group and add rose bot to it.
  # and type /id and paste that id here.
  # replace that -100 with that group id.
  PRIVATE_GROUP_BOT_API_ID = -100

  # Custom Command Handler. 
  COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", r"\."
  #User Command Handler
  HANDLER = os.environ.get("COMMAND_HAND_LER", r"\."
  # enter the userid of sudo users.
  # you can add multiple ids by separating them by space.
  # fill values in [] only.
  SUDO_USERS = []

  # command hanler for sudo users.
  SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", r"\,"

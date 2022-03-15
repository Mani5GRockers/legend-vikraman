from sample_config import Config


class Development(Config):
  # get this values from my.telegram.org. 
  # 6 is just a placeholder. Fill your own api id & hash.
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"

  # the name to display in your alive message.
  # If not filled anything then default value is LEGEND User.
  ALIVE_NAME = "peroness started"

  # create any PostgreSQL database.
  # I recommend to use elephantsql and paste that link here
  DB_URI = "postgresql://postgres:hlbQYis3KWXIYsazvhup@containers-us-west-20.railway.app:7979/railway"

  # After cloning the repo and installing requirements...
  # Do python string_session.py and fill the on screen prompts.
  # String session will be saved in your saved message of telegram.
  # Put that string here.
  LEGEND_STRING = "1AZWarzsBu2nwK8jTEbr-xKL5bQIqqgTo8n4Npe1o_g9LxBjA9PDFpYPVOYqUk0zbpX0tApOCOhHpuKY7VBCzD11rkAiRBErGL6GhEFqhc7PPNKWpVvbQjSfPXfD0O44veK9-hUvlb8kXp_MPwvzg6RifZUKMX9tpPbawOJ4G2uhrGT24FEbUXrVrpsZVZm5uIZ9A_qavd_9WPgzfXCrFYaysiq6YD1CvCwxFmLvqjnwT9lw_yDZzdP0hbCkAzsVzdeGsm7U2fBCM4QTUOnQEPbwMPfEVjNZcH-HDfSNuMEj-QJs5EzmPBDbXSKkFFAJpcqc37gKBjJJgcR6KCqyvjzpLH7Qlxdo="

  # Create a bot in @botfather and fill the following values with bot token and username.
  BOT_TOKEN = "5139784361:AAFSa-7kvEoPCND_SPr8Qa5-lxx8a4YAJDk" #token
  BOT_USERNAME = "vikubsbot" #username

  # Create a private group and add rose bot to it.
  # and type /id and paste that id here.
  # replace that -100 with that group id.
  PRIVATE_GROUP_BOT_API_ID = -1001686939612

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

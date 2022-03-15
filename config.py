from sample_config import Config


class Development(Config):

  APP_ID = 2545223
  API_HASH = "91af3cce4f3e238fd51592eafc7f2f75"

  ALIVE_NAME = "peroness started"

  DB_URI = "postgresql://postgres:hlbQYis3KWXIYsazvhup@containers-us-west-20.railway.app:7979/railway"

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

  SUDO_USERS = []

  # command hanler for sudo users.
  SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", r"\,"

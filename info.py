import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = 26331302
API_HASH = '5d7bbff0c04b119735e4e14bdb402e69'
BOT_TOKEN = '6201307785:AAG0gB_uqvs9_konxBuLouEH9fwvwIQdzsM'
USERBOT_STRING_SESSION = 'BQAFUYDEHtMiZWocKu5762avgI1rUfRqEXdSRnCjItXqSpzDifoGSWhUwQG3XU8pElqA0muKkMSap7L4VIMlI3nneIEGm_woktY4z8u9ghKfNkBjUEaxwEoBUlTADaWfnJ_QT9JV1zrUSJ2Vb0035JI7xifKPD7faa1o-EJSI5lT5KR-QVijaaTXYVoV-1d3RDchKhAp7xUENuT22Yn4e0Uy5mofftxWPzpiFVoHKmmZy17f8Jxtg_sgVFsQZBBV0_RXzUf2HKvX9Ri2BEa9P11iuF_xClfe-d_g7tBHiTjhqIgbhg3ja4SI3rZ48ClzT21sLa1lPrf8dwwUIg1JNQqPAAAAAXauqbEA'

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = True

# Admins, Channels & Users
ADMINS = [6113550151]
CHANNELS = [-1001927205991]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel

# MongoDB information
DATABASE_URI = 'mongodb+srv://music:music@cluster0.6nwpwo2.mongodb.net/?retryWrites=true&w=majority'
DATABASE_NAME = 'music'
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
**Hi, I'm Media Search bot**

Here you can search files in inline mode. Just press following buttons and start searching.
"""

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = environ.get('INVITE_MSG', 'Please join @.... to use this bot')

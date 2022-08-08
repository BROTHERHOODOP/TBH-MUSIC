from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "4110592"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ede0")
BOT_TOKEN = getenv("BOT_TOKEN", "5562514845:AAHjj0jabzqQppP7BkTwT7TUk5M6BN2zka0")
BOT_NAME = getenv("BOT_NAME","⏤͟͟͞͞★𝑻𝑩𝑯ꗄ𝑴𝑼𝑺𝑰𝑪➺")
BOT_USERNAME = getenv("BOT_USERNAME", "TBH_MUSIC_BOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ITS_HELLL_BOYYY")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "SCHOOL_WALLI_MASTII")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/4d83f2e52df49e973e18d.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/4d83f2e52df49e973e18d.jpg")
SESSION_NAME = getenv("SESSION_NAME", AQB34wTqm2_1S_UpifFuVEZJIcQaTl_ARHipQtS5xZN_rZRCvoGK5Rbap87FgVFmQSjEZVLsA5DP03R7OpI0gxrhuBFmFAIg6Q-WNT-6uvIZDQNf27YVKuhM20QHoFAtb5lFGHPMex5Xl7ie8Cl4HJUB9q-YR8CqSUeMK2ccUQKnoRqxzEflHQxzWXhOC3huxoTjzOTlrbHBWyrtdNsxkJiZ3GTsqqhpJbYNt-LJrdk1cC5EniLq4qs4HJiLYS0LZ6QGy1paF_CgCozJORuW4j9uaHcaGxNN3VcgnINMvYQ70Peswd1V_U6k5EicJAjBtH8XHPIfkBxiGNkFY_LtoxcwAAAAAUBkHSkA)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1761766352").split()))

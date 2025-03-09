from aiohttp import web as webserver
from pyrogram import Client, filters, __version__, enums
from os import environ
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
routes = webserver.RouteTableDef()

async def bot_run():
    _app = webserver.Application(client_max_size=30000000)
    _app.add_routes(routes)
    return _app
  
@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return webserver.json_response("GOUTHAMSER")

class User(Client):
    def __init__(self):
        super().__init__(
            "userbot",
            api_hash="7ad4c2b1e5556277d341477b0776b2de",
            api_id="25988816",
            session_string="BQGMjtAAsib3CsRoiRE-1YQo8amIqqtghQwgAyWxSyQgFkS-1UuBhMWQoRgvegYmqFygF6dUlBmmxZDlQ9tm3GSkzI-BsokfH2r_kF6nTb80huAm3B_DKqR39JwWvrgaS0u9rh4acqcV8HIwuCfPYBCg4KLCXl7fnD68ZPBdB6XZnNsxyuor0uaLxSqC3TezzF_iUFqzDymFF_CpIObhCbU12oi8ZSOK-pPOjFbEdUple6SyirNTgnBjI3BkLuimj9MrwwA8CNi4DmrFthdgqBeMzJKrt1XvVX1-N8cNqt9Oqp_hYGPwUSjicwupS40C5Gt9VgDusIkfNpjOnp4juQ01i9ewBAAAAAHILdNiAA",
            workers=20
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        try: await self.export_session_string()
        except: pass
        usr_bot_me = await self.get_me()
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")

PORT_CODE = environ.get("PORT", "8080")
API_ID = "25988816"
API_HASH = "7ad4c2b1e5556277d341477b0776b2de"
BOT_TOKEN = "8123797711:AAGV6PwwARGI5XNoq_ol0rAzLBvcQC0KWLk"

class Bot(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            "bot",
            api_hash=API_HASH,
            api_id=API_ID,
            plugins={
                "root": "bot/plugins"
            },
            workers=200,
            bot_token=BOT_TOKEN,
            sleep_threshold=10
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        
        client = webserver.AppRunner(await bot_run())
        await client.setup()
        bind_address = "0.0.0.0"
        await webserver.TCPSite(client, bind_address,
        PORT_CODE).start()
        
        bot_details = await self.get_me()
        self.set_parse_mode(enums.ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"@{bot_details.username}  started! "
        )
        self.USER, self.USER_ID = await User().start()
        

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")



HKZ = Client(
    "Movie Search Bot",  # Session name (can be anything)
    api_id="25988816",
    api_hash="7ad4c2b1e5556277d341477b0776b2de",
    bot_token="8123797711:AAGV6PwwARGI5XNoq_ol0rAzLBvcQC0KWLk"
)

@Client.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(
        text="""
❗️Use /latest Command For Getting Latest Release Updates.
❗️ Just Send Movie Name and Year Correctly. 
❗️ Use /help command to know How to Search Movies.""")
    await message.reply_photo(
        photo="http://postimg.cc/m1F3zH97"        caption=f"""Hello {message.from_user.mention}, 
Iam a Telegram Movie - Series SearchBot by team @ProSearch.

/start - Start Search Bot
/help - How to Search
/about - About me""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("🤖 BOT Updates Channel", url="https://t.me/+3bGT7Ze6qy0wZGY9"),
            ],[
            InlineKeyboardButton("🎙 Latest Uploads Channel", url="https://t.me/+m2YtjBd2t_k0OGU9"),
            ],[
            InlineKeyboardButton("🔶Movies BOT🔍", url="https://t.me/ProSearchX2Bot"),
            InlineKeyboardButton("🔶TVSeries BOT🔍", url="https://t.me/ProsearchY2Bot")
            ]]
            )
        )

@Client.on_message(filters.command("help"))
async def help_command(client, message):
    await message.reply_text("""
❗️Use /latest Command For Getting Latest Release Updates.
❗️ Just Send Movie Name and Year Correctly. 
❗️ Use /help command to know How to Search Movies.""")
    await message.reply_text("""
❗️How to Search Movies ❓ 
➖➖➖➖➖➖➖➖➖➖➖

1. Just Send Movie Name and Year Correctly.
(Check Google for Correct Spelling and year) 

Examples: - 
Oppam 2016
Baahubali 2015

Oppam 2016 1080p
Baahubali 2015 1080p
(For Getting only 1080p Quality Files)

Baahubali 2015 Malayalam 
Baahubali 2015 Tamil 
(For Dubbed Movie Files)

〰〰〰〰〰〰〰〰〰〰〰
❗️How to Search TVSeries ❓ 
➖➖➖➖➖➖➖➖➖➖➖

1. Just Send Series Name and Season Correctly.
(Check Google for Correct Spelling) 

Examples: - 
Game of Thrones S01
(S01 For Season 1)

Breaking Bad S02 1080p
For Season 2 1080p Files

Lucifer S03E01 
(For Season 3 Episode 1)


〰〰〰〰〰〰〰〰〰〰〰

❗️On Android, Better Use VLC Media Player , MPV Player,  MX Player Pro, X Player Video Players.""")

@Client.on_message(filters.command("about"))
async def about_command(client, message):
    await message.reply_text("""
📌 About @ProSearch Bots
〰〰〰〰〰〰〰〰〰〰〰

❗️Admin     - [@Rocky_Bhayi](https://t.me/Rockybhayibot)
❗️Source Code - [@ELUpdates](https://github.com/EL-Coders/mediafinder)
❗️Hosted Server - [Vpsdime](https://vpsdime.com/)
❗️Database   - [PostgreSQL](https://www.postgresql.org/)""")

@Client.on_message(filters.regex(r"(?i)Terminator\s+Judgement\s+Day\s+Malayalam"))  #  (?i) makes it case-insensitive
async def hello_world_handler(client, message):
    await message.reply_text(
        text="""
🔍 Results for your Search 

➠ Latest Uploads: @ProSearchZ
 ➠➠ BOT Updates: @ProSearch🔻""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("Terminator Judgement Day Malayalam Dubbed 480p x264 600 MB.mkv", callback_data="result")
            ]]
            )
        )

@Client.on_callback_query()
async def callback(bot, msg):
    if msg.data == "result":
        await msg.message.edit_text("""You must /login before receiving the file..❗"""
        )

@Client.on_message(filters.command("login") & filters.user(1687129256) | filters.user(7653413730))
async def login_command(client, message):
    user_id = message.from_user.id

    if await is_admin(client, message.chat.id, user_id):
        await message.reply_text(
            text="Share your contact 📞 using the button to continue.",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("Share Contact ☎", request_contact=True)
                ]]
                )
            )
    else:
        await message.reply_text("You are Banned..🤐")

@Client.on_message(filters.contact)
async def contact_shared(client, message):
    await message.reply_text("Sending OTP Code to your Telegram..📲")

print("Bot Started")

app = Bot()
app.run()


    

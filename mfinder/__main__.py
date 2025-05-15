import uvloop
from pyrogram import Client, idle, __version__
from pyrogram.raw.all import layer
from mfinder import APP_ID, API_HASH, BOT_TOKEN

uvloop.install()


async def main():
    plugins = dict(root="mfinder/plugins")
    app = Client(
        name="mfinder",
        api_id=28862799,
        api_hash=3dc3be3bfb934a68aa280044b064ccee,
        bot_token=8074681333:AAHNHcNbU0nr3epf0fti_AHH36nfzSXxSqU,
        plugins=plugins,
    )
    async with app:
        me = await app.get_me()
        print(
            f"{me.first_name} - @{me.username} - Pyrogram v{__version__} (Layer {layer}) - Started..."
        )
        await idle()
        print(f"{me.first_name} - @{me.username} - Stopped !!!")

uvloop.run(main())

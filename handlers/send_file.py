import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait

async def media_forward(bot: Client, user_id: int, file_id: int):
    try:
        if Config.FORWARD_AS_COPY:
            return await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL, message_id=file_id)
        else:
            return await bot.forward_messages(chat_id=user_id, from_chat_id=Config.DB_CHANNEL, message_ids=file_id)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return await media_forward(bot, user_id, file_id)

async def send_media_and_reply(bot: Client, user_id: int, file_ids: list):
    sent_messages = []
    for file_id in file_ids:
        sent_message = await media_forward(bot, user_id, file_id)
        sent_messages.append(sent_message)

    # Send a single delete notification after all files are forwarded
    deletion_notice = await bot.send_message(
        chat_id=user_id,
        text="All files will be deleted in 30 minutes to avoid copyright issues. Please save them.",
        disable_web_page_preview=True
    )

    # Add the delete notification to the list of messages to delete
    sent_messages.append(deletion_notice)

    # Schedule all messages for deletion after 30 minutes
    asyncio.create_task(delete_after_delay(sent_messages, 1800))

async def delete_after_delay(messages, delay):
    await asyncio.sleep(delay)
    for message in messages:
        try:
            await message.delete()
        except Exception:
            pass
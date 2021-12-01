# Зроблено t.me/Daniel_Maklein | t.me/fumitsu_ua
from pyrogram import Client, filters
from pyrogram.types import Message
from ..utils.utils import modules_help , prefix
import asyncio




@Client.on_message(filters.command("stat", prefix) & filters.me)
def cmd_stat(client, message):
    message.edit_text(f'К-сть повідомлень в чаті = {message.message_id}')

modules_help.append({"stat": [{"stat": "к-сть повідомлень в чаті"}]})
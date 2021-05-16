# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *

# Totally Optional

def instructions(client, callback_query):
    query = callback_query
    query.answer("Please Read Carefully!!!")
    keyb = [
        [InlineKeyboardButton("Search Anime Inline", switch_inline_query_current_chat="")]
    ]
    reply_markup = InlineKeyboardMarkup(keyb)
    query.edit_message_caption(caption="""**𝓣𝓱𝓲𝓼 𝓑𝓸𝓽 𝓬𝓪𝓷 𝓖𝓮𝓽 𝔂𝓸𝓾𝓻 𝓯𝓪𝓿𝓸𝓾𝓻𝓲𝓽𝓮 𝓐𝓷𝓲𝓶𝓮 𝓪𝓷𝓭 𝓘𝓽 𝓹𝓻𝓸𝓿𝓲𝓭𝓮𝓼 𝓕𝓡𝓔𝓔 𝓓𝓸𝔀𝓷𝓵𝓸𝓪𝓭 𝓛𝓲𝓷𝓴 𝔀𝓲𝓽𝓱 𝓪 𝓯𝓪𝓼𝓽𝓮𝓼𝓽 𝓼𝓮𝓻𝓿𝓮𝓻(𝓖𝓸𝓸𝓰𝓵𝓮 𝓭𝓻𝓲𝓿𝓮). ❤️😍**

**𝓟𝓸𝓲𝓷𝓽𝓼 𝓽𝓸 𝓑𝓮 𝓝𝓸𝓽𝓮𝓭 :-**

__👉𝒮𝒾𝓃𝒸𝑒 𝑔𝑜𝑔𝑜𝒶𝓃𝒾𝓂𝑒 𝒸𝒽𝒶𝓃𝑔𝑒𝓈 𝓉𝒽𝑒𝒾𝓇 𝒹𝑜𝓂𝒶𝒾𝓃 𝑜𝒻𝓉𝑒𝓃, 𝒯𝒽𝑒 𝒷𝑜𝓉 𝓌𝒾𝓁𝓁 𝑔𝑜 𝒻𝑜𝓇 𝒻𝓇𝑒𝓆𝓊𝑒𝓃𝓉 𝓂𝒶𝒾𝓃𝓉𝑒𝓃𝒶𝓃𝒸𝑒. 𝒟𝑜𝓃'𝓉 𝓌𝑜𝓇𝓇𝓎, 𝓉𝒽𝑒 𝒷𝑜𝓉 𝓌𝒾𝓁𝓁 𝓈𝓉𝒾𝓁𝓁 𝒷𝑒 𝑜𝓃𝓁𝒾𝓃𝑒 𝒹𝓊𝓇𝒾𝓃𝑔 𝓂𝒶𝒾𝓃𝓉𝑒𝓃𝒶𝓃𝒸𝑒.__

__👉ℱ𝑜𝓇 𝓈𝓉𝓇𝑒𝒶𝓂𝒾𝓃𝑔 𝒾𝓃 𝓂𝑜𝒷𝒾𝓁𝑒, 𝑜𝓅𝑒𝓃 𝓉𝒽𝑒 𝓁𝒾𝓃𝓀𝓈 𝓌𝒾𝓉𝒽 𝒱ℒ𝒞 ℳ𝑒𝒹𝒾𝒶 𝒫𝓁𝒶𝓎𝑒𝓇. 𝒴𝑜𝓊 𝒸𝒶𝓃 𝒶𝓁𝓈𝑜 𝓊𝓈𝑒 ℳ𝒳 𝒫𝓁𝒶𝓎𝑒𝓇.__

__👉ℱ𝑜𝓇 𝓈𝓉𝓇𝑒𝒶𝓂𝒾𝓃𝑔 𝒾𝓃 𝒫𝒞, 𝓊𝓈𝑒 𝒱ℒ𝒞 𝓂𝑒𝒹𝒾𝒶 𝓅𝓁𝒶𝓎𝑒𝓇 𝓃𝑒𝓉𝓌𝑜𝓇𝓀 𝓈𝓉𝓇𝑒𝒶𝓂.__

__👉ℱ𝑜𝓇 𝒹𝑜𝓌𝓃𝓁𝑜𝒶𝒹𝓈, 𝒿𝓊𝓈𝓉 𝑜𝓅𝑒𝓃 𝓉𝒽𝑒 𝓁𝒾𝓃𝓀𝓈 𝒾𝓃 𝒶 𝒷𝓇𝑜𝓌𝓈𝑒𝓇.__

**𝒯𝒽𝒶𝓉'𝓈 𝒾𝓉, 𝒴𝑜𝓊 𝒶𝓇𝑒 𝒶𝓁𝓁 𝒸𝒶𝓊𝑔𝒽𝓉 𝓊𝓅, 𝒿𝓊𝓈𝓉 𝓈𝓉𝒶𝓇𝓉 𝒶𝓃𝒹 𝑒𝓃𝒿𝑜𝓎 𝓎𝑜𝓊𝓇 𝒻𝒶𝓋𝑜𝓊𝓇𝒾𝓉𝑒 𝑜𝓉𝒶𝓀𝓊 𝒶𝓃𝒾𝓂𝑒😁😆**

**𝒯𝓎𝓅𝑒 /search 𝓉𝑜 𝒮𝑒𝒶𝓇𝒸𝒽 𝒻𝑜𝓇 𝒶𝓃 𝒜𝓃𝒾𝓂𝑒...**""", parse_mode="markdown", reply_markup=reply_markup)

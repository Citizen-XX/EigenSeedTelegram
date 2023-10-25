
import logging

from typing import Final
from html import escape
from uuid import uuid4
from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes, InlineQueryHandler

TOKEN : Final = "6466816394:AAFSZbRvkUtfkEjJ-kHm6Xf_bz-atCyZ_Ww"
BOT_USERNAMES : Final = "@coin_swapper_tests_bot"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


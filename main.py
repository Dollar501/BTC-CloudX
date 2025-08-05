# main.py
# Main entry point for the Telegram bot.
# This file initializes the bot, registers all handlers, and starts polling.

import logging
import os
from functools import partial

from dotenv import load_dotenv
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)

# Import handlers from their respective files
from command_processors import start, toggle_main_menu, show_contact_us, select_language, set_language
from devices import show_hardware_menu, browse_devices
from plan import show_investment_plans, display_plan_category
from create_plan import show_plan_creator_webapp, web_app_data_handler

# --- Setup ---
# Load environment variables from .env file
load_dotenv()

# Basic logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# ==============================================================================
# !! خطوة مهمة !!
# قم باستضافة ملف index.html وانسخ الرابط العام هنا.
# ==============================================================================
WEB_APP_URL = "https://YOUR_WEB_APP_URL/index.html"


def main() -> None:
    """Starts the bot."""
    # Get the bot token from environment variables
    BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not BOT_TOKEN:
        logger.error("FATAL: TELEGRAM_BOT_TOKEN not found in .env file.")
        return
    if "YOUR_WEB_APP_URL" in WEB_APP_URL:
        logger.warning("Warning: WEB_APP_URL has not been set in main.py. The 'Create Plan' feature will not work.")

    # Create the Application and pass it your bot's token.
    application = Application.builder().token(BOT_TOKEN).build()

    # --- Register Handlers ---
    
    # Basic Commands
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(start, pattern="^main_menu_from_child$"))
    application.add_handler(CallbackQueryHandler(toggle_main_menu, pattern="^toggle_menu$"))

    # Web App Handlers
    # Use partial to pass the web_app_url to the handler
    webapp_handler = partial(show_plan_creator_webapp, web_app_url=WEB_APP_URL)
    application.add_handler(CallbackQueryHandler(webapp_handler, pattern="^custom_plan$"))
    application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_data_handler))

    # Other Sections
    application.add_handler(CallbackQueryHandler(show_contact_us, pattern="^show_contact_us$"))
    application.add_handler(CallbackQueryHandler(select_language, pattern="^select_language$"))
    application.add_handler(CallbackQueryHandler(set_language, pattern="^set_lang_"))
    application.add_handler(CallbackQueryHandler(show_hardware_menu, pattern="^our_hardware$"))
    application.add_handler(CallbackQueryHandler(browse_devices, pattern="^browse_devices_"))
    application.add_handler(CallbackQueryHandler(show_investment_plans, pattern="^investment_plans$"))
    application.add_handler(CallbackQueryHandler(display_plan_category, pattern="^show_plan_cat_"))

    # Run the bot until the user presses Ctrl-C
    logger.info("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()

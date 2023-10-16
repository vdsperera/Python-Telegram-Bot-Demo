import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, Application, ContextTypes
import ccxt

# Replace with your Telegram Bot API Token
TELEGRAM_API_TOKEN = '6611232105:AAHx7Xc46vMfVLbPMrw-Sl4RJrxDbo1tW1I'

# Create a bot instance
bot = telegram.Bot(token=TELEGRAM_API_TOKEN)

# Create the Application and pass it your bot's token.
application = Application.builder().token(TELEGRAM_API_TOKEN).build()

# Initialize the CCXT cryptocurrency exchange library
exchange = ccxt.binance()

# Define the command handler for the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome to the Crypto Price Bot! Use /price <symbol> to check the price of a cryptocurrency.")

# Define the command handler for the /price command
async def get_crypto_price(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        symbol = context.args[0].upper()
        ticker = exchange.fetch_ticker(symbol + '/USDT')
        price = ticker['last']
        await update.message.reply_text(f"The current price of {symbol} is ${price:.2f}")
    except Exception as e:
        await update.message.reply_text("Error fetching price. Please check the symbol or try again later.")

# Register command handlers
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('price', get_crypto_price))
application.run_polling()

# # Start the bot
# updater.start_polling()
# updater.idle()

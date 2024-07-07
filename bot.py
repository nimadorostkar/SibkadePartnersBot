from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler,\
    ConversationHandler, ContextTypes, MessageHandler, filters, CallbackContext
import json
from datetime import datetime



TOKEN = "7445678382:AAG3-dxleieDz_dBJh4YCeMHQeuj389gM6U"




with open('products.json', 'r') as file:
    data = json.load(file)

CATS=[]
for object_name, items in data.items():
    print(f"Object: {object_name}")
    CATS.append(object_name)
    for item in items:
        print(f"Item: {item}")




# Define states
CATEGORY, PRODUCT, SUBSCRIPTION = range(3)

# Example data for categories, products, and subscription periods
CATEGORIES = CATS
PRODUCTS = data
SUBSCRIPTIONS = ['2 month', '4 months', '6 months']



async def actions(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    selected_product = context.user_data['product']
    subscription = context.user_data['subscription']
    order_code = datetime.now().strftime("%Y%m%d%H%M%S")
    await query.edit_message_text(text=f'🗂️ Order Code: {order_code} \n🛍️ You selected a {selected_product} with {subscription} subscription.')

    if selected_product == "AppleMusic":
        print("apple id begir----")
        await query.message.reply_text("Please enter your AppleID:")
    elif selected_product == "Spotify":
        await query.message.reply_text("Please enter your Email and Password:")
    elif selected_product == "AppleOne":
        await query.message.reply_text("Please enter your AppleID:")
    else:
        await query.message.reply_text("Please enter your accounts information:")

    print(context.user_data)



async def handle_message(update: Update, context: CallbackContext) -> None:
    answer = update.message.text
    if context.user_data['product'] == "AppleMusic":
        print(answer)
        print(update.message.chat)

    elif context.user_data['product'] == "Spotify":
        print(answer)
    elif context.user_data['product'] == "AppleOne":
        print(answer)
    else:
        print(answer)
    await update.message.reply_text("🙏 Thank you for using our bot، \n 🛍️ The request will be sent to you soon after the service is ready.")



# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    keyboard = [[InlineKeyboardButton(category, callback_data=category)] for category in CATEGORIES]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Please choose a category:', reply_markup=reply_markup)
    return CATEGORY

# Category selection handler
async def choose_category(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    category = query.data
    context.user_data['category'] = category
    keyboard = [[InlineKeyboardButton(product, callback_data=product)] for product in PRODUCTS[category]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text=f'You selected {category}. Now, choose a product:', reply_markup=reply_markup)
    return PRODUCT

# Product selection handler
async def choose_product(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    product = query.data
    context.user_data['product'] = product
    keyboard = [[InlineKeyboardButton(subscription, callback_data=subscription)] for subscription in SUBSCRIPTIONS]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text=f'You selected {product}. Now, choose a subscription period:', reply_markup=reply_markup)
    return SUBSCRIPTION

# Subscription selection handler
async def choose_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    subscription = query.data
    context.user_data['subscription'] = subscription
    await actions(update, context)
    return ConversationHandler.END



# Main function to start the bot
def main() -> None:
    application = Application.builder().token(TOKEN).build()
    # Define conversation handler with states
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CATEGORY: [CallbackQueryHandler(choose_category)],
            PRODUCT: [CallbackQueryHandler(choose_product)],
            SUBSCRIPTION: [CallbackQueryHandler(choose_subscription)]
        },
        fallbacks=[CommandHandler('start', start)],
    )

    application.add_handler(conv_handler)

    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    application.add_handler(message_handler)

    # Run the bot
    application.run_polling()

if __name__ == '__main__':
    main()

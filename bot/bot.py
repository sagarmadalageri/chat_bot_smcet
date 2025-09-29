from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8464041520:AAEL4HLtOXA_0h4Jrl7So9W-TERkNGCwW38"

# --- Main Domain Menu ---
domain_menu = [["Engineering", "MTech"], ["MBA"]]
domain_markup = ReplyKeyboardMarkup(domain_menu, resize_keyboard=True, one_time_keyboard=False)

# --- Submenus for Engineering ---
eng_submenu = [["Fees Structure", "Hostel Fees"], ["Documents Required", "Back to Domains"]]
eng_markup = ReplyKeyboardMarkup(eng_submenu, resize_keyboard=True, one_time_keyboard=False)

# --- Submenus for MTech ---
mtech_submenu = [["Fees Structure", "Hostel Fees"], ["Documents Required", "Back to Domains"]]
mtech_markup = ReplyKeyboardMarkup(mtech_submenu, resize_keyboard=True, one_time_keyboard=False)

# --- Submenus for MBA ---
mba_submenu = [["Fees Structure", "Hostel Fees"], ["Documents Required", "Back to Domains"]]
mba_markup = ReplyKeyboardMarkup(mba_submenu, resize_keyboard=True, one_time_keyboard=False)

# --- Hostel Submenu ---
hostel_menu = [["Boys Hostel", "Girls Hostel"], ["Back"]]
hostel_markup = ReplyKeyboardMarkup(hostel_menu, resize_keyboard=True, one_time_keyboard=False)

# --- Start / Main Domain Menu ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to College Helper Bot! Please select your domain:",
        reply_markup=domain_markup
    )

# --- Handle all messages ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    text = update.message.text.strip().lower()

    # --- Domain Selection ---
    if text == "engineering":
        await update.message.reply_text("🏫 Engineering Selected. Choose an option:", reply_markup=eng_markup)
        context.user_data['domain'] = 'engineering'

    elif text == "mtech":
        await update.message.reply_text("🏫 MTech Selected. Choose an option:", reply_markup=mtech_markup)
        context.user_data['domain'] = 'mtech'

    elif text == "mba":
        await update.message.reply_text("🏫 MBA Selected. Choose an option:", reply_markup=mba_markup)
        context.user_data['domain'] = 'mba'

    # --- Back to Domain Selection ---
    elif text == "back to domains":
        await start(update, context)

    # --- Fees Structure ---
    elif text == "fees structure":
        domain = context.user_data.get('domain', None)
        if domain == "engineering":
            await update.message.reply_text(
                "💰 Engineering Fees:\n- CET: Branch-wise fees\n- COMEDK: Branch-wise fees\n- Management: Branch-wise fees",
                reply_markup=eng_markup
            )
        elif domain == "mtech":
            await update.message.reply_text(
                "💰 MTech Fees:\n- PGCET: Branch-wise fees\n- Management: Branch-wise fees",
                reply_markup=mtech_markup
            )
        elif domain == "mba":
            await update.message.reply_text(
                "💰 MBA Fees:\n- PGCET Fees\n- Management Fees",
                reply_markup=mba_markup
            )

    # --- Hostel Fees ---
    elif text == "hostel fees":
        await update.message.reply_text("🏠 Select Hostel Type:", reply_markup=hostel_markup)

    elif text == "boys hostel":
        await update.message.reply_text("Boys Hostel Fees:\n- Single: ₹10,000/semester\n- Double: ₹8,000/semester", reply_markup=hostel_markup)

    elif text == "girls hostel":
        await update.message.reply_text("Girls Hostel Fees:\n- Single: ₹12,000/semester\n- Double: ₹9,000/semester", reply_markup=hostel_markup)

    elif text == "back":
        domain = context.user_data.get('domain', None)
        if domain == "engineering":
            await update.message.reply_text("🏫 Engineering Menu:", reply_markup=eng_markup)
        elif domain == "mtech":
            await update.message.reply_text("🏫 MTech Menu:", reply_markup=mtech_markup)
        elif domain == "mba":
            await update.message.reply_text("🏫 MBA Menu:", reply_markup=mba_markup)

    # --- Documents Required ---
    elif text == "documents required":
        domain = context.user_data.get('domain', None)
        if domain == "engineering":
            await update.message.reply_text("📄 Engineering Documents:\n- CET: Marksheet + ID Proof\n- COMEDK: Marksheet + ID Proof\n- Management: Passport photo + ID", reply_markup=eng_markup)
        elif domain == "mtech":
            await update.message.reply_text("📄 MTech Documents:\n- PGCET: Marksheet + ID Proof\n- Management: Passport photo + ID", reply_markup=mtech_markup)
        elif domain == "mba":
            await update.message.reply_text("📄 MBA Documents:\n- PGCET: Marksheet + ID Proof\n- Management: Passport photo + ID", reply_markup=mba_markup)

    # --- Greetings ---
    elif "hi" in text or "hello" in text:
        await start(update, context)

    # --- Default Response ---
    else:
        await update.message.reply_text("❗ Please select an option from the menu.", reply_markup=domain_markup)

# --- Main Function ---
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 College Helper Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

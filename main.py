import telebot
from telebot import types

TOKEN = "8999235110:AAFjMTKzpYxTxg5Kjup5FmqkUeIn15Srsys"
OWNER_ID = 8360215117  # GANTI ID TELE LU WOK, cara cek: chat @userinfobot
OWNER_IG = "@zforfte1_"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'menu'])
def start(m):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("💫 Alight Motion", callback_data="AM"),
        types.InlineKeyboardButton("✂️ CapCut", callback_data="CC"),
        types.InlineKeyboardButton("🎵 Spotify", callback_data="SP"),
        types.InlineKeyboardButton("🎨 Canva", callback_data="CV"),
        types.InlineKeyboardButton("🎬 Netflix", callback_data="NF"),
    )
    markup.add(
        types.InlineKeyboardButton("👑 OWNER", callback_data="OWNER"),
        types.InlineKeyboardButton("💬 IG @zforfte1_", url="https://instagram.com/zforfte1_")
    )
    bot.send_message(m.chat.id,
        "بسم الله الرحمن الرحيم\n\n"
        "🔥 **ZFOR FTE SHOP** 🔥\n"
        "👑 Owner: @zforfte1_\n"
        "100% ORIGINAL • TRUSTED • INSTANT\n\n"
        "Pilih apk nya wok 👇", parse_mode="Markdown", reply_markup=markup)

@bot.callback_query_handler(func=lambda c: True)
def handle(c):
    chat = c.message.chat.id
    user = c.from_user

    if c.data == "OWNER":
        mk = types.InlineKeyboardMarkup()
        mk.add(types.InlineKeyboardButton("💬 Chat Owner IG", url="https://instagram.com/zforfte1_"))
        mk.add(types.InlineKeyboardButton("📲 Chat Owner Tele", url="https://t.me/zforfte1_")) # ganti username tele lu
        mk.add(types.InlineKeyboardButton("⬅️ Kembali", callback_data="BACK"))
        bot.send_message(chat,
            "👑 **OWNER ZFOR FTE SHOP**\n\n"
            "IG: @zforfte1_\n"
            "Tele: @zforfte1_\n"
            "Status: ONLINE 24 JAM\n\n"
            "Chat owner kalau bot error / mau tanya stok wok!",
            parse_mode="Markdown", reply_markup=mk)
        return

    if c.data == "BACK":
        return start(c.message)

    # LIST HARGA
    menus = {
        "AM": [("1 TAHUN - 5K", "AM_1THN"), ("1 BULAN - 3K", "AM_1BLN")],
        "CC": [("7 DAY PRIVATE - 4K", "CC_7D"), ("1 BLN PRIVATE - 27K", "CC_1BLN")],
        "SP": [("FAMPLAN 20K", "SP_FAM"), ("INDPLAN 15K", "SP_IND")],
        "CV": [("1 BULAN 5K", "CV_1BLN"), ("1 TAHUN 9K", "CV_1THN"), ("EDU LIFETIME 10K", "CV_LIFE")],
        "NF": [("1P 2U 18K", "NF_2U"), ("1P 1U 35K", "NF_1U"), ("PRIVATE 160K", "NF_PRIV")]
    }

    if c.data in menus:
        mk = types.InlineKeyboardMarkup()
        for label, data in menus[c.data]:
            mk.add(types.InlineKeyboardButton(label, callback_data=data))
        mk.add(types.InlineKeyboardButton("⬅️ Kembali", callback_data="BACK"))
        bot.send_message(chat, f"**{c.data}** - Pilih paket wok:", parse_mode="Markdown", reply_markup=mk)
    else:
        # KETIKA CUSTOMER ORDER, OWNER DAPET NOTIF
        paket = c.data.replace("_", " ")
        try:
            bot.send_message(OWNER_ID,
                f"🔔 ORDER BARU WOK!\n\n"
                f"👤 User: @{user.username} ({user.id})\n"
                f"📦 Paket: {paket}\n"
                f"📩 Suruh DM IG @zforfte1_")
        except:
            pass

        mk = types.InlineKeyboardMarkup()
        mk.add(types.InlineKeyboardButton("🛒 ORDER VIA IG", url="https://instagram.com/zforfte1_"))
        mk.add(types.InlineKeyboardButton("👑 CHAT OWNER", callback_data="OWNER"))
        bot.send_message(chat,
            f"✅ Lu pilih **{paket}** dulu!\n\n"
            f"👑 Owner: @zforfte1_ bakal proses\n"
            f"Format: `ORDER {paket}`\n"
            f"DM IG sekarang biar cepet diproses!",
            parse_mode="Markdown", reply_markup=mk)

bot.infinity_polling()

from config import TOKEN
import telebot
from telebot.types import Message, ReplyKeyboardMarkup as RKM,InlineKeyboardMarkup as IKM,InlineKeyboardButton as IKB
from telebot.types import CallbackQuery



bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(m: Message):
    bot.send_message(m.chat.id, "Привет я создал этот бот(я)")


@bot.message_handler(commands=['help'])
def help(m: Message):
    kb = IKM()
    kb.row(IKB("Youtube","https://www.youtube.com/watch?v=xm3YgoEiEDc"),IKB("Rebotica","https://rebotica.ru"))
    kb.row(IKB("teстiroвka",callback_data="тэээкст"))
    bot.send_message(m.chat.id, 'нескам100%клянусьяблоком',reply_markup=kb)


@bot.message_handler(commands=['pon'])
def pon(m:Message):
    kb = IKM()
    kb.row(IKB("komaru",callback_data="komaru"))
    bot.send_message(m.chat.id, 'мммм бананчики, чивооооо это что змея?!',reply_markup=kb)


@bot.message_handler(commands=['register'])
def register(m:Message):
    bot.send_message(m.chat.id, 'привет как тебя зовут')
    bot.register_next_step_handler(m,reg1)


def reg1(m:Message):
    name = m.text
    bot.send_message(m.chat.id, f'ого, {name} мене так же зовут!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    bot.send_message(m.chat.id, 'ну ладнааа а скока тибе лет')
    bot.register_next_step_handler(m,reg2,name)


def reg2(m:Message, name):
    old = m.text
    bot.send_message(m.chat.id, f'чооо,тебя зовут {name} и тебе {old} лет я твой одноклассник ')
    bot.send_message(m.chat.id, 'а в коком ти классе')
    bot.register_next_step_handler(m, reg3, name , old)


def reg3(m:Message, name, old):
    klac = m.text
    bot.send_message(m.chat.id, f'чооо, тебя зовут {name} и тебе {old} лет и ты в {klac} мы точна одноклассники') 



@bot.callback_query_handler(func=lambda call:True)
def callback(call:CallbackQuery):
    print(call.data)
    if call.data=="komaru":
        bot.send_message(call.message.chat.id, 'ответ:это королевский питон')
    if call.data=="тэээкст":
        start(call.message)


@bot.message_handler(commands=['vopros'])
def vopros(m: Message):
    kb = RKM(resize_keyboard=True, one_time_keyboard=True)
    kb.row("кто создал этот бот?")
    bot.send_message(m.chat.id, "выбери vopros", reply_markup=kb)


@bot.message_handler(commands=['clava'])
def clava(m: Message):
    kb = RKM(resize_keyboard=True, one_time_keyboard=True)
    kb.row("кокоя твоя любимоя ида", "кудо ты поркуешь булачку с сасискаю")
    kb.row("виталий,что вы ели на завтрак")
    bot.send_message(m.chat.id, "выбери вапросек", reply_markup=kb)


@bot.message_handler(content_types=['audio'])
def audio(m: Message):
    sound = m.audio
    duration = sound.duration
    minutes = duration // 60
    secondhand = duration % 60
    text = f"bot_got_audio\n" \
           f"продожительность:{minutes}:{secondhand}\n" \
           f"Название:{sound.title}\n" \
           f"Исполнитель:{sound.performer}\n" \
           f"размер файла: {round(sound.file_size / 1024000, 2)} МБАйт"
    bot.send_message(m.chat.id, text)
    print(text)


@bot.message_handler(content_types=['text'])
def text(m: Message):
    if m.text == "кокоя твоя любимоя ида":
        bot.send_message(m.chat.id, "булачка с сасискаю")
    elif m.text == "кудо ты поркуешь  булачку с сасискаю":
        bot.send_message(m.chat.id, "в рот ААААА")
    elif m.text == "виталий,что вы ели на завтрак":
        bot.send_message(m.chat.id, "булачка с сасискаю,чай бутерброд, ииии.... пряники до чаю")
    elif m.text == "кто создал этот бот?":
        bot.send_message(m.chat.id, "я")
    else:
        bot.send_message(m.chat.id, m.text)


bot.infinity_polling()

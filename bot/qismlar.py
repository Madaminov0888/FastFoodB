import telebot
import config
import tools
from telebot import types
from bot.main import *

TOKEN = '5209072169:AAHIkqoHNC38dOAaAJVe9y9siKOGGYa5pVc'

bot = telebot.TeleBot(
    token=TOKEN,
    parse_mode='HTML',
    num_threads=4,
)

def turkcha_pizza(call, PATH):
    text = ''
    son = 0
    c = 'TurkchaPitsa'
    a = tools.garakli_list()
    text = f"Bo'lim: <b>🍛 Pide</b>"
    names = []
    for i in range(len(a)):
        if a[i][2] == 'TurkchaPitsa':
            narx = str(a[i][4])
            son += 1
            names.append(a[i][0][0])
            #text += str(son) + f'. {a[i][0][0]}--{narx[:-3]}.{narx[-3:]}\n'
    tools.make_inline_button(son, c, names)
    try:
        file = open(PATH +'fastfoodphotos/turkcha.jpg', 'rb')
        bot.edit_message_media(types.InputMedia(type='photo', media=file), chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
        bot.edit_message_caption(caption=text, chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    except:
        file = open(PATH +'fastfoodphotos/turkcha.jpg', 'rb')
        bot.delete_message(chat_id = call.message.chat.id, message_id = call.message.id)
        bot.send_photo(chat_id = call.message.chat.id, photo=file, caption = text, reply_markup=tools.mini)
    file.close()

def doner_qismi(call, PATH):
    text = ''
    son = 0
    names = []
    c = 'Doner'
    a = tools.garakli_list()
    text = f"Bo'lim: <b>🥙 {c}</b>"
    for i in range(len(a)):
        if a[i][2] == 'Doner':
            narx = str(a[i][4])
            names.append(a[i][0][0])
            son += 1
            #text += str(son) + f'. {a[i][0][0]}--{narx[:-3]}.{narx[-3:]}\n'
    tools.make_inline_button(son, c, names)
    try:
        file = open(PATH +'fastfoodphotos/doner.jpg', 'rb')
        bot.edit_message_media(types.InputMedia(type='photo', media=file), chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
        bot.edit_message_caption(caption=text, chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    except:
        file = open(PATH +'fastfoodphotos/doner.jpg', 'rb')
        bot.delete_message(chat_id = call.message.chat.id, message_id = call.message.id)
        bot.send_photo(chat_id = call.message.chat.id, photo=file, caption = text, reply_markup=tools.mini)
    file.close()



def kebab_qismi(call, PATH):
    text = ''
    son = 0
    names = []
    c = 'Kavob'
    a = tools.garakli_list()
    text = f"Bo'lim: <b>🥘 Maxsus Taomlar</b>"
    for i in range(len(a)):
        if a[i][2] == 'Kavob':
            narx = str(a[i][4])
            names.append(a[i][0][0])
            son += 1
            #text += str(son) + f'. {a[i][0][0]}--{narx[:-3]}.{narx[-3:]}\n'
    tools.make_inline_button(son, c, names)
    try:
        file = open(PATH +'fastfoodphotos/kebab.jpg', 'rb')
        bot.edit_message_media(types.InputMedia(type='photo', media=file), chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
        bot.edit_message_caption(caption=text, chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    except:
        file = open(PATH +'fastfoodphotos/kebab.jpg', 'rb')
        bot.delete_message(chat_id = call.message.chat.id, message_id = call.message.id)
        bot.send_photo(chat_id = call.message.chat.id, photo=file, caption = text, reply_markup=tools.mini)
    file.close()


def lavash_qism(call, PATH):
    text = ''
    son = 0
    names = []
    c = 'Lavash'
    a = tools.garakli_list()
    text = f"Bo'lim: 🌯 <b>{c}</b>"
    for i in range(len(a)):
        if a[i][2] == 'Lavash':
            narx = str(a[i][4])
            names.append(a[i][0][0])
            son += 1
            #text += str(son) + f'. {a[i][0][0]}--{narx[:-3]}.{narx[-3:]}\n'
    tools.make_inline_button(son, c, names)
    try:
        file = open(PATH +'fastfoodphotos/lavash.jpg', 'rb')
        bot.edit_message_media(types.InputMedia(type='photo', media=file), chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
        bot.edit_message_caption(caption=text, chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
        file.close()
    except:
        file = open(PATH +'fastfoodphotos/lavash.jpg', 'rb')
        bot.delete_message(chat_id = call.message.chat.id, message_id = call.message.id)
        bot.send_photo(chat_id = call.message.chat.id, photo=file, caption = text, reply_markup=tools.mini)
        file.close()
    

def chiz_qismi(call, PATH):
    text = ''
    son = 0
    names = []
    c = 'Chizburger'
    a = tools.garakli_list()
    text = f"Bo'lim: 🍔 <b>Burger</b>"
    for i in range(len(a)):
        if a[i][2] == 'Chizburger':
            narx = str(a[i][4])
            son += 1
            names.append(a[i][0][0])
            #text += str(son) + f'. {a[i][0][0]}--{narx[:-3]}.{narx[-3:]}\n'
    tools.make_inline_button(son, c, names)
    try:
        file = open(PATH +'fastfoodphotos/burger.jpg', 'rb')
        bot.edit_message_media(types.InputMedia(type='photo', media=file), chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
        bot.edit_message_caption(caption=text, chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    except:
        file = open(PATH +'fastfoodphotos/burger.jpg', 'rb')
        bot.delete_message(chat_id = call.message.chat.id, message_id = call.message.id)
        bot.send_photo(chat_id = call.message.chat.id, photo=file, caption = text, reply_markup=tools.mini)
    file.close()



def hotdogqismi(call, PATH):
    text = ''
    son = 0
    names = []
    c = 'Hotdog'
    a = tools.garakli_list()
    text = f"Bo'lim: 🌭 <b>Xot-Dog‍</b>"
    for i in range(len(a)):
        if a[i][2] == 'Hotdog':
            narx = str(a[i][4])
            son += 1
            if len(a[i][0][0].split(' ')) < 2 and not '-' in a[i][0][0] and a[i][0][0] != 'Haggi':
                t = a[i][0][0] + ' Hot-Dog'
                names.append(t)
            else:
                names.append(a[i][0][0])
            #text += str(son) + f'. {a[i][0][0]}--{narx[:-3]}.{narx[-3:]}\n'
    tools.make_inline_button(son, c, names)
    try:
        file = open(PATH +'fastfoodphotos/hotdog.jpg', 'rb')
        bot.edit_message_media(types.InputMedia(type='photo', media=file), chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
        bot.edit_message_caption(caption=text, chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    except:
        file = open(PATH +'fastfoodphotos/hotdog.jpg', 'rb')
        bot.delete_message(chat_id = call.message.chat.id, message_id = call.message.id)
        bot.send_photo(chat_id = call.message.chat.id, photo=file, caption = text, reply_markup=tools.mini)
    file.close()

def pizzaqismi(call, PATH):
    text = ''
    son = 0
    names = []
    c = 'Pizza'
    a = tools.garakli_list()
    text = f"Bo'lim:🍕<b>{c}</b>"
    for i in range(len(a)):
        if a[i][2] == 'Pizza' and a[i][3] == 'Katta':
            narx = str(a[i][4])
            son += 1
            names.append(a[i][0][0])
            #text += str(son) + f'. {a[i][0][0]}--{narx[:-3]}.{narx[-3:]}\n'
    tools.make_inline_button(son, c, names)
    try:
        file = open(PATH +'fastfoodphotos/pizza.jpg', 'rb')
        bot.edit_message_media(types.InputMedia(type='photo', media=file), chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
        bot.edit_message_caption(caption=text, chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    except:
        file = open(PATH +'fastfoodphotos/pizza.jpg', 'rb')
        bot.delete_message(chat_id = call.message.chat.id, message_id = call.message.id)
        bot.send_photo(chat_id = call.message.chat.id, photo=file, caption = text, reply_markup=tools.mini)
    file.close()

def ichimlikqismi(call, PATH):
    text = ''
    son = 0
    names = []
    c = 'Ichimliklar'
    a = tools.garakli_list()
    text = f"Bo'lim:🍹<b>{c}</b>"
    for i in range(len(a)):
        if a[i][2] == 'Ichimliklar' and a[i][3] == 'Katta':
            narx = str(a[i][4])
            names.append(a[i][0][0])
            son += 1
            #text += str(son) + f'. {a[i][0][0]} ---{narx[:-3]}.{narx[-3:]}\n'
    tools.make_inline_button(son, c, names)
    try:
        file = open(PATH +'fastfoodphotos/ich.jpg', 'rb')
        bot.edit_message_media(types.InputMedia(type='photo', media=file), chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
        bot.edit_message_caption(caption=text, chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    except:
        file = open(PATH +'fastfoodphotos/ich.jpg', 'rb')
        bot.delete_message(chat_id = call.message.chat.id, message_id = call.message.id)
        bot.send_photo(chat_id = call.message.chat.id, photo=file, caption = text, reply_markup=tools.mini)
    file.close()


def fri_qism(call, PATH):
    text = ''
    son = 0
    names = []
    c = 'Frie'
    a = tools.garakli_list()
    text = f"Bo'lim:🍟 <b>Fri</b>"
    for i in range(len(a)):
        if a[i][2] == c: 
            narx = str(a[i][4])
            names.append(a[i][0][0])
            son += 1
            #text += str(son) + f'. {a[i][0][0]} ---{narx[:-3]}.{narx[-3:]}\n'
    tools.make_inline_button(son, c, names)
    try:
        file = open(PATH +'fastfoodphotos/frie.jpg', 'rb')
        bot.edit_message_media(types.InputMedia(type='photo', media=file), chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
        bot.edit_message_caption(caption=text, chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    except:
        file = open(PATH +'fastfoodphotos/frie.jpg', 'rb')
        bot.delete_message(chat_id = call.message.chat.id, message_id = call.message.id)
        bot.send_photo(chat_id = call.message.chat.id, photo=file, caption = text, reply_markup=tools.mini)
    file.close()

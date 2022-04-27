from typing import Text
import telebot
import config
import tools
from telebot import types
from bot.main import STICKERS_DICT
from bot.main import *

TOKEN = '5209072169:AAHIkqoHNC38dOAaAJVe9y9siKOGGYa5pVc'

bot = telebot.TeleBot(
    token=TOKEN,
    parse_mode='HTML',
    num_threads=4,
)


def til_tanlash(message):
    text = f'🇺🇿 Tilni tanlang\n🇷🇺Выберите язык'
    made = types.InlineKeyboardMarkup()
    made1 = types.InlineKeyboardButton(text = '🇷🇺 Русский', callback_data='rus_tili')
    made2 = types.InlineKeyboardButton(text = "🇺🇿 O'zbek tili", callback_data='menu_start')
    made.add(made1, made2)
    if message.text != '/start':
        bot.delete_message(chat_id = message.chat.id, message_id = message.id)
    bot.send_message(chat_id=message.chat.id, text = text, reply_markup=made)


def ichimliklar_special_ru(call, r, calldata):
    main_ish = tools.data_parsing_ichimlik(calldata)
    text = f'<b>{main_ish[1][0][-1]}</b>\n<i>Выберите продукта</i> ⬇️ '
    made = types.InlineKeyboardMarkup()
    h = []
    satr = f'<b>{main_ish[1][0][-1]}</b>'
    for i in main_ish[0]:
        if main_ish[1][0][0].split(' ')[0] in ['Fanta','Koka-Kola', 'Pepsi']:
            file = open('fastfoodphotos/kola.jpg', 'rb')
            if i == 'Katta':
                satr = '1 L'
            elif i == "O'rtacha":
                satr = '0.5 L'
            elif i == 'Maxsus':
                satr = '1.5 L'
        elif main_ish[1][0][0].split(' ')[0] == 'Kofe':
            file = open('fastfoodphotos/kofe.jpg', 'rb')
            if i == 'Katta':
                satr = 'Чёрный кофе'
            elif i == 'Maxsus':
                satr = 'Капучино'
            elif i == "O'rtacha": 
                satr = 'Кофе молочный'
        else:
            file = open('fastfoodphotos/choy.jpg', 'rb')
            if i == 'Katta': 
                satr = "Зелёный чай"
            elif i == 'Maxsus':
                satr = 'Чёрный чай'
            elif i == "O'rtacha":
                satr = 'Чай с лимоном'

        made1 = types.InlineKeyboardButton(text = satr, callback_data=main_ish[1][2]+','+ calldata[-1] +','+str(i)+'#')
        h.append(made1)
    made2 = types.InlineKeyboardButton(text = '📋 Меню', callback_data='menu')
    made3 = types.InlineKeyboardButton(text='🔙 Назад', callback_data = 'orqaga_ichimliklar')
    made.add(*h, row_width=3)
    made.add(made3, made2, row_width=1)
    bot.edit_message_media(types.InputMedia(type='photo', media=file), chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=made)
    bot.edit_message_caption(caption=text, chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=made)


def menu_ruscha(message, SAVAT):
    yanam_h = []
    umumiy_summa = 0
    for i in SAVAT:
        if i[-1] == message.chat.id:
            yanam_h.append(i[0])
    if len(yanam_h) > 0: 
        for i in yanam_h:
            umumiy_summa += int(i[-2])*int(i[4])
    mark = types.InlineKeyboardMarkup()
    mark1 = types.InlineKeyboardButton(text='🌯 Лаваш', callback_data='Lavash')
    mark2 = types.InlineKeyboardButton(text='🍔 Бургер', callback_data= 'Chiz')
    mark3 = types.InlineKeyboardButton(text='🌭 Хот Дог', callback_data='hotdog')
    mark4 = types.InlineKeyboardButton(text = '🍕 Пицца', callback_data ='pizza')
    mark01 = types.InlineKeyboardButton(text = '🍛 Пиде', callback_data='turkcha')
    mark8 = types.InlineKeyboardButton(text = '🥙 Донер', callback_data='doner')
    mark6 = types.InlineKeyboardButton(text = '🥘 Кебаб', callback_data='Kavob')
    mark5 = types.InlineKeyboardButton(text = '🍹 Напитки', callback_data='ichimliklar')
    mark9 = types.InlineKeyboardButton(text = '🍟 Фри', callback_data='frie')
    mark7 = types.InlineKeyboardButton(text = '🌐 Выберите язык', callback_data='til_tanlash')
    savat = types.InlineKeyboardButton(text=f'🛒 Корзина({str(umumiy_summa)[:-3]}.{str(umumiy_summa)[-3:]})', callback_data='Savat')
    mark.add(mark4, mark1, mark2, mark3, mark6, mark01, mark5, mark8, mark9, row_width=2)
    mark.add(savat, mark7, row_width=1)
    text = f'😋 Что хотите заказать?'
    file = open(PATH +'fastfoodphotos/maxsusfastfood.png', 'rb')
    bot.send_photo(message.chat.id,
    file,
    caption=text,
    reply_markup=mark
    )
    try:
        bot.delete_message(chat_id = message.chat.id, message_id = message.id)
    except:
        pass
    file.close()




def yetkazib_berish_ru(call):
    text = '''🚚 Вы выбрали службу доставки.

Нажмите кнопку "<b>📍Отправить геолокацию</b>", чтобы ваш заказ был доставлен на ваш адрес.'''
    key = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    #key1 = types.KeyboardButton(text = '📍 Number',request_contact=True)
    key0 = types.KeyboardButton(text = "📍 Ввести адрес вручную", )
    key3 = types.KeyboardButton(text = '📍 Отправить геолокацию', request_location=True)
    key2 = types.KeyboardButton(text = 'Меню')
    key.add(key3, key0, key2)
    bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=key)


def buyurtma_bolimi_ru(call):
    text = 'Как вы хотите разместить заказ?'
    made = types.InlineKeyboardMarkup()
    made1 = types.InlineKeyboardButton(text = '🚚 Доставка', callback_data='yetkazib_berish')
    made2 = types.InlineKeyboardButton(text = '🚶 Прийти и взять', callback_data='olib_ketish')
    menu = types.InlineKeyboardButton(text = '📋 Меню', callback_data= 'menu')
    made.add(made1, made2, menu, row_width=1)
    file = open(PATH +'fastfoodphotos/maxsusfastfood.png', 'rb')
    bot.delete_message(chat_id=call.message.chat.id, message_id = call.message.id)
    bot.send_photo(chat_id = call.message.chat.id, photo = file, caption= text,reply_markup=made)

def clear_ru(call, SAVAT):
    text = 'Корзина очеслено '
    for i in SAVAT.copy():
        if i[-1] == call.message.chat.id:
            SAVAT.pop(SAVAT.index(i))

    made = types.InlineKeyboardMarkup()
    menu = types.InlineKeyboardButton(text = '📋 Меню', callback_data= 'menu')
    made.add(menu, row_width=1)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
    bot.send_message(chat_id=call.message.chat.id, text = text, reply_markup=made)

def delete_from_sevat_ru(call, number, SAVAT):
    s = SAVAT
    x = 1
    for i in s:
        if i[-1] == call.message.chat.id:
            if x == int(number):
                SAVAT.pop(SAVAT.index(i))
                break
            else:
                x += 1
    text = f'{i[0][0][-1]} удалено'
    bot.answer_callback_query(call.id, text = text, show_alert=True)
    return savat_ru(call, SAVAT=SAVAT)


def turkcha_pizza_ru(call):
    text = ''
    son = 0
    names = []
    c = 'TurkchaPitsa'
    a = tools.garakli_list()
    for i in range(len(a)):
        if a[i][2] == 'TurkchaPitsa':
            narx = str(a[i][4])
            son += 1
            names.append(a[i][0][-1])
            #text += str(son) + f'. {a[i][0][-1]}--{narx[:-3]}.{narx[-3:]}\n'
    tools.make_inline_button(son, c, names)
    text += f"Категория: <b>🍛 Пиде</b>"
    file = open(PATH +'fastfoodphotos/turkcha.jpg', 'rb')
    bot.edit_message_media(types.InputMedia(type='photo', media=file), chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    bot.edit_message_caption(caption=text, chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    file.close()





def savat_ru(call, SAVAT:list):
    s = SAVAT
    cpy = s.copy()
    umumiy_summa = 0
    text = '''📦 Корзина\n\n''' 
    se = 1
    yanam_h = []
    made = types.InlineKeyboardMarkup()
    made1 = types.InlineKeyboardButton(text='✅ Заказать', callback_data='buyurtma_berish')
    made.add(made1, row_width=1)
    for i in s:
        xs = 0
        if i[-1] == call.message.chat.id:
            yanam_h.append(i[0])
            for j in cpy:
                if i[0][0][0] == j[0][0][0] and i[0][2] == j[0][2]:
                    xs += 1
                    if xs >= 2:
                        i[0][-2] += int(j[0][-2])
                        s.pop(cpy.index(j))
                        cpy.pop(cpy.index(j))
    buttons = []
    if len(yanam_h) > 0: 
        for i in yanam_h:
            turi = ''
            if i[2] == 'Hotdog' and len(i[0][0].split(' ')) < 2 and not '-' in i[0][0] and i[0][0] != 'Haggi':
                turi = 'Хот-Дог'
            elif i[2] == 'Pizza':
                turi = 'Пицца'
            narx = str(int(i[-2])*int(i[4]))
            text += f'''{STICKERS_DICT[i[2]]}<b>{i[0][-1]} {turi}</b> x{i[-2]}:\n   {i[-2]}x{str(i[4])[:-3]}.{str(i[4])[-3:]} = {narx[:-3]}.{narx[-3:]} \n\n'''
            sd = types.InlineKeyboardButton(text = f'❌ {i[0][-1]} {turi}', callback_data=f'$ochirish_{se}')
            buttons.append(sd)
            se += 1
            umumiy_summa += int(i[-2])*int(i[4])
        if len(yanam_h) > 1:
            made.add(*buttons, row_width=1)
        text += 'Обшый сумма: '+str(umumiy_summa)[:-3]+'.' + str(umumiy_summa)[-3:]
        made2 = types.InlineKeyboardButton(text = '🗑 Очистить корзину', callback_data='clear_savat')
        menu = types.InlineKeyboardButton(text = '📋 Menu', callback_data= 'menu')
        made.add(made2, menu, row_width=1)

    else:
        text += '📂 Корзина пусто'
        made = types.InlineKeyboardMarkup()
        menu = types.InlineKeyboardButton(text = '📋 Меню', callback_data= 'menu')
        made.add(menu, row_width=1)

    bot.delete_message(chat_id=call.message.chat.id, message_id = call.message.id)
    bot.send_message(chat_id=call.message.chat.id, text = text, reply_markup=made)




def savatga_qoshish_ru(call, test, SAVAT):
    kal_main = test.split('.')
    soni, data = int(kal_main[2]), kal_main[1]
    data_pizza = data.split(',')[0]
    if data_pizza == 'Pizza':
        mini_ish = tools.poisk_pizza(data)
    elif data_pizza == 'Ichimliklar':
        mini_ish = tools.poisk_ichimlik(data)
    else:
        mini_ish = tools.data_parsing(data)
    mini_ish.append(soni)
    mini_ish.append(data)
    h = []
    h.append(mini_ish)
    h.append(call.message.chat.id)
    SAVAT.append(h)
    #made = types.InlineKeyboardMarkup(row_width=3)
    #menu = types.InlineKeyboardButton(text = 'Menu', callback_data= 'menu')
    #savat = types.InlineKeyboardButton(text='🛒 Savat', callback_data='Savat')
    #made.add(menu, savat)
    text = f'''✅ Добовлено\n{mini_ish[0][-1]} x{mini_ish[-2]} - {str(mini_ish[4])[:-3]}.{str(mini_ish[4])[-3:]}\nПродолжим? 🤗 '''
    bot.answer_callback_query(call.id, text = text, show_alert=True)
    return edit_menu_ruscha(call, SAVAT=SAVAT)



def bushachi_ru(call, callbakdata):
    kal = callbakdata.split('.')
    calldata = kal[1]
    number, response= int(kal[0]), kal[-1]
    #mini_ish = tools.data_parsing(calldata)
    if response == '+':
        number += 1
    elif number >1:
        number -= 1
    made = types.InlineKeyboardMarkup()
    made1 = types.InlineKeyboardButton(text = '➕ ', callback_data=str(number)[0]+'.'+ calldata+'.' + '+')
    made2 = types.InlineKeyboardButton(text = str(number)[0], callback_data = 'nothing')
    made3 = types.InlineKeyboardButton(text='➖ ', callback_data=str(number)[0]+'.'+ calldata+'.' + '-')
    made4 = types.InlineKeyboardButton(text = "🛒 Добовить в корзину", callback_data='savatga_qoshish'+'.'+calldata+'.'+str(number)+'.'+'&')
    made5 = types.InlineKeyboardButton(text = '🔙 Назад', callback_data = calldata+','+'¥')
    menu = types.InlineKeyboardButton(text = '📋 Меню', callback_data= 'menu')
    made.add(made3, made2, made1, row_width=3)
    made.add(made4, made5 ,menu, row_width=1)
    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=made)




def page_answer_ru(call, calldata):
    hajmi = ''
    if calldata.split(',')[0] == 'Pizza':
        main_ish = tools.poisk_pizza(calldata)
        if main_ish[3] == 'Katta':
            hajmi = 'Большой'
    elif calldata.split(',')[0] == 'Ichimliklar':
        main_ish = tools.poisk_ichimlik(calldata)
    else:
        main_ish = tools.data_parsing(calldata)
    text = f'''{STICKERS_DICT[main_ish[2]]}<b>{main_ish[0][-1]} {hajmi}</b>
Цена: {str(main_ish[4])[:-3]}.{str(main_ish[4])[-3:]}
~~~~~~~~~~~~~~~~~
Сколько нужно ⬇️ '''
    number_of_good = 1
    made = types.InlineKeyboardMarkup(row_width=3)
    made1 = types.InlineKeyboardButton(text = '➕ ', callback_data=str(number_of_good)[0]+'.'+ calldata+'.' + '+')
    made2 = types.InlineKeyboardButton(text = str(number_of_good)[0], callback_data = 'nothing')
    made3 = types.InlineKeyboardButton(text='➖ ', callback_data=str(number_of_good)[0]+'.'+ calldata+'.' + '-')
    made4 = types.InlineKeyboardButton(text = "🛒 Добовить в корзину ", callback_data='savatga_qoshish'+'.'+calldata+'.'+str(number_of_good)+'.'+'&')
    made5 = types.InlineKeyboardButton(text = '🔙 Назад', callback_data = calldata+','+'¥')
    menu = types.InlineKeyboardButton(text = '📋 Меню', callback_data= 'menu')
    made.add(made3, made2, made1, row_width=3)
    made.add(made4, made5 ,menu, row_width=1)
    #file = open(str(main_ish[-1]), 'rb')
    #bot.edit_message_media(media=types.InputMedia(type = 'photo', media=file),
    #chat_id =call.message.chat.id,
    #message_id=call.message.id,
    #reply_markup=made
    #)
    bot.edit_message_caption(caption=text, chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=made)
    #file.close()


def pizza_special_ru(call, r, calldata):
    main_ish = tools.data_parsing_pizza(calldata)
    text = f'<b>{STICKERS_DICT[main_ish[1][2]]}{main_ish[1][0][-1]}</b>\n<i>Выберите размер пиццы</i> ⬇️ '
    made = types.InlineKeyboardMarkup()
    h = []
    if len(main_ish[0]) > 1:
        for i in main_ish[0]:
            if i == 'Katta':
                satr = 'Большой'
            elif i == 'Maxsus':
                satr = 'Заказной'
            else:
                satr = 'Средный'
            made1 = types.InlineKeyboardButton(text = satr, callback_data=main_ish[1][2]+','+ calldata[-1] +','+str(i)+'#')
            h.append(made1)
    else:
        return page_answer_ru(call, main_ish[1][2]+','+ calldata[-1] +','+'Katta')
    made2 = types.InlineKeyboardButton(text = '📋 Меню', callback_data='menu')
    made3 = types.InlineKeyboardButton(text='🔙 Назад', callback_data = 'orqaga_pizza')
    made.add(*h, row_width=3)
    made.add(made3, made2, row_width=1)
    #file = open('317599-black-hole-wallpaper.jpg', 'rb')
    #bot.edit_message_media(media=types.InputMedia(type = 'photo', media=file),
    ##chat_id =call.message.chat.id,
    #message_id=call.message.id,
    #reply_markup= made
    #)
    bot.edit_message_caption(caption=text, chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=made)
    #file.close()

def edit_menu_ruscha(call, SAVAT):
    yanam_h = []
    umumiy_summa = 0
    for i in SAVAT:
        if i[-1] == call.message.chat.id:
            yanam_h.append(i[0])
    if len(yanam_h) > 0: 
        for i in yanam_h: 
            umumiy_summa += int(i[-2])*int(i[4])
    mark = types.InlineKeyboardMarkup()
    mark1 = types.InlineKeyboardButton(text='🌯 Лаваш', callback_data='Lavash')
    mark2 = types.InlineKeyboardButton(text='🍔 Бургер', callback_data= 'Chiz')
    mark3 = types.InlineKeyboardButton(text='🌭 Хот Дог', callback_data='hotdog')
    mark4 = types.InlineKeyboardButton(text = '🍕 Пицца', callback_data ='pizza')
    mark01 = types.InlineKeyboardButton(text = '🍛 Пиде', callback_data='turkcha')
    mark8 = types.InlineKeyboardButton(text = '🥙 Донер', callback_data='doner')
    mark6 = types.InlineKeyboardButton(text = '🥘 Кебаб', callback_data='Kavob')
    mark5 = types.InlineKeyboardButton(text = '🍹 Напитки', callback_data='ichimliklar')
    mark9 = types.InlineKeyboardButton(text = '🍟 Фри', callback_data='frie')
    mark7 = types.InlineKeyboardButton(text = '🌐 Выберите язык', callback_data='til_tanlash')
    savat = types.InlineKeyboardButton(text=f'🛒 Корзина({str(umumiy_summa)[:-3]}.{str(umumiy_summa)[-3:]})', callback_data='Savat')
    mark.add(mark4, mark1, mark2, mark3, mark6, mark01,mark5,mark8, mark9, row_width=2)
    mark.add(savat, mark7, row_width=1)
    text = '😋 Что хотите заказать?'
    file = open(PATH +'fastfoodphotos/maxsusfastfood.png', 'rb')
    bot.delete_message(chat_id=call.message.chat.id, message_id = call.message.id)
    bot.send_photo(chat_id = call.message.chat.id, photo = file, caption = text, reply_markup=mark)
    file.close()

def doner_qismi_ru(call):
    text = ''
    son = 0
    names = []
    c = 'Doner'
    a = tools.garakli_list()
    for i in range(len(a)):
        if a[i][2] == 'Doner':
            narx = str(a[i][4])
            names.append(a[i][0][-1])
            son += 1
            #text += str(son) + f'. {a[i][0][-1]} - {narx[:-3]}.{narx[-3:]} сум\n'
    tools.make_inline_button(son, c, names)
    text += f"Категория:🥙 <b>Донер</b>"
    file = open(PATH +'fastfoodphotos/doner.jpg', 'rb')
    bot.edit_message_media(types.InputMedia(type='photo', media=file), chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    bot.edit_message_caption(caption=text, chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    file.close()

def fri_qism_ru(call):
    text = ''
    son = 0
    names = []
    c = 'Frie'
    a = tools.garakli_list()
    text = f"Категория:🍟 <b>Фри</b>"
    for i in range(len(a)):
        if a[i][2] == c: 
            narx = str(a[i][4])
            names.append(a[i][0][-1])
            son += 1
            #text += str(son) + f'. {a[i][0][0]} ---{narx[:-3]}.{narx[-3:]}\n'
    tools.make_inline_button(son, c, names)
    file = open(PATH +'fastfoodphotos/frie.jpg', 'rb')
    bot.edit_message_media(types.InputMedia(type='photo', media=file), chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    bot.edit_message_caption(caption=text, chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    file.close()


def kebab_qismi_ru(call):
    text = ''
    son = 0
    names = []
    c = 'Kavob'
    a = tools.garakli_list()
    for i in range(len(a)):
        if a[i][2] == 'Kavob':
            son += 1
            names.append(a[i][0][-1])
            #text += str(son) + f'. {a[i][0][-1]}--{a[i][4]}\n'
    tools.make_inline_button(son, c, names)
    text += f"Категория:🥘 <b>Кебаб</b>"
    file = open(PATH +'fastfoodphotos/kebab.jpg', 'rb')
    bot.edit_message_media(types.InputMedia(type='photo', media=file), chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    bot.edit_message_caption(caption=text, chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    file.close()

def lavash_qism_ru(call):
    text = ''
    son = 0
    names = []
    c = 'Lavash'
    a = tools.garakli_list()
    for i in range(len(a)):
        if a[i][2] == 'Lavash':
            names.append(a[i][0][-1])
            son += 1
            #text += str(son) + f'. {a[i][0][-1]} - {a[i][4]}\n'
    tools.make_inline_button(son, c, names)
    text += "Категория: 🌯 <b>Лаваш</b>"
    file = open(PATH +'fastfoodphotos/lavash.jpg', 'rb')
    bot.edit_message_media(types.InputMedia(type='photo', media=file), chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    bot.edit_message_caption(caption=text, chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    file.close()
    

def chiz_qismi_ru(call):
    text = ''
    son = 0
    c = 'Chizburger'
    names = []
    a = tools.garakli_list()
    for i in range(len(a)):
        if a[i][2] == 'Chizburger':
            son += 1
            names.append(a[i][0][-1])
            #text += str(son) + f'. {a[i][0][-1]}--{a[i][4]}\n'
    tools.make_inline_button(son, c, names)
    text += "Категория: 🍔 <b>Бургер</b>"
    file = open(PATH +'fastfoodphotos/burger.jpg', 'rb')
    bot.edit_message_media(types.InputMedia(type='photo', media=file), chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    bot.edit_message_caption(caption=text, chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    file.close()

 
def hotdogqismi_ru(call):
    text = ''
    son = 0
    names = []
    c = 'Hotdog'
    a = tools.garakli_list()
    for i in range(len(a)):
        if a[i][2] == 'Hotdog':
            son += 1
            if len(a[i][0][0].split(' ')) < 2 and not '-' in a[i][0][0] and a[i][0][0] != 'Haggi':
                t = a[i][0][-1] + ' Хoт-Дoг'
                names.append(t)
            else:
                names.append(a[i][0][-1])
            #text += str(son) + f'. {a[i][0][-1]}--{a[i][4]}\n'
    text += "Категория: 🌭 <b>Xoт-Дoг</b>"
    tools.make_inline_button(son, c, names)
    file = open(PATH +'fastfoodphotos/hotdog.jpg', 'rb')
    bot.edit_message_media(types.InputMedia(type='photo', media=file), chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    bot.edit_message_caption(caption=text, chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    file.close()

def pizzaqismi_ru(call):
    text = ''
    son = 0
    names = []
    c = 'Pizza'
    a = tools.garakli_list()
    for i in range(len(a)):
        if a[i][2] == 'Pizza' and a[i][3] == 'Katta':
            narx = str(a[i][4])
            names.append(a[i][0][-1])
            son += 1
            #text += str(son) + f'. {a[i][0][-1]}--{narx[:-3]}.{narx[-3:]}\n'
    tools.make_inline_button(son, c, names)
    text += "Категория: 🍕<b>Пицца</b>"
    file = open(PATH +'fastfoodphotos/pizza.jpg', 'rb')
    bot.edit_message_media(types.InputMedia(type='photo', media=file), chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    bot.edit_message_caption(caption=text, chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    file.close()

def ichimlikqismi_ru(call):
    text = ''
    son = 0
    names = []
    c = 'Ichimliklar'
    a = tools.garakli_list()
    for i in range(len(a)):
        if a[i][2] == 'Ichimliklar' and a[i][3] == 'Katta':
            son += 1
            names.append(a[i][0][-1])
            #text += str(son) + f'. {a[i][0][-1]}----{a[i][4]}\n'
    tools.make_inline_button(son, c, names)
    text += "Категория:🍹 <b>Напитки</b>"
    file = open(PATH +'fastfoodphotos/ich.jpg', 'rb')
    bot.edit_message_media(types.InputMedia(type='photo', media=file), chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    bot.edit_message_caption(caption=text, chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    file.close()

def olib_ketish_ru(call):
    text = '''🚶 Вы выбрали тип самовывоза,

Отправьте нам свой номер телефона, чтобы мы могли связаться с вами👇 '''
    key = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    key1 = types.KeyboardButton(text = '📲 Номер телефона', request_contact=True)
    key2 = types.KeyboardButton(text = 'Меню')
    key.add(key1, key2)
    bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=key)

def yana_bir_gemaroy_ru(message):
    text = '📍 Пожалуйста, пишите свой адрес в виде полного сообщения\n\n<b>Например</b>: название улицы, номер дома и популярное общественное место рядом с вашим домом.'
    key = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    key2 = types.KeyboardButton(text = 'Menu')
    key.add(key2)
    bot.send_message(chat_id=message.chat.id, text = text, reply_markup=key)





def after_location_ru(message, SAVAT, ZAKAZLAR):
    contact_id = 0
    re = 0
    for i in ZAKAZLAR:
        if i[-2] == message.chat.id:
            contact_id = i[-1]
            location_id = i[0]
            if len(i) > 2:
                re += 1
    se = 1
    yanam_h = []
    for i in SAVAT:
        if i[-1] == message.chat.id:
            yanam_h.append(i[0])
    text1 = f'BUYURTMA\n{message.from_user.full_name}\n'
    umumiy_summa = 0
    for i in yanam_h:
        text1 += f'''{se}.{i[0][0]} {i[2]} (x{i[-2]})\n  {int(i[-2])*int(i[4])}\n'''
        se += 1
        umumiy_summa += int(i[-2])*int(i[4])
    text1 += '\nUmumiy narx = '+str(umumiy_summa)[:-3] + '.' + str(umumiy_summa)[-3:]
    if re != 0:
        text1 += '\n<i>Yetkazib beriladi</i>'
        bot.send_message(chat_id=-634542393, text = text1)
        bot.forward_message(chat_id=-634542393, from_chat_id=message.chat.id, message_id=location_id)
        bot.forward_message(chat_id=-634542393, from_chat_id=message.chat.id, message_id=contact_id)
    else:
        text1 += '\n<i>Kelib olib ketiladi</i>'
        bot.send_message(chat_id=-634542393, text = text1)
        bot.forward_message(chat_id=-634542393, from_chat_id=message.chat.id, message_id=contact_id)
    text = '✅ Ваш заказ принят'
    made = types.ReplyKeyboardRemove()
    bot.delete_message(chat_id=message.chat.id, message_id=message.id)
    bot.send_message(chat_id=message.chat.id, text = text, reply_markup=made)
    for u in ZAKAZLAR:
            if u[1] == message.chat.id:
                ZAKAZLAR.pop(ZAKAZLAR.index(u))
                break
    return menu_ruscha(message, SAVAT=SAVAT)
    

def tasdiqlash_ru(message, SAVAT, ZAKAZLAR):
    re = 0
    contact = 0
    location = 0
    for i in ZAKAZLAR:
        if i[-1] == message.chat.id:
            phone = message.contact.phone_number
            contact = message.id
            location = i[0]
            i.append(message.id)
            re += 1
            break
    else:
        phone = message.contact.phone_number
        ZAKAZLAR.append([message.chat.id, message.id])
    
    yanam_h = []
    for i in SAVAT:
        if i[-1] == message.chat.id:
            yanam_h.append(i[0])
    text = f'<b>ВАШ ЗАКАЗ:</b>\n'
    umumiy_summa = 0
    for i in yanam_h:
        turi = ''
        if i[2] == 'Hotdog' and len(i[0][0].split(' ')) < 2 and not '-' in i[0][0] and i[0][0] != 'Haggi':
            turi = 'Хот-Дог'
        elif i[2] == 'Pizza':
            turi = 'Пицца'
        narx = str(int(i[-2])*int(i[4]))
        text += f'''{STICKERS_DICT[i[2]]}<b>{i[0][-1]} {turi}</b> (x{i[-2]}):\n └ {i[-2]}x{str(i[4])[:-3]}.{str(i[4])[-3:]} = {narx[:-3]}.{narx[-3:]} \n\n'''
        umumiy_summa += int(narx)
    text += '\n<b>Итого:</b> '+str(umumiy_summa)[:-3] + '.' + str(umumiy_summa)[-3:]
    text += '\n<b>Тип доставки:</b>'
    if re != 0:
        text += '🚚 Доставка'
    else:
        text += '🚶 Прийти и взять'
    text += f'\n<b>Номер телефона</b>: +{phone}'
    mark = types.InlineKeyboardMarkup(row_width=1)
    mark1 = types.InlineKeyboardButton(text = '✅ Подтверждать', callback_data='tasdiqlash_menu')
    mark2 = types.InlineKeyboardButton(text = '❌ Отменить', callback_data='bekor_menu')
    mark.add(mark1, mark2)
    bot.send_message(chat_id = message.chat.id, text = text, reply_markup=mark)



def before_location_ru(message, ZAKAZLAR):
    text = '''✅ Ваш адрес введен.

Отправьте нам свой номер телефона, чтобы мы могли связаться с вами👇'''
    ZAKAZLAR.append([message.id, message.chat.id])
    key = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    key3 = types.KeyboardButton(text = '📲 Отправить номер телефона',request_contact=True)
    #key3 = types.KeyboardButton(text = '📍Location', request_location=True)
    key2 = types.KeyboardButton(text = 'Меню')
    key.add(key3, key2) 
    bot.send_message(chat_id=message.chat.id, text=text, reply_markup=key)

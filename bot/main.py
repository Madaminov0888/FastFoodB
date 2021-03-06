import telebot
from ruscha_main import *
from qismlar import *
import config
from app.models import Foods, BotUser, Boshagurung
import tools
from telebot import types


TOKEN = '5209072169:AAHIkqoHNC38dOAaAJVe9y9siKOGGYa5pVc'

bot = telebot.TeleBot(
    token=TOKEN,
    parse_mode='HTML',
    num_threads=4,
)
SAVAT = []
LANG = []
SPECIPIC_ID=-634542393
ZAKAZLAR = []
STICKERS_DICT = {'Lavash':'π― ', 'Chizburger': 'π ', 'Hotdog':'π­ ', 'Pizza' : 'π', 'Ichimliklar': 'πΉ', 'Frie':'π ', 'Kavob':'π₯ ', 'Doner':'π₯ ', 'TurkchaPitsa':'π '}


@bot.message_handler(commands=['start'])
def til_tanlash(message):
    text = f'πΊπΏ Tilni tanlang\nπ·πΊΠΡΠ±Π΅ΡΠΈΡΠ΅ ΡΠ·ΡΠΊ'
    made = types.InlineKeyboardMarkup()
    made1 = types.InlineKeyboardButton(text = 'π·πΊ Π ΡΡΡΠΊΠΈΠΉ', callback_data='rus_tili')
    made2 = types.InlineKeyboardButton(text = "πΊπΏ O'zbek tili", callback_data='uzbek_tili')
    made.add(made1, made2)
    bot.set_my_commands(commands=['start', 'menu', "tilni_o'zgartirish"])
    bot.send_message(chat_id=message.chat.id, text = text, reply_markup=made)

@bot.message_handler(commands=["tilni_o'zgartirish"])
def rerun(message):
    return til_tanlash(message)


@bot.message_handler(commands=['menu'])

def menu(message):
    yanam_h = []
    umumiy_summa = 0
    for i in SAVAT:
        if i[-1] == message.chat.id:
            yanam_h.append(i[0])
    if len(yanam_h) > 0: 
        for i in yanam_h:
            umumiy_summa += int(i[-2])*int(i[4])
    mark = types.InlineKeyboardMarkup()
    mark1 = types.InlineKeyboardButton(text='π― Lavash', callback_data='Lavash')
    mark2 = types.InlineKeyboardButton(text='π Burgerlar', callback_data= 'Chiz')
    mark3 = types.InlineKeyboardButton(text='π­ Hot-Dog', callback_data='hotdog')
    mark4 = types.InlineKeyboardButton(text = 'π Pizza', callback_data ='pizza')
    mark01 = types.InlineKeyboardButton(text = 'π Turkcha Pitsa', callback_data='turkcha')
    mark6 = types.InlineKeyboardButton(text = 'π₯ Kavoblar', callback_data='Kavob')
    mark5 = types.InlineKeyboardButton(text = 'πΉ Ichimliklar', callback_data='ichimliklar')
    mark8 = types.InlineKeyboardButton(text = 'π₯ Doner', callback_data ='doner')
    mark9 = types.InlineKeyboardButton(text = 'π Frie', callback_data='frie')
    mark7 = types.InlineKeyboardButton(text = 'π Til tanlash', callback_data='til_tanlash')
    savat = types.InlineKeyboardButton(text=f"π Savat({str(umumiy_summa)[:-3]}.{str(umumiy_summa)[-3:]} so'm)", callback_data='Savat')
    mark.add(mark4, mark1, mark2, mark3, mark01,mark6, mark5, mark8, mark9,row_width=2)
    mark.add(savat, mark7, row_width=1)
    text = f'π Nima buyurtma bermoqchisiz?'
    file = open('fastfoodphotos/maxsusfastfood.png', 'rb')
    bot.send_photo(message.chat.id,
    file,
    caption=text,
    reply_markup=mark
    )
    file.close()


@bot.callback_query_handler(func = lambda call: True)
def inli(call, LANG=LANG):
    if call.data == 'til_tanlash':
        return til_tanlash(call.message)
    elif call.data == 'uzbek_tili':
        for i in LANG:
            if i[-1] == call.message.chat.id:
                if i[0] == 'uz':
                    return menu(call.message)
                else:
                    i[0] = 'uz'
                    return menu(call.message)
        else:
            LANG.append(['uz', call.message.chat.id])
            return menu(call.message)
    elif call.data == 'rus_tili':
        for i in LANG:
            if i[-1] == call.message.chat.id:
                if i[0] == 'rus':
                    return menu_ruscha(call.message, SAVAT=SAVAT)
                else:
                    i[0] = 'rus'
                    return menu_ruscha(call.message, SAVAT = SAVAT)
        else:
            LANG.append(['rus', call.message.chat.id])
            return menu_ruscha(call.message, SAVAT=SAVAT)
    elif call.data == 'menu_start':
        for i in LANG:
            if i[-1] == call.message.chat.id and i[0] == 'rus':
                return menu_ruscha(call.message, SAVAT = SAVAT)
        return menu(call.message)
    for i in LANG:
        if i[-1] == call.message.chat.id and i[0] == 'rus':
            if call.data == 'Chiz':
                return chiz_qismi_ru(call)
            elif call.data == 'menu': 
                return edit_menu_ruscha(call, SAVAT=SAVAT)
            elif call.data == 'Lavash':
                return lavash_qism_ru(call)
            elif call.data == 'hotdog':
                return hotdogqismi_ru(call)
            elif call.data == 'pizza':
                return pizzaqismi_ru(call)
            elif call.data == 'ichimliklar':
                return ichimlikqismi_ru(call)
            elif call.data[-1] == '&':
                return savatga_qoshish_ru(call, call.data, SAVAT=SAVAT)
            elif call.data == 'Savat':
                return savat_ru(call, SAVAT=SAVAT)
            elif call.data == 'Kavob':
                return kebab_qismi_ru(call)
            elif call.data.split(',')[-1] == 'Β₯':
                return tools.orqaga_tugmalari_ru(call, call.data)
            elif call.data == 'clear_savat':
                return clear_ru(call, SAVAT=SAVAT)
            elif call.data == 'frie':
                return fri_qism_ru(call)
            elif call.data == 'buyurtma_berish':
                return buyurtma_bolimi_ru(call)
            elif call.data == 'yetkazib_berish':
                return yetkazib_berish_ru(call)
            elif call.data == 'orqaga_pizza':
                return pizzaqismi_ru(call)
            elif call.data == 'orqaga_ichimliklar':
                return ichimlikqismi_ru(call)
            elif call.data == 'doner':
                return doner_qismi_ru(call)
            elif call.data == 'turkcha':
                return turkcha_pizza_ru(call)
            elif call.data[-1] == '#':
                a = call.data[:-1]
                return page_answer_ru(call, a)
            elif call.data[-1] == '+' or call.data[-1] == '-':
                return bushachi_ru(call, call.data)
            elif call.data == 'olib_ketish':
                return olib_ketish_ru(call)
            elif call.data[0] == '$':
                return delete_from_sevat_ru(call, call.data[-1], SAVAT=SAVAT)
            elif call.data[-1] in '1234567890':
                a = call.data
                r = a.split(',')
                if r[0] == 'Pizza':
                    return pizza_special_ru(call, r, a)
                elif r[0] == 'Ichimliklar':
                    return ichimliklar_special_ru(call, r, call.data)
                return page_answer_ru(call, str(a))
    else:
        if call.data == 'Chiz':
            return chiz_qismi(call)
        elif call.data == 'Lavash':
            return lavash_qism(call)
        elif call.data[0] == '$':
            return delete_from_sevat(call, call.data[-1])
        elif call.data == 'menu':
            return edit_menu(call)
        elif call.data == 'hotdog':
            return hotdogqismi(call)
        elif call.data == 'pizza':
            return pizzaqismi(call)
        elif call.data == 'frie':
            return fri_qism(call)
        elif call.data == 'ichimliklar':
            return ichimlikqismi(call)
        elif call.data[-1] == '&':
            return savatga_qoshish(call, call.data)
        elif call.data == 'Savat':
            return savat(call)
        elif call.data == 'Kavob':
            return kebab_qismi(call)
        elif call.data == 'clear_savat':
            return clear(call)
        elif call.data == 'buyurtma_berish':
            return buyurtma_bolimi(call)
        elif call.data == 'orqaga_pizza':
            return pizzaqismi(call)
        elif call.data == 'orqaga_ichimliklar':
            return ichimlikqismi(call)
        elif call.data == 'yetkazib_berish':
            return yetkazib_berish(call)
        elif call.data[-1] == '+' or call.data[-1] == '-':
            return bushachi(call, call.data)
        elif call.data == 'olib_ketish':
            return olib_ketish(call)
        elif call.data == 'doner':
            return doner_qismi(call)
        elif call.data.split(',')[-1] == 'Β₯':
            return tools.orqaga_tugmalari(call, call.data)
        elif call.data == 'turkcha':
            return turkcha_pizza(call)
        elif call.data[-1] == '#':
            a = call.data[:-1]
            return page_answer(call, a)
        elif call.data[-1] in '1234567890':
            a = call.data
            r = a.split(',')
            if r[0] == 'Pizza':
                return pizza_special(call, r, a)
            elif r[0] == 'Ichimliklar':
                return ichimliklar_special(call, r, call.data)
            return page_answer(call, str(a))


def yetkazib_berish(call):
    text = '''π Siz yetkazib berish bolimini tanladingiz
<i>Sizga buyurtmangizni yetkazib berish uchun uzingizning geolakatsiayangizni yuboring</i>'''
    key = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    key0 = types.KeyboardButton(text = "π Manzilni qo'lda kiritish", )
    key1 = types.KeyboardButton(text = 'π Manzil', request_location=True)
    key2 = types.KeyboardButton(text = 'π Menu')
    key.add(key1, key0, key2)
    bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=key)


def buyurtma_bolimi(call):
    text = 'Buyurtmani qanday olmoqchisiz??'
    made = types.InlineKeyboardMarkup()
    made1 = types.InlineKeyboardButton(text = 'π Yetkazib berish', callback_data='yetkazib_berish')
    made2 = types.InlineKeyboardButton(text = 'πΆ Kelib olib ketish', callback_data='olib_ketish')
    menu = types.InlineKeyboardButton(text = 'π Menu', callback_data= 'menu')
    made.add(made1, made2, menu, row_width=1)
    file = open('fastfoodphotos/maxsusfastfood.png', 'rb')
    #bot.edit_message_caption(caption=text, chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=made)
    bot.delete_message(chat_id=call.message.chat.id, message_id = call.message.id)
    bot.send_photo(chat_id = call.message.chat.id, photo = file, caption= text,reply_markup=made)


def delete_from_sevat(call, number):
    s = SAVAT
    x = 1
    for i in s:
        if i[-1] == call.message.chat.id:
            if x == int(number):
                SAVAT.pop(SAVAT.index(i))
                break
            else:
                x += 1
    text = f"{i[0][0][0]} o'chirildi"
    bot.answer_callback_query(call.id, text = text, show_alert=True)
    return savat(call)

            

def clear(call):
    text = '''Savat tozalandi'''
    for i in SAVAT.copy():
        if i[-1] == call.message.chat.id:
            SAVAT.pop(SAVAT.index(i))

    made = types.InlineKeyboardMarkup()
    menu = types.InlineKeyboardButton(text = 'π Menu', callback_data= 'menu')
    made.add(menu, row_width=1)
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
    bot.send_message(chat_id=call.message.chat.id, text = text, reply_markup=made)


def savat(call):
    s = SAVAT
    umumiy_summa = 0
    text = '''π¦ SAVAT\n\n'''
    se = 1
    yanam_h = []
    made = types.InlineKeyboardMarkup()
    made1 = types.InlineKeyboardButton(text='β Buyurtma berish', callback_data='buyurtma_berish')
    made.add(made1, row_width=1)
    for i in s:
        if i[-1] == call.message.chat.id:
            yanam_h.append(i[0])
    buttons = []
    if len(yanam_h) > 0:
        for i in yanam_h:
            turi = ''
            if i[2] == 'Hotdog' and len(i[0][0].split(' ')) < 2 and not '-' in i[0][0] and i[0][0] != 'Haggi':
                turi = 'Hot-Dog'
            elif i[2] == 'Pizza':
                turi = 'Pizza'
            narx = str(int(i[-2])*int(i[4]))
            text += f'''{STICKERS_DICT[i[2]]}<b>{i[0][0]} {turi}</b> (x{i[-2]}):\n   {i[-2]}x{str(i[4])[:-3]}.{str(i[4])[-3:]} = {narx[:-3]}.{narx[-3:]} so'm\n\n'''
            sd = types.InlineKeyboardButton(text = f'β {i[0][0]} {turi}', callback_data=f'$ochirish_{se}')
            buttons.append(sd)
            se += 1
            umumiy_summa += int(i[-2])*int(i[4])
        if len(yanam_h) > 1:
            made.add(*buttons, row_width=1)
        text += 'Umumiy narx: '+str(umumiy_summa)[:-3]+'.' + str(umumiy_summa)[-3:]+" so'm"
        made2 = types.InlineKeyboardButton(text = 'π Savatchani tozalash', callback_data='clear_savat')
        menu = types.InlineKeyboardButton(text = 'π Menu', callback_data= 'menu')
        made.add(made2, menu, row_width=1)

    else:
        text += 'π Savat bosh'
        made = types.InlineKeyboardMarkup()
        menu = types.InlineKeyboardButton(text = 'π Menu', callback_data= 'menu')
        made.add(menu, row_width=1)

    #file = open('317599-black-hole-wallpaper.jpg', 'rb')
    #bot.edit_message_media(media=types.InputMedia(type = 'photo', media=file),
    #chat_id =call.message.chat.id,
    #message_id=call.message.id,
    #reply_markup=made
    #)
    bot.delete_message(chat_id=call.message.chat.id, message_id = call.message.id)
    bot.send_message(chat_id=call.message.chat.id, text = text, reply_markup=made)
    #file.close()



def savatga_qoshish(call, test):
    kal_main = test.split('.')
    soni, data = kal_main[2], kal_main[1]
    data_pizza = data.split(',')[0]
    if data_pizza == 'Pizza':
        m = tools.poisk_pizza(data)
    elif data_pizza == 'Ichimliklar':
        m = tools.poisk_ichimlik(data)
    else:
        m = tools.data_parsing(data)
    m.append(soni)
    m.append(data)
    h = []
    h.append(m)
    h.append(call.message.chat.id)
    SAVAT.append(h)
    #made = types.InlineKeyboardMarkup(row_width=3)
    #menu = types.InlineKeyboardButton(text = 'Menu', callback_data= 'menu')
    #savat = types.InlineKeyboardButton(text='π Savat', callback_data='Savat')
    #made.add(menu, savat)
    s = m[4]
    t = m[0][0]
    text = f'''β Savatga joylandi\n{t} x{m[-2]} - {str(m[4])[:-3]}.{str(m[4])[-3:]} so'm\nDavom ettiramizmi?'''
    #bot.send_message(chat_id=call.message.chat.id, text = text)
    bot.answer_callback_query(call.id,text = text, show_alert=True)
    return edit_menu(call)



def bushachi(call, callbakdata):
    kal = callbakdata.split('.')
    calldata = kal[1]
    number, response= int(kal[0]), kal[-1]
    #mini_ish = tools.data_parsing(calldata)
    if response == '+':
        number += 1
    elif number >1:
        number -= 1
    made = types.InlineKeyboardMarkup()
    made1 = types.InlineKeyboardButton(text = 'β ', callback_data=str(number)[0]+'.'+ calldata+'.' + '+')
    made2 = types.InlineKeyboardButton(text = str(number)[0], callback_data = 'nothing')
    made3 = types.InlineKeyboardButton(text='β ', callback_data=str(number)[0]+'.'+ calldata+'.' + '-')
    made4 = types.InlineKeyboardButton(text = "π Savatga qo'shish", callback_data='savatga_qoshish'+'.'+calldata+'.'+str(number)+'.'+'&')
    made5 = types.InlineKeyboardButton(text = 'π orqaga', callback_data = calldata+','+'Β₯')
    menu = types.InlineKeyboardButton(text = 'π Menu', callback_data= 'menu')
    made.add(made3, made2, made1, row_width=3)
    made.add(made4, made5 ,menu, row_width=1)
    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=made)


def pizza_special(call, r, calldata):
    main_ish = tools.data_parsing_pizza(calldata)
    text = f'<b>π {main_ish[1][0][0]}</b>\n<i>Pitsaning hajmini tanlang</i> β¬οΈ '
    made = types.InlineKeyboardMarkup()
    h = []
    s = ''
    if len(main_ish[0]) > 1:
        for i in main_ish[0]:
            made1 = types.InlineKeyboardButton(text = str(i), callback_data=main_ish[1][2]+','+ calldata[-1] +','+str(i)+'#')
            h.append(made1)
    else:
        return page_answer(call, main_ish[1][2]+','+ calldata[-1] +','+'Katta')
    made3 = types.InlineKeyboardButton(text = 'π Orqaga', callback_data='orqaga_pizza')
    made2 = types.InlineKeyboardButton(text = 'π Menu', callback_data='menu')
    made.add(*h, row_width=3)
    made.add(made3, made2, row_width=1)
    #file = open('317599-black-hole-wallpaper.jpg', 'rb')
    #bot.edit_message_media(media=types.InputMedia(type = 'photo', media=file),
    #chat_id =call.message.chat.id,
    #message_id=call.message.id,
    #reply_markup=made
    #)
    bot.edit_message_caption(caption=text, chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=made)
    #file.close()


def ichimliklar_special(call, r, calldata):
    main_ish = tools.data_parsing_ichimlik(calldata)
    text = f'<b>{main_ish[1][0][0]}</b>\n<i>Ichimlik turini tanlang</i> β¬οΈ '
    made = types.InlineKeyboardMarkup()
    h = []
    satr = ''
    for i in main_ish[0]:
        if main_ish[1][0][0].split(' ')[0] in ['Fanta','Koka-Kola', 'Pepsi']:
            file = open('fastfoodphotos/kola.jpg', 'rb')
            if i == 'Katta':
                satr = '1 Litrlik'
            elif i == "O'rtacha":
                satr = '0.5 Litrlik'
            elif i == 'Maxsus':
                satr = '1.5 Litrlik'
        elif main_ish[1][0][0].split(' ')[0] == 'Kofe':
            file = open('fastfoodphotos/kofe.jpg', 'rb')
            if i == 'Katta':
                satr = 'Qora kofe'
            elif i == 'Maxsus':
                satr = 'Kapuchino'
            elif i == "O'rtacha":
                satr = 'Sutli Kofe'
        else:
            file = open('fastfoodphotos/choy.jpg', 'rb')
            if i == 'Katta':
                satr = 'Qora choy'
            elif i == 'Maxsus':
                satr = "Ko'k choy"
            elif i == "O'rtacha":
                satr = 'Limonli choy'

        made1 = types.InlineKeyboardButton(text = satr, callback_data=main_ish[1][2]+','+ calldata[-1] +','+str(i)+'#')
        h.append(made1)
    made2 = types.InlineKeyboardButton(text = 'π Menu', callback_data='menu')
    made3 = types.InlineKeyboardButton(text = 'π Orqaga', callback_data='orqaga_ichimliklar')
    made.add(*h, row_width=3)
    made.add(made3, made2, row_width=1)
    bot.edit_message_media(types.InputMedia(type='photo', media=file), chat_id= call.message.chat.id, message_id= call.message.id, reply_markup=tools.mini)
    bot.edit_message_caption(caption=text, chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=made)

def page_answer(call, calldata):
    hajmi = ''
    if calldata.split(',')[0] == 'Pizza':
        main_ish = tools.poisk_pizza(calldata)
        if main_ish[3] == 'Katta':
            hajmi = 'Katta'
    elif calldata.split(',')[0] == 'Ichimliklar': 
        main_ish = tools.poisk_ichimlik(calldata)
    else:
        main_ish = tools.data_parsing(calldata)
    text = f'''{STICKERS_DICT[main_ish[2]]}<b>{main_ish[0][0]} {hajmi}</b>
Narxi: {str(main_ish[4])[:-3]}.{str(main_ish[4])[-3:]} so'm
~~~~~~~~~~~~~~~~~
<i>Iltimos kerakli miqdorni kiriting</i> β¬οΈ
    '''
    number_of_good = 1
    made = types.InlineKeyboardMarkup(row_width=3)
    made1 = types.InlineKeyboardButton(text = 'β ', callback_data=str(number_of_good)[0]+'.'+ calldata+'.' + '+')
    made2 = types.InlineKeyboardButton(text = str(number_of_good)[0], callback_data = 'nothing')
    made3 = types.InlineKeyboardButton(text='β ', callback_data=str(number_of_good)[0]+'.'+ calldata+'.' + '-')
    made4 = types.InlineKeyboardButton(text = "π Savatga qo'shish", callback_data='savatga_qoshish'+'.'+calldata+'.'+str(number_of_good)+'.'+'&')
    made5 = types.InlineKeyboardButton(text = 'π orqaga', callback_data = calldata+','+'Β₯')
    menu = types.InlineKeyboardButton(text = 'π Menu', callback_data= 'menu')
    made.add(made3, made2, made1, row_width=3)
    made.add(made4, made5 ,menu, row_width=1)
    #file = open(str(main_ish[-1]), 'rb')
    #bot.edit_message_media(media=types.InputMedia(type = 'photo', media=file),
    #chat_id =call.message.chat.id,
    #message_id=call.message.id,
    #reply_markup=made
    #)
    bot.edit_message_caption(caption=text, chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=made)



def edit_menu(call):
    yanam_h = []
    umumiy_summa = 0
    for i in SAVAT:
        if i[-1] == call.message.chat.id:
            yanam_h.append(i[0])
    if len(yanam_h) > 0:
        for i in yanam_h:
            umumiy_summa += int(i[-2])*int(i[4])
    mark = types.InlineKeyboardMarkup()
    mark1 = types.InlineKeyboardButton(text='π― Lavash', callback_data='Lavash')
    mark2 = types.InlineKeyboardButton(text='π Burgerlar', callback_data= 'Chiz')
    mark3 = types.InlineKeyboardButton(text='π­ Hot-Dog', callback_data='hotdog')
    mark4 = types.InlineKeyboardButton(text = 'π Pizza', callback_data ='pizza')
    mark01 = types.InlineKeyboardButton(text = 'π Turkcha Pitsa', callback_data='turkcha')
    mark6 = types.InlineKeyboardButton(text = 'π₯ Kavoblar', callback_data='Kavob')
    mark5 = types.InlineKeyboardButton(text = 'πΉ Ichimliklar', callback_data='ichimliklar')
    mark8 = types.InlineKeyboardButton(text = 'π₯ Doner', callback_data ='doner')
    mark9 = types.InlineKeyboardButton(text = 'π Frie', callback_data='frie')
    mark7 = types.InlineKeyboardButton(text = 'π Til tanlash', callback_data='til_tanlash')
    savat = types.InlineKeyboardButton(text=f"π Savat({str(umumiy_summa)[:-3]}.{str(umumiy_summa)[-3:]} so'm)", callback_data='Savat')
    mark.add(mark4, mark1, mark2, mark3, mark01,mark6, mark5, mark8, mark9,row_width=2)
    mark.add(savat, mark7, row_width=1)
    text = 'π Nima buyurtma bermoqchisiz?'
    file = open('fastfoodphotos/maxsusfastfood.png', 'rb')
    bot.delete_message(chat_id=call.message.chat.id, message_id = call.message.id)
    bot.send_photo(chat_id = call.message.chat.id, photo = file, caption = text, reply_markup=mark)
    file.close()




def olib_ketish(call):
    text = '''Siz olib ketish turini tanladingiz
    Iltimos telefon raqamingizni qoldiring'''
    key = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    key1 = types.KeyboardButton(text = 'π² Telefon raqam', request_contact=True)
    key2 = types.KeyboardButton(text = 'Menu')
    key.add(key1, key2)
    bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=key)


@bot.message_handler()
def keybord(message):
    if message.text == 'Menu':
        return menu(message)
    elif message.text == 'ΠΠ΅Π½Ρ':
        return menu_ruscha(message, SAVAT)
    elif message.text == "π Manzilni qo'lda kiritish":
        return yana_bir_gemaroy(message)
    elif message.text == 'π ΠΠ²Π΅ΡΡΠΈ Π°Π΄ΡΠ΅Ρ Π²ΡΡΡΠ½ΡΡ':
        return yana_bir_gemaroy_ru(message)
    else:
        for i in LANG:
            if i[-1] == message.chat.id:
                if i[0] == 'uz':
                    return before_location(message)
                else:
                    return before_location_ru(message, ZAKAZLAR=ZAKAZLAR)
        else:
            return before_location(message)

def yana_bir_gemaroy(message):
    text = 'Iltimos manzilingizni toliq xabar shaklida yuboring\nMasalan: Kocha nomi, uy nomeri va uyingiz yaqinidagi mashhur jamoat joyi'
    key = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    key2 = types.KeyboardButton(text = 'Menu')
    key.add(key2)
    bot.send_message(chat_id=message.chat.id, text = text, reply_markup=key)



@bot.message_handler(func=lambda message: True, content_types=['contact'])
def ajibuju(message):
    for i in LANG:
        if i[-1] == message.chat.id:
            if i[0] == 'uz':
                return after_location(message)
            else:
                return after_location_ru(message, SAVAT = SAVAT,ZAKAZLAR=ZAKAZLAR)
    else:
        return after_location(message)


def after_location(message):
    contact_id = 0
    re = 0
    for i in ZAKAZLAR:
        if i[-1] == message.chat.id:
            contact_id = i[0]
            re += 1
    se = 1
    yanam_h = []
    for i in SAVAT:
        if i[-1] == message.chat.id:
            yanam_h.append(i[0])
    text1 = f'π¨ BUYURTMA\n{message.from_user.full_name}\n'
    umumiy_summa = 0
    for i in yanam_h:
        text1 += f'''{se}.{i[0][0]} {i[2]} x{i[-2]}\n  {int(i[-2])*int(i[4])}\n'''
        se += 1
        umumiy_summa += int(i[-2])*int(i[4])
    text1 += '\nUmumiy narx = '+str(umumiy_summa)[:-3] + '.' + str(umumiy_summa)[-3:]
    if re != 0:
        text1 += '\n<i>Yetkazib beriladi</i>'
        bot.send_message(chat_id=-634542393, text = text1)
        bot.forward_message(chat_id=-634542393, from_chat_id=message.chat.id, message_id=message.id)
        bot.forward_message(chat_id=-634542393, from_chat_id=message.chat.id, message_id=contact_id)
        for u in ZAKAZLAR:
            if u[1] == message.chat.id:
                ZAKAZLAR.pop(ZAKAZLAR.index(u))
                break
    else:
        text1 += '\n<i>Kelib olib ketiladi</i>'
        bot.send_message(chat_id=-634542393, text = text1)
        bot.forward_message(chat_id=-634542393, from_chat_id=message.chat.id, message_id=message.id)
    text = 'Sizning buyurtmangiz qabul qilindi'
    made = types.ReplyKeyboardRemove()
    bot.send_message(chat_id=message.chat.id, text = text, reply_markup=made)
    return menu(message)
    


@bot.message_handler(func=lambda message: True, content_types=['location'])
def ajibuju(message):
    return before_location(message)

def before_location(message):
    text = '''π Siz yetkazib berish bolimini tanladingiz
<u>Sizga buyurtmani yetkazish uchun telefon raqamingizni yuboring</u>'''
    ZAKAZLAR.append([message.id, message.chat.id])
    key = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    key3 = types.KeyboardButton(text = 'π Number',request_contact=True)
    #key3 = types.KeyboardButton(text = 'πLocation', request_location=True)
    key2 = types.KeyboardButton(text = 'Menu')
    key.add(key3, key2)
    bot.send_message(chat_id=message.chat.id, text=text, reply_markup=key)




if __name__ == '__main__':
    bot.polling(none_stop=True)
    bot.infinity_polling()



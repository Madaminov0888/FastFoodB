from turtle import title
from telebot import types
from bot.main import *
from bot.ruscha_main import *
import telebot
import config
from app.models import Foods, BotUser, Boshagurung
from django.contrib.auth.models import User

SAVAT = []

def garakli_list()->list:
    title_of_fields = Foods.objects.values_list('title')
    x = 0
    for i in title_of_fields:
        x += 1
    title_ru = Foods.objects.values_list('title_ru')
    rest = []
    for i in range(x):
        h = [[str(title_of_fields[i][0]), title_ru[i][0]],]
        h.append([Foods.objects.filter(title = str(title_of_fields[i][0])).values_list('description')[0][0], Foods.objects.filter(title = str(title_of_fields[i][0])).values_list('description_ru')[0][0]])
        h.append(Foods.objects.filter(title = str(title_of_fields[i][0])).values_list('type')[0][0])
        h.append(Foods.objects.filter(title = str(title_of_fields[i][0])).values_list('Size')[0][0])
        h.append(Foods.objects.filter(title = str(title_of_fields[i][0])).values_list('sum')[0][0])
        #h.append(Foods.objects.filter(title = str(title_of_fields[i][0])).values_list('file')[0][0])
        rest.append(h)
    return rest
#[['Lavash', 'Лаваш'], ['DIM zor', 'пап'], 'Lavash', 'Kichik', 17000]
#print(garakli_list())

mini = 0
garakdir = []

#print(BotUser.objects.get(chat_id = 1285748848, full_name = 'Muhammadjon Madaminov').chat_id)


def make_inline_button(raqam, callbak, names):
    global mini, garakdir
    mini = types.InlineKeyboardMarkup()
    menu = types.InlineKeyboardButton(text = '📋 Menu', callback_data= 'menu')
    h = []
    for i in range(raqam):
        text = names[i]
        call_back_data = callbak + ','+ str(i+1)
        garakdir.append(call_back_data)
        x = types.InlineKeyboardButton(text, callback_data = call_back_data)
        h.append(x)
    mini.add(*h, row_width=2)
    mini.add(menu)


def searcher_len(tpy):
    er = Foods.objects.filter(type = str(tpy))
    return len(er)


def data_parsing(calldata:str)->list:
    pars = calldata.split(',')
    a, b = pars[0], int(pars[1])
    x = 0
    if a != 'Pizza' and a!= 'Ichimliklar':
        for i in garakli_list():
            if i[2] == a:
                x += 1
            if x == b:
                return i
    else:
        for i in garakli_list():
            if i[2] == a and i[3] == 'Katta':
                x += 1
            if x == b:
                return i


def data_parsing_pizza(calldata:str)->list:
    pars = calldata.split(',')
    a, b = pars[0], int(pars[-1])
    x = 0
    h = []
    z = []
    d = data_parsing(calldata)[0][0]
    for i in garakli_list():
        if i[0][0].split(' ')[0] == d:
            h.append(i[3])
    z.append(h)
    z.append(data_parsing(calldata))
    return z

#print(data_parsing_pizza('Pizza,8'))


def data_parsing_ichimlik(calldata:str)->list:
    pars = calldata.split(',')
    a, b = pars[0], int(pars[-1])
    x = 0
    h = []
    z = []
    d = data_parsing(calldata)[0][0]
    for i in garakli_list():
        if i[0][0].split(' ')[0] == d:
            h.append(i[3])
    z.append(h)
    z.append(data_parsing(calldata))
    return z
#print(data_parsing_ichimlik('Ichimliklar,3'))

def poisk_pizza(calldata:str):
    ser = calldata.split(',')
    a, b, c = ser[0], ser[1], ser[2]
    dr =[]
    x = 0
    for i in garakli_list():
        if i[2] == a and i[3] == 'Katta':
            x += 1
            if x == int(b):
                dr.append(i)
    title1 = dr[0][0][0]
    for i in garakli_list():
        title = i[0][0].split(' ')[0]
        size = i[3]
        tpy = i[2]
        if tpy == 'Pizza' and title == title1 and size == c:
            return i


def poisk_ichimlik(calldata:str):
    ser = calldata.split(',')
    a, b, c = ser[0], ser[1], ser[2]
    dr =[]
    x = 0
    for i in garakli_list():
        if i[2] == a and i[3] == 'Katta':
            x += 1
            if x == int(b):
                dr.append(i)
    title1 = dr[0][0][0]
    for i in garakli_list():
        title = i[0][0].split(' ')[0]
        size = i[3]
        tpy = i[2]
        if tpy == 'Ichimliklar' and title == title1 and size == c:
            return i

#print(poisk_ichimlik('Ichimliklar,1,Maxsus'))

def orqaga_tugmalari(call, callbak:str):
    a = callbak.split(',')[0]
    kall = callbak.split(',')
    need = kall[0]+','+kall[1]
    if a == 'Pizza' and int(kall[1]) == 2:
        return pizzaqismi(call)
    elif a == 'Pizza':
        return pizza_special(call, 2, need)
    elif a == 'TurkchaPitsa':
        return turkcha_pizza(call)
    elif a == 'Doner':
        return doner_qismi(call)
    elif a == 'Chizburger':
        return chiz_qismi(call)
    elif a == 'Kavob':
        return kebab_qismi(call)
    elif a == 'Lavash':
        return lavash_qism(call)
    elif a == 'Hotdog':
        return hotdogqismi(call)
    elif a == 'Ichimliklar':
        return ichimliklar_special(call, 2, need)
    elif a == 'Frie':
        return fri_qism(call)
    

def orqaga_tugmalari_ru(call, callbak:str):
    a = callbak.split(',')[0]
    kall = callbak.split(',')
    need = kall[0]+','+kall[1]
    if a == 'Pizza' and int(kall[1]) == 2:
        return pizzaqismi_ru(call)
    elif a == 'Pizza':
        return pizza_special_ru(call, 2, need)
    elif a == 'TurkchaPitsa':
        return turkcha_pizza_ru(call)
    elif a == 'Doner':
        return doner_qismi_ru(call)
    elif a == 'Chizburger':
        return chiz_qismi_ru(call)
    elif a == 'Kavob':
        return kebab_qismi_ru(call)
    elif a == 'Lavash':
        return lavash_qism_ru(call)
    elif a == 'Hotdog':
        return hotdogqismi_ru(call)
    elif a == 'Ichimliklar':
        return ichimliklar_special_ru(call, 2, need)
    elif a == 'Frie':
        return fri_qism(call)
import requests
from telebot import TeleBot
from decouple import config
import pprintpp
from telebot.types import ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from parser_auto import main,clear_code,get_page_data
import csv
import pandas as pd
import urllib



#  E:\Disc_E\DMLab\week4\def_project
                 
   





    
# #=========================
bot = TeleBot(config('TOKEN'))

declorations = '📣обьявления'
filter = '🔍фильтр'
last_declorations ='📌последние обьявления'
all_declorations = '📌все обьявления'


markup_decl = ReplyKeyboardMarkup(resize_keyboard=True)
btn_decl = KeyboardButton(declorations)
btn_dec2 = KeyboardButton(filter)
markup_decl.add(btn_decl,btn_dec2)


markup_decl_vubor = ReplyKeyboardMarkup(resize_keyboard=True)
btn_last_decl = KeyboardButton(last_declorations)
btn_all_decl = KeyboardButton(all_declorations)
markup_decl_vubor.add(btn_last_decl,btn_all_decl)

@bot.message_handler(commands=['start'])
def commands_start(message):


    text = f'Welcome {message.from_user.username}'
    bot.reply_to(message,text,reply_markup=markup_decl) 


@bot.message_handler(func=lambda message: message.text == filter)
def commands_filter(message):

    def price_int(lst):
        price = []

        for i in lst[0:5]:
            res = i[1][0:-4]
            price.append(res)
        return price
    
    for i in price_int(clear_code()):
        i.replace(' ','')
        bot.send_message(message.chat.id,i)
    


@bot.message_handler(func=lambda message: message.text == declorations)
def commands_declarations(message):
    text = f'Ввыберите какое обьявление хотите выбрать'
    bot.reply_to(message,text,reply_markup=markup_decl_vubor) 








@bot.message_handler(func=lambda message: message.text == last_declorations)
def commands_declarations(message):

        
    def last_decl(lst):  
        for i,v in enumerate(lst[0:5]):
        
            with open(f"img/img{i}.jpg", "rb") as image:
                bot.send_photo(message.chat.id, photo=image) 

            url_auto = f"<a href= '{v[2][7:]}'> {v[0]} </a>"
            text = f'Название авто: {url_auto} ,Цена: {v[1]}'
            bot.send_message(message.chat.id,text,reply_markup=markup_decl,parse_mode='html')



             
    last_decl(clear_code())


    

@bot.message_handler(func=lambda message: message.text == all_declorations)
def commands_declarations(message):

    def all_decl(lst):   
       for i,v in enumerate(lst):
            
            with open(f"img/img{i}.jpg", "rb") as image:
                bot.send_photo(message.chat.id, photo=image)   

            url_auto = f"<a href= '{v[2][7:]}'> {v[0]} </a>"
            text = f'Название авто: {url_auto} ,Цена: {v[1]}'
            bot.send_message(message.chat.id,text,reply_markup=markup_decl,parse_mode='html')



    all_decl(clear_code())

bot.polling()



if __name__ =='__main__':
    main()
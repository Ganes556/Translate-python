import requests
import re
from bs4 import BeautifulSoup
sessions = []
def google_translate():
    global sessions
    if sessions:
        translate = raw_input("Translate text >> ").replace(" ","+")
        get = requests.get("https://translate.google.com/m?hl=id&sl="+sessions[0]+"&tl="+sessions[1]+"&ie=UTF-8&prev=_m&q=" + translate )
        sessions_translate = BeautifulSoup(get.content,"lxml")
        div_sessions = sessions_translate.find_all("div")
        out_translate(div_sessions)
        google_translate()
    dari = raw_input("\ndari >> ").lower()
    ke = raw_input("ke >> ").lower()
    sessions = dari,ke
    translate = raw_input("Translate text >> ").replace(" ","+")
    get_dict = requests.get("https://translate.google.com/m?hl=id&sl=en&tl=id&ie=UTF-8&prev=_m&q=where&mui=sl")
    content_dict = BeautifulSoup(get_dict.content,"lxml")
    kode_bhs = {'telugu': 'te', 'finlandia': 'fi', 'yoruba': 'yo', 'slovenia': 'sl', 'bengali': 'bn', 'makedonia': 'mk', 'belarussia': 'be', 'chichewa': 'ny', 'sesotho': 'st', 'tamil': 'ta', 'yiddi': 'yi', 'magyar': 'hu', 'amhara': 'am', 'tagalog': 'tl', 'malayalam': 'ml', 'melayu': 'ms', 'albania': 'sq', 'samoa': 'sm', 'azerbaijan': 'az', 'rusia': 'ru', 'tajik': 'tg', 'urdu': 'ur', 'farsi': 'fa', 'kirghiz': 'ky', 'xhosa': 'xh', 'marathi': 'mr', 'polandia': 'pl', 'slovakia': 'sk', 'laos': 'lo', 'turki': 'tr', 'korea': 'ko', 'zulu': 'zu', 'spanyol': 'es', 'gaelik skotlandia': 'gd', 'china': 'zh-cn', 'armenia': 'hy', 'thai': 'th', 'ukraina': 'uk', 'uzbek': 'uz', 'punjabi': 'pa', 'indonesia': 'id', 'kreol haiti': 'ht', 'vietnam': 'vi', 'gaelig': 'ga', 'ibrani': 'iw', 'portugis': 'pt', 'latvia': 'lv', 'jepang': 'ja', 'jawa': 'jw', 'wales': 'cy', 'belanda': 'nl', 'swahili': 'sw', 'galisia': 'gl', 'kurdi': 'ku', 'prancis': 'fr', 'pashto': 'ps', 'malagasi': 'mg', 'gujarati': 'gu', 'frisia': 'fy', 'hindi': 'hi', 'hmong': 'hmn', 'sindhi': 'sd', 'khmer': 'km', 'maori': 'mi', 'igbo': 'ig', 'cek': 'cs', 'katala': 'ca', 'bulgaria': 'bg', 'shona': 'sn', 'cebuano': 'ceb', 'kazak': 'kk', 'yunani': 'el', 'denmark': 'da', 'mongol': 'mn', 'korsika': 'co', 'hausa': 'ha', 'swensk': 'sv', 'estonia': 'et', 'kannada': 'kn', 'afrikans': 'af', 'deteksi bahasa': 'auto', 'basque': 'eu', 'italia': 'it', 'sinhala': 'si', 'sunda': 'su', 'nepal': 'ne', 'luksemburg': 'lb', 'malta': 'mt', 'jerman': 'de', 'georgia': 'ka', 'somali': 'so', 'kroat': 'hr', 'inggris': 'en', 'arab': 'ar', 'klasik': 'en', 'bosnia': 'bs', 'hawaii': 'haw', 'latin': 'la', 'serb': 'sr', 'burma': 'my', 'norsk': 'no', 'rumania': 'ro', 'lituania': 'lt', 'esperanto': 'eo', 'islan': 'is'}
    
    get = requests.get("https://translate.google.com/m?hl=id&sl="+kode_bhs[dari]+"&tl="+kode_bhs[ke]+"&ie=UTF-8&prev=_m&q=" + translate )
    response_translate = BeautifulSoup(get.content,"lxml")
    return response_translate.find_all("div")
def out_translate(div):
    for i in div:
        dirs = i.get("dir")
        if dirs:
            print ">> " + i.get_text().encode("utf-8")
            Lagi = raw_input("[+]Lagi y/n >>").lower()
            if Lagi == "y":
                google_translate()
            elif Lagi =="n":
                print "THANKS FOR USE THIS CODE"
                exit()
            else:
                print "Pilih yang bener coks :)"
                exit()
div = google_translate()
out_translate(div)
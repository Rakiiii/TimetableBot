#основной код
import csv # на будущее
import telebot #телеграмовское апи
import Config  #файлик с константами
import urllib  # тырим файлы по урл
import xlrd,xlwt #апи маломягких для exl
from difflib import ndiff #на будущее


Bot = telebot.TeleBot(Config.Token) #содаем объект бот
OldTimetable = xlrd.open_workbook(' ' , formatting_info=True) #грузим старое расписание
NewTimetable = xlrd.open_workbook( ' ' , formatting_info=True) #тырим новое расписание

@Bot.messege_handler(content_types=['commands'])  #получаем команду и предлагаем выбрать номер группы
def get_commands(message):
    if message.command == "/список групп":
        Bot.send_message(message.chat.id , "напиши номер группым из доступных")
        i = 0
        for i in range(Config.Groups):
            Bot.send_message(message.chat.id, Config.GroupsNumber[i] )



@Bot.message_handler(content_types=['text'])  #получем номер группы и определяем его номер в нашем массиве
def get_text(message):
    i = 0
    for i in range(Config.Groups):
        if message.text == Config.GroupsNumber[i]:
            if differens(OldTimetable , NewTimetable) == True:  #проверяем расписание
                OldTimetable = NewTimetable
            timetable[i]


def timetable(OldTimetable , Number):                                #должно доставать из базы данных и отсылать расписание

    Bot.send_message(message.chat.id ,   )





#def XlsToCsv(file_xls): можно будет сделать,но пока просто воозьмем побольше смазки
#  должно превращать xls в csv для уменьшения неъобходимого объема смазки





def differens(OldTimetable ,  NewTimetable):               #сравниваем старое расписание с новым
    OldSheet = OldTimetable.sheet_by_index(0)
    NewSheet = NewTimetable.sheet_by_index(0)
    OldVals = [OldSheet.row_values(rownum) for rownum in range(OldSheet.nrows)]
    NewVals = [NewSheet.row_values(rownum) for rownum in range(NewSheet.nrows)]
    if OldVals != NewVals:
        return True







#основной код
import csv # на будущее
import telebot #телеграмовское апи
import Config  #файлик с константами
import urllib  # тырим файлы по урл
import xlrd,xlwt #апи маломягких для exl
from urllib.request import urlopen
from difflib import ndiff #на будущее


Bot = telebot.TeleBot(Config.Token) #содаем объект бот
#OldTimetable = xlrd.open_workbook(' ' , formatting_info=True) #грузим старое расписание
#NewTimetable = xlrd.open_workbook( ' ' , formatting_info=True) #тырим новое расписание




def timetable(Timetable , Number):                                #должно доставать из базы данных и отсылать расписание
     Bot.send_message(message.chat.id , 'вроде что-то делает'   )





#def XlsToCsv(file_xls): можно будет сделать,но пока просто воозьмем побольше смазки
#  должно превращать xls в csv для уменьшения неъобходимого объема смазки





def differens(OldTimetable ,  NewTimetable):               #сравниваем старое расписание с новым
    OldSheet = OldTimetable.sheet_by_index(0)
    NewSheet = NewTimetable.sheet_by_index(0)
    OldVals = [OldSheet.row_values(rownum) for rownum in range(OldSheet.nrows)]
    NewVals = [NewSheet.row_values(rownum) for rownum in range(NewSheet.nrows)]
    if OldVals != NewVals:
        return True






def changeURL(Url , Number ):
    Number += 1
    Url = Url + str(Number) + '.xls'
    return Url


@Bot.message_handler(commands = ['groupslist'])  #получаем команду и предлагаем выбрать номер группы
def get_commands(message):
        Bot.send_message(message.chat.id , "напиши номер группым из доступных")
        i = 0
        StrGroups = ' '
        for i in range(Config.Groups):
          StrGroups = StrGroups + Config.GroupsNumber[] + ' , '
        Bot.send_message(message.chat.id, StrGroups )



@Bot.message_handler(content_types=['text'])  #получем номер группы и определяем его номер в нашем массиве
def get_text(message):
        if message.text in Config.GroupsNumber:
            OldTimetableUrl = urlopen(changeURL(Config.Unn , Config.TimetableNumber - 1))#делаем урл для старого расписания
            NewTimetableUrl = urlopen(changeURL(Config.Unn , Config.TimetableNumber))#делаем урл для нового расписания
            OldTimetable = xlrd.open_workbook(OldTimetableUrl , formatting_info=True)#берем старое расписание
            NewTimetable = xlrd.open_workbook(NewTimetableUrl , formatting_info=True)#берем новое расписание
            if differens(OldTimetable , NewTimetable) == True:  #проверяем расписание
                OldTimetable = NewTimetable #если расписания отличаются ,то берем новое
            Bot.send_message(message.chat.id , 'vrode chto-to delaet')



Bot.polling(none_stop=True , interval = 0) #бот работает постоянно
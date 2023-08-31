from tkinter import END
from unicodedata import name
from fpdf import FPDF
from datetime import datetime
from pymsgbox import *
import time, customtkinter, fitz, os

currentDay = str(datetime.now().day)
currentMonth = int(datetime.now().month)
currentYear = str(datetime.now().year)

months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
currentMonth = str(months[currentMonth-1])

orderType = -1
workPosition = ''
workRank = ''
nameSurname = ''
orderNumber = ''
orderReason = ''
orderFreetext = ''
punishmentReason = ''
oldNickname = ''
nickname = ''
punishmentPreds = ''
punishmentVygs = ''
ePosition = ''
rank = ''
uvalReason = ''
blacklist = ''
blacklistDuration1 = ''
blacklistDuration2 = ''

def PDFgenerator():
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=10)
    
    pdf.add_font('Times New Roman', '', r'C:\Windows\Fonts\times.ttf', uni=True)
    pdf.add_font('Times New Roman', 'B', r'C:\Windows\Fonts\timesbd.ttf', uni=True)
    pdf.add_font('Times New Roman', 'I', r'C:\Windows\Fonts\timesi.ttf', uni=True)
    pdf.add_font('Times New Roman', 'BI', r'C:\Windows\Fonts\timesbi.ttf', uni=True)
    pdf.set_font('Times New Roman', '', 14)

    pdf.image('logo.png', 'C', 10, 30)
    pdf.cell(0, 35, '', ln=True)
    pdf.cell(0, 7, 'ГЛАВНОЕ УПРАВЛЕНИЕ ПО ОБЕСПЕЧЕНИЮ', ln=True, align='C')
    pdf.cell(0, 7, 'БЕЗОПАСНОСТИ ДОРОЖНОГО ДВИЖЕНИЯ', ln=True, align='C')
    pdf.cell(0, 7, 'МИНИСТЕРСТВА ВНУТРЕННИХ ДЕЛ', ln=True, align='C')
    pdf.cell(0, 7, 'РЕСПУБЛИКИ ПРОВИНЦИЯ', ln=True, align='C')
    pdf.set_font('Times New Roman', 'B', 16)
    pdf.cell(0, 14, 'П Р И К А З', ln=True, align='C')
    pdf.set_font('Times New Roman', 'U', 14)
    pdf.cell(0, 14, '«'+ currentDay +'»  '+ currentMonth +'  '+ currentYear +' г.', ln=True)
    pdf.set_font('Times New Roman', '', 14)
    pdf.cell(0, 7, 'г. Мирный', ln=True, align='C')
    pdf.set_font('Times New Roman', 'U', 14)
    pdf.cell(0, 14, '№ '+ orderNumber, ln=True, align='R')

    pdf.set_font('Times New Roman', 'BI', 12)

    global orderType

    if orderType == 0:
        orderReason = enteredOrderReason.get()
        pdf.cell(0, 6, '«'+orderReason+'»', ln=True, align='L')
        pdf.set_font('Times New Roman', 'I', 12)
        pdf.cell(0, 6, 'В соответствии с действующими правилами и уставной документацией.', ln=True, align='L')
    if orderType == 1 or orderType == 2:
        pdf.cell(0, 6, '«О выдаче дисциплинарного взыскания»', ln=True, align='L')
        pdf.set_font('Times New Roman', 'I', 12)
        punishmentReason = enteredPunishmentReason.get()
        pdf.cell(0, 6, 'В соответствии с пунктом/пунктами ' + punishmentReason + '.', ln=True, align='L')
    if orderType == 3:
        pdf.cell(0, 6, '«О написании объяснительной»', ln=True, align='L')
        pdf.set_font('Times New Roman', 'I', 12)
        punishmentReason = enteredPunishmentReason.get()
        pdf.cell(0, 6, 'В соответствии с пунктом/пунктами ' + punishmentReason + '.', ln=True, align='L')
    if orderType == 4:
        pdf.cell(0, 6, '«Об увольнении из органов внутренних дел»', ln=True, align='L')
        pdf.set_font('Times New Roman', 'I', 12)
        pdf.cell(0, 6, 'В соответствии с действующими правилами и уставной документацией.', ln=True, align='L')
    if orderType == 5:
        pdf.cell(0, 6, '«О cмене паспортных данных»', ln=True, align='L')
        pdf.set_font('Times New Roman', 'I', 12)
        pdf.cell(0, 6, 'В соответствии с действующими правилами и уставной документацией.', ln=True, align='L')

    pdf.set_font('Times New Roman', 'B', 16)
    pdf.cell(0, 21, 'П Р И К А З Ы В А Ю:', ln=True, align='C')
    pdf.set_font('Times New Roman', '', 14)

    if orderType == 0:
        orderFreetext = enteredOrderFreetext.get(0.1, customtkinter.END)
        pdf.multi_cell(0, 7, orderFreetext, ln=True, align='L')
    if orderType == 1:
        nickname = enteredNickname.get()
        pdf.multi_cell(0, 7, '      '+'1. Выдать дисциплинарное взыскание в виде предупреждения сотруднику ' + nickname + '.', ln=True, align='L')
        punishmentPreds = enteredPreds.get()
        punishmentVygs = enteredVygs.get()
        pdf.multi_cell(0, 7, '      '+'1.2. Состояние взысканий на данный момент ['+punishmentPreds+'/3]['+punishmentVygs+'/3].', ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'2. Контроль за исполнением настоящего приказа оставляю за собой.', ln=True, align='L')
    if orderType == 2:
        nickname = enteredNickname.get()
        pdf.multi_cell(0, 7, '        '+'1. Выдать дисциплинарное взыскание в виде выговора сотруднику ' + nickname + '.', ln=True, align='L')
        punishmentPreds = enteredPreds.get()
        punishmentVygs = enteredVygs.get()
        pdf.multi_cell(0, 7, '      '+'1.2. Состояние взысканий на данный момент ['+punishmentPreds+'/3]['+punishmentVygs+'/3].', ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'2. Контроль за исполнением настоящего приказа оставляю за собой.', ln=True, align='L')
    if orderType == 3:
        nickname = enteredNickname.get()
        pdf.multi_cell(0, 7, '      '+'1. Написать объяснительную сотруднику: ' + nickname + ' на имя Марцинкевича Ричарда Юрьевича в Кабинет Начальника ГУОБДД.', ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'1.2. Приказ должен быть исполнен в течение 24 часов с момента его издания, за его неисполнение полагается дисциплинарное взыскание.', ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'2. Контроль за исполнением настоящего приказа оставляю за собой.', ln=True, align='L')
    if orderType == 4:
        nickname = enteredNickname.get()
        ePosition = enteredEPosition.get()
        rank = enteredERank.get()
        uvalReason = enteredUvalReason.get()
        pdf.multi_cell(0, 7, '      '+'1. Уволить из органов внутренних дел, '+ePosition+', '+rank+' инспекции, '+nickname+' '+uvalReason+'.', ln=True, align='L')
        blacklistList = ['Без ОЧС', 'ОЧС-1', 'ОЧС-2', 'ОЧС-1 и 2']
        blacklist = blacklistSelection.get()
        blacklist = blacklistList.index(blacklist)
        if blacklist == 1:
            blacklistDuration1 = enteredBlack1.get()
            pdf.multi_cell(0, 7, '      '+'1.1. Сотрудник уволен с занесением в общий черный список государственных организаций первой степени сроком на '+blacklistDuration1+' дней.', ln=True, align='L')
        if blacklist == 2:
            blacklistDuration2 = enteredBlack2.get()
            pdf.multi_cell(0, 7, '      '+'1.1. Сотрудник уволен с занесением в общий черный список государственных организаций второй степени сроком на '+blacklistDuration2+' дней.', ln=True, align='L')
        if blacklist == 3:
            blacklistDuration1 = enteredBlack1.get()
            blacklistDuration2 = enteredBlack2.get()
            pdf.multi_cell(0, 7, '      '+'1.1. Сотрудник уволен с занесением в общий черный список государственных организаций первой и второй степени сроком на '+blacklistDuration1+' и '+blacklistDuration2+' дней соответственно.', ln=True, align='L')
        if blacklist == 0:
            pdf.multi_cell(0, 7, '      '+'1.1. Сотрудник уволен без занесения в общий черный список государственных организаций.', ln=True, align='L')
        punishmentPreds = enteredPreds.get()
        punishmentVygs = enteredVygs.get()
        pdf.multi_cell(0, 7, '      '+'1.2. Состояние выговоров на момент увольнения: ['+punishmentPreds+'/3]['+punishmentVygs+'/3].', ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'2. Контроль за исполнением настоящего приказа оставляю за собой.', ln=True, align='L')
    if orderType == 5:
        oldNickname = enteredOldNickname.get()
        nickname = enteredNickname.get()
        pdf.multi_cell(0, 7, '      '+'1. Сменить сотруднику '+oldNickname+' имя на '+nickname+'.', ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'2. Контроль за исполнением настоящего приказа оставляю за собой.', ln=True, align='L')

    pdf.set_font('Times New Roman', 'I', 12)
    pdf.cell(0, 24, '', ln=True, align='R')
    pdf.cell(0, 6, 'Подписал и оформил:', align='L')
    pdf.set_font('Times New Roman', 'BI', 12)
    pdf.cell(0, 6, workPosition + ', ' + workRank, ln=True, align='R')
    pdf.cell(0, 6, 'инспекции Республики Провинция ' + nameSurname, ln=True, align='R')
    pdf.cell(0, 12, '', ln=True, align='R')
    try:
        pdf.cell(0, 0, align='R', link=pdf.image('signature.png', x=150, h=25))
    except:
        pass

    pdf.output('output.pdf')

    file_path = "output.pdf"
    doc = fitz.open(file_path)
    for i, page in enumerate(doc):
        pix = page.get_pixmap()
        pix.save(f"page_{i+1}.png")

    msg = alert(text='Приказ сохранён как "output.pdf" и "page_1.png".', title="Операция выполнена", button='OK')
    if msg == "OK":
        root.destroy()

def selectedOrderType(choice):
    global orderType
    int(orderType)
    listOfOrders = ['Выберите тип приказа', 'Кастом', 'Выдача предупреждения', 'Выдача выговора', 'Написание объяснительной', 'Увольнение сотрудника', 'Смена паспортных данных', 'Принятие человека', 'Повышение', 'Перевод в другой отдел', 'Отработка взыскания', 'Выпуск из ЦПП', 'Построение', 'Премирование сотрудника']
    orderType = listOfOrders.index(choice) - 1

def continuePressed():
    if orderType >= 0:
        global workPosition, workRank, nameSurname, orderNumber, orderReason, orderFreetext, enteredOrderReason, enteredOrderFreetext, punishmentReason, enteredPunishmentReason, nickname, oldNickname, enteredNickname, enteredOldNickname, enteredPreds, enteredVygs, punishmentPreds, punishmentVygs, enteredERank, enteredEPosition, enteredUvalReason, blacklistSelection, enteredBlack1, enteredBlack2
        workPosition = enteredPosition.get()
        workRank = enteredRank.get()
        nameSurname = enteredNameSurname.get()
        orderNumber = selectedNumber.get()
        enteredPosition.pack_forget()
        enteredRank.pack_forget()
        enteredNameSurname.pack_forget()
        selectedNumber.pack_forget()
        orderTypeSelection.pack_forget()
        continueButton.pack_forget()
        rememberMeCheckbox.pack_forget()
        usePreviousDataCheckbox.pack_forget()
    else:
        return
    if orderType == 0:
        root.geometry('500x425')
        enteredOrderReason = customtkinter.CTkEntry(master=frame, placeholder_text='О чём приказ?')
        enteredOrderReason.pack(pady=12, padx=10)
        textboxLabel = customtkinter.CTkLabel(master=frame, text='Введите текст приказа ниже:', font=('Roboto', 18))
        textboxLabel.pack(pady=12, padx=10)
        enteredOrderFreetext = customtkinter.CTkTextbox(master=frame, width=325, height=125)
        enteredOrderFreetext.pack(pady=12, padx=10)
    if orderType == 1 or orderType == 2:
        root.geometry('500x375')
        enteredPunishmentReason = customtkinter.CTkEntry(master=frame, placeholder_text='Нарушенные пункты')
        enteredPunishmentReason.pack(pady=12, padx=10)
        enteredNickname = customtkinter.CTkEntry(master=frame, placeholder_text='Ник нарушителя')
        enteredNickname.pack(pady=12, padx=10)
        enteredPreds = customtkinter.CTkEntry(master=frame, placeholder_text='Кол-во предов (0-3)')
        enteredPreds.pack(pady=12, padx=10)
        enteredVygs = customtkinter.CTkEntry(master=frame, placeholder_text='Кол-во выгов (0-3)')
        enteredVygs.pack(pady=12, padx=10)
    if orderType == 3:
        root.geometry('500x275')
        enteredPunishmentReason = customtkinter.CTkEntry(master=frame, placeholder_text='Нарушенные пункты')
        enteredPunishmentReason.pack(pady=12, padx=10)
        enteredNickname = customtkinter.CTkEntry(master=frame, placeholder_text='Ник нарушителя')
        enteredNickname.pack(pady=12, padx=10)
    if orderType == 4:
        root.geometry('500x725')
        enteredNickname = customtkinter.CTkEntry(master=frame, placeholder_text='Ник сотрудника')
        enteredNickname.pack(pady=12, padx=10)
        attentionLabel = customtkinter.CTkLabel(master=frame, text='Должность и звание пишутся в род.падеже!', font=('Roboto', 12))
        attentionLabel.pack(pady=12, padx=10)
        enteredEPosition = customtkinter.CTkEntry(master=frame, placeholder_text='Должность сотрудника')
        enteredEPosition.pack(pady=12, padx=10)
        enteredERank = customtkinter.CTkEntry(master=frame, placeholder_text='Звание сотрудника')
        enteredERank.pack(pady=12, padx=10)
        attentionLabel2 = customtkinter.CTkLabel(master=frame, text='Примеры причины увольнения: "по факту нарушения 6.4 ОПСГО", "ПСЖ"...', font=('Roboto', 10))
        attentionLabel2.pack(pady=12, padx=10)
        enteredUvalReason = customtkinter.CTkEntry(master=frame, placeholder_text='Причина увольнения')
        enteredUvalReason.pack(pady=12, padx=10)
        blacklistSelection = customtkinter.CTkOptionMenu(master=frame, values=['Без ОЧС', 'ОЧС-1', 'ОЧС-2', 'ОЧС-1 и 2'])
        blacklistSelection.pack(pady=12, padx=10)
        enteredBlack1 = customtkinter.CTkEntry(master=frame, placeholder_text='Срок ОЧС-1 в днях')
        enteredBlack1.pack(pady=12, padx=10)
        enteredBlack2 = customtkinter.CTkEntry(master=frame, placeholder_text='Срок ОЧС-2 в днях')
        enteredBlack2.pack(pady=12, padx=10)
        enteredPreds = customtkinter.CTkEntry(master=frame, placeholder_text='Кол-во предов (0-3)')
        enteredPreds.pack(pady=12, padx=10)
        enteredVygs = customtkinter.CTkEntry(master=frame, placeholder_text='Кол-во выгов (0-3)')
        enteredVygs.pack(pady=12, padx=10)
    if orderType == 5:
        root.geometry('500x275')
        enteredOldNickname = customtkinter.CTkEntry(master=frame, placeholder_text='Старый ник сотрудника')
        enteredOldNickname.pack(pady=12, padx=10)
        enteredNickname = customtkinter.CTkEntry(master=frame, placeholder_text='Новый ник сотрудника')
        enteredNickname.pack(pady=12, padx=10)
    generateButton = customtkinter.CTkButton(master=frame, text='Сгенерировать', command=PDFgenerator)
    generateButton.pack(pady=12, padx=10)

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.geometry('500x525')

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand='true')

label = customtkinter.CTkLabel(master=frame, text='Генератор приказов ГУОБДД', font=('Roboto', 24))
label.pack(pady=12, padx=10)

enteredPosition = customtkinter.CTkEntry(master=frame, placeholder_text='Ваша должность')
enteredPosition.pack(pady=12, padx=10)

enteredRank = customtkinter.CTkEntry(master=frame, placeholder_text='Ваше звание')
enteredRank.pack(pady=12, padx=10)

enteredNameSurname = customtkinter.CTkEntry(master=frame, placeholder_text='Фамилия инициалы')
enteredNameSurname.pack(pady=12, padx=10)

selectedNumber = customtkinter.CTkEntry(master=frame, placeholder_text='Номер приказа')
selectedNumber.pack(pady=12, padx=10)

orderTypeSelection = customtkinter.CTkOptionMenu(master=frame, values=['Выберите тип приказа', 'Кастом', 'Выдача предупреждения', 'Выдача выговора', 'Написание объяснительной', 'Увольнение сотрудника', 'Смена паспортных данных', 'Принятие человека', 'Повышение', 'Перевод в другой отдел', 'Отработка взыскания', 'Выпуск из ЦПП', 'Построение', 'Премирование сотрудника'], command=selectedOrderType)
orderTypeSelection.pack(pady=12, padx=10)

rememberMeCheckbox = customtkinter.CTkCheckBox(master=frame, text='Запомнить должность, звание, фамилию, инициалы')
rememberMeCheckbox.pack(pady=12, padx=10)

usePreviousDataCheckbox = customtkinter.CTkCheckBox(master=frame, text='Использовать данные, введённые в прошлый раз')
usePreviousDataCheckbox.pack(pady=12, padx=10)

continueButton = customtkinter.CTkButton(master=frame, text='Продолжить', command=continuePressed)
continueButton.pack(pady=12, padx=10)

root.mainloop()

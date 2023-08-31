from tkinter import END, Toplevel
from unicodedata import name
from fpdf import FPDF
from datetime import datetime
from pymsgbox import *
from tkcalendar import *
import customtkinter, fitz

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
blacklist = ''

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
        pdf.cell(0, 6, '«'+ enteredOrderReason.get() +'»', ln=True, align='L')
        pdf.set_font('Times New Roman', 'I', 12)
        pdf.cell(0, 6, 'В соответствии с действующими правилами и уставной документацией.', ln=True, align='L')
    if orderType == 1 or orderType == 2:
        pdf.cell(0, 6, '«О выдаче дисциплинарного взыскания»', ln=True, align='L')
        pdf.set_font('Times New Roman', 'I', 12)
        pdf.cell(0, 6, 'В соответствии с пунктом/пунктами ' + enteredPunishmentReason.get() + '.', ln=True, align='L')
    if orderType == 3:
        pdf.cell(0, 6, '«О написании объяснительной»', ln=True, align='L')
        pdf.set_font('Times New Roman', 'I', 12)
        pdf.cell(0, 6, 'В соответствии с пунктом/пунктами ' + enteredPunishmentReason.get() + '.', ln=True, align='L')
    if orderType == 4:
        pdf.cell(0, 6, '«Об увольнении из органов внутренних дел»', ln=True, align='L')
        pdf.set_font('Times New Roman', 'I', 12)
        pdf.cell(0, 6, 'В соответствии с действующими правилами и уставной документацией.', ln=True, align='L')
    if orderType == 5:
        pdf.cell(0, 6, '«О cмене паспортных данных»', ln=True, align='L')
        pdf.set_font('Times New Roman', 'I', 12)
        pdf.cell(0, 6, 'В соответствии с действующими правилами и уставной документацией.', ln=True, align='L')
    if orderType == 6:
        pdf.cell(0, 6, '«О принятии человека в организацию по факту прохождения собеседования»', ln=True, align='L')
        pdf.set_font('Times New Roman', 'I', 12)
        pdf.cell(0, 6, 'В соответствии с действующими правилами и уставной документацией.', ln=True, align='L')
    if orderType == 7:
        pdf.cell(0, 6, '«О повышении сотрудника в звании»', ln=True, align='L')
        pdf.set_font('Times New Roman', 'I', 12)
        pdf.cell(0, 6, 'В соответствии с действующими правилами и уставной документацией.', ln=True, align='L')
    if orderType == 8:
        pdf.cell(0, 6, '«О переводе сотрудника в новый отдел»', ln=True, align='L')
        pdf.set_font('Times New Roman', 'I', 12)
        pdf.cell(0, 6, 'В соответствии с действующими правилами и уставной документацией.', ln=True, align='L')
    if orderType == 9:
        pdf.cell(0, 6, '«Об отработке дисциплинарного взыскания»', ln=True, align='L')
        pdf.set_font('Times New Roman', 'I', 12)
        pdf.cell(0, 6, 'В соответствии с действующими правилами и уставной документацией.', ln=True, align='L')
    if orderType == 10:
        pdf.cell(0, 6, '«О проведении построения для младшего состава»', ln=True, align='L')
        pdf.set_font('Times New Roman', 'I', 12)
        pdf.cell(0, 6, 'В соответствии с действующими правилами и уставной документацией.', ln=True, align='L')

    pdf.set_font('Times New Roman', 'B', 16)
    pdf.cell(0, 21, 'П Р И К А З Ы В А Ю:', ln=True, align='C')
    pdf.set_font('Times New Roman', '', 14)

    if orderType == 0:
        pdf.multi_cell(0, 7, enteredOrderFreetext.get(0.1, customtkinter.END), ln=True, align='L')
    if orderType == 1:
        pdf.multi_cell(0, 7, '      '+'1. Выдать дисциплинарное взыскание в виде предупреждения сотруднику ' + enteredNickname.get() + '.', ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'1.1. Состояние взысканий на данный момент ['+ enteredPreds.get() +'/3]['+ enteredVygs.get() +'/3].', ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'2. Контроль за исполнением настоящего приказа оставляю за собой.', ln=True, align='L')
    if orderType == 2:
        pdf.multi_cell(0, 7, '        '+'1. Выдать дисциплинарное взыскание в виде выговора сотруднику ' + enteredNickname.get() + '.', ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'1.1. Состояние взысканий на данный момент ['+ enteredPreds.get() +'/3]['+ enteredVygs.get() +'/3].', ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'2. Контроль за исполнением настоящего приказа оставляю за собой.', ln=True, align='L')
    if orderType == 3:
        pdf.multi_cell(0, 7, '      '+'1. Написать объяснительную сотруднику: ' + enteredNickname.get() + ' на имя Марцинкевича Ричарда Юрьевича в Кабинет Начальника ГУОБДД.', ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'1.1. Приказ должен быть исполнен в течение 24 часов с момента его издания, за его неисполнение полагается дисциплинарное взыскание.', ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'2. Контроль за исполнением настоящего приказа оставляю за собой.', ln=True, align='L')
    if orderType == 4:
        pdf.multi_cell(0, 7, '      '+'1. Уволить из органов внутренних дел, '+ enteredEPosition.get() +', '+ enteredERank.get() +' инспекции, '+ enteredNickname.get() +' '+ enteredUvalReason.get() +'.', ln=True, align='L')
        blacklistList = ['Без ОЧС', 'ОЧС-1', 'ОЧС-2', 'ОЧС-1 и 2']
        blacklist = blacklistList.index(blacklistSelection.get())
        if blacklist == 1:
            pdf.multi_cell(0, 7, '      '+'1.1. Сотрудник уволен с занесением в общий черный список государственных организаций первой степени сроком на '+ enteredBlack1.get() +' дней.', ln=True, align='L')
        if blacklist == 2:
            pdf.multi_cell(0, 7, '      '+'1.1. Сотрудник уволен с занесением в общий черный список государственных организаций второй степени сроком на '+ enteredBlack2.get() +' дней.', ln=True, align='L')
        if blacklist == 3:
            pdf.multi_cell(0, 7, '      '+'1.1. Сотрудник уволен с занесением в общий черный список государственных организаций первой и второй степени сроком на '+ enteredBlack1.get() +' и '+ enteredBlack2.get() +' дней соответственно.', ln=True, align='L')
        if blacklist == 0:
            pdf.multi_cell(0, 7, '      '+'1.1. Сотрудник уволен без занесения в общий черный список государственных организаций.', ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'1.2. Состояние выговоров на момент увольнения: ['+ enteredPreds.get() +'/3]['+ enteredVygs.get() +'/3].', ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'2. Контроль за исполнением настоящего приказа оставляю за собой.', ln=True, align='L')
    if orderType == 5:
        pdf.multi_cell(0, 7, '      '+'1. Сменить сотруднику '+ enteredOldNickname.get() +' имя на '+ enteredNickname.get() +'.', ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'2. Контроль за исполнением настоящего приказа оставляю за собой.', ln=True, align='L')
    if orderType == 6:
        pdf.multi_cell(0, 7, '      '+'1. Принять человека '+ enteredNickname.get() +' в организацию.', ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'1.1. Ваш отдел: '+ enteredDepartament.get(), ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'1.2. Ваша должность: '+ enteredEPosition.get(), ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'1.3. Ваше звание: '+ enteredERank.get() +' инспекции', ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'2. Контроль за исполнением настоящего приказа оставляю за собой.', ln=True, align='L')
    if orderType == 7:
        pdf.multi_cell(0, 7, '      '+'1. Повысить сотрудника '+ enteredNickname.get() +' в звании, в связи с отставленным отчетом на гос. портале.', ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'1.1. Ваше звание: '+ enteredERank.get() +' инспекции', ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'2. Контроль за исполнением настоящего приказа оставляю за собой.', ln=True, align='L')
    if orderType == 8:
        pdf.multi_cell(0, 7, '      '+'1. Перевести сотрудника '+ enteredNickname.get() +' из '+ enteredOldDepartament.get() +'.', ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'1.1. Ваш новый отдел: '+ enteredDepartament.get(), ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'1.2. Ваша новая должность: '+ enteredEPosition.get(), ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'2. Контроль за исполнением настоящего приказа оставляю за собой.', ln=True, align='L')
    if orderType == 9:
        pdf.multi_cell(0, 7, '      '+'1. Снять дисциплинарное взыскание в виде '+ enteredPunishmentType.get() +' сотруднику '+ enteredNickname.get() +'.', ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'1.1. Состояние взысканий на данный момент ['+ enteredPreds.get() +'/3]['+ enteredVygs.get() +'/3].', ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'2. Контроль за исполнением настоящего приказа оставляю за собой.', ln=True, align='L')
    if orderType == 10:
        if premia.get() == 1:
            pdf.multi_cell(0, 7, '      '+'1. Провести построение для младшего состава '+ enteredDate.get() +'. За явку на строй полагаются премии.', ln=True, align='L')
        else:
            pdf.multi_cell(0, 7, '      '+'1. Провести построение для младшего состава '+ enteredDate.get() +'.', ln=True, align='L')
        pdf.multi_cell(0, 7, '      '+'1.1. На данном построении '+ formationType.get() +'.', ln=True, align='L')
        if mandatory.get() == 1:
            pdf.multi_cell(0, 7, '      '+'1.2. Посещение построения сотрудниками Младшего состава обязательно. В случае невозможности явится на построение, требуется отписать в комментарии по форме: Ник и причина.', ln=True, align='L')
        else:
            pdf.multi_cell(0, 7, '      '+'1.2. Посещение построения сотрудниками Младшего состава необязательно, но крайне желательно.', ln=True, align='L')
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
    listOfOrders = ['Самостоятельное написание', 'Выдача предупреждения', 'Выдача выговора', 'Написание объяснительной', 'Увольнение сотрудника', 'Смена паспортных данных', 'Принятие человека', 'Повышение', 'Перевод в другой отдел', 'Отработка взыскания', 'Построение']
    orderType = listOfOrders.index(choice)

def continuePressed():
    if orderType >= 0:
        global workPosition, workRank, nameSurname, orderNumber, enteredOrderReason, enteredOrderFreetext, enteredPunishmentReason, enteredNickname, enteredOldNickname, enteredPreds, enteredVygs, enteredERank, enteredEPosition, enteredUvalReason, blacklistSelection, enteredBlack1, enteredBlack2, enteredDepartament, enteredOldDepartament, enteredPunishmentType, enteredDate, premia, formationType, mandatory
        if rememberMeCheckbox.get() == 1:
            with open('userData.txt', 'w', encoding='utf-8') as file:
                file.seek(0)
                file.write(enteredPosition.get()+'\n'+enteredRank.get()+'\n'+enteredNameSurname.get())
                print('Записано!')
        
        if usePreviousDataCheckbox.get() == 1:
            with open('userData.txt', 'r', encoding='utf-8') as file:
                workPosition = file.readline()
                workRank = file.readline()
                nameSurname = file.readline()
        else:
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
        positionLabel.pack_forget()
        rankLabel.pack_forget()
        typeSelectionLabel.pack_forget()
    else:
        return
    if orderType == 0:
        def sixSpaces():
            enteredOrderFreetext.insert(text='      ')
        root.geometry('500x475')
        enteredOrderReason = customtkinter.CTkEntry(master=frame, placeholder_text='О чём приказ?')
        enteredOrderReason.pack(pady=12, padx=10)
        textboxLabel = customtkinter.CTkLabel(master=frame, text='Введите текст приказа ниже:', font=('Roboto', 18))
        textboxLabel.pack(pady=12, padx=10)
        enteredOrderFreetext = customtkinter.CTkTextbox(master=frame, width=325, height=125)
        enteredOrderFreetext.pack(pady=12, padx=10)
        enteredOrderFreetext.bind("Tab", command=sixSpaces)
        absatzLabel = customtkinter.CTkLabel(master=frame, text='Tab - отступ первой строки абзаца', font=('Roboto', 12))
        absatzLabel.pack(pady=12, padx=10)
    if orderType == 1 or orderType == 2:
        root.geometry('500x475')
        enteredPunishmentReason = customtkinter.CTkEntry(master=frame, placeholder_text='Нарушенные пункты')
        enteredPunishmentReason.pack(pady=12, padx=10)
        enteredNickname = customtkinter.CTkEntry(master=frame, placeholder_text='Ник нарушителя')
        enteredNickname.pack(pady=12, padx=10)
        predsLabel = customtkinter.CTkLabel(master=frame, text='Кол-во предупреждений у сотрудника:', font=('Roboto', 12))
        predsLabel.pack(pady=12, padx=10)
        enteredPreds = customtkinter.CTkOptionMenu(master=frame, values=['0', '1', '2', '3'])
        enteredPreds.pack(pady=12, padx=10)
        vygsLabel = customtkinter.CTkLabel(master=frame, text='Кол-во выговоров у сотрудника:', font=('Roboto', 12))
        vygsLabel.pack(pady=12, padx=10)
        enteredVygs = customtkinter.CTkOptionMenu(master=frame, values=['0', '1', '2', '3'])
        enteredVygs.pack(pady=12, padx=10)
    if orderType == 3:
        root.geometry('500x275')
        enteredPunishmentReason = customtkinter.CTkEntry(master=frame, placeholder_text='Нарушенные пункты')
        enteredPunishmentReason.pack(pady=12, padx=10)
        enteredNickname = customtkinter.CTkEntry(master=frame, placeholder_text='Ник нарушителя')
        enteredNickname.pack(pady=12, padx=10)
    if orderType == 4:
        root.geometry('500x875')
        enteredNickname = customtkinter.CTkEntry(master=frame, placeholder_text='Ник сотрудника')
        enteredNickname.pack(pady=12, padx=10)
        epositionLabel = customtkinter.CTkLabel(master=frame, text='Должность сотрудника:', font=('Roboto', 12))
        epositionLabel.pack(pady=12, padx=10)
        enteredEPosition = customtkinter.CTkOptionMenu(master=frame, values=['Курсанта ЦПП', 'Инспектора 2-ой ОР ДПС', 'Инспектора 1-ой ОСР ДПС', 'Инструктора ЦПП', 'Начальника ЦПП', 'Заместителя Командира 2-ой ОР ДПС', 'Командира 2-ой ОР ДПС', 'Заместителя Командира 1-ой ОСР ДПС', 'Командира 1-ой ОСР ДПС', 'Заместителя Начальника ГУОБДД'])
        enteredEPosition.pack(pady=12, padx=10)
        erankLabel = customtkinter.CTkLabel(master=frame, text='Звание сотрудника:', font=('Roboto', 12))
        erankLabel.pack(pady=12, padx=10)
        enteredERank = customtkinter.CTkOptionMenu(master=frame, values=['рядового', 'сержанта', 'старшину', 'прапорщика', 'лейтенанта', 'старшего лейтенанта', 'капитана', 'майора', 'подполковника', 'полковника'])
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
        predsLabel = customtkinter.CTkLabel(master=frame, text='Кол-во предупреждений у сотрудника:', font=('Roboto', 12))
        predsLabel.pack(pady=12, padx=10)
        enteredPreds = customtkinter.CTkOptionMenu(master=frame, values=['0', '1', '2', '3'])
        enteredPreds.pack(pady=12, padx=10)
        vygsLabel = customtkinter.CTkLabel(master=frame, text='Кол-во выговоров у сотрудника:', font=('Roboto', 12))
        vygsLabel.pack(pady=12, padx=10)
        enteredVygs = customtkinter.CTkOptionMenu(master=frame, values=['0', '1', '2', '3'])
        enteredVygs.pack(pady=12, padx=10)
    if orderType == 5:
        root.geometry('500x275')
        enteredOldNickname = customtkinter.CTkEntry(master=frame, placeholder_text='Старый ник сотрудника')
        enteredOldNickname.pack(pady=12, padx=10)
        enteredNickname = customtkinter.CTkEntry(master=frame, placeholder_text='Новый ник сотрудника')
        enteredNickname.pack(pady=12, padx=10)
    if orderType == 6:
        root.geometry('500x525')
        enteredNickname = customtkinter.CTkEntry(master=frame, placeholder_text='Ник сотрудника')
        enteredNickname.pack(pady=12, padx=10)
        departamentLabel = customtkinter.CTkLabel(master=frame, text='Отдел сотрудника:', font=('Roboto', 12))
        departamentLabel.pack(pady=12, padx=10)
        enteredDepartament = customtkinter.CTkOptionMenu(master=frame, values=['ЦПП', '2-я ОР ДПС', '1-я ОСР ДПС', 'СС', 'РС'])
        enteredDepartament.pack(pady=12, padx=10)
        epositionLabel = customtkinter.CTkLabel(master=frame, text='Должность сотрудника:', font=('Roboto', 12))
        epositionLabel.pack(pady=12, padx=10)
        enteredEPosition = customtkinter.CTkOptionMenu(master=frame, values=['Курсант ЦПП', 'Инспектор 2-ой ОР ДПС', 'Инспектор 1-ой ОСР ДПС', 'Инструктор ЦПП', 'Начальник ЦПП', 'Заместитель Командира 2-ой ОР ДПС', 'Командир 2-ой ОР ДПС', 'Заместитель Командира 1-ой ОСР ДПС', 'Командир 1-ой ОСР ДПС', 'Заместитель Начальника ГУОБДД'])
        enteredEPosition.pack(pady=12, padx=10)
        erankLabel = customtkinter.CTkLabel(master=frame, text='Звание сотрудника:', font=('Roboto', 12))
        erankLabel.pack(pady=12, padx=10)
        enteredERank = customtkinter.CTkOptionMenu(master=frame, values=['рядовой', 'сержант', 'старшина', 'прапорщик', 'лейтенант', 'старший лейтенант', 'капитан', 'майор', 'подполковник', 'полковник'])
        enteredERank.pack(pady=12, padx=10)
    if orderType == 7:
        root.geometry('500x325')
        enteredNickname = customtkinter.CTkEntry(master=frame, placeholder_text='Ник сотрудника')
        enteredNickname.pack(pady=12, padx=10)
        erankLabel = customtkinter.CTkLabel(master=frame, text='Новое звание сотрудника:', font=('Roboto', 12))
        erankLabel.pack(pady=12, padx=10)
        enteredERank = customtkinter.CTkOptionMenu(master=frame, values=['сержант', 'старшина', 'прапорщик', 'лейтенант', 'старший лейтенант', 'капитан', 'майор', 'подполковник', 'полковник'])
        enteredERank.pack(pady=12, padx=10)
    if orderType == 8:
        root.geometry('500x525')
        enteredNickname = customtkinter.CTkEntry(master=frame, placeholder_text='Ник сотрудника')
        enteredNickname.pack(pady=12, padx=10)
        oldDepartamentLabel = customtkinter.CTkLabel(master=frame, text='Старый отдел сотрудника:', font=('Roboto', 12))
        oldDepartamentLabel.pack(pady=12, padx=10)
        enteredOldDepartament = customtkinter.CTkOptionMenu(master=frame, values=['ЦПП', '2-я ОР ДПС', '1-я ОСР ДПС', 'СС', 'РС'])
        enteredOldDepartament.pack(pady=12, padx=10)
        departamentLabel = customtkinter.CTkLabel(master=frame, text='Новый отдел сотрудника:', font=('Roboto', 12))
        departamentLabel.pack(pady=12, padx=10)
        enteredDepartament = customtkinter.CTkOptionMenu(master=frame, values=['ЦПП', '2-я ОР ДПС', '1-я ОСР ДПС', 'СС', 'РС'])
        enteredDepartament.pack(pady=12, padx=10)
        epositionLabel = customtkinter.CTkLabel(master=frame, text='Новая должность сотрудника:', font=('Roboto', 12))
        epositionLabel.pack(pady=12, padx=10)
        enteredEPosition = customtkinter.CTkOptionMenu(master=frame, values=['Курсант ЦПП', 'Инспектор 2-ой ОР ДПС', 'Инспектор 1-ой ОСР ДПС', 'Инструктор ЦПП', 'Начальник ЦПП', 'Заместитель Командира 2-ой ОР ДПС', 'Командир 2-ой ОР ДПС', 'Заместитель Командира 1-ой ОСР ДПС', 'Командир 1-ой ОСР ДПС', 'Заместитель Начальника ГУОБДД'])
        enteredEPosition.pack(pady=12, padx=10)
    if orderType == 9:
        root.geometry('500x525')
        enteredNickname = customtkinter.CTkEntry(master=frame, placeholder_text='Ник сотрудника')
        enteredNickname.pack(pady=12, padx=10)
        punishmentTypeLabel = customtkinter.CTkLabel(master=frame, text='Снять взыскание в виде:', font=('Roboto', 12))
        punishmentTypeLabel.pack(pady=12, padx=10)
        enteredPunishmentType = customtkinter.CTkOptionMenu(master=frame, values=['предупреждения', 'выговора'])
        enteredPunishmentType.pack(pady=12, padx=10)
        predsLabel = customtkinter.CTkLabel(master=frame, text='Кол-во предупреждений у сотрудника:', font=('Roboto', 12))
        predsLabel.pack(pady=12, padx=10)
        enteredPreds = customtkinter.CTkOptionMenu(master=frame, values=['0', '1', '2', '3'])
        enteredPreds.pack(pady=12, padx=10)
        vygsLabel = customtkinter.CTkLabel(master=frame, text='Кол-во выговоров у сотрудника:', font=('Roboto', 12))
        vygsLabel.pack(pady=12, padx=10)
        enteredVygs = customtkinter.CTkOptionMenu(master=frame, values=['0', '1', '2', '3'])
        enteredVygs.pack(pady=12, padx=10)
    if orderType == 10:
        root.geometry('500x425')
        def pick_date(event):
            global cal, date_window, enteredHour, enteredMinute
            date_window = Toplevel(background='#212221')
            date_window.title('Дата и время')
            date_window.iconbitmap('icon.ico')
            date_window.grab_set()
            date_window.geometry('250x250')
            cal = Calendar(master=date_window, selectmode='day', date_pattern='dd.mm.y')
            cal.place(x=0, y=0)
            timeLabel = customtkinter.CTkLabel(master=date_window, width=50, text='Время:', font=('Roboto', 12))
            timeLabel.place(x=25, y=190)
            enteredHour = customtkinter.CTkComboBox(master=date_window, width=55, values=['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'])
            enteredHour.place(x=100, y=190)
            enteredMinute = customtkinter.CTkComboBox(master=date_window, width=55, values=['00', '30'])
            enteredMinute.place(x=175, y=190)
            submit_btn = customtkinter.CTkButton(master=date_window, width=150, text='OK', command=grab_date)
            submit_btn.place(x=50, y=220)
        def grab_date():
            enteredDate.insert(0, cal.get_date()+' '+enteredHour.get()+':'+enteredMinute.get())
            date_window.destroy()
        enteredDate = customtkinter.CTkEntry(master=frame, placeholder_text='Дата и время строя')
        enteredDate.pack(pady=12, padx=10)
        enteredDate.bind('<1>', pick_date)
        enteredDate.bind('<2>', pick_date)
        enteredDate.bind('<3>', pick_date)
        premia = customtkinter.CTkCheckBox(master=frame, text='Премии за явку на строй')
        premia.pack(pady=12, padx=10)
        formationTypeLabel = customtkinter.CTkLabel(master=frame, text='Что будет на построении:', font=('Roboto', 12))
        formationTypeLabel.pack(pady=12, padx=10)
        formationType = customtkinter.CTkOptionMenu(master=frame, values=['будут проведены познавательные лекции с тренировками, увлекательные мероприятия', 'будет проведён рейд', 'будет проведено ГМП', 'будет проведено ГРП'])
        formationType.pack(pady=12, padx=10)
        mandatory = customtkinter.CTkCheckBox(master=frame, text='Обязательная явка')
        mandatory.pack(pady=12, padx=10)
    generateButton = customtkinter.CTkButton(master=frame, text='Сгенерировать', command=PDFgenerator)
    generateButton.pack(pady=12, padx=10)

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.iconbitmap('icon.ico')
root.title('Генератор приказов ГУОБДД')
root.geometry('500x675')

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand='true')

label = customtkinter.CTkLabel(master=frame, text='Генератор приказов ГУОБДД', font=('Roboto', 24))
label.pack(pady=12, padx=10)

selectedNumber = customtkinter.CTkEntry(master=frame, placeholder_text='Номер приказа')
selectedNumber.pack(pady=12, padx=10)

enteredNameSurname = customtkinter.CTkEntry(master=frame, placeholder_text='Фамилия инициалы')
enteredNameSurname.pack(pady=12, padx=10)

positionLabel = customtkinter.CTkLabel(master=frame, text='Ваша должность:', font=('Roboto', 12))
positionLabel.pack(pady=12, padx=10)
enteredPosition = customtkinter.CTkOptionMenu(master=frame, values=['Инструктор ЦПП', 'Начальник ЦПП', 'Заместитель Командира 2-ой ОР ДПС', 'Командир 2-ой ОР ДПС', 'Заместитель Командира 1-ой ОСР ДПС', 'Командир 1-ой ОСР ДПС', 'Заместитель Начальника ГУОБДД', 'Начальник ГУОБДД'])
enteredPosition.pack(pady=12, padx=10)

rankLabel = customtkinter.CTkLabel(master=frame, text='Ваше звание:', font=('Roboto', 12))
rankLabel.pack(pady=12, padx=10)
enteredRank = customtkinter.CTkOptionMenu(master=frame, values=['майор', 'подполковник', 'полковник', 'генерал-лейтенант'])
enteredRank.pack(pady=12, padx=10)

typeSelectionLabel = customtkinter.CTkLabel(master=frame, text='Выберите шаблон приказа:', font=('Roboto', 12))
typeSelectionLabel.pack(pady=12, padx=10)
orderTypeSelection = customtkinter.CTkOptionMenu(master=frame, values=['Самостоятельное написание', 'Выдача предупреждения', 'Выдача выговора', 'Написание объяснительной', 'Увольнение сотрудника', 'Смена паспортных данных', 'Принятие человека', 'Повышение', 'Перевод в другой отдел', 'Отработка взыскания', 'Построение'], command=selectedOrderType)
orderTypeSelection.pack(pady=12, padx=10)

rememberMeCheckbox = customtkinter.CTkCheckBox(master=frame, text='Запомнить должность, звание, фамилию, инициалы')
rememberMeCheckbox.pack(pady=12, padx=10)

usePreviousDataCheckbox = customtkinter.CTkCheckBox(master=frame, text='Использовать данные, введённые в прошлый раз')
usePreviousDataCheckbox.pack(pady=12, padx=10)

continueButton = customtkinter.CTkButton(master=frame, text='Продолжить', command=continuePressed)
continueButton.pack(pady=12, padx=10)

root.mainloop()

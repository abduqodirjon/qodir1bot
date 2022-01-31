
from email import message
from turtle import update
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, ConversationHandler, MessageHandler,Filters
import base
import messages
import date
import datetime, time

API_TOKEN = '5269458930:AAFkc7XFJUoLCiz8kMM_docwSgAdOYJl7ME'

btn_register = "Ro'yxatdan o'tish"

btn_admin_teacher = "O'qituvchi qo'shish"
btn_admin_student = "O'quvchi qo'shish"
btn_admin_table = "Jadvalni ko'rish"
btn_eslatma = "Eslatma"
btn_parol = "Parol"
btn_teacher_davomat = "Davomat olish"

btn_teacher_group = "Guruh"
btn_teacher_student = "O'quvchi"

BTN_REGISTER = ReplyKeyboardMarkup(
		[
			[f"{btn_register}"],
		],resize_keyboard=True)

BTN_ADMIN = ReplyKeyboardMarkup(
		[
			[f"{btn_admin_teacher}"],
			[f"{btn_admin_student}"],
			[f"{btn_admin_table}"],
			[f"{btn_eslatma}"],
			[f"{btn_parol}"],
		],resize_keyboard=True)

BTN_TEACHER = ReplyKeyboardMarkup(
		[
			[f"{btn_teacher_group}"],
			[f"{btn_teacher_student}"],
			[f"{btn_teacher_davomat}"],
		],resize_keyboard=True)

BTN_PARENT = ReplyKeyboardMarkup(
		[
			# [f"Izoh yozish"],
			# [f"Xabar yozish"],
			[f"Ro'yxatdan o'tish"],
		],resize_keyboard=True)

REGISTER = 0
INFOR = 1
FILIAL = 2
TEACHER = 3
INFO_TEACHER = 4
TEACHER_BTN = 5
PARENT_BTN = 6
TEACHER_GROUP = 7
TEACHER_GROUP_CREATE = 8
TEACHER_GROUP_DELETE = 9
TEACHER_GROUP_INFO = 10
TEACHER_GROUP_CREATE_INFO = 11
DAVOMAT = 12
DAVOMAT_OLISH = 13
TEACHER_GROUP_DELETE_INFO = 14
TEACHER_GROUP_DELETE_INFO_ANSWER = 15
ADMIN = 16
LOGIN = 17
EDIT_PASSWORD = 18
NEW_PASSWORD = 19

step = 0
arr = []
password = '5269458930'
arr_info = ["<b>O'quvchi ism familiyasi</b>ni yozib yuboring\n\n<i>Masalan: Karimov Shavkat</i>", "<b>Tarbiyachi ism familiyasi</b>ni yozib yuboring", "<b>Telefon raqam</b>ni yozib yuboring\n\n<i>Masalan: 91 123 45 67</i>", "<b>Maktab raqam</b>ni yozib yuboring\n\n<i>Masalan: 3</i>", "<b>Manzil</b>ni yozib yuboring\n(qishloq)\n<i>Masalan: Sarmijon</i>"]
filial_arr = ["Sarmijon", "Zarafshon", "G'ovshun", "Dodarak", "Cho'g'alon", "Gulistonobod"]
teacher_arr = ["Telefon raqam", "Mutaxasislik fan"]

btn_filial = [
		[InlineKeyboardButton(f"{filial_arr[0]} filiali", callback_data=f"{filial_arr[0]}")],
		[InlineKeyboardButton(f"{filial_arr[1]} filiali", callback_data=f"{filial_arr[1]}")],
		[InlineKeyboardButton(f"{filial_arr[2]} filiali", callback_data=f"{filial_arr[2]}")],
		[InlineKeyboardButton(f"{filial_arr[3]} filiali", callback_data=f"{filial_arr[3]}")],
		[InlineKeyboardButton(f"{filial_arr[4]} filiali", callback_data=f"{filial_arr[4]}")],
		[InlineKeyboardButton(f"{filial_arr[5]} filiali", callback_data=f"{filial_arr[5]}")],
	]

def start(update, context):
    if update.effective_user.username == "Abduqodir_GQ":
       update.message.reply_html(f'Assalomu aleykum {update.effective_user.first_name}', reply_markup = BTN_ADMIN)
       return ADMIN
    elif base.tek_parent_id(update.message.chat.id):
        update.message.reply_html("Botimiz qayta ishga tushdi", reply_markup = BTN_REGISTER)
        return REGISTER
    else:
       update.message.reply_html(f'Assalomu aleykum {update.effective_user.first_name}\nUshbu botdan foydalanish uchun\n<b>Ro\'yxatdan o\'tish</b>ni bosing', reply_markup = BTN_REGISTER)
       return REGISTER

def register(update, context):
	update.message.reply_html(f"<b>Qaysi filialda ro'yxatdan o'tmoqchisiz tanlang</b>", reply_markup = InlineKeyboardMarkup(btn_filial))
	return FILIAL

def filial(update, context):
	query = update.callback_query
	txt = query.data
	query.message.delete()
	arr.append(txt)
	query.message.reply_html(f"<b>O'quvchi guruhi nomini yozib yuboring.</b>\n\n<i>Bilmasangiz o'qituvchidan so'rang</i>")
	return INFOR
	


def infor(update, context):
	global step, arr
	if update.message.text == password:
		update.message.reply_html(f"Xush kelibsiz ustoz\n<b>Ro'yxatdan o'tish</b> tugmasini bosing", reply_markup=BTN_REGISTER)
		return TEACHER
	else:
		if step == 0:
			if base.info_group_students(update.message.text):
				update.message.reply_html(f"Kechirasiz bunday guruh topilmadi.\nO'qituvchi bilan bog'lanib, \n<b>\tRo'yxatdan o'tish</b> \ntugmasini qayta bosing")
				return REGISTER
			else:
				arr.append(update.message.text)
				arr.append(update.message.chat.id)
		arr.append(update.message.text)	
		if step < 5 :
			update.message.reply_html(f"{arr_info[step]}")
			step += 1
			return INFOR
		else:
			base.create_student(arr[0], arr[1], arr[4], arr[5], arr[6], arr[7], arr[2])
			update.message.reply_html(f"Tabriklaymiz {arr[5]} !\nSiz muvaffaqqiyatli ro'yxatdan o'tdingiz. Yana ro'yxatdan o'tish uchun tugmani bosing", reply_markup=BTN_PARENT)
			step = 0
			arr = []
			return REGISTER
			
			

def teacher(update, context):
	update.message.reply_html(f"Familiya Ismingizni yozib yuboring")
	return INFO_TEACHER

def info_teacher(update, context):
	global step, arr
	arr.append(update.message.text)
	if step < 2:
		update.message.reply_html(f"{teacher_arr[step]}ingizni yozib yuboring.")
		step += 1
	else:
		arr.append(update.message.chat.id)
		base.create_teacher(arr[1], arr[2], arr[3], arr[4])
		update.message.reply_html(f"Tabriklaymiz {arr[1]} ustoz !\nSiz muvaffaqqiyatli ro'yxatdan o'tdingiz.", reply_markup=BTN_TEACHER)
		step = 0
		arr = []
		return TEACHER_BTN
	return INFO_TEACHER

teacher_group_arr = ["Qo'shish", "O'chirish", "Ma'lumotlari", "Orqaga"]
def teacher_group(update, context):
	btn_teacher_group = [
		[InlineKeyboardButton(f"{teacher_group_arr[0]}", callback_data=f"{teacher_group_arr[0]}")],
		[InlineKeyboardButton(f"{teacher_group_arr[1]}", callback_data=f"{teacher_group_arr[1]}")],
		[InlineKeyboardButton(f"{teacher_group_arr[2]}", callback_data=f"{teacher_group_arr[2]}")],
		[InlineKeyboardButton(f"{teacher_group_arr[3]}", callback_data=f"{teacher_group_arr[3]}")],
	]
	update.message.reply_html(f"Nima qilishni tanlang", reply_markup = InlineKeyboardMarkup(btn_teacher_group))
	return TEACHER_GROUP

def teacher_student(update, context):
	pass

def teacher_group_btns(update, context):
	query = update.callback_query
	txt = query.data
	query.message.delete()
	if txt == teacher_group_arr[0]:
		query.message.reply_html(f"<b>Qaysi filialga guruh qo'shmoqchisiz tanlang</b>", reply_markup = InlineKeyboardMarkup(btn_filial))
		return TEACHER_GROUP_CREATE
	elif txt == teacher_group_arr[1]:
		query.message.reply_html(f"<b>Qaysi filialdagi guruhni o'chirmoqchisiz tanlang</b>", reply_markup = InlineKeyboardMarkup(btn_filial))
		return TEACHER_GROUP_DELETE
	elif txt == teacher_group_arr[2]:
		query.message.reply_html(f"Ma'lumotini bilmoqchi bo'lgan <b>guruh nomi</b>ni yuboring")
		return TEACHER_GROUP_INFO
	elif txt == teacher_group_arr[3]:
		return TEACHER_BTN
	else:
		return TEACHER_GROUP
	
# create_group(filial, guruh, hafta_kunlari, fan, teacher)
def teacher_group_create(updete, context):
	query = updete.callback_query
	txt = query.data
	arr.append(txt)
	query.message.delete()
	query.message.reply_html(f"Guruh nomini yuboring")

	return TEACHER_GROUP_CREATE_INFO

def teacher_group_delete(updete, context):
	query = updete.callback_query
	txt = query.data
	arr.append(txt)
	query.message.delete()
	query.message.reply_html(f"Guruh nomini yuboring")

	return TEACHER_GROUP_DELETE_INFO	

def teacher_group_create_info(update, context):
	global step, arr
	if step == 0:
		# print(base.detected_group(update.message.text))
		if base.detected_group(update.message.text):
			arr.append(update.message.text)
			update.message.reply_html(f"Jadvalni yuboring\n\n<b>Masalan:</b>\n<i>Dushanba - 08:30\n Juma - 08:30\n bo'lsa, quyidagicha yozing\n\nDushanba/08:30/Juma/08:30</i>")
			step+=1
		else:
			update.message.reply_html(f"<i>Bunday guruh mavjud. Boshqa nom o'ylab toping va qayta jo'nating</i>")
			step = 0
		return TEACHER_GROUP_CREATE_INFO
	elif step == 1:	
		# print(update.message.text)
		arr.append(update.message.text)
		# print(arr)
		a = list(map(str, arr[2].split("/")))
		if date.jadval_tek(a):
			base.create_group(arr[0], arr[1], arr[2], update.message.chat.id)
			update.message.reply_html(f"Guruh muvaffaqqiyatli tashkil etildi\n\nNima qilishni, tugmalardan tanlang")
			for t in range(len(a)):
				if t%2==1:
					continue
				base.date_info(date.jadval(a[t]), arr[1], a[t+1])
		else:
			arr.remove(arr[2])
			update.message.reply_html(f"<i>Hafta kunlari xato yuborildi, qayta urinib ko'ring </i>")
			return TEACHER_GROUP_CREATE_INFO
		step = 0
		arr = []
		return TEACHER_BTN

def teacher_group_delete_info(update, context):
	btn_teacher_delete_group = [
		[
			InlineKeyboardButton("YO'Q", callback_data="yoq"),
			InlineKeyboardButton("HA", callback_data="ha"),
		]
		]
	if base.detected_group(update.message.text):
		update.message.reply_html("Bunday guruh topilmadi. Guruh nomini to'g'ri yuboring")
		return TEACHER_GROUP_DELETE_INFO
	else:
		if base.permisson_group(update.message.text, update.message.chat.id):
		# if True:
			global arr
			arr.append(update.message.text)
			print(arr)
			update.message.reply_html(f"Haqiqatdan ham <b>{update.message.text}</b> - guruhini o'chirishni xohlaysizmi ?", reply_markup=InlineKeyboardMarkup(btn_teacher_delete_group))
			return TEACHER_GROUP_DELETE_INFO_ANSWER
		else:
			update.message.reply_html("Sizga bu guruh ma'lumotlari uchun ruxsat yo'q\n\nNima qilishni, tugmalardan tanlang")
			return TEACHER_BTN
def teacher_group_delete_answer(update, context):
	query = update.callback_query
	txt = query.data
	query.message.delete()
	if txt == "ha":
		global arr
		print(arr)
		base.delete_group(arr[1])
		query.message.reply_html(f"<b>{arr[1]}</b> guruhi o'chirildi.\n\nNima qilishni, tugmalardan tanlang")
		arr = []
	else:
		query.message.reply_html("Nima qilishni, tugmalardan tanlang")
	return TEACHER_BTN

def teacher_group_info(update, context):
	if base.detected_group(update.message.text):
		update.message.reply_html("Bunday guruh topilmadi. Guruh nomini to'g'ri yuboring")
		return TEACHER_GROUP_INFO
	else:
		update.message.reply_html(f"    <b>{update.message.text}</b> guruh ro'yxati\n\n{base.info_group_student(update.message.text)}\n{base.dars_jadval_info(update.message.text)}\n\nNima qilishni, tugmalardan tanlang")
		return TEACHER_BTN

def davomat(update, context):
	update.message.reply_html("Guruh nomini yuboring")
	return DAVOMAT

def davomat_group(update, context):
	if base.detected_group(update.message.text):
		update.message.reply_html("Bunday guruh topilmadi. Guruh nomini to'g'ri yuboring")
		return DAVOMAT
	else:
		if base.permisson_group(update.message.text, update.message.chat.id):
		# if True:
			global arr
			arr.append(update.message.text)
			if base.info_group_student(update.message.text)!="":
				update.message.reply_html(f"    <b>{update.message.text}</b> guruh ro'yxati\n\n{base.info_group_student(update.message.text)}" + "\n\nDarsda yo'q o'quvchilarni nomerini yozib yuboring\nMasalan: 1/7/24")
				return DAVOMAT_OLISH
			else:
				update.message.reply_html(f"<b>{update.message.text}</b> guruhiga o'quvchilar qo'shilmagan\n\nNima qilishni, tugmalardan tanlang")
				return TEACHER_BTN
		else:
			update.message.reply_html("Sizga bu guruh ma'lumotlari uchun ruxsat yo'q\n\nNima qilishni, tugmalardan tanlang")
			return TEACHER_BTN



def davomat_olish(update, context):
	global arr
	davomat_arr = list(map(int, update.message.text.split("/")))
	s = 0
	r = ""
	for item in base.info_davomat_nb(arr[0], davomat_arr):
		txt = f"Assalomu aleykum {item[3]}.\nSizning qaramog'ingizdagi {item[2]}, bugun\nSalimov akademiyasining {item[0]} filialida tashkil etilgan {base.group_fan(arr[0])[4]} darsiga qatnashmadi."
		messages.send(item[7], txt)
	for item in base.info_davomat_b(arr[0], davomat_arr):
		txt = f"Assalomu aleykum {item[3]}.\nSizning qaramog'ingizdagi {item[2]}, bugun\nSalimov akademiyasining {item[0]} filialida tashkil etilgan {base.group_fan(arr[0])[4]} darsiga qatnashdi."
		messages.send(item[7], txt)
	for item in base.info_davomat_nb(arr[0], davomat_arr):
		s+=1
		r += f"\n{s}. {item[2]}"
	update.message.reply_html(f"Darsga kelmagan o'quvchilar{r}\n\ntarbiyachilariga xabar yuborildi\n\nNima qilishni, tugmalardan tanlang")
	# print(base.info_davomat(arr[0], davomat_arr))
	arr = []
	return TEACHER_BTN


def yordam(update, context):
	update.message.reply_html("asd")
	return REGISTER

e_arr = [0]
def eslatma(update, context):
	x = datetime.datetime.now()
	global e_arr
	print(e_arr[0])
	if e_arr[0]==str(x.strftime("%M")):
		update.message.reply_html("Yuborilgan")
	else:
		text = """Hurmatli tarbiyachi ertaga sizning farzandingizga Salimov akademiyasida dars bor. 
		Iltimos farzandingizni ertaga darsga qatnashishini taminlang va eng asosiysi uyga vazifalarini shaxsan o'zingiz nazoratga oling"""
		e_arr[0] = str(x.strftime("%M"))
		for i in base.group_user_id():
			messages.send(i, text)
		update.message.reply_html("Eslatma ertaga darsi bo'lgan barcha guruhlarga yuborildi.")
	return ADMIN

def login(update, context):
	update.message.reply_html("Parolni kiriting.")
	return LOGIN

def signin(update, context):
	txt = update.message.text
	if txt == password:
		update.message.reply_html("Xush kelibsiz ustoz", reply_markup = BTN_TEACHER)
		return TEACHER_BTN
	elif txt == "seven7beautiful":
		update.message.reply_html("Xush kelibsiz admin", reply_markup = BTN_ADMIN)
		return ADMIN
	else:
		update.message.reply_html("Parol xato. Parolni bilish uchun Salimov bilan bo'g'laning. Siz foydalanuvchisiz", reply_markup = BTN_REGISTER)
		return REGISTER

def logout(update, context):
	update.message.reply_html("Siz foydalanuvchisiz", reply_markup = BTN_REGISTER)
	return REGISTER

def edit_parol(update, context):
	btn_password = [
		[InlineKeyboardButton("O'zgartirish", callback_data = 'edit')],
		[InlineKeyboardButton("Orqaga", callback_data = 'back')],
	]
	update.message.reply_html(f"Hozirgi parol: {password}", reply_markup = InlineKeyboardMarkup(btn_password))
	return EDIT_PASSWORD

def edit_password(update, context):
	query = update.callback_query
	txt = query.data
	query.message.delete()
	if txt == "edit":
		query.message.reply_html("Yangi parolni jo'nating.")
		return NEW_PASSWORD
	else:
		return ADMIN

def new_password(update, context):
	global password
	txt = update.message.text
	if len(txt) != 0:
		password = txt
		update.message.reply_html(f"Parol o'zgartirildi.\n Yangi parol: {password}")
		return ADMIN
	else:
		update.message.reply_html(f"Boshqa parol kiriting.")
		return NEW_PASSWORD




def main():
	updater = Updater(API_TOKEN, use_context=True)

	dispatcher = updater.dispatcher
	conv_handler = ConversationHandler(
		entry_points = [CommandHandler('start', start)],

		states = {
			ADMIN: [
				MessageHandler(Filters.regex(f'^{btn_eslatma}$'), eslatma),
				MessageHandler(Filters.regex(f'^{btn_parol}$'), edit_parol),
			],
			REGISTER: [
				MessageHandler(Filters.regex(f'^{btn_register}$'), register)
			],
			INFOR: [
				MessageHandler(Filters.text, infor)
			],
			FILIAL: [
				CallbackQueryHandler(filial)
			],
			TEACHER: [
				MessageHandler(Filters.regex(f'^{btn_register}$'), teacher)
			],
			INFO_TEACHER: [MessageHandler(Filters.text, info_teacher)],
			TEACHER_BTN: [
				MessageHandler(Filters.regex(f'^{btn_teacher_group}$'), teacher_group),
				MessageHandler(Filters.regex(f'^{btn_teacher_student}$'), teacher_student),
				MessageHandler(Filters.regex(f'^{btn_teacher_davomat}$'), davomat)
			],
			PARENT_BTN: [],
			TEACHER_GROUP: [CallbackQueryHandler(teacher_group_btns)],
			TEACHER_GROUP_CREATE: [CallbackQueryHandler(teacher_group_create)],
			TEACHER_GROUP_DELETE: [CallbackQueryHandler(teacher_group_delete)],
			TEACHER_GROUP_INFO: [MessageHandler(Filters.text, teacher_group_info)],
			TEACHER_GROUP_CREATE_INFO: [MessageHandler(Filters.text, teacher_group_create_info)],
			DAVOMAT: [MessageHandler(Filters.text, davomat_group)],
			DAVOMAT_OLISH: [
				MessageHandler(Filters.text, davomat_olish)
			],
			TEACHER_GROUP_DELETE_INFO: [MessageHandler(Filters.text, teacher_group_delete_info)],
			TEACHER_GROUP_DELETE_INFO_ANSWER: [CallbackQueryHandler(teacher_group_delete_answer)],
			LOGIN: [MessageHandler(Filters.text, signin)],
			EDIT_PASSWORD: [CallbackQueryHandler(edit_password)],
			NEW_PASSWORD: [MessageHandler(Filters.text, new_password)],



		},

		fallbacks = [CommandHandler('help', help),
					CommandHandler('yordam', yordam),
					CommandHandler('login', login),
					CommandHandler('logout', logout),
					]
	)
	
	dispatcher.add_handler(conv_handler)
	updater.start_polling()
	updater.idle()
	
main()

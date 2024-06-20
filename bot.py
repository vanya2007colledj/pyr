import random
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import CallbackQuery
from datetime import datetime
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import phonenumbers
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import Throttled
import random
import requests
import sqlite3
from bs4 import BeautifulSoup
import time, asyncio
import aiogram.utils.exceptions
from aiogram.types.message import ContentTypes
import re, hashlib
from config import TOKEN, support_username, admin_id, CHANNEL_ID, CRYPTOPAY
from kb import subc, button_s2, but, adminpanel

fullochered = 1

connection = sqlite3.connect('botcasino.db')
q = connection.cursor()

bot = Bot(token='7459768815:AAFa8V8AuKXi6cjEOkRg1PXPupYP20xdqhI', parse_mode=ParseMode.HTML)
dp = Dispatcher(bot,storage=MemoryStorage())

texts = ["куб", "Куб", "кУб", "каб", "куБ", "кУБ", "КуБ", "КУБ", "КУ", "Куб", "чет"]

baab = ["победа1", "победа2", "Победа1", "Победа2"]
basket = ["Баскет", "баскет", "баскетбол", "баскет", "Баскетбол"]

adminpanel = types.InlineKeyboardMarkup(row_width=2)
adminpanel.add(
	types.InlineKeyboardButton(text='Параметры', callback_data="popoln")
	)
import sys

sys.path.append('aiocryptopay')

from aiocryptopay import AioCryptoPay
import asyncio

crypto = AioCryptoPay(token=CRYPTOPAY)

import json

@dp.message_handler(commands='check_c')
async def snsnns(message: types.Message):
	try:
		arg = message.get_args()
		arg = float(arg)
		f = open('admins.txt', 'r')
		lines = f.readlines()
		f.close()
		user_id = int(message.from_user.id)
		for line in lines:
			if user_id == int(line):
				ch = types.InlineKeyboardMarkup(row_width=1)
				ch.add(
				types.InlineKeyboardButton(text='...', callback_data="idinahuuuuu"))
				m = await message.answer(f"🕒 Создание чека на {arg} USDT (${arg})", reply_markup=ch)
				await asyncio.sleep(2)
				checkab = await crypto.create_check(asset='USDT', amount=arg)
				chch = types.InlineKeyboardMarkup(row_width=1)
				chch.add(
				types.InlineKeyboardButton(text='Активировать чек', url=f"{checkab.bot_check_url}"))
				await m.edit_text(f"```\nЧек на {arg} USDT (${arg})\n```", reply_markup=chch, parse_mode='Markdown')
	except Exception as er:
		await message.answer(er)
@dp.message_handler(commands='kazna')
async def kaznananan(message: types.Message):
	summa = message.get_args()
	invoice = await crypto.create_invoice(asset='USDT', amount=summa)
	await bot.send_message(message.from_user.id, invoice.bot_invoice_url)
4
@dp.message_handler(commands='app_balance')
async def kaznananan(message: types.Message):
	bal = await crypto.get_me()
	await bot.send_message(message.from_user.id, bal)


@dp.message_handler(commands='start')
async def messagebsbs(message: types.Message):
	ref_id = message.get_args()
	user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
	# Проверка регистрации в боте
	q.execute(f"SELECT * FROM reg WHERE user_id = {message.from_user.id}")
	result = q.fetchall()
	if len(result) == 0:
		ref_id = message.get_args()
		if ref_id >= '_':
			ref_id = 'False'
		q.execute(f"INSERT INTO reg (user_id, balance, registered, ref_id)"
		f"VALUES ('{message.from_user.id}', '0', '0', '{ref_id}')")
		connection.commit()
		dt = datetime.now()
		dt = dt.strftime('%Y-%m-%d')
		q.execute(f"INSERT INTO user (user_id, wins, loses, time)"
		f"VALUES ('{message.from_user.id}', '0', '0', '{dt}')")
		connection.commit()
		ref_id = message.get_args()
		try:
			regss = q.execute(f"SELECT registered from reg where user_id = ?", (ref_id,)).fetchone()
			regss = int(regss[0])
			regsss = int(regss) + 1
			q.execute(f'UPDATE reg SET registered = "{regsss}" WHERE user_id = ?', (ref_id,))
			name = f"{message.from_user.first_name}"
			half_length = len(name) // 2
			hidden_name = name[:half_length] + '*' * (len(name) - half_length)
			print(hidden_name)
			await bot.send_message(ref_id, f"<i>🌟 Через вашу персональную ссылку вступил {hidden_name}</i>", parse_mode='HTML')
			connection.commit()
		except:
			connection.commit()
			pass
		if user_channel_status["status"] != 'left':
			time = q.execute(f"SELECT time from user where user_id = ?", (message.from_user.id,)).fetchone()
			time = str(time[0])
			wins = q.execute(f"SELECT wins from user where user_id = ?", (message.from_user.id,)).fetchone()
			wins = float(wins[0])
			loses = q.execute(f"SELECT loses from user where user_id = ?", (message.from_user.id,)).fetchone()
			loses = float(loses[0])
			reg = q.execute(f"SELECT registered from reg where user_id = ?", (message.from_user.id,)).fetchone()
			reg = int(reg[0])
			balik = q.execute(f"SELECT balance from reg where user_id = ?", (message.from_user.id,)).fetchone()
			balik = float(balik[0])
			suma = float(wins) / 1.7 + float(loses)
			registered_date_str = str(time)
			registered_date = datetime.strptime(registered_date_str, '%Y-%m-%d')
			current_date = datetime.now()
			time_elapsed = current_date - registered_date
			days_elapsed = time_elapsed.days
			print("Дней прошло с момента регистрации:", days_elapsed)
			await message.answer(f"""⭐ Профиль @{message.from_user.username}

📊 Статистика:
— Выигрышей: <code>{wins}$</code>
— Проигрышей: <code>{loses}$</code>
— Сумма ставок: <code>{suma}$</code>

👥 Реферальная программа
— Ты получаешь 5% от проигрыша ставки реферала.
— Вывод доступен от 1.25$!
— Количество приглашенных пользователей: <code>{reg}</code>
— Реферальный баланс: <code>{balik}$</code>
— Персональная ссылка: <code>https://t.me/MegaBetRobot?start={message.from_user.id}</code>

🔥 Ты уже с нами {days_elapsed} дней!""", reply_markup=button_s2)
		else:
			await message.answer(f"❌ Вы не подписались на наш канал!", reply_markup=subc)
	else:
		q.execute(f"SELECT * FROM user WHERE user_id = {message.from_user.id}")
		result = q.fetchall()
		if len(result) == 0:
			dt = datetime.now()
			dt = dt.strftime('%Y-%m-%d')
			q.execute(f"INSERT INTO user (user_id, wins, loses, time)"
			f"VALUES ('{message.from_user.id}', '0', '0', '{dt}')")
			connection.commit()
			pass
		if user_channel_status["status"] != 'left':
			time = q.execute(f"SELECT time from user where user_id = ?", (message.from_user.id,)).fetchone()
			time = str(time[0])
			wins = q.execute(f"SELECT wins from user where user_id = ?", (message.from_user.id,)).fetchone()
			wins = float(wins[0])
			loses = q.execute(f"SELECT loses from user where user_id = ?", (message.from_user.id,)).fetchone()
			loses = float(loses[0])
			reg = q.execute(f"SELECT registered from reg where user_id = ?", (message.from_user.id,)).fetchone()
			reg = int(reg[0])
			balik = q.execute(f"SELECT balance from reg where user_id = ?", (message.from_user.id,)).fetchone()
			balik = float(balik[0])
			registered_date_str = str(time)
			registered_date = datetime.strptime(registered_date_str, '%Y-%m-%d')
			current_date = datetime.now()
			time_elapsed = current_date - registered_date
			days_elapsed = time_elapsed.days
			print("Дней прошло с момента регистрации:", days_elapsed)
			suma = float(wins) / 1.7 + float(loses)
			await message.answer(f"""⭐ Профиль @{message.from_user.username}

📊 Статистика:
— Выигрышей: {wins}$
— Проигрышей: {loses}$
— Сумма ставок: {suma}$

👥 Реферальная программа
— Ты получаешь 5% от проигрыша ставки реферала.
— Вывод доступен от 1.25$!
— Количество приглашенных пользователей: {reg}
— Реферальный баланс: {balik}$
— Персональная ссылка: <code>https://t.me/MegaBetRobot?start={message.from_user.id}</code>

🔥 Ты уже с нами {days_elapsed} дней!""", reply_markup=button_s2)
		else:
			await message.answer(f"❌ Вы не подписались на наш канал!", reply_markup=subc)
	try:
		args = message.get_args()
		if args == f'_{message.from_user.id}_':
			status = q.execute(f"SELECT status from users where user_id = ?", (message.from_user.id,)).fetchone()
			status = str(status[0])
			summa = q.execute(f"SELECT summa from users where user_id = ?", (message.from_user.id,)).fetchone()
			summa = float(summa[0])
			ren = random.randint(1,10000000)
			mystring = f"{ren}_secret"
			hash_object = hashlib.md5(mystring.encode())
			random_n = hash_object.hexdigest()
			q.execute(f'UPDATE users SET user_id = "{random_n}" WHERE user_id = ?', (message.from_user.id,))
			if status == 'win':
				try:
					check = await crypto.create_check(asset='USDT', amount=summa)
					connection.commit()
					ch = types.InlineKeyboardMarkup(row_width=1)
					ch.add(types.InlineKeyboardButton(text='Активировать чек', url=f"{check.bot_check_url}"))
					await message.answer(f"⚡ Ваша выплата на сумму {summa} USDT. Заберите выигрыш по кнопке ниже.", reply_markup=ch)
				except Exception as er:
					print(er)
					await message.answer(f"<b>❌ Казна бота пуста!\n— Для того чтобы забрать выигрыш напишите {support_username}</b>")
					stopstop
				print(check)
		else:
			pass
	except Exception as bab:
		print(bab)

@dp.message_handler(commands="baba")
async def babo(message: types.Message):
    arg = message.get_args()
    checkab = await crypto.create_check(asset='USDT', amount=arg)
    await message.answer(checkab)

@dp.channel_post_handler()
async def roll_dice(message: types.Message):
	text = message.text
	entata = message.entities
	print(message.entities)
	msgsg = f"""<b>{message.text}</b>""".replace('отправил(а)', 'поставил')
	maja = await message.answer(f"[✅] Ваша ставка принята в работу!")
	prefix = "($"
	await asyncio.sleep(1)
	try:
		cb_winid = entata[0].user.id
		nickname = entata[0].user.first_name
	except:
		cb_winid, nickname = '', ''
		await maja.delete()
		stop_stop
	comment = message.text.split('💬 ')
	try:
		comment_data = comment[1]
	except:
		comment_data = ''
	comm = comment_data.replace('💬', '')
	stt = text[text.index(prefix) + len(prefix):].strip()
	summ = stt.replace(').', '').replace(f"\n", "").replace(f"{comment_data}", "").replace('💬', '')
	await message.delete()
	summ = float(summ)
	f = open('max.txt', 'r')
	simo = f.read()
	link = entata[2].url
	username = entata[0].user.username
	win = q.execute(f"SELECT wins from stats where tabas = ?", ('statistic',)).fetchone()
	win = int(win[0])
	los = q.execute(f"SELECT loses from stats where tabas = ?", ('statistic',)).fetchone()
	los = int(los[0])
	vuplas = q.execute(f"SELECT thestb from stats where tabas = ?", ('statistic',)).fetchone()
	vuplas = float(vuplas[0])
	if summ >= float(simo):
		await maja.edit_text('<b>💎 Ставка не принята. Идет донат администратору!</b>')
		stop
	cubik = ["чет", "Чет", "чёт", "Чёт", "Куб", "куб", "кубик", "четное", "Четное", "Чётное", "чётное", "нечет", "Нечет", "нечёт", "Нечёт", "Нечётное", "нечетное", "Больше", "больше", "большой", "Большой", "меньше", "Меньше", "Меньший", "меньший", "Куб чёт", "куб чёт", "куб чет", "куб Чет", "Куб чет"]
	bask = ["Баскет","баскетбол","баск","мимо","попал","Баскет попал", "баскет мимо", "баскет попал", "Баскет мимо"]
	fot = ["Футбол", "фут", "фут мимо", "фут гол", "фут попал", "Футбол попал", "Футбол мимо", "Футбол гол", "Фут попал", "Фут гол", "Фут мимо", "футбол попал", "футбол гол", "футбол мимо"]
	boul = ["Боулинг страйк", "боул", "боулинг", "боулинг 1", "боулинг 2","боулинг 3","боулинг 4","боулинг 5"]
	if any(word in comm for word in cubik):
		emoj = '🎲'
	if any(word in comm for word in bask):
		emoj = '🏀'
	if any(word in comm for word in fot):
		emoj = '⚽'
	if any(word in comm for word in boul):
		emoj = '🎳'
	fullochered = 1
	try:
		memas = await maja.edit_text(f"""🏹 Делается новая ставка!

<blockquote>Игрок: {nickname}

Сумма ставки: {summ} $

Исход: {comm}</blockquote>

<b>💵 Всего выплачено: {vuplas}$</b>""")
	except:
		memas = await maja.edit_text(f"""🏹 Делается новая ставка!

<blockquote>Игрок: {nickname}

Сумма ставки: {summ} $

Исход: {comm}</blockquote>

<b>💵 Всего выплачено: {vuplas}$</b>""")
	#entana = f"{entata}".replace('[<MessageEntity ', '').replace('')
	await asyncio.sleep(2)
	word_list = ["Куб", "куб", "баскет", "Баскет", "фут", "футбол", "Фут", "Футбол", "Боулинг", "боул", "боулинг", "Боул", "Победа 1", "Победа 2", "победа 1", "победа 2", "чет", "чёт", "нечет", "Нечет", "нечёт", "мимо", "Мимо","Попал", "попал", "Гол", "гол", "победа1", "победа2", "страйк", "четное", "нечетное", "нечетное", "больше", "меньше", "Больше", "Меньше"]
	sum_value = float(summ)
	print(word_list)
	otpa = types.InlineKeyboardMarkup(row_width=2)
	otpa.add(types.InlineKeyboardButton(text='Поставить ставку', url='http://t.me/send?start=IVeH7bZj20R2'))
	txt = message.text
	print(txt)
	if any(word in txt for word in word_list):
		pass
	else:
		await memas.delete()
		if summ >= 1.24:
			try:
				kik = float(summ)*90 / 100
				ran = random.randint(1,100000000)
				await crypto.transfer(spend_id=ran, user_id=cb_winid, amount=kik, asset='USDT')
				await message.answer(f"""
❌ {nickname} не ввел правильно комментарий/игру к депозиту.

<blockquote>😢 На ваш кошелек зачислено {summ}$ с комиссией 10%.</blockquote>

— Посмотрите правильные команды для того чтобы играть без ошибок.""", reply_markup=otpa)
				dksksksk
			except:
				await message.answer(f"""
❌ {nickname} не ввел правильно комментарий/игру к депозиту.

<blockquote>😢 На ваш кошелек будет зачислено {summ}$ администратором с комиссией 10%.</blockquote>

— Посмотрите правильные команды для того чтобы играть без ошибок.""", reply_markup=otpa)
				ksksksk
		else:
			q.execute(f'UPDATE users SET status = "win" WHERE user_id = ?', (cb_winid,))
			print(summ)
			kik = float(summ)*90 / 100
			summa = float(kik)
			q.execute(f'UPDATE users SET summa = "{summa}" WHERE user_id = ?', (cb_winid,))
			connection.commit()
			ch = types.InlineKeyboardMarkup(row_width=1)
			ch.add(
			types.InlineKeyboardButton(text='Забрать', url=f'https://t.me/MegaBetRobot?start=_{cb_winid}_'),
			types.InlineKeyboardButton(text='Поставить ставку', url='http://t.me/send?start=IVeH7bZj20R2'))
			connection.commit()
			await message.answer(f"""
❌ {nickname} не ввел правильно комментарий/игру к депозиту.

<blockquote>😢 Получите возврат средств в размере {summ}$ с комиссией 10%!</blockquote>

— Так как ваш депозит содержит сумму ниже 1.25$, мы выдадим вам чеком.""", reply_markup=ch)
			kdkdkdk
	nickname = f"<code>{nickname}</code>"
	q.execute(f"SELECT * FROM users WHERE user_id = {cb_winid}")
	result = q.fetchall()
	if len(result) == 0:
		q.execute(f"INSERT INTO users (user_id, status, summa)"
		f"VALUES ('{cb_winid}', 'user', '0')")
		connection.commit()
	q.execute(f"SELECT * FROM wins WHERE user_id = {cb_winid}")
	result = q.fetchall()
	if len(result) == 0:
		q.execute(f"INSERT INTO wins (user_id, stavka, wined)"
		f"VALUES ('{cb_winid}', '0', '0')")
		connection.commit()
	else:
		pass
	q.execute(f"SELECT * FROM reg WHERE user_id = {cb_winid}")
	result = q.fetchall()
	if len(result) == 0:
		ref_id = ''
		q.execute(f"INSERT INTO reg (user_id, balance, registered, ref_id)"
		f"VALUES ('{cb_winid}', '0', '0', '{ref_id}')")
		connection.commit()
	else:
		pass
	q.execute(f"SELECT * FROM user WHERE user_id = {cb_winid}")
	result = q.fetchall()
	if len(result) == 0:
		dt = datetime.now()
		dt = dt.strftime('%Y-%m-%d')
		q.execute(f"INSERT INTO user (user_id, wins, loses, time)"
		f"VALUES ('{cb_winid}', '0', '0', '{dt}')")
		connection.commit()
	else:
		pass
	ref_id = q.execute(f"SELECT ref_id from reg where user_id = ?", (cb_winid,)).fetchone()
	ref_id = str(ref_id[0])
	wins = q.execute(f"SELECT wins from user where user_id = ?", (cb_winid,)).fetchone()
	wins = float(wins[0])
	loses = q.execute(f"SELECT loses from user where user_id = ?", (cb_winid,)).fetchone()
	loses = float(loses[0])
	stavka = q.execute(f"SELECT stavka from wins where user_id = ?", (cb_winid,)).fetchone()
	stavka = float(stavka[0])
	wineds = q.execute(f"SELECT wined from wins where user_id = ?", (cb_winid,)).fetchone()
	wineds = int(wineds[0])
	prefix = "($"
	ran = random.randint(1,1000000)
	try:
		msga = message.text.split('💬')
		msga = msga[1]
		msga = msga.split(' ')
		msgas = msga[1]
		msgasa = msga[1]
		msgasa = f"{msgasa}" + msga[2].replace('💬 ', '')
		msgsba = f"{msgasa}"
		msgb = '💬 ' + msga[0] + msga[1] + ' ' + msga[2]
		print(msgasa)
		sum_str = text[text.index(prefix) + len(prefix):].strip()
		sum_value = sum_str.replace(').', '').replace(f"\n", "").replace(f"{msgb}", "")
	except:
		pass
	txt = f"{comm}"
	cub = ["чет", "чёт", "Чет", "Чёт"]
	if txt >= "ч":
		msg = await bot.send_dice(CHANNEL_ID)
		chetcheck = int(msg.dice.value)
		chetsh = int(chetcheck)
		if chetcheck in [2, 4, 6]:
			await asyncio.sleep(3)
			vuplach = float(summ) * 1.7  + float(vuplas)
			q.execute(f'UPDATE stats SET wins = {win + 1} WHERE tabas = ?', ('statistic',))
			q.execute(f'UPDATE stats SET thestb = "{vuplach}" WHERE tabas = ?', ('statistic',))
			q.execute(f'UPDATE users SET status = "win" WHERE user_id = ?', (cb_winid,))
			print(summ)
			summa = float(summ)*1.7
			q.execute(f'UPDATE users SET summa = "{summa}" WHERE user_id = ?', (cb_winid,))
			connection.commit()
			bab = float(wins) + float(summa)
			q.execute(f'UPDATE user SET wins = "{bab}" WHERE user_id = ?', (cb_winid,))
			connection.commit()
			ch = types.InlineKeyboardMarkup(row_width=1)
			ch.add(
			types.InlineKeyboardButton(text='Забрать выигрыш', url=f'https://t.me/MegaBetRobot?start=_{cb_winid}_'),
			types.InlineKeyboardButton(text='Поставить ставку', url='http://t.me/send?start=IVeH7bZj20R2'))
			if summa >= 1.25:
				try:
					await crypto.transfer(spend_id=ran, user_id=cb_winid, amount=summa, asset='USDT')
					await bot.send_photo(chat_id=CHANNEL_ID, photo=open('chet.png', 'rb'), caption=f"Победа! Выпало четное значение [{chetcheck}]\n\n<blockquote><b>\nНа ваш кошелек зачислено {summa} USDT. Ставь и выигрывай!</b></blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", parse_mode='HTML')
				except Exception as ehh:
					print(ehh)
					await bot.send_photo(chat_id=CHANNEL_ID, photo=open('chet.png', 'rb'), caption=f"Победа! Выпало четное значение [{chetcheck}]\n\n<blockquote><b>\nНа ваш кошелек будет {summa} USDT зачислено администратором. Ставь и выигрывай!</b></blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa, parse_mode='HTML')
			else:
				await bot.send_photo(chat_id=CHANNEL_ID, photo=open('chet.png', 'rb'), caption=f"Победа! Выпало четное значение [{chetcheck}]\n\n<blockquote><b>\nВаш выигрыш {summa} USDT создан в чеке. Заберите по кнопке ниже.</b></blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=ch, parse_mode='HTML')
		else:
			q.execute(f'UPDATE stats SET loses = {los + 1} WHERE tabas = ?', ('statistic',))
			bab = float(loses) + float(summ)
			q.execute(f'UPDATE user SET loses = "{bab}" WHERE user_id = ?', (cb_winid,))
			connection.commit()
			try:
				ref_balance = q.execute("SELECT balance from reg where user_id = ?", (ref_id,)).fetchone()
				ref_balance = f"{ref_balance}".replace('(', '').replace(')', '').replace(',', '')
				bol = float(ref_balance) + float(sum_value)*5/100
				q.execute(f'UPDATE reg SET balance = "{bol}" WHERE user_id = ?', (ref_id,))
				connection.commit()
				await bot.send_message(ref_id, f"🔥 ТВОЙ РЕФЕРАЛ ПРОИГРАЛ {summ}$\n🔑 Вы получили {bol}$ (5%)")
				print(ref_balance)
			except Exception as bp:
				print(bp)
				pass
			await bot.send_photo(chat_id=CHANNEL_ID, photo=open('lose.png', 'rb'), caption=f"Вы проиграли! Выпало нечетное значение [{chetcheck}]\n\n<blockquote>Сыграйте еще раз, попробуйте испытать удачу и выиграть!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa)
		kkk
	nechet = ["нечет", "Нечет", "нечёт", "Нечёт"]
	if txt >= "не":
		msg = await bot.send_dice(CHANNEL_ID)
		chetcheck = int(msg.dice.value)
		chetsh = int(chetcheck)
		nechet = 1
		if txt == "нечет":
			nechet = 2
		if txt == "Нечет":
			nechet = 2
		if txt == "нечёт":
			nechet = 2
		if nechet == 2:
			pass
		else:
			await msg.delete()
			NAHYIdidi
		if chetcheck in [1, 3, 5]:
			vuplach = float(summ) * 1.7  + float(vuplas)
			q.execute(f'UPDATE stats SET wins = {win + 1} WHERE tabas = ?', ('statistic',))
			q.execute(f'UPDATE stats SET thestb = "{vuplach}" WHERE tabas = ?', ('statistic',))
			await asyncio.sleep(3)
			q.execute(f'UPDATE users SET status = "win" WHERE user_id = ?', (cb_winid,))
			print(summ)
			summa = float(summ)*1.7
			q.execute(f'UPDATE users SET summa = "{summa}" WHERE user_id = ?', (cb_winid,))
			connection.commit()
			bab = float(wins) + float(summa)
			q.execute(f'UPDATE user SET wins = "{bab}" WHERE user_id = ?', (cb_winid,))
			connection.commit()
			ch = types.InlineKeyboardMarkup(row_width=1)
			ch.add(
			types.InlineKeyboardButton(text='Забрать выигрыш', url=f'https://t.me/MegaBetRobot?start=_{cb_winid}_'),
			types.InlineKeyboardButton(text='Поставить ставку', url='http://t.me/send?start=IVeH7bZj20R2'))
			if summa >= 1.25:
				try:
					await crypto.transfer(spend_id=ran, user_id=cb_winid, amount=summa, asset='USDT')
					await bot.send_photo(chat_id=CHANNEL_ID, photo=open('nechet.png', 'rb'), caption=f"Победа! Выпало нечетное значение [{chetcheck}]\n\n<blockquote>\nНа ваш кошелек зачислено {summa} USDT. Ставь и выигрывай!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", parse_mode='HTML')
				except Exception as ehh:
					print(ehh)
					await bot.send_photo(chat_id=CHANNEL_ID, photo=open('nechet.png', 'rb'), caption=f"Победа! Выпало нечетное значение [{chetcheck}]\n\n<blockquote>\n<b>На ваш кошелек будет {summa} USDT зачислено администратором. Ставь и выигрывай!</b></blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa, parse_mode='HTML')
			else:
				await bot.send_photo(chat_id=CHANNEL_ID, photo=open('nechet.png', 'rb'), caption=f"Победа! Выпало нечетное значение [{chetcheck}]\n\n<blockquote><b>\nВаш выигрыш {summa} USDT создан в чеке. Заберите по кнопке ниже.</b></blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=ch, parse_mode='HTML')
		else:
			q.execute(f'UPDATE stats SET loses = {los + 1} WHERE tabas = ?', ('statistic',))
			bab = float(loses) + float(summ)
			q.execute(f'UPDATE user SET loses = "{bab}" WHERE user_id = ?', (cb_winid,))
			connection.commit()
			try:
				ref_balance = q.execute("SELECT balance from reg where user_id = ?", (ref_id,)).fetchone()
				ref_balance = f"{ref_balance}".replace('(', '').replace(')', '').replace(',', '')
				bol = float(ref_balance) + float(sum_value)*5/100
				q.execute(f'UPDATE reg SET balance = "{bol}" WHERE user_id = ?', (ref_id,))
				connection.commit()
				await bot.send_message(ref_id, f"🔥 ТВОЙ РЕФЕРАЛ ПРОИГРАЛ {summ}$\n🔑 Вы получили {bol}$ (5%)")
				print(ref_balance)
			except Exception as bp:
				print(bp)
				pass
			await bot.send_photo(chat_id=CHANNEL_ID, photo=open('lose.png', 'rb'), caption=f"Вы проиграли! Выпало четное значение [{chetcheck}]\n\n<blockquote>Сыграйте еще раз, попробуйте испытать удачу и выиграть!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa)
		kkkkl
	bolsh = ["больше", "Больше"]
	if any(word in txt for word in bolsh):
		msg = await bot.send_dice(CHANNEL_ID)
		chetcheck = int(msg.dice.value)
		chetsh = int(chetcheck)
		if chetcheck in [4, 5, 6]:
			vuplach = float(summ) * 1.7  + float(vuplas)
			q.execute(f'UPDATE stats SET wins = {win + 1} WHERE tabas = ?', ('statistic',))
			q.execute(f'UPDATE stats SET thestb = "{vuplach}" WHERE tabas = ?', ('statistic',))
			await asyncio.sleep(3)
			q.execute(f'UPDATE users SET status = "win" WHERE user_id = ?', (cb_winid,))
			print(summ)
			summa = float(summ)*1.7
			bab = float(wins) + float(summa)
			q.execute(f'UPDATE user SET wins = "{bab}" WHERE user_id = ?', (cb_winid,))
			connection.commit()
			q.execute(f'UPDATE users SET summa = "{summa}" WHERE user_id = ?', (cb_winid,))
			connection.commit()
			ch = types.InlineKeyboardMarkup(row_width=1)
			ch.add(
			types.InlineKeyboardButton(text='Забрать выигрыш', url=f'https://t.me/MegaBetRobot?start=_{cb_winid}_'),
			types.InlineKeyboardButton(text='Поставить ставку', url='http://t.me/send?start=IVeH7bZj20R2'))
			if summa >= 1.25:
				try:
					await crypto.transfer(spend_id=ran, user_id=cb_winid, amount=summa, asset='USDT')
					await bot.send_photo(chat_id=CHANNEL_ID, photo=open('bolshe.png', 'rb'), caption=f"Победа! Выпало значение больше [{chetcheck}]\n\n<blockquote>\nНа ваш кошелек зачислено {summa} USDT. Ставь и выигрывай!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", parse_mode='HTML')
				except Exception as ehh:
					print(ehh)
					await bot.send_photo(chat_id=CHANNEL_ID, photo=open('bolshe.png', 'rb'), caption=f"Победа! Выпало значение больше [{chetcheck}]\n\n<blockquote>\nНа ваш кошелек будет {summa} USDT зачислено администратором. Ставь и выигрывай!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa, parse_mode='HTML')
			else:
				await bot.send_photo(chat_id=CHANNEL_ID, photo=open('bolshe.png', 'rb'), caption=f"Победа! Выпало значение больше [{chetcheck}]\n\n<blockquote>\nВаш выигрыш {summa} USDT создан в чеке. Заберите по кнопке ниже.</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=ch, parse_mode='HTML')
		else:
			try:
				ref_balance = q.execute("SELECT balance from reg where user_id = ?", (ref_id,)).fetchone()
				ref_balance = f"{ref_balance}".replace('(', '').replace(')', '').replace(',', '')
				bol = float(ref_balance) + float(sum_value)*5/100
				q.execute(f'UPDATE reg SET balance = "{bol}" WHERE user_id = ?', (ref_id,))
				connection.commit()
				await bot.send_message(ref_id, f"🔥 ТВОЙ РЕФЕРАЛ ПРОИГРАЛ {summ}$\n🔑 Вы получили {bol}$ (5%)")
				print(ref_balance)
			except Exception as bp:
				print(bp)
				pass
			q.execute(f'UPDATE stats SET loses = {los + 1} WHERE tabas = ?', ('statistic',))
			bab = float(loses) + float(summ)
			q.execute(f'UPDATE user SET loses = "{bab}" WHERE user_id = ?', (cb_winid,))
			connection.commit()
			await bot.send_photo(chat_id=CHANNEL_ID, photo=open('lose.png', 'rb'), caption=f"Вы проиграли! Выпало значение меньше [{chetcheck}]\n\n<blockquote>Сыграйте еще раз, попробуйте испытать удачу и выиграть!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa)
		kkll
	mesnh = ["меньше", "Меньше"]
	if any(word in txt for word in mesnh):
		msg = await bot.send_dice(CHANNEL_ID)
		chetcheck = int(msg.dice.value)
		chetsh = int(chetcheck)
		if chetcheck in [1, 2, 3]:
			vuplach = float(summ) * 1.7  + float(vuplas)
			q.execute(f'UPDATE stats SET wins = {win + 1} WHERE tabas = ?', ('statistic',))
			q.execute(f'UPDATE stats SET thestb = "{vuplach}" WHERE tabas = ?', ('statistic',))
			await asyncio.sleep(3)
			q.execute(f'UPDATE users SET status = "win" WHERE user_id = ?', (cb_winid,))
			print(summ)
			summa = float(summ)*1.7
			bab = float(wins) + float(summa)
			q.execute(f'UPDATE user SET wins = "{bab}" WHERE user_id = ?', (cb_winid,))
			connection.commit()
			q.execute(f'UPDATE users SET summa = "{summa}" WHERE user_id = ?', (cb_winid,))
			connection.commit()
			ch = types.InlineKeyboardMarkup(row_width=1)
			ch.add(
			types.InlineKeyboardButton(text='Забрать выигрыш', url=f'https://t.me/MegaBetRobot?start=_{cb_winid}_'),
			types.InlineKeyboardButton(text='Поставить ставку', url='http://t.me/send?start=IVeH7bZj20R2'))
			if summa >= 1.25:
				try:
					await crypto.transfer(spend_id=ran, user_id=cb_winid, amount=summa, asset='USDT')
					await bot.send_photo(chat_id=CHANNEL_ID, photo=open('menshe.png', 'rb'), caption=f"Победа! Выпало значение меньше [{chetcheck}]\n\n<blockquote>\nНа ваш кошелек зачислено {summa} USDT. Ставь и выигрывай!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", parse_mode='HTML')
				except Exception as ehh:
					print(ehh)
					await bot.send_photo(chat_id=CHANNEL_ID, photo=open('menshe.png', 'rb'), caption=f"Победа! Выпало значение меньше [{chetcheck}]\n\n<blockquote>\nНа ваш кошелек будет {summa} USDT зачислено  администратором. Ставь и выигрывай!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa, parse_mode='HTML')
			else:
				await bot.send_photo(chat_id=CHANNEL_ID, photo=open('menshe.png', 'rb'), caption=f"Победа! Выпало значение меньше [{chetcheck}]\n\n<blockquote>\nВаш выигрыш {summa} USDT создан в чеке. Заберите по кнопке ниже.</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=ch, parse_mode='HTML')
		else:
			await bot.send_photo(chat_id=CHANNEL_ID, photo=open('lose.png', 'rb'), caption=f"Вы проиграли! Выпало значение больше [{chetcheck}]\n\n<blockquote>Сыграйте еще раз, попробуйте испытать удачу и выиграть!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa)
			q.execute(f'UPDATE stats SET loses = {los + 1} WHERE tabas = ?', ('statistic',))
			bab = float(loses) + float(summ)
			q.execute(f'UPDATE user SET loses = "{bab}" WHERE user_id = ?', (cb_winid,))
			connection.commit()
			try:
				ref_balance = q.execute("SELECT balance from reg where user_id = ?", (ref_id,)).fetchone()
				ref_balance = f"{ref_balance}".replace('(', '').replace(')', '').replace(',', '')
				bol = float(ref_balance) + float(sum_value)*5/100
				q.execute(f'UPDATE reg SET balance = "{bol}" WHERE user_id = ?', (ref_id,))
				connection.commit()
				await bot.send_message(ref_id, f"🔥 ТВОЙ РЕФЕРАЛ ПРОИГРАЛ {summ}$\n🔑 Вы получили {bol}$ (5%)")
				print(ref_balance)
			except Exception as bp:
				print(bp)
				pass
		nb
	summa = float(sum_value)
	otvetv = msga[2]
	otvetv = otvetv[:1]
	aavt = msga[2]
	texte = msga[1]
	textev = msga[2]
	if msgas in texts:
		msg = await bot.send_dice(CHANNEL_ID)
		chetcheck = int(msg.dice.value)
		chetsh = int(chetcheck)
		if chetcheck == 1:
			chetcheck = 'н'
		if chetcheck == 2:
			chetcheck = 'ч'
		if chetcheck == 3:
			chetcheck = 'н'
		if chetcheck == 4:
			chetcheck = 'ч'
		if chetcheck == 5:
			chetcheck = 'н'
		if chetcheck == 6:
			chetcheck = 'ч'
		print(chetcheck)
		otvex = otvetv[:1]
		if "м" in otvetv:
			fullochered = int(fullochered) - 1
			f = open('очередь.txt', 'w')
			f.write(f"{fullochered}")
			f.close()
			if chetsh == 4:
				stata = 'lose'
			if chetsh == 5:
				stata = 'lose'
			if chetsh == 6:
				stata = 'lose'
			if chetsh == 1:
				stata = 'win'
			if chetsh == 2:
				stata = 'win'
			if chetsh == 3:
				stata = 'win'
			if stata == 'win':
				vuplach = float(summ) * 1.7  + float(vuplas)
				q.execute(f'UPDATE stats SET wins = {win + 1} WHERE tabas = ?', ('statistic',))
				q.execute(f'UPDATE stats SET thestb = "{vuplach}" WHERE tabas = ?', ('statistic',))
				await asyncio.sleep(3)
				q.execute(f'UPDATE users SET status = "win" WHERE user_id = ?', (cb_winid,))
				print(summa)
				summa = float(summa)*1.7
				bab = float(wins) + float(summa)
				q.execute(f'UPDATE user SET wins = "{bab}" WHERE user_id = ?', (cb_winid,))
				connection.commit()
				q.execute(f'UPDATE users SET summa = "{summa}" WHERE user_id = ?', (cb_winid,))
				connection.commit()
				ch = types.InlineKeyboardMarkup(row_width=1)
				ch.add(
				types.InlineKeyboardButton(text='Забрать выигрыш', url=f'https://t.me/MegaBetRobot?start=_{cb_winid}_'),
				types.InlineKeyboardButton(text='Поставить ставку', url='http://t.me/send?start=IVeH7bZj20R2'))
				if summa >= 1.25:
					try:
						await crypto.transfer(spend_id=ran, user_id=cb_winid, amount=summa, asset='USDT')
						await bot.send_photo(chat_id=CHANNEL_ID, photo=open('menshe.png', 'rb'), caption=f"Победа!\n\n<blockquote>\nНа ваш кошелек зачислено {summa} USDT. Ставь и выигрывай!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", parse_mode='HTML')
					except Exception as ehh:
						print(ehh)
						await msg.reply(f"Победа!\n\n<blockquote>\nНа ваш кошелек будет {summa} USDT зачислено администратором. Ставь и выигрывай!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa, parse_mode='HTML')
				else:
					await msg.reply(f"Победа!\n\n<blockquote>\nВаш выигрыш {summa} USDT создан в чеке. Заберите по кнопке ниже.</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=ch, parse_mode='HTML')
				f = open('акция.txt', 'r')
				akce = f.read()
				akce = f"{akce}".split(":")
				akc2 = akce[0]
				akc = akce[1]
				f.close()
				if stavka > float(akc):
					wineds = q.execute(f"SELECT wined from wins where user_id = ?", (cb_winid,)).fetchone()
					wineds = int(wineds[0])
					wineds2 = int(wineds) + 1
					q.execute(f'UPDATE wins SET wined = "{wineds2}" WHERE user_id = ?', (cb_winid,))
					connection.commit()
				winwin
			if stata == 'lose':
				q.execute(f'UPDATE stats SET loses = {los + 1} WHERE tabas = ?', ('statistic',))
				ref_id = q.execute(f"SELECT ref_id from reg where user_id = ?", (cb_winid,)).fetchone()
				ref_id = str(ref_id[0])
				if ref_id == "":
					pass
				else:
					print(ref_id)
					try:
						ref_balance = q.execute("SELECT balance from reg where user_id = ?", (ref_id,)).fetchone()
						ref_balance = f"{ref_balance}".replace('(', '').replace(')', '').replace(',', '')
						bol = float(ref_balance) + float(sum_value)*5/100
						q.execute(f'UPDATE reg SET balance = "{bol}" WHERE user_id = ?', (ref_id,))
						connection.commit()
						await bot.send_message(ref_id, f"<b>⚡ На ваш баланс зачислено 5 процентов от проигранной ставки реферала.</b>")
						print(ref_balance)
					except Exception as bp:
						print(bp)
						pass
				await msg.reply(f"Вы проиграли!\n\n<blockquote>Сыграйте еще раз, попробуйте испытать удачу и выиграть!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa)
				bab = float(loses) + float(summ)
				q.execute(f'UPDATE user SET loses = "{bab}" WHERE user_id = ?', (cb_winid,))
				connection.commit()
				q.execute(f'UPDATE wins SET wined = "0" WHERE user_id = ?', (cb_winid,))
				connection.commit()
				loselose
		if "б" in otvetv:
			fullochered = int(fullochered) - 1
			f = open('очередь.txt', 'w')
			f.write(f"{fullochered}")
			f.close()
			if chetsh == 4:
				stata = 'win'
			if chetsh == 5:
				stata = 'win'
			if chetsh == 6:
				stata = 'win'
			if chetsh == 1:
				stata = 'lose'
			if chetsh == 2:
				stata = 'lose'
			if chetsh == 3:
				stata = 'lose'
			if stata == 'win':
				await asyncio.sleep(3)
				q.execute(f'UPDATE users SET status = "win" WHERE user_id = ?', (cb_winid,))
				print(summa)
				summa = float(summa)*1.7
				vuplach = float(summ) * 1.7  + float(vuplas)
				q.execute(f'UPDATE stats SET wins = {win + 1} WHERE tabas = ?', ('statistic',))
				q.execute(f'UPDATE stats SET thestb = "{vuplach}" WHERE tabas = ?', ('statistic',))
				q.execute(f'UPDATE users SET summa = "{summa}" WHERE user_id = ?', (cb_winid,))
				connection.commit()
				bab = float(wins) + float(summa)
				q.execute(f'UPDATE user SET wins = "{bab}" WHERE user_id = ?', (cb_winid,))
				connection.commit()
				ch = types.InlineKeyboardMarkup(row_width=1)
				ch.add(
				types.InlineKeyboardButton(text='Забрать выигрыш', url=f'https://t.me/MegaBetRobot?start=_{cb_winid}_'),
				types.InlineKeyboardButton(text='Поставить ставку', url='http://t.me/send?start=IVeH7bZj20R2'))
				if summa >= 1.25:
					try:
						await crypto.transfer(spend_id=ran, user_id=cb_winid, amount=summa, asset='USDT')
						await msg.reply(f"Победа!\n\n<blockquote>\nНа ваш кошелек зачислено {summa} USDT. Ставь и выигрывай!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa, parse_mode='HTML')
					except:
						await msg.reply(f"Победа!\n\n<blockquote>\nНа ваш кошелек будет {summa} USDT зачислено администратором. Ставь и выигрывай!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa, parse_mode='HTML')
				else:
					await msg.reply(f"Победа!\n\n<blockquote>\nВаш выигрыш {summa} USDT создан в чеке. Заберите по кнопке ниже.</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=ch, parse_mode='HTML')
				winwin
				f = open('акция.txt', 'r')
				akce = f.read()
				akce = f"{akce}".split(":")
				akc2 = akce[0]
				akc = akce[1]
				f.close()
				if stavka > float(akc):
					wineds = q.execute(f"SELECT wined from wins where user_id = ?", (cb_winid,)).fetchone()
					wineds = int(wineds[0])
					wineds2 = int(wineds) + 1
					q.execute(f'UPDATE wins SET wined = "{wineds2}" WHERE user_id = ?', (cb_winid,))
					connection.commit()
			if stata == 'lose':
				q.execute(f'UPDATE stats SET loses = {los + 1} WHERE tabas = ?', ('statistic',))
				ref_id = q.execute(f"SELECT ref_id from reg where user_id = ?", (cb_winid,)).fetchone()
				ref_id = str(ref_id[0])
				if ref_id == "":
					pass
				else:
					print(ref_id)
					try:
						ref_balance = q.execute("SELECT balance from reg where user_id = ?", (ref_id,)).fetchone()
						ref_balance = f"{ref_balance}".replace('(', '').replace(')', '').replace(',', '')
						bol = float(ref_balance) + float(sum_value)*5/100
						q.execute(f'UPDATE reg SET balance = "{bol}" WHERE user_id = ?', (ref_id,))
						connection.commit()
						await bot.send_message(ref_id, f"<b>⚡ На ваш баланс зачислено 5 процентов от проигранной ставки реферала.</b>")
						print(ref_balance)
					except Exception as bp:
						print(bp)
						pass
				await bot.send_photo(chat_id=CHANNEL_ID, photo=open('lose.png', 'rb'), caption=f"Вы проиграли!\n\n<blockquote>Сыграйте еще раз, попробуйте испытать удачу и выиграть!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", parse_mode='HTML', reply_markup=otpa)
				bab = float(loses) + float(summ)
				q.execute(f'UPDATE user SET loses = "{bab}" WHERE user_id = ?', (cb_winid,))
				connection.commit()
				q.execute(f'UPDATE wins SET wined = "0" WHERE user_id = ?', (cb_winid,))
				connection.commit()
				oslsos
		fullochered = int(fullochered) - 1
		f = open('очередь.txt', 'w')
		f.write(f"{fullochered}")
		f.close()
		if chetcheck == otvex:
			await asyncio.sleep(3)
			q.execute(f'UPDATE users SET status = "win" WHERE user_id = ?', (cb_winid,))
			print(summa)
			summa = float(summa)*1.7
			q.execute(f'UPDATE users SET summa = "{summa}" WHERE user_id = ?', (cb_winid,))
			connection.commit()
			user_id = message.chat.id
			print(user_id)
			ch = types.InlineKeyboardMarkup(row_width=1)
			ch.add(
			types.InlineKeyboardButton(text='Забрать выигрыш', url=f'https://t.me/MegaBetRobot?start=_{cb_winid}_'),
			types.InlineKeyboardButton(text='Поставить ставку', url='http://t.me/send?start=IVeH7bZj20R2'))
			if summa >= 1.25:
				try:
					await crypto.transfer(spend_id=ran, user_id=cb_winid, amount=summa, asset='USDT')
					if msg.dice.value in [2,4,6]:
						await bot.send_photo(chat_id=CHANNEL_ID, photo=open('chet.png', 'rb'), caption=f"Победа!\n\n<blockquote>\nНа ваш кошелек зачислено {summa} USDT. Ставь и выигрывай!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", parse_mode='HTML', reply_markup=otpa)
					else:
						await msg.reply(f"Победа!\n\n<blockquote>\nНа ваш кошелек зачислено {summa} USDT. Ставь и выигрывай!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", parse_mode='HTML', reply_markup=otpa)
				except:
					await msg.reply(f"Победа!\n\n<blockquote>\nНа ваш кошелек будет {summa} USDT зачислено администратором. Ставь и выигрывай!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a>", reply_markup=otpa, parse_mode='HTML')
			else:
				await msg.reply(f"Победа!\n\n<blockquote>\nВаш выигрыш {summa} USDT создан в чеке. Заберите по кнопке ниже.</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=ch, parse_mode='HTML')
			f = open('акция.txt', 'r')
			akce = f.read()
			akce = f"{akce}".split(":")
			akc2 = akce[0]
			akc = akce[1]
			f.close()
			if stavka > float(akc):
				wineds = q.execute(f"SELECT wined from wins where user_id = ?", (cb_winid,)).fetchone()
				wineds = int(wineds[0])
				wineds2 = int(wineds) + 1
				q.execute(f'UPDATE wins SET wined = "{wineds2}" WHERE user_id = ?', (cb_winid,))
				connection.commit()
			print(msga[2])
		else:
				ref_id = q.execute(f"SELECT ref_id from reg where user_id = ?", (cb_winid,)).fetchone()
				ref_id = str(ref_id[0])
				if ref_id == "":
					pass
				else:
					print(ref_id)
					try:
						ref_balance = q.execute("SELECT balance from reg where user_id = ?", (ref_id,)).fetchone()
						ref_balance = f"{ref_balance}".replace('(', '').replace(')', '').replace(',', '')
						bol = float(ref_balance) + float(sum_value)*5/100
						q.execute(f'UPDATE reg SET balance = "{bol}" WHERE user_id = ?', (ref_id,))
						connection.commit()
						await bot.send_message(ref_id, f"<b>⚡ На ваш баланс зачислено 5 процентов от проигранной ставки реферала.</b>")
						print(ref_balance)
					except Exception as bp:
						print(bp)
						pass
				q.execute(f'UPDATE stats SET loses = {los + 1} WHERE tabas = ?', ('statistic',))
				await msg.reply(f"Вы проиграли!\n\n<blockquote>Сыграйте еще раз, попробуйте испытать удачу и выиграть!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa)
				bab = float(loses) + float(summ)
				q.execute(f'UPDATE user SET loses = "{bab}" WHERE user_id = ?', (cb_winid,))
				connection.commit()
				q.execute(f'UPDATE wins SET wined = "0" WHERE user_id = ?', (cb_winid,))
				connection.commit()
				print(msga[2])
	momb = message.text.split('💬 ')
	momb2 = momb[1]
	momb23 = momb2[:1]
	print(momb2)
	boba = ["Футбол", "фут", "футбол", "футик", "футбо", "ф","Ф", "Фут"]
	boul = ["Боулинг", "боулинг", "Боул", "боул", "Б", "б"]
	momb3 = f"{momb2}".split()
	momb3 = momb3[1]
	dota = message.text.split('💬 ')
	dota = momb[1]
	dota = f"{momb}".split(' ')
	mambo = momb[1]
	print(mambo)
	boulo = ["Боулинг", "боул", "Боул", "боулинг"]
	if "Бо" in mambo:
		fullochered = int(fullochered) - 1
		f = open('очередь.txt', 'w')
		f.write(f"{fullochered}")
		f.close()
		summa = float(summa)
		msg = await bot.send_dice(CHANNEL_ID,emoji='🎳')
		dedo = int(msg.dice.value)
		print(dedo)
		stavko = f"{mambo}".replace('Боул ', '').replace('боулинг ', '').replace('Боулинг', '').replace('боул ', '').replace('Боулинк ', '')
		if stavko >= "ст":
			chest = 6
		else:
			try:
				chest = int(stavko)
			except:
				chest = random.randint(1,6)
		if "," in stavko:
			if dedo in [chest]:
				await asyncio.sleep(3)
				q.execute(f'UPDATE users SET status = "win" WHERE user_id = ?', (cb_winid,))
				print(summa)
				sotavko = f"{stavko}".split(',')
				sotavko = sotavko[1]
				if sotavko == 6:
					summa = float(summa)*0.9
				else:
					summa = float(summa)*1.1
				bab = float(wins) + float(summa)
				q.execute(f'UPDATE user SET wins = "{bab}" WHERE user_id = ?', (cb_winid,))
				connection.commit()
				q.execute(f'UPDATE users SET summa = "{summa}" WHERE user_id = ?', (cb_winid,))
				connection.commit()
				user_id = message.chat.id
				print(user_id)
				ch = types.InlineKeyboardMarkup(row_width=1)
				ch.add(
				types.InlineKeyboardButton(text='Забрать выигрыш', url=f'https://t.me/MegaBetRobot?start=_{cb_winid}_'),
				types.InlineKeyboardButton(text='Поставить ставку', url='http://t.me/send?start=IVeH7bZj20R2'))
				if summa >= 1.25:
					await crypto.transfer(spend_id=ran, user_id=cb_winid, amount=summa, asset='USDT')
					await msg.reply(f"Победа!\n\n<blockquote>\nНа ваш кошелек зачислено {summa} USDT. Ставь и выигрывай!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa, parse_mode='HTML')
				else:
					await msg.reply(f"Победа!\n\n<blockquote>\nВаш выигрыш {summa} USDT создан в чеке. Заберите по кнопке ниже.</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=ch, parse_mode='HTML')
			else:
				ref_id = q.execute(f"SELECT ref_id from reg where user_id = ?", (cb_winid,)).fetchone()
				ref_id = str(ref_id[0])
				if ref_id == "":
					pass
				else:
					print(ref_id)
					try:
						ref_balance = q.execute("SELECT balance from reg where user_id = ?", (ref_id,)).fetchone()
						ref_balance = f"{ref_balance}".replace('(', '').replace(')', '').replace(',', '')
						bol = float(ref_balance) + float(sum_value)*5/100
						q.execute(f'UPDATE reg SET balance = "{bol}" WHERE user_id = ?', (ref_id,))
						connection.commit()
						await bot.send_message(ref_id, f"<b>⚡ На ваш баланс зачислено 5 процентов от проигранной ставки реферала.</b>")
						print(ref_balance)
					except Exception as bp:
						print(bp)
						pass
				await msg.reply(f"Вы проиграли!\n\n<blockquote>Сыграйте еще раз, попробуйте испытать удачу и выиграть!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa)
				bab = float(loses) + float(summ)
				q.execute(f'UPDATE user SET loses = "{bab}" WHERE user_id = ?', (cb_winid,))
				connection.commit()
		dedo = dedo / chest
		if dedo == chest:
			await asyncio.sleep(3)
			q.execute(f'UPDATE users SET status = "win" WHERE user_id = ?', (cb_winid,))
			print(summa)
			if dedo == 6:
				summa = float(summa)*1.7
			if "," in stavko:
				summa = float(summa)*1.1
			else:
				summa = float(summa)*1.4
			q.execute(f'UPDATE users SET summa = "{summa}" WHERE user_id = ?', (cb_winid,))
			connection.commit()
			user_id = message.chat.id
			print(user_id)
			ch = types.InlineKeyboardMarkup(row_width=1)
			ch.add(
			types.InlineKeyboardButton(text='Забрать', url=f'https://t.me/MegaBetRobot?start=_{cb_winid}_'))
			if summa >= 1.25:
				await crypto.transfer(spend_id=ran, user_id=cb_winid, amount=summa, asset='USDT')
				await msg.reply(f"Победа!\n\n<blockquote>\nНа ваш кошелек зачислено {summa} USDT. Ставь и выигрывай!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa, parse_mode='HTML')
			else:
				await msg.reply(f"Победа!\n\n<blockquote>\nВаш выигрыш {summa} USDT создан в чеке. Заберите по кнопке ниже.</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=ch, parse_mode='HTML')
		else:
				ref_id = q.execute(f"SELECT ref_id from reg where user_id = ?", (cb_winid,)).fetchone()
				ref_id = str(ref_id[0])
				if ref_id == "":
					pass
				else:
					print(ref_id)
					try:
						ref_balance = q.execute("SELECT balance from reg where user_id = ?", (ref_id,)).fetchone()
						ref_balance = f"{ref_balance}".replace('(', '').replace(')', '').replace(',', '')
						bol = float(ref_balance) + float(sum_value)*5/100
						q.execute(f'UPDATE reg SET balance = "{bol}" WHERE user_id = ?', (ref_id,))
						connection.commit()
						await bot.send_message(ref_id, f"<b>⚡ На ваш баланс зачислено 5 процентов от проигранной ставки реферала.</b>")
						print(ref_balance)
					except Exception as bp:
						print(bp)
						pass
				await msg.reply(f"Вы проиграли!\n\n<blockquote>Сыграйте еще раз, попробуйте испытать удачу и выиграть!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa)
				bab = float(loses) + float(summ)
				q.execute(f'UPDATE user SET loses = "{bab}" WHERE user_id = ?', (cb_winid,))
				connection.commit()
	if msgasa in baab:
		fullochered = int(fullochered) - 1
		f = open('очередь.txt', 'w')
		f.write(f"{fullochered}")
		f.close()
		summa = float(summa)*1.6
		msg = await bot.send_dice(CHANNEL_ID)
		chetcheck = int(msg.dice.value)
		msg2 = await bot.send_dice(CHANNEL_ID)
		chetcheck2 = int(msg2.dice.value)
		aavt = int(aavt)
		await asyncio.sleep(2)
		if aavt == 1:
			if chetcheck > chetcheck2:
				q.execute(f'UPDATE users SET summa = "{summa}" WHERE user_id = ?', (cb_winid,))
				connection.commit()
				user_id = message.chat.id
				print(user_id)
				ch = types.InlineKeyboardMarkup(row_width=1)
				ch.add(
				types.InlineKeyboardButton(text='Забрать выигрыш', url=f'https://t.me/MegaBetRobot?start=_{cb_winid}_'),
				types.InlineKeyboardButton(text='Поставить ставку', url='http://t.me/send?start=IVeH7bZj20R2'))
				bab = float(wins) + float(summa)
				q.execute(f'UPDATE user SET wins = "{bab}" WHERE user_id = ?', (cb_winid,))
				connection.commit()
				if summa >= 1.25:
				    await bot.send_photo(chat_id=CHANNEL_ID, photo=open('pobeda1.png', 'rb'), caption=f"Победа! [{chetcheck}:{chetcheck2}]\n\n<blockquote>\nНа ваш кошелек зачислено {summa} USDT. Ставь и выигрывай!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa, parse_mode='HTML')
				    await crypto.transfer(spend_id=ran, user_id=cb_winid, amount=summa, asset='USDT')
				else:
					await bot.send_photo(chat_id=CHANNEL_ID, photo=open('pobeda1.png', 'rb'), caption=f"Победа! [{chetcheck}:{chetcheck2}]\n\n<blockquote>\nВаш выигрыш {summa} USDT создан в чеке. Заберите по кнопке ниже.</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=ch, parse_mode='HTML')
					ksks
			else:
				ref_id = q.execute(f"SELECT ref_id from reg where user_id = ?", (cb_winid,)).fetchone()
				ref_id = str(ref_id[0])
				if ref_id == "":
					pass
				else:
					print(ref_id)
					try:
						ref_balance = q.execute("SELECT balance from reg where user_id = ?", (ref_id,)).fetchone()
						ref_balance = f"{ref_balance}".replace('(', '').replace(')', '').replace(',', '')
						bol = float(ref_balance) + float(sum_value)*5/100
						q.execute(f'UPDATE reg SET balance = "{bol}" WHERE user_id = ?', (ref_id,))
						connection.commit()
						await bot.send_message(ref_id, f"<b>⚡ На ваш баланс зачислено 5 процентов от проигранной ставки реферала.</b>")
						print(ref_balance)
					except Exception as bp:
						print(bp)
						pass
				await bot.send_photo(chat_id=CHANNEL_ID, photo=open('pobeda2.png', 'rb'), caption=f"Вы проиграли! [{chetcheck}:{chetcheck2}]\n\n<blockquote>Сыграйте еще раз, попробуйте испытать удачу и выиграть!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa)
				bab = float(loses) + float(summ)
				q.execute(f'UPDATE user SET loses = "{bab}" WHERE user_id = ?', (cb_winid,))
				connection.commit()
				ekekek
		if aavt == 2:
			if chetcheck2 > chetcheck:
				q.execute(f'UPDATE users SET summa = "{summa}" WHERE user_id = ?', (cb_winid,))
				connection.commit()
				user_id = message.chat.id
				print(user_id)
				ch = types.InlineKeyboardMarkup(row_width=1)
				ch.add(
				types.InlineKeyboardButton(text='Забрать выигрыш', url=f'https://t.me/MegaBetRobot?start=_{cb_winid}_'),
				types.InlineKeyboardButton(text='Поставить ставку', url='http://t.me/send?start=IVeH7bZj20R2'))
				if summa >= 1.25:
				    	await bot.send_photo(chat_id=CHANNEL_ID, photo=open('pobeda2.png', 'rb'), caption=f"Победа! [{chetcheck2}:{chetcheck}]\n\n<blockquote>\nНа ваш кошелек зачислено {summa} USDT. Ставь и выигрывай!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa, parse_mode='HTML')
				    	await crypto.transfer(spend_id=ran, user_id=cb_winid, amount=summa, asset='USDT')
				else:
					await bot.send_photo(chat_id=CHANNEL_ID, photo=open('pobeda2.png', 'rb'), caption=f"Победа! [{chetcheck2}:{chetcheck}]\n\n<blockquote>\nВаш выигрыш {summa} USDT создан в чеке. Заберите по кнопке ниже.</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=ch, parse_mode='HTML')
					wkdd
			else:
				ref_id = q.execute(f"SELECT ref_id from reg where user_id = ?", (cb_winid,)).fetchone()
				ref_id = str(ref_id[0])
				if ref_id == "":
					pass
				else:
					print(ref_id)
					try:
						ref_balance = q.execute("SELECT balance from reg where user_id = ?", (ref_id,)).fetchone()
						ref_balance = f"{ref_balance}".replace('(', '').replace(')', '').replace(',', '')
						bol = float(ref_balance) + float(sum_value)*5/100
						q.execute(f'UPDATE reg SET balance = "{bol}" WHERE user_id = ?', (ref_id,))
						connection.commit()
						await bot.send_message(ref_id, f"<b>⚡ На ваш баланс зачислено 5 процентов от проигранной ставки реферала.</b>")
						print(ref_balance)
					except Exception as bp:
						print(bp)
						pass
				await bot.send_photo(chat_id=CHANNEL_ID, photo=open('pobeda1.png', 'rb'), caption=f"Вы проиграли! [{chetcheck2}:{chetcheck}]\n\n<blockquote>Сыграйте еще раз, попробуйте испытать удачу и выиграть!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa)
				bab = float(loses) + float(summ)
				q.execute(f'UPDATE user SET loses = "{bab}" WHERE user_id = ?', (cb_winid,))
				connection.commit()
				ks
	mimo = ["м", "Мимо", "мимо"]
	if texte in basket:
		fullochered = int(fullochered) - 1
		f = open('очередь.txt', 'w')
		f.write(f"{fullochered}")
		f.close()
		basc = await bot.send_dice(CHANNEL_ID,emoji='🏀')
		values = basc.dice.value
		print(values)
		tdata = message.text.split('💬 ')
		tdata = tdata[1].split(' ')
		txt = tdata[1]
		print(txt)
		if "м" in txt:
			if values in [1,2,3]:
				await asyncio.sleep(3)
				q.execute(f'UPDATE users SET status = "win" WHERE user_id = ?', (cb_winid,))
				print(summa)
				summa = float(summa)*1.3
				bab = float(wins) + float(summa)
				q.execute(f'UPDATE user SET wins = "{bab}" WHERE user_id = ?', (cb_winid,))
				connection.commit()
				q.execute(f'UPDATE users SET summa = "{summa}" WHERE user_id = ?', (cb_winid,))
				connection.commit()
				user_id = message.chat.id
				print(user_id)
				ch = types.InlineKeyboardMarkup(row_width=1)
				ch.add(
				types.InlineKeyboardButton(text='Забрать выигрыш', url=f'https://t.me/MegaBetRobot?start=_{cb_winid}_'),
				types.InlineKeyboardButton(text='Поставить ставку', url='http://t.me/send?start=IVeH7bZj20R2'))
				f = open('акция.txt', 'r')
				akce = f.read()
				akce = f"{akce}".split(":")
				akc2 = akce[0]
				akc = akce[1]
				f.close()
				if summa >= 1.25:
				    	await crypto.transfer(spend_id=ran, user_id=cb_winid, amount=summa, asset='USDT')
				    	await basc.reply(f"Победа!\n\n<blockquote>\nНа ваш кошелек зачислено {summa} USDT. Ставь и выигрывай!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa, parse_mode='HTML')
				else:
					await basc.reply(f"Победа!\n\n<blockquote>\nВаш выигрыш {summa} USDT создан в чеке. Заберите по кнопке ниже.</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=ch, parse_mode='HTML')
			else:
				ref_id = q.execute(f"SELECT ref_id from reg where user_id = ?", (cb_winid,)).fetchone()
				ref_id = str(ref_id[0])
				if ref_id == "":
					pass
				else:
					print(ref_id)
					try:
						ref_balance = q.execute("SELECT balance from reg where user_id = ?", (ref_id,)).fetchone()
						ref_balance = f"{ref_balance}".replace('(', '').replace(')', '').replace(',', '')
						bol = float(ref_balance) + float(sum_value)*5/100
						q.execute(f'UPDATE reg SET balance = "{bol}" WHERE user_id = ?', (ref_id,))
						connection.commit()
						await bot.send_message(ref_id, f"<b>⚡ На ваш баланс зачислено 5 процентов от проигранной ставки реферала.</b>")
						print(ref_balance)
					except Exception as bp:
						print(bp)
						pass
				await basc.reply(f"Вы проиграли!\n\n<blockquote>Сыграйте еще раз, попробуйте испытать удачу и выиграть!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa)
				q.execute(f'UPDATE wins SET wined = "0" WHERE user_id = ?', (cb_winid,))
				connection.commit()
				bab = float(loses) + float(summ)
				q.execute(f'UPDATE user SET loses = "{bab}" WHERE user_id = ?', (cb_winid,))
				connection.commit()
		if "по" in txt:
			if values in [4,5]:
				await asyncio.sleep(3)
				q.execute(f'UPDATE users SET status = "win" WHERE user_id = ?', (cb_winid,))
				print(summa)
				summa = float(summa)*1.3
				q.execute(f'UPDATE users SET summa = "{summa}" WHERE user_id = ?', (cb_winid,))
				connection.commit()
				user_id = message.chat.id
				print(user_id)
				ch = types.InlineKeyboardMarkup(row_width=1)
				bab = float(wins) + float(summa)
				q.execute(f'UPDATE user SET wins = "{bab}" WHERE user_id = ?', (cb_winid,))
				connection.commit()
				ch.add(
				types.InlineKeyboardButton(text='Забрать', url=f'https://t.me/MegaBetRobot?start=_{cb_winid}_'))
				f = open('акция.txt', 'r')
				akce = f.read()
				akce = f"{akce}".split(":")
				akc2 = akce[0]
				akc = akce[1]
				f.close()
				if summa >= 1.25:
				    	await crypto.transfer(spend_id=ran, user_id=cb_winid, amount=summa, asset='USDT')
				    	await msg.reply(f"Победа!\n\n<blockquote>\nНа ваш кошелек зачислено {summa} USDT. Ставь и выигрывай!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa, parse_mode='HTML')
				else:
					await basc.reply(f"Победа!\n\n<blockquote>\nВаш выигрыш {summa} USDT создан в чеке. Заберите по кнопке ниже.</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=ch, parse_mode='HTML')
			else:
				ref_id = q.execute(f"SELECT ref_id from reg where user_id = ?", (cb_winid,)).fetchone()
				ref_id = str(ref_id[0])
				if ref_id == "":
					pass
				else:
					print(ref_id)
					try:
						ref_balance = q.execute("SELECT balance from reg where user_id = ?", (ref_id,)).fetchone()
						ref_balance = f"{ref_balance}".replace('(', '').replace(')', '').replace(',', '')
						bol = float(ref_balance) + float(sum_value)*5/100
						q.execute(f'UPDATE reg SET balance = "{bol}" WHERE user_id = ?', (ref_id,))
						connection.commit()
						await bot.send_message(ref_id, f"<b>⚡ На ваш баланс зачислено 5 процентов от проигранной ставки реферала.</b>")
						print(ref_balance)
					except Exception as bp:
						print(bp)
						pass
				await basc.reply(f"Вы проиграли!\n\n<blockquote>Сыграйте еще раз, попробуйте испытать удачу и выиграть!</blockquote>\n\n<a href='https://t.me/clashbetperexod'>Переходник</a> | <a href='https://t.me/+7USe1PP4ApQ5NzFk'>Новостной канал</a> | <a href='https://t.me/c/2066075762/2'>Правила</a>", reply_markup=otpa)
				bab = float(loses) + float(summ)
				q.execute(f'UPDATE user SET loses = "{bab}" WHERE user_id = ?', (cb_winid,))
				connection.commit()
				q.execute(f'UPDATE wins SET wined = "0" WHERE user_id = ?', (cb_winid,))
				connection.commit()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

import sqlite3

conn = sqlite3.connect("wish_service.db")
cursor = conn.cursor()

def new_name():
	res = []
	name = input("Input your name - ")
	active = int(input("Input active status \n"\
		"Yes (1) \n"\
		"No (0) \n"))
	if active == 0 or active == 1:
		res.append(name.capitalize());res.append(active)
		cursor.execute("""INSERT INTO wishes(name, active) VALUES (?,?);""", res)
		conn.commit()
		print("Succsessful!")
	else:
		print("Error!")


def update_name():
	cursor.execute("""SELECT name FROM wishes""")
	lists_info = cursor.fetchall()
	print(lists_info)
	name_id = int(input(f"Input name position from 1 to {len(lists_info)}: "))
	name = input("Input new name for upadate - ")
	if name_id > 0 and name_id <= len(lists_info):
		cursor.execute("""UPDATE wishes SET name = (?) WHERE id = (?);""", (name.capitalize(), name_id))
		conn.commit()
		print("Succsessful!")
	else:
		print("Error!")


def update_active_status():
	cursor.execute("""SELECT name, active  FROM wishes""")
	lists_info = cursor.fetchall()
	print(lists_info)
	active_id = int(input(f"Input active status position from 1 to {len(lists_info)}: "))
	active = int(input("Input new active status for upadate - "))
	if active_id > 0 and active_id <= len(lists_info) and (active == 1 or active == 0):
		cursor.execute("""UPDATE wishes SET active = (?) WHERE id = (?);""", (active, active_id))
		conn.commit()
		print("Succsessful!")
	else:
		print("Error!")


def update_all():
	cursor.execute("""SELECT name, active  FROM wishes""")
	lists_info = cursor.fetchall()
	print(lists_info)
	position = int(input(f"Input datas position from 1 to {len(lists_info)}: "))
	name = input("Input new name for upadate - ")
	active = int(input("Input new active status for upadate - "))
	if position > 0 and position <= len(lists_info) and (active == 1 or active == 0):
		cursor.execute("""UPDATE wishes SET active = (?) WHERE id = (?);""", (active, position))
		cursor.execute("""UPDATE wishes SET name = (?) WHERE id = (?);""", (name.capitalize(), position))
		conn.commit()
		print("Succsessful!")
	else:
		print("Error!")


def delete():
	cursor.execute("""SELECT name, active FROM wishes""")
	lists_info = cursor.fetchall()
	print(lists_info)
	position = int(input(f"Input from 1 to {len(lists_info)} which datas do you want delete - "))
	if position > 0 and position <= len(lists_info):
		cursor.execute("""DELETE FROM wishes WHERE id = (?);""", (position,))
		conn.commit()
		print("Succsessful!")
	else:
		print("Error!")

def show():
	cursor.execute("""SELECT id FROM wishes""")
	lists_info = cursor.fetchall()
	position = int(input(f"Input position from 1 to {len(lists_info)} which you want see - "))
	if position > 0 and position <= len(lists_info):
		cursor.execute("""SELECT name, active FROM wishes WHERE id = (?);""", (position,))
		show = cursor.fetchall()
		print(show)
	else:
		print("Error!")

def show_all():
	cursor.execute("""SELECT name, active FROM wishes""")
	print(cursor.fetchall())
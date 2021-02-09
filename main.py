# Создать таблицу wishes с полями id, name, active
# Создать функции : По добавлению – редактированию – удалению – получению по ID – получение активных списка желаний
import second

def main():

	while True:
		action = input("Input your action \n"\
			"New Data (n) \n"\
			"Update Data (u) \n"\
			"Delete Data (d) \n"\
			"Show Data (s)\n"\
			"Exit Program (e) \n")

		if action.lower() == "n":
			second.new_name()
		elif action.lower() == "u":
			action = input("What you want update \n"\
				"Name (n) \n"\
				"Active Status (a) \n"\
				"All (all) \n")
			if action.lower() == "n":
				second.update_name()
			elif action.lower() == "a":
				second.update_active_status()
			elif action.lower() == "all":
				second.update_all()
			else:
				print("Error!")
		elif action.lower() == "d":
			second.delete()
		elif action.lower() == "s":
			action = input("Input action \n"\
				"show all (sa) \n"\
				"show with id (si)")
			if action == "sa":
				second.show_all()
			elif action == "si":
				second.show()
			else:
				print("Error!")
		elif action.lower() == "e":
			break
		else:
			print("Error!")
main()
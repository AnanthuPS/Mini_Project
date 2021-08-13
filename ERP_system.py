print("ERP System using Dictionary")
print("---------------------------")

emp = {}
while True:
	print("1.Add Employee")
	print("2.Delete Employee")
	print("3.Search Employee")
	print("4.Change Employee Data")
	print("5.Display Employee")
	print("6.Exit")

	ch = int(input("Enter your choice : "))
	if ch == 1:
		#Add Employee
		serial_no = int(input("\tEnter the serial number : "))

		if serial_no not in emp.keys():
			emp_id = int(input("\tEnter the employee ID : "))
			name = input("\tEnter name : ")
			age = int(input("\tEnter the age : "))
			gender = input("\tEnter the gender : ")
			place = input("\tEnter the place : ")
			salary = int(input("\tEnter the salary : "))
			prev_cmp = input("\tEnter the name of previous company : ")
			date = input("\tEnter the joining date : ")

			temp = {
				"emp_id":emp_id,
				"name":name,
				"age":age,
				"gender":gender,
				"place":place,
				"salary":salary,
				"prev_cmp":prev_cmp,
				"date":date
				}

			emp[serial_no] = temp

		else:
			print("\tSerial number already in the dictionary!!!")

	elif ch == 2:
		#Delete Employee
		print(emp)
		print("\tChoose serial num of employee for deletion ")
		serial = int(input("\tEnter serial num to delete : "))
		if serial in emp.keys():
			del emp[serial]
		else:
			print(f"\t{serial} not in the dictionary")

	elif ch == 3:
		#Search Employee
		name = input("\tEnter name you want to search : ")
		found = False
		for i in emp.values():
			if i["name"] == name:
				print(f"\t{i['emp_id']} | {i['name']} | {i['age']} | {i['gender']} | {i['place']} | {i['salary']} | {i['prev_cmp']} | {i['date']}")
				found = True
				break
		if found == False:
			print("\tData not found")


	elif ch == 4:
                #Change a Employee data
		print("1  .Change name")
		print("2  .change age")
		print("3  .Change gender")
		print("4  .change salary")
		choice = int(input("/tenter your choice : "))
		if choice == 1:
			serial_no = int(input("\tEnter serial number :"))
			if serial_no not in emp.keys():
				print("\twrong employee no")
			else:
				emp[serial_no]['name'] = input("\tEnter new name")  
		elif choice == 2:
			serial_no = int(input("\tEnter serial number :"))
			if serial_no not in emp.keys():
				print("\twrong employee no")
			else:
				emp[serial_no]['age'] = input("\tEnter new age")  
		elif choice == 3:
			serial_no = int(input("\tEnter serial number :"))
			if serial_no not in emp.keys():
				print("\twrong employee no")
			else:
				emp[serial_no]['gender'] = input("\tEnter new gender")
		elif choice == 4:
			serial_no = int(input("\tEnter serial number :"))
			if serial_no not in emp.keys():
				print("\twrong employee no")
			else:
				emp[serial_no]['salary'] = input("\tEnter new salary")


	elif ch == 5:
		#Display Employee
		for serial,empl in emp.items():
			print(f"\t{serial} | {empl['emp_id']} | {serial} | {empl['name']} | {empl['age']} | {empl['gender']} | {empl['place']} | {empl['salary']} | {empl['prev_cmp']} | | {empl['date']}")


	elif ch == 6:
		break

	else:
		print("Invalid Choice")

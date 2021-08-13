#Mini project console ERP system.


employees={}
def add_employee():
	employee_id = input("\tenter Employee id ")
	if employee_id not in employees.keys():
		name = input("\tEnter name : ")
		age = int(input("\tEnter age : "))
		gender = input("\tEnter the gender : ")
		place = input("\tEnter place : ")
		salary = int(input("\tEnter salary : "))
		previous_company = input("\tEnter your previous company : ")
		joining_date = input("\tEnter joining date : ")
		temp ={
			"name":name,
			"age":age,
			"gender":gender,
			"place":place,
			"salary":salary,
			"previous_company":previous_company,
			"joining_date":joining_date,
			}
		employees[employee_id] = temp
	else:
			print("\tEmployee id  already Taken")

def delete_employee():
	eid = int(input("\tEnter employee id : "))
	if eid not in employees.keys():
		print("\tWrong Employee id")
	else:
		del employees[employee_id]

def search_employee():
	name = input("\tEnter employee name : ")
	found = False
	for i in employees.values():
		if i["name"] == name: 
			print(f"\t{i['name']} | {i['age']} | {i['place']} | {i['gender']} | {i['previous_company']} | {i['salary']} ")
			found = True
			break
		if found==False:
			print("\tEmployee not in the list")

def display_employee():
	for id,employee in employees.items():
		print(f"\t{id} | {employee['name']} | {employee['age']} | {employee['place']} | {employee['gender']} | {employee['previous_company']} | {employee['salary']} ")

def change_employee():
	print("\t1.Change name")
	print("\t2.Change age")
	print("\t3.Change gender")
	print("\t4.Change salary")
	cho =int(input("\tEnter your choice : "))
	employee_id = input("\tEnter employee id : ")
	if cho == 1:
		employees[employee_id]['name'] = input("\tEnter new name : ") 
	elif cho == 2:
		employees[employee_id]['age'] = int(input("\tEnter new age : "))
	elif cho == 3:
		employees[employee_id]['gender'] = input("\tEnter gender : ")
	elif cho == 4:
		employees[employee_id]['salary'] = int(input("\tEnter new salary : "))
	else:
		print("Invalid choice")




while True:
	print("1.Add employee")
	print("2.Delete employee ")
	print("3.Search employee")
	print("4.Display  employee")
	print("5.Change employee details")
	print("6.Quit")
	ch = int(input("Enter your choice : "))
	if ch == 1:
	#adding employee
		add_employee()
			
	elif ch == 2:
	#delete
		delete_employee()
	elif ch == 3:
	#search
		search_employee()
	elif ch == 4:
	#display employee
		display_employee()
	elif ch== 5:
	#change employee details
		change_employee()
	elif ch == 6:
		break;
	else:
		print("Invalid Choice")




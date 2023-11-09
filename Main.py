tasks = []

#Function to display the to-do list

def display_tasks():
	if not tasks:
		print("No tasks in your to-do list.")
	else:
		print("To-do list:")
		for i, task in enumerate(tasks,start=1):
			print(f"{i}.{task}")
#Function to add a task to the list
def add_task():
	task = input("Enter the task: ")
	tasks.append(task)
	print(f"Task '{task}' added to the to-do list.")

#main program loop
while True:
	print("1. Display to-do list")
	print("2. Add a task")
	print("4. Quit")

	choice = input("Enter your choice: ")

	if choice == '1':
		display_tasks()
	elif choice == '2': 
		add_task()
	elif choice == '4':
		print("Goodbye!")
		break
	else: 
		print("Invalid choice. Please select a valid option")
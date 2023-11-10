import os

tasks = []

#Function to clear the screen
def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

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

#Function to remove a task from the list 
def remove_task():
	display_tasks()
	try:
		task_number = int(input("Enter the task number to remove: "))
		if 1 <= task_number <= len(tasks):
			removed_task = tasks.pop(task_number-1)
			print(f"Task '{removed_task}' removed from to-do list.")
		else: 
			print("Invalid task number. Please try again")
	except ValueError:
		print("Invalid input. Please enter a valid task number")
	
# Dictionary to map choices to functions
options = {
    '1': display_tasks,
    '2': add_task,
    '3': remove_task,
    '4': lambda: print("Goodbye!"),
}

#main program loop
while True:
	clear_screen()

	print("\nOptions:")
	print("1. Display to-do list")
	print("2. Add a task")
	print("3. Remove a task")
	print("4. Quit")
	
	choice = input("Enter your choice: ")

	if choice in options:
		if choice == '4':
			options[choice]()  # Execute the 'Quit' function
			break
		else:
			options[choice]()  # Execute the corresponding function
	else:
		print("Invalid choice. Please select a valid option.")

	input("Press Enter to continue...")
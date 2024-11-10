import datetime
import calendar
import os
from collections import deque, defaultdict
from expenses import Expenses
#Initializes the runner of the code
def main():
	print("Running expense tracker!")
	#Sets the variable expense_file_path equal to the csv file of all expenses
	expense_file_path = "expenses.csv"
	#Initializes the monthly budget of a user
	budget = check_or_set_budget(expense_file_path)
	
	# Initialize expenses as a queue to keep them in chronological order
	expenses = load_expenses_as_queue(expense_file_path)
	
	# Get user input for a new expense
	expense = get_user_expense()
	
	# Add the expense to the queue and save it to the file
	add_expense(expenses, expense, expense_file_path)

	# Summarize expenses based on the loaded data and the new expense
	summarize_expenses(expenses, budget)

#Gets the monthly budget of a user on the first use or the first of the month
def check_or_set_budget(expense_file_path):
	now = datetime.datetime.now()
	budget_file_path = "budget.txt"
	
	#Check if its the first day of the month, or the csv is empty
	is_first_day = now.day == 1
	is_csv_empty = not os.path.exists(expense_file_path) or os.path.getsize(expense_file_path) == 0
	
	#if either variables above are true, set up budget amount
	if is_first_day or is_csv_empty:
		print("Welcome! Setting up your budget for the month.")


		while True:
			try:
				#Gets the budget and saves it
				budget = float(input("Enter your budget for this month: "))
				with open(budget_file_path, "w") as f:
					f.write(str(budget))
				#Clears or creates a csv
				with open(expense_file_path, "w") as f:
					f.write("")  #Clears existing content a previously made csv
				print(f"Monthly budget set to ${budget:.2f}")
				break
			#If a non float value is input, request a new input
			except ValueError:
				print("Invalid input. Please enter a numeric value.")
	#If its not the first day or first use, read already made budget
	else:
		try:
			with open(budget_file_path, "r") as f:
				budget = float(f.read().strip())
			print(f"Using saved monthly budget: ${budget:.2f}")
		#if budget is not set, get the budget from the user
		except FileNotFoundError:
			print("No budget file found. Please set your budget.")
			budget = check_or_set_budget(expense_file_path) #Recursive call to receive the budget

	return budget

#Creates a queue named expenses to keep track of user expenses. Allows for easy access
def load_expenses_as_queue(expense_file_path):
	expenses = deque()
	'''
	Checks if a csv is already made. if not, returns empty queue. If it does, adds expense info to a queue
	'''
	if os.path.exists(expense_file_path):
		with open(expense_file_path, "r") as f:
			lines = f.readlines()
			for line in lines:
				expense_name, expense_amount, expense_category = line.strip().split(",")
				expense = Expenses(name=expense_name, category=expense_category, amount=float(expense_amount))
				expenses.append(expense)
	return expenses

#Adds expenses to the queue, and adds the information to the csv
def add_expense(expenses, expense, expense_file_path):
	expenses.append(expense)
	with open(expense_file_path, "a") as f:
		f.write(f"{expense.name},{expense.amount},{expense.category}\n")
	print(f"Expense saved: {expense}")

#Receives the user expenses
def get_user_expense():
	print("Getting User Expenses!")
	expense_name = input("Enter expense name: ").strip()

	#If the user inputs nothing, prompt again
	while not expense_name:
		print("Expense name cannot be empty.")
		expense_name = input("Enter expense name: ").strip()
	#Get the expense amount as a float, if an invalid input is entered, prompt user again
	while True:
		try:
			expense_amount = float(input("Enter expense amount: "))
			break
		except ValueError:
			print("Invalid amount. Please enter a numeric value.")

	#List of expenses
	expense_categories = ["Food", "Home", "Work", "Fun", "Misc"]

	#Get the category from the user, from 1-5
	while True:
		print("Select a Category: ")
		for i, category_name in enumerate(expense_categories, start=1):
			print(f"  {i}. {category_name}")
		#Make sure the input is valid
		try:
			#Make sure that the number is between 1-5
			selected_index = int(input(f"Enter a Category Number [1 - {len(expense_categories)}]: ")) - 1
			if selected_index not in range(len(expense_categories)):
				print("Selected number is not listed")
			else:
				#Create new expense object with all the information so far
				selected_category = expense_categories[selected_index]
				return Expenses(name=expense_name, category=selected_category, amount=expense_amount)
		#Prompt user to input new category if the input is not a number
		except ValueError:
			print("Input is not a number between 1-5")

#Summarizes expenses by month and category
def summarize_expenses(expenses, budget):
	print(f"Summarizing User Expense:")
	
	# Use defaultdict for efficient category-based expense aggregation
	amount_by_category = defaultdict(float)
	for expense in expenses:
		amount_by_category[expense.category] += expense.amount

	#Displays the expenses by category
	print("Expenses by Category:")
	for category, amount in amount_by_category.items():
		print(f"  {category}: ${amount:.2f}")

	#Displays the total spent for the month
	total_spent = sum(expense.amount for expense in expenses)
	print(f"Total Spent: ${total_spent:.2f}")

	#Displays the budget remaining for the month
	remaining_budget = budget - total_spent
	print(f"Budget Remaining: ${remaining_budget:.2f}")

	#Calculates the current date
	now = datetime.datetime.now()
	days_in_month = calendar.monthrange(now.year, now.month)[1]
	remaining_days = days_in_month - now.day

	#Calculates and displays the average budget per day, for the remaining days of the month
	daily_budget = remaining_budget / remaining_days if remaining_days > 0 else 0
	print(f"Budget Per Day:  ${daily_budget:.2f}")


if __name__ == "__main__":
	main()


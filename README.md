# Expense Tracker

## Overview
This is a simple expense tracker application built in Python. It helps users manage their monthly budget by tracking expenses and categorizing them. The program stores expenses in a CSV file, allowing users to add, categorize, and summarize their monthly spending.

## Features
- **Monthly Budget Setup**: Prompts the user to set a budget for the month if it’s the first day of the month or if it's the first time the program is used.
- **Expense Entry**: Allows users to input details about each expense, including the name, amount, and category.
- **Categorized Expense Summarization**: Provides a breakdown of spending by category and calculates the remaining budget for the month.
- **Persistent Storage**: Saves expenses in a CSV file to retain data across program runs.
- **Daily Budget Calculation**: Calculates the daily budget for the remaining days in the month based on the budget left.

## Setup and Requirements
This project requires Python 3.x. Ensure you have the following libraries installed:
- `datetime`
- `calendar`
- `os`
- `collections` (specifically, `deque` and `defaultdict`)

The `Expenses` class, which is part of the `expenses.py` module, should be available in the project directory.

## Usage

    Running expense tracker!
    
    Welcome! Setting up your budget for the month.
    
    Enter your budget for this month: 2000
    
    Monthly budget set to $2000.00
    
    Getting User Expenses!
    
    Enter expense name: Sushi
    
    Enter expense amount: 8
    
    Select a Category: 
      1. Food
      2. Home
      3. Work
      4. Fun
      5. Misc
    Enter a Category Number [1 - 5]: 1
    
    Expense saved: <Expense: Sushi,8.00,Food>

    Summarizing User Expense:
    
    Expenses by Category:
      Food: $8.00
      
    Total Spent: $8.00
    
    Budget Remaining: $1992.00

    Budget Per Day:  $99.60

## Future Work
To improve this code, I would like to allow users to create their own categories. This will make the program much more versatile and similar to a real expense tracker. I would also like to create a new CSV file each month. This will allow people to see a CSV of their purchases over time, not just during a monthly period. 

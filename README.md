# Personal Finance Tracker 💰

A simple yet powerful command-line application to track your personal finances, manage expenses, and visualize your financial data.

## Features ✨

- 📝 Add and track income and expenses
- 📊 View transaction history with date filtering
- 💹 Generate visual charts of income and expenses
- 📈 Calculate net savings and financial summaries
- 📅 Date-based transaction filtering
- 💾 Automatic data persistence using CSV storage

## Installation 🚀

1. Clone the repository:
```bash
git clone https://github.com/Rian-D/FinanceTracker.git
cd FinanceTracker
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage 📖

Run the application:
```bash
python main.py
```

### Main Menu Options:

1. **Add a new transaction**
   - Enter the date (dd-mm-yyyy)
   - Enter the amount
   - Specify if it's Income or Expense
   - Add an optional description

2. **View transactions and summary**
   - Filter transactions by date range
   - View detailed transaction list
   - See summary of income, expenses, and net savings
   - Generate visual charts of your financial data

3. **Exit**
   - Save and exit the application

## Data Storage 💾

- All transactions are stored in `data.csv`
- The file is automatically created when you add your first transaction
- Data is saved after each transaction entry

## Requirements 📋

- Python 3.x
- pandas >= 2.0.0
- matplotlib >= 3.7.0


## Future Improvements 🎯

- Budget management system
- Enhanced categorization with subcategories
- Data export/import functionality
- Advanced analytics and reporting
- Search and filter capabilities
- Recurring transactions support 

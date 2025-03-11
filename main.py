import os
import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = "data.csv"
DATE_FORMAT = "%d-%m-%Y"


def load_data():
    # Loads transaction data from CSV or creates an empty DataFrame if the file doesn't exist.
    if os.path.exists(FILE_PATH):
        return pd.read_csv(FILE_PATH, parse_dates=["Date"], dayfirst=True)
    return pd.DataFrame(columns=["Date", "Amount", "Category", "Description"])


def save_data(df):
    # Saves transaction data to CSV.
    df.to_csv(FILE_PATH, index=False)


def get_valid_date(prompt):
    # Prompts the user for a valid date input.
    while True:
        try:
            date_str = input(prompt)
            return pd.to_datetime(date_str, format=DATE_FORMAT)
        except ValueError:
            print("Invalid date format. Please enter the date in dd-mm-yyyy format.")


def get_valid_amount(prompt):
    # Prompts the user for a valid numerical amount input.
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid amount. Please enter a valid number.")


def add_transaction(df):
    # Adds a new transaction to the DataFrame.
    date = get_valid_date("Enter the date (dd-mm-yyyy): ")
    amount = get_valid_amount("Enter the amount: ")
    category = input("Is it an Income or an Expense? ").strip().title()
    description = input("Enter a short description (optional): ").strip()

    if category not in ["Income", "Expense"]:
        print("Invalid category. Please enter 'Income' or 'Expense'.")
        return df

    new_entry = pd.DataFrame([[date, amount, category, description]], columns=df.columns)
    df = pd.concat([df, new_entry], ignore_index=True)

    save_data(df)
    print("✅ Entry added successfully!")
    return df


def filter_transactions(df):
    # Filters transactions within a user-specified date range and prints summary.
    start_date = get_valid_date("Enter the start date (dd-mm-yyyy): ")
    end_date = get_valid_date("Enter the end date (dd-mm-yyyy): ")

    if start_date > end_date:
        print("⚠️ Start date cannot be after end date.")
        return

    filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

    if filtered_df.empty:
        print("No transactions found in the selected date range.")
        return

    print("\n📌 Transactions from", start_date.strftime(DATE_FORMAT), "to", end_date.strftime(DATE_FORMAT), ":")
    print(filtered_df.to_string(index=False))

    # Calculate totals
    income = filtered_df[filtered_df["Category"] == "Income"]["Amount"].sum()
    expenses = filtered_df[filtered_df["Category"] == "Expense"]["Amount"].sum()
    net_savings = income - expenses

    print("\n🔹 Summary:")
    print(f"   💰 Total Income: £{income:.2f}")
    print(f"   💸 Total Expenses: £{expenses:.2f}")
    print(f"   🏦 Net Savings: £{net_savings:.2f}")

    if input("\nWould you like to see a plot? (y/n) ").strip().lower() == "y":
        plot_transactions(filtered_df)


def plot_transactions(df):
    # Plots income and expenses over time.
    df.set_index("Date", inplace=True)

    income_df = df[df["Category"] == "Income"].resample("D").sum()
    expense_df = df[df["Category"] == "Expense"].resample("D").sum()

    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["Amount"], label="Income", color="g", marker="o")
    plt.plot(expense_df.index, expense_df["Amount"], label="Expense", color="r", marker="o")

    plt.xlabel("Date")
    plt.ylabel("Amount (£)")
    plt.title("📊 Income and Expenses Over Time")
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()


def main():
    # Main function to run the finance tracker.
    df = load_data()

    while True:
        print("\n===== 💰 Personal Finance Tracker =====")
        print("1️⃣  Add a new transaction")
        print("2️⃣  View transactions and summary")
        print("3️⃣  Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            df = add_transaction(df)
        elif choice == "2":
            filter_transactions(df)
        elif choice == "3":
            print("📍 Exiting... Thanks for using the finance tracker! 🎯")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

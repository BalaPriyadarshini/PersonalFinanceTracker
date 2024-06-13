import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import Error


# -------------Database connection-------------


def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='finance_tracker',
            user='root',
            password='root'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None


# -------------GUI setup & Functionalities-------------
        

class FinanceTrackerApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.root.geometry("626x352")
        self.opening_screen()

    # Opening Screen
    def opening_screen(self):
        self.image_path = r"C:\Users\saivi\OneDrive\Desktop\FinanceTracker\openingscreen.png"
        self.image = Image.open(self.image_path)
        self.image = self.image.resize((626, 352), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.image)
        self.label = tk.Label(root, image=self.bg_image)
        self.label.place(x=0, y=0, relwidth=1, relheight=1)
        tk.Button(self.root, text="USERS", command=self.users_frame, bg='white', fg='black', font=('Helvetica', 12, 'bold')).place(x=220, y=120)
        tk.Button(self.root, text="ACCOUNTS", command=self.accounts_frame, bg='white', fg='black', font=('Helvetica', 12, 'bold')).place(x=220, y=190)
        tk.Button(self.root, text="TRANSACTIONS", command=self.transactions_frame, bg='white', fg='black', font=('Helvetica', 12, 'bold')).place(x=420, y=120)
        tk.Button(self.root, text="CHECK", command=self.check_frame, bg='white', fg='black', font=('Helvetica', 12, 'bold')).place(x=420, y=190)

    # Background Setup
    def background(self):
        self.image_path = r"C:\Users\saivi\OneDrive\Desktop\FinanceTracker\background.png"
        self.image = Image.open(self.image_path)
        self.image = self.image.resize((626, 352), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.image)
        self.label = tk.Label(root, image=self.bg_image)
        self.label.place(x=0, y=0, relwidth=1, relheight=1)

    # User frame
    def users_frame(self):
        self.background()
        tk.Label(self.root, text="USERS", bg='ghost white', fg='black', font=('Helvetica', 16, 'bold italic')).place(x=365, y=50)

        tk.Label(self.root, text="User ID:", bg='ghost white', fg='black', font=('Helvetica', 10)).place(x=320, y=110)
        self.userid_entry = tk.Entry(self.root, bg='white', fg='black', font=('Helvetica', 10))
        self.userid_entry.place(x=420, y=110)
        tk.Label(self.root, text="Username:", bg='ghost white', fg='black', font=('Helvetica', 10)).place(x=320, y=150)
        self.username_entry = tk.Entry(self.root, bg='white', fg='black', font=('Helvetica', 10))
        self.username_entry.place(x=420, y=150)
        tk.Label(self.root, text="Password:", bg='ghost white', fg='black', font=('Helvetica', 10)).place(x=320, y=190)
        self.password_entry = tk.Entry(self.root, show='*', bg='white', fg='black', font=('Helvetica', 10))
        self.password_entry.place(x=420, y=190)
        tk.Button(self.root, text="Add User", command=self.add_user, bg='white', fg='black', font=('Helvetica', 10, 'bold')).place(x=250, y=240)
        tk.Button(self.root, text="Update User", command=self.update_user, bg='white', fg='black', font=('Helvetica', 10, 'bold')).place(x=365, y=240)
        tk.Button(self.root, text="Delete User", command=self.delete_user, bg='white', fg='black', font=('Helvetica', 10, 'bold')).place(x=500, y=240)
        tk.Button(self.root, text="EXIT", command=self.opening_screen, bg='white', fg='black', font=('Helvetica', 12, 'bold')).place(x=550, y=290)

    # Account frame
    def accounts_frame(self):
        self.background()
        tk.Label(self.root, text="ACCOUNTS", bg='ghost white', fg='black', font=('Helvetica', 16, 'bold italic')).place(x=365, y=50)

        tk.Label(self.root, text="Account ID:", bg='ghost white', fg='black', font=('Helvetica', 10)).place(x=320, y=100)
        self.accountid_entry = tk.Entry(self.root, bg='white', fg='black', font=('Helvetica', 10))
        self.accountid_entry.place(x=420, y=100)
        tk.Label(self.root, text="User ID:", bg='ghost white', fg='black', font=('Helvetica', 10)).place(x=320, y=140)
        self.account_userid_entry = tk.Entry(self.root, bg='white', fg='black', font=('Helvetica', 10))
        self.account_userid_entry.place(x=420, y=140)
        tk.Label(self.root, text="Account Name:", bg='ghost white', fg='black', font=('Helvetica', 10)).place(x=320, y=180)
        self.account_name_entry = tk.Entry(self.root, bg='white', fg='black', font=('Helvetica', 10))
        self.account_name_entry.place(x=420, y=180)
        tk.Label(self.root, text="Balance:", bg='ghost white', fg='black', font=('Helvetica', 10)).place(x=320, y=220)
        self.account_balance_entry = tk.Entry(self.root, bg='white', fg='black', font=('Helvetica', 10))
        self.account_balance_entry.place(x=420, y=220)
        tk.Button(self.root, text="Add Account", command=self.add_account, bg='white', fg='black', font=('Helvetica', 10, 'bold')).place(x=250, y=255)
        tk.Button(self.root, text="Update Account", command=self.update_account, bg='white', fg='black', font=('Helvetica', 10, 'bold')).place(x=365, y=255)
        tk.Button(self.root, text="Delete Account", command=self.delete_account, bg='white', fg='black', font=('Helvetica', 10, 'bold')).place(x=500, y=255)
        tk.Button(self.root, text="EXIT", command=self.opening_screen, bg='white', fg='black', font=('Helvetica', 12, 'bold')).place(x=550, y=290)

    # Transaction frame
    def transactions_frame(self):
        self.background()
        tk.Label(self.root, text="TRANSACTIONS", bg='ghost white', fg='black', font=('Helvetica', 16, 'bold italic')).place(x=355, y=50)

        tk.Label(self.root, text="Transaction ID:", bg='ghost white', fg='black', font=('Helvetica', 10)).place(x=320, y=100)
        self.transactionid_entry = tk.Entry(self.root, bg='white', fg='black', font=('Helvetica', 10))
        self.transactionid_entry.place(x=450, y=100)
        tk.Label(self.root, text="Account ID:", bg='ghost white', fg='black', font=('Helvetica', 10)).place(x=320, y=130)
        self.transaction_accountid_entry = tk.Entry(self.root, bg='white', fg='black', font=('Helvetica', 10))
        self.transaction_accountid_entry.place(x=450, y=130)
        tk.Label(self.root, text="Amount:", bg='ghost white', fg='black', font=('Helvetica', 10)).place(x=320, y=160)
        self.transaction_amount_entry = tk.Entry(self.root, bg='white', fg='black', font=('Helvetica', 10))
        self.transaction_amount_entry.place(x=450, y=160)
        tk.Label(self.root, text="Transaction Date:", bg='ghost white', fg='black', font=('Helvetica', 10)).place(x=320, y=190)
        self.transaction_date_entry = tk.Entry(self.root, bg='white', fg='black', font=('Helvetica', 10))
        self.transaction_date_entry.place(x=450, y=190)
        tk.Label(self.root, text="Description:", bg='ghost white', fg='black', font=('Helvetica', 10)).place(x=320, y=220)
        self.transaction_description_entry = tk.Entry(self.root, bg='white', fg='black', font=('Helvetica', 10))
        self.transaction_description_entry.place(x=450, y=220)
        tk.Button(self.root, text="Add Transaction", command=self.add_transaction, bg='white', fg='black', font=('Helvetica', 10, 'bold')).place(x=200, y=260)
        tk.Button(self.root, text="Update Transaction", command=self.update_transaction, bg='white', fg='black', font=('Helvetica', 10, 'bold')).place(x=335, y=260)
        tk.Button(self.root, text="Delete Transaction", command=self.delete_transaction, bg='white', fg='black', font=('Helvetica', 10, 'bold')).place(x=490, y=260)
        tk.Button(self.root, text="EXIT", command=self.opening_screen, bg='white', fg='black', font=('Helvetica', 12, 'bold')).place(x=550, y=290)

    # Check balance frame
    def check_frame(self):
        self.background()
        tk.Label(self.root, text="CHECK", bg='ghost white', fg='black', font=('Helvetica', 16, 'bold italic')).place(x=385, y=50)

        tk.Label(self.root, text="Account ID:", bg='ghost white', fg='black', font=('Helvetica', 10)).place(x=320, y=130)
        self.check_accountid_entry = tk.Entry(self.root, bg='white', fg='black', font=('Helvetica', 10))
        self.check_accountid_entry.place(x=450, y=130)
        tk.Button(self.root, text="Display balance", command=self.check_balance, bg='white', fg='black', font=('Helvetica', 10, 'bold')).place(x=380, y=175)
        tk.Button(self.root, text="Display transactions", command=self.check_transactions, bg='white', fg='black', font=('Helvetica', 10, 'bold')).place(x=365, y=220)
        tk.Button(self.root, text="EXIT", command=self.opening_screen, bg='white', fg='black', font=('Helvetica', 12, 'bold')).place(x=550, y=290)

    # Inserting User
    def add_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username and password:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor()
                try:
                    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
                    connection.commit()
                    messagebox.showinfo("Success", "User registered successfully!")
                except Error as e:
                    messagebox.showerror("Error", f"Error: {e}")
                finally:
                    cursor.close()
                    connection.close()
        else:
            messagebox.showerror("Error", "Please fill in both fields")

    # Updating User
    def update_user(self):
        user_id = self.userid_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        if user_id and username and password:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor()
                try:
                    cursor.execute("UPDATE users SET username=%s, password=%s WHERE user_id=%s",
                                   (username, password, user_id))
                    connection.commit()
                    messagebox.showinfo("Success", "User updated successfully!")
                except Error as e:
                    messagebox.showerror("Error", f"Error: {e}")
                finally:
                    cursor.close()
                    connection.close()
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    # Deleting User
    def delete_user(self):
        user_id = self.userid_entry.get()
        if user_id:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor()
                try:
                    cursor.execute("DELETE FROM users WHERE user_id=%s", (user_id,))
                    connection.commit()
                    messagebox.showinfo("Success", "User deleted successfully!")
                except Error as e:
                    messagebox.showerror("Error", f"Error: {e}")
                finally:
                    cursor.close()
                    connection.close()
        else:
            messagebox.showerror("Error", "Please enter a User ID")

    # Inserting account
    def add_account(self):
        user_id = self.account_userid_entry.get()
        account_name = self.account_name_entry.get()
        balance = self.account_balance_entry.get()
        if user_id and account_name and balance:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor()
                try:
                    cursor.execute("INSERT INTO accounts (user_id, account_name, balance) VALUES (%s, %s, %s)",
                                   (user_id, account_name, balance))
                    connection.commit()
                    messagebox.showinfo("Success", "Account added successfully!")
                except Error as e:
                    messagebox.showerror("Error", f"Error: {e}")
                finally:
                    cursor.close()
                    connection.close()
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    # Updating account
    def update_account(self):
        account_id = self.accountid_entry.get()
        user_id = self.account_userid_entry.get()
        account_name = self.account_name_entry.get()
        balance = self.account_balance_entry.get()
        if account_id and user_id and account_name and balance:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor()
                try:
                    cursor.execute("UPDATE accounts SET user_id=%s, account_name=%s, balance=%s WHERE account_id=%s",
                                   (user_id, account_name, balance, account_id))
                    connection.commit()
                    messagebox.showinfo("Success", "Account updated successfully!")
                except Error as e:
                    messagebox.showerror("Error", f"Error: {e}")
                finally:
                    cursor.close()
                    connection.close()
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    # Deleting account
    def delete_account(self):
        account_id = self.accountid_entry.get()
        if account_id:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor()
                try:
                    cursor.execute("DELETE FROM accounts WHERE account_id=%s", (account_id,))
                    connection.commit()
                    messagebox.showinfo("Success", "Account deleted successfully!")
                except Error as e:
                    messagebox.showerror("Error", f"Error: {e}")
                finally:
                    cursor.close()
                    connection.close()
        else:
            messagebox.showerror("Error", "Please enter an Account ID")

    # Inserting transaction
    def add_transaction(self):
        account_id = self.transaction_accountid_entry.get()
        amount = self.transaction_amount_entry.get()
        transaction_date = self.transaction_date_entry.get()
        description = self.transaction_description_entry.get()
        if account_id and amount and transaction_date and description:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor()
                try:
                    cursor.execute(
                        "INSERT INTO transactions (account_id, amount, transaction_date, description) VALUES (%s, %s, %s, %s)",
                        (account_id, amount, transaction_date, description))
                    cursor.execute(
                        "SELECT balance FROM accounts WHERE account_id = %s", (account_id,))
                    current_balance = cursor.fetchone()[0]
                    new_balance = current_balance
                    amount = int(amount)
                    new_balance -= amount
                    cursor.execute(
                        "UPDATE accounts SET balance = %s WHERE account_id = %s", (new_balance, account_id))

                    connection.commit()
                    messagebox.showinfo("Success", "Transaction added successfully!")
                except Error as e:
                    messagebox.showerror("Error", f"Error: {e}")
                finally:
                    cursor.close()
                    connection.close()
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    # Updating transaction
    def update_transaction(self):
        transaction_id = self.transactionid_entry.get()
        account_id = self.transaction_accountid_entry.get()
        amount = self.transaction_amount_entry.get()
        transaction_date = self.transaction_date_entry.get()
        description = self.transaction_description_entry.get()
        if transaction_id and account_id and amount and transaction_date and description:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor()
                try:
                    cursor.execute(
                        "UPDATE transactions SET account_id=%s, amount=%s, transaction_date=%s, description=%s WHERE transaction_id=%s",
                        (account_id, amount, transaction_date, description, transaction_id))
                    connection.commit()
                    messagebox.showinfo("Success", "Transaction updated successfully!")
                except Error as e:
                    messagebox.showerror("Error", f"Error: {e}")
                finally:
                    cursor.close()
                    connection.close()
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    # Deleting transaction
    def delete_transaction(self):
        transaction_id = self.transactionid_entry.get()
        if transaction_id:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor()
                try:
                    cursor.execute("DELETE FROM transactions WHERE transaction_id=%s", (transaction_id,))
                    connection.commit()
                    messagebox.showinfo("Success", "Transaction deleted successfully!")
                except Error as e:
                    messagebox.showerror("Error", f"Error: {e}")
                finally:
                    cursor.close()
                    connection.close()
        else:
            messagebox.showerror("Error", "Please enter a Transaction ID")

    # Check Balance
    def check_balance(self):
        account_id = self.check_accountid_entry.get()
        if account_id:
            connection = connect_to_db()
            if connection:
                cursor = connection.cursor()
                try:
                    cursor.execute("Select * from accounts where account_id = %s",(account_id,))

                    current_balance = cursor.fetchone()[3]
                    connection.commit()
                    messagebox.showinfo("Balance", f"Your current balance: {current_balance}")
                except Error as e:
                    messagebox.showerror("Error", f"Error: {e}")
                finally:
                    cursor.close()
                    connection.close()
        else:
            messagebox.showerror("Error", "Please enter an Account ID")

    # Check transaction
    def check_transactions(self):
        accountid = self.check_accountid_entry.get()

        if not accountid:
            messagebox.showwarning("Input Error", "Account ID is required")
            return

        connection = connect_to_db()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute(
                    "SELECT transaction_id, amount, transaction_date, description FROM transactions WHERE account_id = %s",
                    (accountid,))
                transactions = cursor.fetchall()
                if transactions:
                    transactions_window = tk.Toplevel(self.root)
                    transactions_window.title("Transactions")
                    tree = ttk.Treeview(transactions_window,
                                        columns=("Transaction ID", "Amount", "Date", "Description"),
                                        show='headings')
                    tree.heading("Transaction ID", text="Transaction ID")
                    tree.heading("Amount", text="Amount")
                    tree.heading("Date", text="Date")
                    tree.heading("Description", text="Description")
                    for txn in transactions:
                        tree.insert("", "end", values=txn)
                    tree.pack(fill=tk.BOTH, expand=True)
                else:
                    messagebox.showinfo("No Transactions", "No transactions found for this account")
            except Error as e:
                messagebox.showerror("Error", f"Failed to retrieve transactions: {e}")
            finally:
                cursor.close()
                connection.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceTrackerApp(root)
    root.mainloop()

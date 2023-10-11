expenses = [
    {'tanggal': '2023-07-25', 'deskripsi': 'Makan Siang', 'jumlah': 50000},
    {'tanggal': '2023-07-25', 'deskripsi': 'Transportasi', 'jumlah': 25000},
    {'tanggal': '2023-07-26', 'deskripsi': 'Belanja', 'jumlah': 100000},
]


# TODO 1 Buatlah Fungsi add_expense disini
def add_expense(expenses, date, description, amount):
    new_expense = {'tanggal': date, 'deskripsi': description, 'jumlah': amount}
    expenses.append(new_expense)
    return expenses

# TODO 2 Buatlah fungsi calculate_total_expenses disini


def calculate_total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense['jumlah']
    return total

# TODO 3 Buatlah fungsi get_expenses_by_date disini


def get_expenses_by_date(expenses, date):
    expenses_on_date = [
        expense for expense in expenses if expense['tanggal'] == date]
    return expenses_on_date

# TODO 4 Buatlah fungsi generate_expenses_report disini


def generate_expenses_report(expenses):
    report = {}
    for expense in expenses:
        date = expense['tanggal']
        amount = expense['jumlah']
        if date in report:
            report[date] += amount
        else:
            report[date] = amount
    return report


# TODO 6 ubah fungsi berikut ke dalam bentuk lambda
def get_user_input(command): return int(input(command))


def add_expense_interactively(expenses):
    date = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
    description = input("Masukkan deskripsi pengeluaran: ")
    amount = int(input("Masukkan jumlah pengeluaran: "))

    # new_expenses = #Panggil fungsi 'add_expense'
    new_expenses = add_expense(expenses, date, description, amount)
    print("Pengeluaran berhasil ditambahkan.")
    return new_expenses


def view_expenses_by_date(expenses):
    date = input("Masukkan tanggal (YYYY-MM-DD): ")

    # expenses_on_date = get_expenses_by_date(date, date)
    expenses_on_date = get_expenses_by_date(expenses, date)
    print(f"\nPengeluaran pada tanggal {date}:")
    for expense in expenses_on_date:
        print(f"{expense['deskripsi']} - Rp {expense['jumlah']}")


def view_expenses_report(expenses):
    print("\nLaporan Pengeluaran Harian:")

    # expenses_report = #Panggil fungsi 'generate_expenses_report'
    expenses_report = generate_expenses_report(expenses)
    for entry in expenses_report:
        print(entry)


def display_menu():
    print("\n===== Aplikasi Pencatat Pengeluaran Harian =====")
    print("1. Tambah Pengeluaran")
    print("2. Total Pengeluaran Harian")
    print("3. Lihat Pengeluaran berdasarkan Tanggal")
    print("4. Lihat Laporan Pengeluaran Harian")
    print("5. Keluar")


def main():
    global expenses
    while True:
        display_menu()
        choice = get_user_input("Pilih menu (1/2/3/4/5): ")
        if choice == 1:
            expenses = add_expense_interactively(expenses)
        elif choice == 2:
            total_expenses = calculate_total_expenses(expenses)
            print(f"\nTotal Pengeluaran Harian: Rp {total_expenses}")
        elif choice == 3:
            view_expenses_by_date(expenses)
        elif choice == 4:
            view_expenses_report(expenses)
        elif choice == 5:
            print("Terima kasih telah menggunakan aplikasi kami.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")


if __name__ == "__main__":
    main()

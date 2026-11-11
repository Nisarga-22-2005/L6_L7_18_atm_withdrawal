def notes_needed(amount):
    try:
        if amount is None:
            return 0
        amount = int(amount.replace(',', ''))
        if amount < 0:
            return 0
        return amount // 100
    except (ValueError, AttributeError):
        return 0


def mask_card(card_number):
    if not isinstance(card_number, str):
        return "Invalid card number"

    groups = card_number.split()

    if len(groups) != 4 or not all(group.isdigit() for group in groups):
        return "Invalid card number"

    return "XXXX XXXX XXXX " + groups[3]


def average_withdrawal(amounts_csv):
    try:
        if not isinstance(amounts_csv, str) or not amounts_csv.strip():
            return 0

        amounts = [int(a.strip()) for a in amounts_csv.split(',')]

        if not amounts or any(a < 0 for a in amounts):
            return 0

        return sum(amounts) // len(amounts)
    except ValueError:
        return 0


def main():
    print("==== Running notes_needed ====")
    user_input = input("Enter an amount (e.g. 2,500): ")
    result = notes_needed(user_input)
    print("Number of 100 Notes:", result)

    print("\n==== Running mask_card ====")
    user_input = input("Enter a card number (e.g. 1234 5678 9012 3456): ")
    result = mask_card(user_input)
    print("Masked Card:", result)

    print("\n==== Running average_withdrawal ====")
    user_input = input("Enter withdrawals as CSV (e.g. 500,1000,2000): ")
    result = average_withdrawal(user_input)
    print("Average Withdrawal:", result)


if __name__ == "__main__":
    main()
# myapp/service.py

def add_six_percent_to_amounts(transactions):
    if isinstance(transactions, dict):  # If it's a single transaction
        transactions['amount'] = float(transactions['amount']) * 1.06
    elif isinstance(transactions, list):  # If it's a list of transactions
        for transaction in transactions:
            transaction['amount'] = float(transaction['amount']) * 1.06

    return transactions


def subtract_percentage_from_amounts(transactions):
    for transaction in transactions:
        if isinstance(transactions, dict):  # If it's a single transaction
            transaction['amount'] = float(
                transaction['amount']) * (1 - 0.1)
        elif isinstance(transactions, list):  # If it's a list of transactions
            for transaction in transactions:
                transaction['amount'] = float(
                    transaction['amount']) * (1 - 0.1)

    return transactions

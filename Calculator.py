"""
[I want to create a Python program that can convert between US currency and Australian currency. As well, I want to be able to add or subtract the two together and get an accurate value in either currencies.]

US:1.00 = AUD:1.51
"""
#convertors
def usd_to_aud(amount):
    return amount * 1.51
def aud_to_usd(amount):
    return amount * 0.66

#performers
def add_currencies(first_amount, first_type, second_amount, second_type, end_type):
    if end_type == first_type and end_type == second_type:
        return first_type + second_type
    if end_type != first_type or end_type != second_type:
        if first_type == "usd" and end_type == "usd":
            second_amount = aud_to_usd(second_amount)
            return first_amount + second_amount
        if first_type == "aud" and end_type == "aud":
            second_amount = usd_to_aud(second_amount)
            return first_amount + second_amount
def subtract_currencies(first_amount, first_type, second_amount, second_type, end_type):
    if end_type == first_type and end_type == second_type:
        return first_type - second_type
    if end_type != first_type or end_type != second_type:
        if first_type == "usd" and end_type == "usd":
            second_amount = aud_to_usd(second_amount)
            return first_amount - second_amount
        if first_type == "aud" and end_type == "aud":
            second_amount = usd_to_aud(second_amount)
            return first_amount - second_amount
        
#program
perform = str(input("What do you want to do? convert, add or subtract: ")).lower()

if perform == "convert":
    amount = float(input("Enter the amount: "))
    type = str(input("What currency is it? usd or aud: ")).lower()
    end_type = str(input("What currency do you want the result to be? usd or aud: ")).lower()
    if type == "usd" and end_type == "aud":
        print(usd_to_aud(amount))
    if type == "aud" and end_type == "usd":
        print(aud_to_usd(amount))

elif perform == "add" or perform == "subtract":
    first_amount = float(input("Enter the first amount: "))
    first_type = str(input("What currecncy is it? usd or aud: ")).lower()
    second_amount = float(input("Enter the second amount: "))
    second_type = str(input("What currency is it? usd or aud: ")).lower()
    end_type = str(input("What currency do you want it to be? usd or aud: ")).lower()
    if perform == "add":
        print(add_currencies(first_amount, first_type, second_amount, second_type, end_type))
    if perform == "subtract":
        print(subtract_currencies(first_amount, first_type, second_amount, second_type, end_type))
"""
iQualify Challenge 3: Cell Phone Bill.

A particular cell phone plan includes 50 minutes of air time and 50 text messages for $15.00 a month.
Each additional minute of air time costs $0.25, while additional text messages cost $0.15 each.
All cell phone bills include an additional flat charge of $0.44 to support 111 call centres, and
the entire bill (including the 111 charge) is subject to 5 percent sales tax.

Write a program that reads the number of minutes and text messages used in a month from the user.
Display the base charge, additional minutes charge (if any), additional text message charge (if any),
the 111 fee, tax and total bill amount. Only display the additional minute and text message charges if
the user incurred costs in these categories. Ensure that all of the charges are displayed using 2 decimal places.

So ask the user how many minutes they used
then ask how many text messages were sent
then give them the total bill. Break it down to base rates plus extra rates

@author John Wright <20210556>
19 May 2021

"""


# function to print out a bill given how many texts and minutes you use.
def get_bill(mins, txts):
    # First lets declare some stuff. Base cost and emergency fee don't change, additional costs start at 0.
    base_cost = 15.00  # 15 dollars for 50 or less minutes and 50 or less texts.
    emergency_fee = 0.44
    extra_charges = 0.00

    print("****Your bill: ****")
    print(f"111 fee: ${emergency_fee}")

    # minutes calculation
    print(f"minutes: {mins} ")
    if mins > 50:  # checking if the more than 50 minutes were used
        extra_mins = mins-50  # calculate extra minutes
        extra_mins_charge = extra_mins * 0.25  # calculate the charges
        extra_charges += extra_mins_charge  # add the extra charges to the total
        print(f"additional charges of ${extra_mins_charge} for {extra_mins} additional minutes")

    # texts calculation
    print(f"texts: {txts}")
    if txts > 50:  # checking if the more than 50 texts were used
        extra_txts = txts - 50  # calculate extra texts
        extra_txts_charge = extra_txts * 0.15  # calculate charges
        extra_charges += extra_txts_charge  # add the extra charges to the total
        print(f"additional charges of ${extra_txts_charge} for {extra_txts} additional texts")

    # totals calculation
    total = base_cost + emergency_fee + extra_charges  # sum all the charges
    tax = 0.05 * total  # tax only occurs after all other charges are summed
    total += tax  # add on tax
    print(f"tax: ${round(tax, 2)}")
    print(f"Total Charge: ${round(total, 2)}\n")


# Get minutes and texts from users
used_minutes = int(input("How many minutes did you use? "))
used_texts = int(input("How many texts did you send? "))
get_bill(used_minutes, used_texts)

print("Test case assertions ... ")
print("Testing bill that uses 10 mins and 10 txts. No extra charges incurred. Expected total $16.21")
get_bill(10, 10)
print("\nTesting bill that uses 100 mins and 99 txts. Mins and Txts incur extra charges. Expected total $37.05")
get_bill(100, 99)
print("\nTesting bill that uses 49 mins and 99 txts. Only txts incur extra charges. Expected total $23.93")
get_bill(49, 99)
print("\nTesting bill that uses 99 mins and 49 txts. Only mins incur extra charges. Expected total $29.07")
get_bill(99, 49)

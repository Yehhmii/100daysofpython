print("Welcome to tip calculator.")
bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, 0r 15? "))
people_to_slipt = int(input("How many people to slipt the bill? "))

new_percentage_tip = percentage_tip / 100
total_tip = bill * new_percentage_tip
total_bill = bill + total_tip
bill_per_person = total_bill / people_to_slipt

new_bill = round(bill_per_person, 2)    #instead of using this which may not always follow our rule 
new_bill = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${new_bill}")
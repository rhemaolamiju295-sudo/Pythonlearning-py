# # What is state?

# # State is not a special programming language feature. It is simply the current values of the data a program is working with.

# # State changes step by step
# # Let us trace a simple transfer as an execution pipeline. We will use plain English and a table to see how the state changes.
# # Initial state:
# # Label 	Value
# balance 	= 10000
# amount 	=3000
# recipient_balance 	= 2000
# # receipt 	= "empty"

# # Step 1: Check that amount is less than or equal to balance.

# if amount <= balance:
#     check_pass = True 

# # The check succeeds because 3000 <= 10000. We might record this as:
# # Label 	Value
# # check_passed 	true
# # Now the state includes a new piece of information: check_passed is true.

# # Step 2: Subtract amount from balance.

# # The new balance is 10000 - 3000 = 7000. The state changes:
# # Label 	Value
# # balance 	7000
# # amount 	3000
# # recipient_balance 	2000
# # receipt 	empty

# balance = balance - amount 

# # Step 3: Add amount to recipient_balance.

# # The recipient's new balance is 2000 + 3000 = 5000.
# # Label 	Value
# # balance 	7000
# # amount 	3000
# # recipient_balance 	5000
# # receipt 	empty

# recipient_balance += amount 

# # Step 4: Create a receipt.

# # The receipt might be a message: "₦3,000 sent to friend."
# # Label 	Value
# # balance 	7000
# # amount 	3000
# # recipient_balance 	5000
# # receipt 	"₦3,000 sent to friend"

# reciept = "N3,000 sent to friend"

# # This is the final state.

# # Notice how we tracked each box and how its value changed. If we skipped Step 2, the balance would remain ₦10,000, and the transfer would not be reflected in the records. If we skipped Step 3, the recipient would not receive the money. If we forgot to update the receipt, the user would not see confirmation.


cur_balance = 100000
cur_balance = float(cur_balance)
amount = float(input("Enter the amount you want to send: "))
recipent_account = float(input("Enter recipent acc number: "))
recipent_balance = 300
recipent_balance = float(recipent_balance)

if amount <= cur_balance:
    cur_balance -= amount
    recipent_balance += amount 
    reciept = (f"{amount} sent to {recipent_account}," 
           f"your remaining balance is {cur_balance}", f"recipent's balance is {recipent_balance}"
           )
    print(reciept)
else:
    print("Insufficient funds")



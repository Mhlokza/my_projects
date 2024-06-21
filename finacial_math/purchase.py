payment = int(input("Enter the monthly payment: "))
house_cost= int(input("enter the price of a house: "))
total_monthly_payment =house_cost// payment
due_money = house_cost-payment
print(f"house cost R{house_cost} and you have made a payment of R{payment} outstanding payment is R{due_money},total month of payment {total_monthly_payment} months")
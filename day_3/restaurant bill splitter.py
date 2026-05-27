                                     #Restaurant bill splitter
                                     

food_bill = 5000                                      #food bill charged

tip_percent = 5                                      #percent of tip given to the waiter

tip_amount = tip_percent / 100  *  food_bill              #amount given to the                                                                                                   waiter as tip

total_bill = food_bill + tip_amount                   #total bill which has to be paid                                                                         including food bill and tip amount

people_no = 5                                      #no of people came to restaurant

each_person_pay = total_bill / people_no                 #amount each person                                                                                                         has to pay

print(f"1. amount of food = ₹{food_bill}")

print()                                        #one line space     

print(f"2. amount of tip for staff accourding to the bill = ₹{tip_amount}")

print()                                        #one line space     

print(f"3. Total bill which has to pay = ₹{total_bill}")

print()                                        #one line space     

print(f"4. Bill on each person = ₹{each_person_pay}")

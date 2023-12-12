number_of_left_shoes= int(input("how many left shoes ?"))
number_of_right_shoes= int(input("how many right shoes ?"))
total_amount_of_shoes = number_of_left_shoes + number_of_right_shoes
pairs = min(number_of_left_shoes,number_of_right_shoes)
remaining = total_amount_of_shoes - pairs * 2
print(f"the numbe of pairs are : {pairs} and the amount of remaining shoes are : {remaining}")

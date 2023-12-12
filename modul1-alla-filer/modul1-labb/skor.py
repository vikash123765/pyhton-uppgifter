

left_shoes = int(input("Hur många vänsterskor finns det? "))
right_shoes = int(input("Hur många högerskor finns det? "))

total_amount_amount = left_shoes + right_shoes  

min_value = min(left_shoes,right_shoes)

shoes_remainder =   total_amount_amount - (min_value  * 2 )

print(f"Det finns {min_value} par och {shoes_remainder} överblivna skor.")




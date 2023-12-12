import listfunktioner

nums = input("Ange ett par tal (separerade med mellanslag): ").split()
nums = [int(num) for num in nums]

number = int(input("Ange ett sökt tal: "))

min= listfunktioner.arg_min(nums)
print(f"Det minsta talet finns på position {min}.")

position= listfunktioner.find_all_positions(nums,number)
print(f"Talet {position} finns på positionerna {position}.")


amount_of_socks = int(input("Hur många strumpor finns det i tvättmaskinen?"))


pairs_of_socks = amount_of_socks // 2  # devide with heltals to se how many pairs of 2

remainder_of_socks = amount_of_socks % 2  # sheck remainde if we do modular devison o of pairs of 2

print(f"Det finns {pairs_of_socks} par och {remainder_of_socks} överbliven strumpa.")
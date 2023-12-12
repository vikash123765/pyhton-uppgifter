user_input = input("Ange en serie heltal, åtskilda av mellanslag: ").split()
goal_number = int(input("Ange ett målvärde: "))

closest_num = int(user_input[0])
closest_distance = abs(int(user_input[0]) - goal_number)

for number in user_input:
    current_num = int(number)
    distance = abs(current_num - goal_number)
    if distance < closest_distance:
        closest_num = current_num
        closest_distance = distance

print(f"Närmast: {closest_num}") 
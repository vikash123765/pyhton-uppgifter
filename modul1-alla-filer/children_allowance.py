num_of_children = int(input("how many children you have ?s" ))
child_allowance = 1250  * num_of_children
if num_of_children == 1:
    one_child= child_allowance 
    print(f"for 1 child amount is: {one_child}")
elif num_of_children == 2:
    two_child= child_allowance  + 150
    print(f"for 2 child amount is: {two_child}")
elif num_of_children == 3:
    three_child= child_allowance + 730
    print(f"for 3 child amount is: {three_child}")
elif num_of_children == 4:
    four_child= child_allowance + 1740
    print(f"for 4 child amount is: {four_child}")
elif num_of_children == 5:
    five_child= child_allowance  + 2990
    print(f"for 5 child amount is: {five_child}")
else:
    num_of_children >= 6
    six_child= child_b allowance + 4240
    print(f"for{num_of_children}child amount is: {six_child}")

    

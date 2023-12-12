num_of_children = int(input("how many children you have ?s" ))
child_allowance = 1250 * num_of_children
match num_of_children:
    case 1:
        pass
    case 2:
        child_allowance = child_allowance + 150
    case 3 :
        child_allowance += 730
    case 4 :
        child_allowance += 1740
    case 5:
        child_allowance += 2990
    case _:
        child_allowance += 4240
print(f"total allowance for {num_of_children} is: {child_allowance}")        
        
        
        
        
        
    
        


        

 
        

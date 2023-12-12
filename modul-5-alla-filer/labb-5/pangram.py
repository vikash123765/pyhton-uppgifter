def is_pangram(text): 
    
    text=text.lower()

    found_chars=set()  
    
    for char in text: 

        if 'a' <= char <= 'z' and char not in found_chars: 
          
            found_chars.add(char) 
    
    return len(found_chars) == 26   


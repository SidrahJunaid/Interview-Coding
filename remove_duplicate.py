# Remove Duplicates from a List
    

def remove_duplicate(duplicate):
    
       final_list=[]
    
       for num in duplicate:
        
           if num not in final_list:
            
             final_list.append(num)
            
    
       return final_list

            

duplicate=[2,3,2,4,5,3]

print(remove_duplicate(duplicate))
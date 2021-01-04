lst = [] 

n = int(input("Enter number of Subjects then Marks : "))   
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) 
print(lst)
total = sum(lst)
print("Total Marks: ",total)
      
def Average(lst): 
    return sum(lst) / len(lst) 

average = Average(lst) 

print("Average  =", round(average, 2))
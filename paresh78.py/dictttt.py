#dict1={i:f"item{i}"for i in range(100)}
#print(dict1)

#dict1={i:f"item{i}"for i in range(100) if i%3==0}
#print(dict1)

#dict1={i:f"item{i}"for i in range(100) if i%3==0}
#dict1={value:key for key,value in dict1.items()}
#print(dict1)

#dict1={i:f"item{i}"for i in range(20) if i%3==0}
#dict2={value:key for key,value in dict1.items()}
#print(dict1,"\n",dict2)

dresses={dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2"] }
print(dresses)

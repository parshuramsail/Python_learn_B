
dict1={i:f"item{i}"for i in range(20) if i%3==0}
dict2={value:key for key,value in dict1.items()}
print(dict1,"\n",dict2)

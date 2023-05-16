"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
   # result.insert(1,"@")
   # result.insert(3,"@")
   # result.insert(5,"@")
   #======================
    #for i in range(1,6,2):
     #   result.insert(i,"@")
    #======================
    i=1
    while(i<6):
        result.insert(i,"@")
        i+=2
    return result
print(fn_hack_9()) 
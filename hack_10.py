"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    lista = []
    for i in result:
        if(i=="o"):
            lista.append("0")
        elif(i=="i"):
            lista.append("1")
        elif(i=="a"):
            lista.append("@")
        elif(i.islower):
            lista.append(i.upper())
    result=lista
    return result  
print(fn_hack_10())
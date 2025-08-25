import random

import string




def hide (message):
    result = []


    for i in message:
        result.append(i)
        for _ in range(3):
            result.append(random.choice(string.digits + string.ascii_letters))
    return "" .join(result)     















name = input("Enter message to be encoded: ")

hidden_name = hide(name)
#hidden_name2 = hide(hidden_name)
print(f"Hidden name is {hidden_name}")    
#print(f"Hidden name is {hidden_name2}") 













def decode (message):
  
    actual_message = message[::4]
    #print(f"The actual message is {actual_message}")
    return actual_message

    #print("Second round/..............")
    #def decode2(actual_message):
       # realmessage = actual_message[::4]
        #print(f"The actual message is {realmessage}")


    #decode2(actual_message)




message1 = decode(hidden_name)
print(f"decoded  to ........................\n{message1}")

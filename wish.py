import datetime

'''JARVIS will wish at the begining of program
depending upon time.
'''

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        wish_statement = "Good Morning sir!"
    elif hour >= 12 and hour < 18:
        wish_statement = "Good Afternoon sir!"
    else:
        wish_statement = "Good Evening sir!"
    
    return wish_statement
    

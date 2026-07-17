""" 4,-8,12,-16,20,-24,....,-800,804"""
x = 4
while(x <= 804):
    if(x % 8 == 0):
        print(-x,end = ',')
    else:
        print(x,end = ',')
    x = x + 4
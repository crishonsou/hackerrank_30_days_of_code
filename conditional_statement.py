def conditionalStatement(N):
    
    if N % 2 != 0:
        print('Weird')
    else:
        if N == 20:
            print('Weird') 
        elif N % 2 == 0 and N >= 2 and N <= 5:
            print('Not Weird')
        elif N % 2 == 0 and N >= 6 and N <= 19:
            print('Weird') 
        else:
            print('Not Weird')


conditionalStatement(3)






  


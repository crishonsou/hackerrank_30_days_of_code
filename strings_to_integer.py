def str_to_int(S):
    try:
        S = int(S)
        return S
    except:
        return 'Bad String'


S = input().strip()

result = str_to_int(S)

print(result)
        
        

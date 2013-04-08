import re

def check_nric(n):
    pattern = re.compile("^[sStTfFgG][0-9]{7}[a-zA-Z]$")
    if not pattern.match(n):
        print("Invalid NRIC")
        
    else:
        weight = [2, 7, 6, 5, 4, 3, 2]
        ST = ['J', 'Z', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
        FG = ['X', 'W', 'U', 'T', 'R', 'Q', 'P', 'N', 'M', 'L', 'K']

        tsum = 0
        for i in range (1,8):
            tsum = tsum + int(n[i])*int(weight[i-1])

        if re.compile("[tTgG]").match(n[0]):
            mod = (tsum+4) % 11
        else:
            mod = tsum % 11
            
        if re.compile("[tTsS]").match(n[0]):
            if 'n[8]' == ST[mod]:
                print("NRIC is valid")
            else:
                print("Invalid NRIC")
        elif re.compile("[fFgG]").match(n[0]):
            if n[8] == FG[mod]:
                print("NRIC is valid")
            else:
                print("Invalid NRIC")

NRIC=input("NRIC:")
check_nric(NRIC)
        
            
        


def stds(n):
    match n:
        case 1:
            return 'I'
        case 2:
            return 'II'
        case 3:
            return 'III'
        case 4:
            return 'IV'
        case 5:
            return 'V'
        case 6:
            return 'VI'                
        case 7:
            return 'VII'
        case 8:
            return 'VIII'
        case 9:
            return 'IX'
        case 10:
            return 'X'    
        case 50:
            return 'L'                                    
        case 100:
            return 'C'
        case 500:
            return 'D'
        case 1000:
            return 'M'
        case _:
            return ''
def concat_str(source_str, to_add):
    if len(source_str)==0:
        return to_add
    else:
        return source_str+to_add
def romans_10(n):
    rem = n%10
    lastbit = self.stds(rem)
    div = n//10
    tens = self.stds(rem)*div
    final_str = tens+lastbit
    return final_str
def run(n):
    n_in_roman_alphabet = None
    n = str(n)
    for i in range(len(str(n))):
        print(i)
        if int(n[:i])<11:
            n_in_roman_alphabet = self.concat_str(n_in_roman_alphabet,self.stds(int(n[:1])))
        elif 50<int(n[:i])<=11:
            n_in_roman_alphabet = self.concat_str(n_in_roman_alphabet,self.romans_10(int(n[:i])))
            return n_in_roman_alphabet

run(10)
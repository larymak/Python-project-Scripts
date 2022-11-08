def binaryToDecimal(binary):
    binary = str(binary)
    if '.' in binary: integral, fractional = binary.split('.')
    else: 
        integral = binary
        fractional = 0

    if integral:
        integral = integral[::-1]

        decimal = 0
        for i in range(len(integral)):
            decimal += int(integral[i]) * (2**i)

    if fractional:
        for i in range(len(fractional)):
            decimal += int(fractional[i]) * (1/(2**(1+i)))
    
    return decimal

def octalToDecimal(octal):
    octal = str(octal)
    if '.' in octal: integral, fractional = octal.split('.')
    else: 
        integral = octal
        fractional = 0

    if integral:
        integral = integral[::-1]

        decimal = 0
        for i in range(len(integral)):
            decimal += int(integral[i]) * (8**i)

    if fractional:
        for i in range(len(fractional)):
            decimal += int(fractional[i]) * (1/(8**(1+i)))
    return decimal

def hexToDecimal(hex):
    hex = str(hex)

    hex_nos = {
        'a': '10',
        'b': '11',
        'c': '12',
        'd': '13',
        'e': '14',
        'f': '15',
    }
    
    if '.' in hex: integral, fractional = hex.split('.')
    else: 
        integral = hex
        fractional = 0

    if integral:
        integral = integral[::-1]

        decimal = 0
        for i in range(len(integral)):
            if integral[i].isalpha():
                j = hex_nos[integral[i]]
                decimal += int(j) * (16**i)
            else: 
                decimal += int(integral[i]) * (16**i)
            

    if fractional:
        for i in range(len(fractional)):
            if fractional[i].isalpha():
                j = hex_nos[fractional[i]]
                decimal += int(j) * (1/(16**(1+i)))
            else:
                decimal += int(fractional[i]) * (1/(16**(1+i)))

    return decimal
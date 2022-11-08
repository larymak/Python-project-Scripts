def decimalToBinary(decimal):
    decimal = str(decimal)
    if '.' in decimal: integral, fractional = decimal.split('.')
    else: 
        integral = decimal
        fractional = 0

    binaryNo = ''
    if integral:
        integral = int(integral)
        while integral > 0:
            binaryNo += str(integral % 2)
            integral = integral // 2
        
        binaryNo = binaryNo[::-1]

    if fractional:
        fractional = '0.' + fractional
        binaryNo += '.'
        for i in range(20):
            prod = float(fractional) * 2
            num = int(prod)
            fractional = prod - num
            binaryNo += str(num)

    return binaryNo

def octalToBinary(octal):
    octToBin = {
        '0': '000',
        '1': '001',
        '2': '010',
        '3': '011',
        '4': '100',
        '5': '101',
        '6': '110',
        '7': '111',
        '.': '.'
    }

    binary = ''
    for o in str(octal):
        try:
            binary += octToBin[o]
        except (KeyError, ValueError):
            return 'Invalid Input'
    return binary

def hexToBinary(hex):
    hexToBin = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'a': '1010',
        'b': '1011',
        'c': '1100',
        'd': '1101',
        'e': '1110',
        'f': '1111',
        '.': '.'
    }

    binary = ''
    for h in str(hex):
        try:
            if h.isalpha():
                h = h.lower()
            binary += hexToBin[h]
        except (KeyError, ValueError):
            return 'Invalid Input'
    return binary
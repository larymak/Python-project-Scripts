from tobinary import octalToBinary

def decimalToHex(decimal):
    binaryNo = ''

    hex_nos = {
        '10': 'a',
        '11': 'b',
        '12': 'c',
        '13': 'd',
        '14': 'e',
        '15': 'f',
    }

    decimal = str(decimal)
    if '.' in decimal: integral, fractional = decimal.split('.')
    else: 
        integral = decimal
        fractional = 0

    binaryNo = ''
    if integral:
        integral = int(integral)
        while integral > 0:
            rem = integral % 16 
            if rem >=10:
                rem = hex_nos[str(rem)]
            binaryNo += str(rem)
            integral = integral // 16
        
        binaryNo = binaryNo[::-1]

    if fractional:
        fractional = '0.' + fractional
        binaryNo += '.'
        for i in range(20):
            prod = float(fractional) * 16
            num = int(prod)
            fractional = prod - num
            if num >=10:
                num = hex_nos[str(num)]
            binaryNo += str(num)

    return binaryNo

def binaryToHex(binary):
    binToHex= {
        '0000': '0',
        '0001': '1',
        '0010': '2',
        '0011': '3',
        '0100': '4',
        '0101': '5',
        '0110': '6',
        '0111': '7',
        '1000': '8',
        '1001': '9',
        '1010': 'a',
        '1011': 'b',
        '1100': 'c',
        '1101': 'd',
        '1110': 'e',
        '1111': 'f',
        '.': '.'
    }

    binary = str(binary)
    if '.' in binary: integral, fractional = binary.split('.')
    else: 
        integral = binary
        fractional = 0

    if integral:
        if len(integral) % 4 == 1:
            integral = '000' + integral
        if len(integral) % 4 == 2:
            integral = '00' + integral
        if len(integral) % 4 == 3:
            integral = '0' + integral

        groups = []
        bno = ''
        for i in range(len(integral)+1):
            if len(bno) < 4:
                bno += integral[i]
            else:
                groups.append(bno)
                try: bno = integral[i]
                except IndexError: pass
        
        hex = ''
        for g in groups:
            try:
                hex += binToHex[g]
            except (KeyError, ValueError):
                return 'Invalid Input'
    
    if fractional:

        if len(fractional) % 4 == 1:
            fractional += '000'
        if len(fractional) % 4 == 2:
            fractional += '00'
        if len(fractional) % 4 == 3:
            fractional += '0'

        groups = []
        bno = ''
        for i in range(len(fractional)+1):
            if len(bno) < 4:
                bno += fractional[i]
            else: 
                groups.append(bno)
                try: bno = fractional[i]
                except IndexError: pass

        hex += '.'
        for g in groups:
            try:
                hex += binToHex[g]
            except (KeyError, ValueError):
                return 'Invalid Input'

    return hex

def octalToHex(octal):
    binary = octalToBinary(octal)
    return binaryToHex(binary)
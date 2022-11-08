from tobinary import hexToBinary

def decimalToOctal(decimal):
    decimal = str(decimal)
    if '.' in decimal: integral, fractional = decimal.split('.')
    else: 
        integral = decimal
        fractional = 0

    binaryNo = ''
    if integral:
        integral = int(integral)
        while integral > 0:
            binaryNo += str(integral % 8)
            integral = integral // 8
        
        binaryNo = binaryNo[::-1]

    if fractional:
        fractional = '0.' + fractional
        binaryNo += '.'
        for i in range(20):
            prod = float(fractional) * 8
            num = int(prod)
            fractional = prod - num
            binaryNo += str(num)

    return binaryNo

def binaryToOctal(binary):
    binToOct = {
        '000': '0',
        '001': '1',
        '010': '2',
        '011': '3',
        '100': '4',
        '101': '5',
        '110': '6',
        '111': '7',
    }

    binary = str(binary)
    if '.' in binary: integral, fractional = binary.split('.')
    else: 
        integral = binary
        fractional = 0

    if integral:
        if len(integral) % 3 == 1:
            integral = '00' + integral
        if len(integral) % 3 == 2:
            integral = '0' + integral

        groups = []
        bno = ''
        for i in range(len(integral)+1):
            if len(bno) < 3:
                bno += integral[i]
            else:
                groups.append(bno)
                try: bno = integral[i]
                except IndexError: pass
        
        octal = ''
        for g in groups:
            try:
                octal += binToOct[g]
            except (KeyError, ValueError):
                return 'Invalid Input'
    
    if fractional:

        if len(fractional) % 3 == 1:
            fractional += '00'
        if len(fractional) % 3 == 2:
            fractional += '0'

        groups = []
        bno = ''
        for i in range(len(fractional)+1):
            if len(bno) < 3:
                bno += fractional[i]
            else: 
                groups.append(bno)
                try: bno = fractional[i]
                except IndexError: pass

        octal += '.'
        for g in groups:
            try:
                octal += binToOct[g]
            except (KeyError, ValueError):
                return 'Invalid Input'

    return octal

def hexToOctal(hex):
    binary = hexToBinary(hex) 
    return binaryToOctal(binary)


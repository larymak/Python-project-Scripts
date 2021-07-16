import os,sys
currentdir=os.path.dirname(os.path.realpath(__file__))
parentdir=os.path.dirname(currentdir)
sys.path.append(parentdir)
hda='0123456789abcdef';b64t="""ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"""
fn=f'{currentdir}/log.txt';fh=open(fn,'w');fh.close();fh=open(fn,'r+')
def hextodec(s):
    l,h=[],list(s)
    while len(h)>0:
        hp=''.join(h[:2]);fh.write(f'Parsed hex pair {hp}\n')
        l.append(hp);h=h[2:]
    fh.write(f'----List of parsed hex pairs is {l}\n')
    dl=[]
    for p in l:
        dcp=list(p.lower())
        fh.write(f'\tLowercase pair list is {dcp}\n')
        dcp.reverse()
        fh.write(f'\tReversed list is {dcp}\n')
        t=0
        for c in dcp:
            fh.write(f'\t\t{hda.index(c)} is index of character in hda list\n')
            fh.write(f'\t\t{dcp.index(c)} is index of character in input\n')
            fh.write(f'\t----{16**dcp.index(c)} is 16 to the power of the index of the character in the input\n')
            fh.write(f'----Equation will be {hda.index(c)}*{16**dcp.index(c)}\n')
            t+=((hda.index(c))*(16**dcp.index(c)))
            fh.write(f'----Running total is {t}\n')
        t=str(t)
        fh.write(f'\t\t----{t} is decimal conversion\n')
        dl.append(t)
    fh.write(f'____{dl} is list of decimal conversions\n')
    bl=[]
    for n in dl:
        bc=''.join(list(f'{int(n):08b}'))
        fh.write(f'{bc} is binary conversion of decimal\n')
        bl.append(bc)
    bl=''.join(bl)
    for i in range(2):
        if not len(bl)%6==0:
            bl=list(bl)
            bl.append('00')
            bl=''.join(bl)
    sb=[]
    while len(bl)>0:
        w,bl=bl[:6],bl[6:]
        w=''.join(w)
        fh.write(f'-Parsed 6-bit word {w}\n')
        sb.append(w)
    fdl=[]
    for i in sb:
        fd=str(int(i,2))
        fh.write(f'{fd}\tis decimal conversion of 6-bit word {i}\n')
        fdl.append(fd)
    fl=[]
    for i in fdl:
        c=str(b64t[int(i)])
        fh.write(f'\t{i} is decimal in list to convert using base64 table\n')
        fh.write(f'\t----{c} is final character in base64 list using decimal conversion of 6-bit binary word as index\n')
        fl.append(c)
    fw=list(''.join(fl))
    for i in range(3):
        if not len(fw)%4==0:fw.append('=')
    fw=''.join(fw)
    fh.write(f'{fw} is base64 conversion of {s}\n')
    return fw
print(hextodec(input('')))
from playsound import playsound
playsound('0.mp3')                   
sufix='KQkq'
past='rnbkqbnr/1p1pp1pp/8/p1p2p2/1P1PP1PP/8/P1P2P2/RNBKQBNR'
no=0
def extend(s):
    atem1=''
    for iii in s:
        if ord(iii)>=49 and ord(iii)<=57:
                atem1+='o'*int(iii)
        else:
            atem1+=iii
    return atem1
tem=extend(past).split('/')
tem2=extend('r3qbnr/1p1p2p1/8/p1p1pp1p/1PPPP1PP/8/P4P2/RNBKQBNR').split('/')
if tem[0][3]!=tem2[0][3]and sufix!='':
    sufix=sufix.replace('k','').replace('q','')
if tem[7][3]!=tem2[7][3]and sufix!='':
    sufix=sufix.replace('K','').replace('Q','')
if tem[0][0]!=tem2[0][0] and 'k' in sufix:
    sufix=sufix.replace('k','')
if tem[0][7]!=tem2[0][7] and 'q' in sufix:
    sufix=sufix.replace('q','')
if tem[7][0]!=tem[7][0]and 'K' in sufix:
    sufix=sufix.replace('K','')
if tem[7][7]!=tem[7][7]and 'Q' in sufix:
    sufix=sufix.replace('Q','')
alf=['a','b','c','d','e','f','g','h']

geto='-'




if tem[1].count('p')+tem[3].count('p')==tem2[1].count('p')+tem2[3].count('p'):
    print('in')
    atem=''
    for ip in tem[1]:
        if ord(ip)>=49 and ord(ip)<=57:
            atem+='o'*int(ip)
        elif ip=='p':
            atem+='p'
        else:
            atem+=ip
    btem=''
    for ip in tem2[1]:
        if ord(ip)>=49 and ord(ip)<=57:
            
            btem+='o'*int(ip)
        elif ip=='p':
            btem+='p'
        else:
            btem+=ip
    for ig in range(8):
        if atem[ig] =='p' and  btem[ig]!='p':
            geto=alf[ig]+'6'
if tem[6].count('P')+tem[4].count('P')==tem2[6].count('P')+tem2[4].count('P'):
    atem=''
    for ip in tem[6]:
        if ord(ip)>=49 and ord(ip)<=57:
            atem+='o'*int(ip)
        elif ip=='p':
            atem+='p'
        else:
            atem+=ip
    btem=''
    for i in tem2[6]:
        if ord(i)>=49 and ord(ip)<=57:
            
            btem+='o'*int(ip)
        elif ip=='P':
            btem+='P'
        else:
            btem+=ip
    for ig in range(8):
        if atem[ig] =='P' and  btem[ig]!='P':
            geto=alf[ig]+'4'

print(sufix,geto)

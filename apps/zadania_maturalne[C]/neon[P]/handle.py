alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def handle(txt, y):
    x = y.split(" ")
    if x[0]=="DOPISZ":
        txt+=x[1]
    elif x[0]=="USUN":
        txt = txt[0:len(txt)-int(x[1])]
    elif x[0]=="ZMIEN":
        txt = txt[0:len(txt)-len(x[1])]
        txt+=x[1]
    elif x[0]=="PRZESUN":
        ind = alph.index(x[1])+1
        if ind>=len(alph):
            ind=0
        txt = txt.replace(x[1], alph[ind], 1)
    return txt
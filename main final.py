ni = ''

x = int(input())
nn = x

while True :
    nn = int(nn)


    if nn == 0 :
        nf = list(reversed(ni))
        nfr = ni[::-1]
        print(nfr)
        break

    elif((nn % 2) == 0) :
        ni = ni+'0'
        nn = nn/2


    else :
        ni = ni + '1'
        nn = (nn - 1)/2
    

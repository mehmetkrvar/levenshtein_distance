import numpy
def minimum(a,b,c):
    if a<=b and a<=c:
        return a
    if b<=c and b<=a:
        return b
    if c<=b and c<=a:
        return c

def max(a,b):
    if(a<b):
        return b
    else:
        return a
    
def normalize(X,size):
    if len(X) < size:
        fark = size - len(X)
        for i in range(fark):
            X=X+" "
    return X
def levenshteinMesafesi(A,B):
    K=numpy.zeros((len(A)+1,len(B) +1))
    A_len=len(A)
    B_len=len(B)
    for i in range(A_len):
        K[i][0]
    for i in range(B_len):
        K[0][i]
    silme=0
    ekleme=0
    yerdegistirme=0
    for i in range(1,A_len+1):
        for j in range(1,B_len+1):
            if A[i-1]==B[j-1]:
                K[i][j]=K[i-1][j-1]
            else:
                silme = K[i-1][j]+1
                ekleme=K[i][j-1]+1
                yerdegistirme=K[i-1][j-1]+1
                K[i][j] = minimum(silme,ekleme,yerdegistirme)
    return K[B_len-1][A_len-1]


print("1. kelimeyi girin")
kelime_1=input()
print("2. kelimeyi girin")
kelime_2=input()
max_len=max(len(kelime_1),len(kelime_2))
kelime_1=normalize(kelime_1,max_len)
kelime_2=normalize(kelime_2,max_len)
mesafe=levenshteinMesafesi(kelime_1,kelime_2)

print("1. ve 2. kelime arası mesafe : ")
print(mesafe)
benzerlik_oran=(max_len-mesafe)/max_len
print("1. ve 2. kelime arası benzerlik oranı :")
print(benzerlik_oran)
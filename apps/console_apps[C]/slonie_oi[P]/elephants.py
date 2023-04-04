#################################
#                               #
#   n - liczba słoni            #
#   m - masy słoni              #
#   a - aktualne ustawienie     #
#   b - docelowe ustawienie     #
#                               #
#################################
    

try:
    n = int(input(""))
    m = list(map(int, input("").strip().split(" ")))
    a = list(map(int, input("").strip().split(" ")))
    b = list(map(int, input("").strip().split(" ")))
except:
    print(0)
    exit()

#suma wysiłków
sum = 0

#kopia ustawienia początkowego (po to żeby nie modyfikować oryginalnej tablicy)
cur_cycle = a.copy()

#cykle
cc = []

#zamiana tablicy aktualnego ustawienia słoni na pojedyńcze cykle 
while (len(cur_cycle) != 0):
    cc_cur = []
    cur = cur_cycle[0]
    first_c = cur
    firstIndex = 0
    while (True):
        if (cur == first_c):
            firstIndex += 1
        if (firstIndex == 2):
            #złamanie loopa w momencie powrotu do początku cyklu po raz 2 (pierwszy odbywa się przy starcie pętli)
            break
        cc_cur.append(cur)
        cur_cycle.remove(cur)
        cur = a[b.index(cur)]
    cc.append(cc_cur)

#obliczenie sumy wartości wysiłku każdego cyklu
for x in cc:
    h = []
    z = []

    for k in a:
        h.append(m[k-1])
    for k in x:
        z.append(m[k-1])

    #suma wag w cyklu
    sum_x = 0
    
    #minimalna waga słonia z całości
    min_a = min(h)

    #minimalna waga w cyklu
    min_x = min(z)

    for k in x:
        sum_x += m[k-1]

    m1 = sum_x+(len(x)-2)*min_x
    m2 = sum_x+min_x+(len(x)+1)*min_a

    #dodanie mniejszej z sum (spośród 2 metod powyżej) poszczególnych cyklów do wyniku całościowego
    sum += min(m1, m2)

print(sum)
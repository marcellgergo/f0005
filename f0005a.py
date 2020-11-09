gondolt_szám = 4
tipp = input('Szerinted melyik számra gondolok 1 és 5 között? ')
tipp = int(tipp)
if gondolt_szám == tipp: # a gondolt szám egyenlő a tippel?
    print('Eltaláltad!')
    print('Kis ügyes!')
else: #különben
    print('Ez most sajnos nem sikerült...')
    print('De majd legközelebb... talán... ha nagyobb szerencséd lesz...')
print('Pápá!')
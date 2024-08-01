numtup = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

print(numtup[-4])
print(numtup[7])
print(numtup[:11:3])
print(numtup[-1:-4])

dct = {}
dct["I"] = 'watashi','atashi', 'me', 'my'
dct["mother"] = 'okasan','kachan', 'mother', 'mom'
dct["father"] = 'otosan', 'tochan', 'father', 'dad'

dct.setdefault('like',('suki','daisuki', 'enjoy', 'crush'))

dct.setdefault('friend',('yuujin', 'tomodachi', 'homie', 'buddy'))


for x in dct.values():
    print(type(x))
    

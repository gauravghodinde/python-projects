tic = {'tl':' ','tm':' ','tr':' ',
       'ml':' ','mm':' ','mr':' ',
       'll':' ','lm':' ','lr':' '}

def toc(h):
    print(h['tl']+ '|' +h['tm']+'|'+h['tr'])
    print('-+-+-')
    print(h['ml']+ '|' +h['mm']+'|'+h['mr'])
    print('-+-+-')
    print(h['ll']+ '|' +h['lm']+'|'+h['lr'])

toc(tic)

print('welcome to my first game,\nthis is an tic tac toe game,\nhope you will enjoy this game,\nplease support me so i can make more games')
print(             )
print('NOTE:for top left(tl) | top middle(tm)   | top right(tr)\n------------------------------------------------------------------\n   for middle left(ml)| middle middle(mm)| middle right(mr)\n-------------------------------------------------------------\n     for low left(ll) | low middle(lm)   | low left(ll)')
chance = 'X'
for i in range(9):
    toc(tic)
    print('it\'s turn for ' + chance + '\n move to which space?????')
    move = input()
    tic[move]=chance
    if chance=='X':
        chance='O'
    else:
        chance='X'
    if 'tl'=='mm'=='lr'=='X':
     break
    






















































































































































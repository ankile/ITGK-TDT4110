import fil
import bruker

print('Yo vil du laste inn et brett?')

brett = fil.load(input('Brettnavn: '))

print('Dette brettet ble lastet:')

bruker.print_board(brett)

print('\nvil du gjøre endringer på brettet?\n')

col = int(input('Hvilken kolonne vil du endre? '))
row = int(input('Hvilken rad vil du endre? '))
nytt_tall = int(input('Hva skal det nye tallet være? '))

brett[row - 1][col - 1] = nytt_tall

print('Ditt nye brett:\n')

bruker.print_board(brett)

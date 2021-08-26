import sys

logs = []

while True:
    action = input('Jaką akcję chcesz wykonać? (saldo/zakup/sprzedaż/stop)')
    if action == 'saldo':
        balance_change = int(input('Wprowadź kwotę o jaką zmienia się stan konta (w groszach). W przypadku wypłaty z konta poprzedź kwotę znakiem minus ("-"): '))
        comment = input('Komentarz do zmiany salda: ')
        logs.append(f'Saldo konta zmienione o {balance_change}, komentarz: {comment}')
        #print('saldo')
    elif action == 'zakup':
        product_id = input('Wprowadź nazwę produktu: ')
        price = int(input('Wprowadź cenę jednostkową produktu (w groszach): '))
        quantity = int(input('Wprowadź liczbę sztuk zakupionego produktu: '))
        logs.append(f'Zakupiono {quantity} szt. produktu {product_id} o wartości {price}gr/szt.')
        #print('zakup')
    elif action == 'sprzedaż':
        print('sprzedaż')
    elif action == 'stop':
        print('stop')
        break #przejscie do podsumowania
    else:
        print('Błąd: wybierz jedną z wymienionych akcji.')



if sys.argv[1] == 'saldo':
    logs.append(f'Zmiana saldo o: {sys.argv[2]} gr, komentarz: {sys.argv[3]}')

elif sys.argv[1] == 'sprzedaż':
    logs.append(f'Sprzedano {sys.argv[4]} szt. produktu {sys.argv[2]} o wartości {sys.argv[3]}gr/szt.')

elif sys.argv[1] == 'zakup':
    logs.append(f'Zakupiono {sys.argv[4]} szt. produktu {sys.argv[2]} o wartości {sys.argv[5]}gr/szt.')
print(logs)

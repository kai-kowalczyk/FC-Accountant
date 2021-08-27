import sys

logs = [] #historia operacji

account_balance = 2000.0 #Saldo poczatkowe

store = {
    'mleko': {'quantity': 20, 'price': 4.50},
    'parasol': {'quantity': 5, 'price': 25.00}
} #Magazyn sklepu

while True:
    action = input('Jaką akcję chcesz wykonać? (saldo/zakup/sprzedaz/stop)')
    if action == 'stop':
        print('Koniec działania programu!')
        break #przejscie do podsumowania
    elif action == 'saldo':
        balance_change = float(input('Wprowadź kwotę o jaką zmienia się stan konta. W przypadku wypłaty z konta poprzedź kwotę znakiem minus ("-"): '))
        comment = input('Komentarz do zmiany salda: ')
        if (balance_change < 0) and (account_balance + balance_change < 0):
            print('Za mało środków na koncie!')
        logs.append(f'Zmiana saldo o: {balance_change} zł, komentarz: {comment}')
        account_balance = account_balance + balance_change
    elif action == 'zakup':
        product_id = input('Wprowadź nazwę produktu: ')
        price = float(input('Wprowadź cenę jednostkową produktu: '))
        quantity = int(input('Wprowadź liczbę sztuk zakupionego produktu: '))
        logs.append(f'Zakupiono {quantity} szt. produktu {product_id} o wartości {price} zł/szt.')
    elif action == 'sprzedaz':
        product_id = input('Wprowadź nazwę produktu: ')
        price = int(input('Wprowadź cenę jednostkową produktu (w groszach): '))
        quantity = int(input('Wprowadź liczbę sztuk sprzedanego produktu: '))
        logs.append(f'Sprzedano {quantity} szt. produktu {product_id} o wartości {price}gr/szt.')
    else:
        print('Błąd: wybierz jedną z wymienionych akcji.')
        continue



if sys.argv[1] == 'saldo':
    logs.append(f'Zmiana saldo o: {sys.argv[2]} zł, komentarz: {sys.argv[3]}')

elif sys.argv[1] == 'sprzedaz':
    logs.append(f'Sprzedano {sys.argv[4]} szt. produktu {sys.argv[2]} o wartości {sys.argv[3]} zł/szt.')

elif sys.argv[1] == 'zakup':
    logs.append(f'Zakupiono {sys.argv[4]} szt. produktu {sys.argv[2]} o wartości {sys.argv[5]} zł/szt.')

elif sys.argv[1] == 'konto':
    print(f'Stan konta: {account_balance}')

elif sys.argv[1] == 'magazyn':
    print(store)

print(logs)

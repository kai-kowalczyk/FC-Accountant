import sys
ALLOWED_ACTIONS = ('saldo', 'zakup', 'sprzedaz', 'stop', 'konto', 'magazyn', 'przeglad')

mode = sys.argv[1]
logs = [] #historia operacji

account_balance = 2000.0 #saldo poczatkowe

store = {
    'mleko': {'quantity': 20, 'price': 4.50},
    'parasol': {'quantity': 5, 'price': 25.00}
} #magazyn sklepu

while True:
    action = input('Jaką akcję chcesz wykonać? (saldo/zakup/sprzedaz/stop)')

    if action not in ALLOWED_ACTIONS:
        print('Akcja niedozwolona! Wybierz jedną z wymienionych: saldo/zakup/sprzedaz/stop.')
        continue
    if action == 'stop':
        print('Koniec działania programu!')
        break #przejscie do podsumowania

    elif action == 'saldo':
        balance_change = float(input('Wprowadź kwotę o jaką zmienia się stan konta. W przypadku wypłaty z konta poprzedź kwotę znakiem minus ("-"): '))
        comment = input('Komentarz do zmiany salda: ')
        if (balance_change < 0) and (account_balance + balance_change < 0):
            print('Za mało środków na koncie!')
        logs.append(f'Zmiana saldo o: {balance_change} zł, komentarz: {comment}.')
        account_balance = account_balance + balance_change

    elif action == 'zakup':
        product_id = input('Wprowadź nazwę produktu: ')
        price = float(input('Wprowadź cenę jednostkową produktu: '))
        quantity = int(input('Wprowadź liczbę sztuk zakupionego produktu: '))
        total_price = price * quantity
        if total_price > account_balance:
            print(f'Za mało środków na koncie ({account_balance}), by zakupić produkty w cenie: {total_price}.')
            continue
        elif price < 0:
            print('Błąd! Cena musi być liczbą dodatnią.')
            continue
        elif quantity < 0:
            print('Błąd! Liczba sztuk produktu musi być większa od 0.')
            continue
        else:
            account_balance = account_balance - total_price
            if not store.get(product_id):
                store[product_id] = {'quantity': quantity, 'price': price}
            else:
                store_product_quantity = store[product_id]['quantity']
                store[product_id] = {'quantity': store_product_quantity + quantity, 'price': price}
        logs.append(f'Zakupiono {quantity} szt. produktu {product_id} o wartości {price} zł/szt.')

    elif action == 'sprzedaz':
        product_id = input('Wprowadź nazwę produktu: ')
        price = float(input('Wprowadź cenę jednostkową produktu: '))
        quantity = int(input('Wprowadź liczbę sztuk sprzedanego produktu: '))
        if not store.get(product_id):
            print('Brak produktu w magazynie!')
            continue
        elif store.get(product_id)['quantity'] < quantity:
            store_product_quantity = store(product_id)['quantity']
            print(f'Niewystarczająca ilość produktu w magazynie. Pozostało: {store_product_quantity} szt.')
            continue
        elif price < 0:
            print('Błąd! Cena musi być liczbą dodatnią.')
            continue
        elif quantity < 0:
            print('Błąd! Liczba sztuk produktu musi być większa od 0.')
            continue
        else:
            account_balance += quantity * price
            store[product_id] = {'quantity': store.get(product_id)['quantity'] - quantity, 'price': price}
        if store.get(product_id)['quantity'] == 0:
            del store[product_id]
        logs.append(f'Sprzedano {quantity} szt. produktu {product_id} o wartości {price} zł/szt.')



if mode == 'saldo':
    logs.append(f'Zmiana saldo o: {sys.argv[2]} zł, komentarz: {sys.argv[3]}')

elif mode == 'sprzedaz':
    logs.append(f'Sprzedano {sys.argv[4]} szt. produktu {sys.argv[2]} o wartości {sys.argv[3]} zł/szt.')

elif mode == 'zakup':
    logs.append(f'Zakupiono {sys.argv[4]} szt. produktu {sys.argv[2]} o wartości {sys.argv[5]} zł/szt.')

elif mode == 'konto':
    print(f'Stan konta: {account_balance}')

elif mode == 'magazyn':
    print(f'Stan magazynu: {store}')

elif mode == 'przeglad':
    print(f'Historia operacji: {logs}')

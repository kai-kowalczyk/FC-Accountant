import sys

action = input('Jaką akcję chcesz wykonać? (saldo/zakup/sprzedaż/stop)')
if action == 'saldo':
    print('saldo')
elif action == 'zakup':
    print('zakup')
elif action == 'sprzedaż':
    print('sprzedaż')
elif action == 'stop':
    print('stop')
else:
    print('Błąd: wybierz jedną z wymienionych akcji.')
    quit()


logs = []
if sys.argv[1] == 'saldo':
    logs.append(f'Zmiana saldo o: {sys.argv[2]} gr, komentarz: {sys.argv[3]}')

elif sys.argv[1] == 'sprzedaż':
    logs.append(f'Sprzedano {sys.argv[4]} szt. produktu {sys.argv[2]} o wartości {sys.argv[3]}gr/szt.')

elif sys.argv[1] == 'zakup':
    logs.append(f'Zakupiono {sys.argv[4]} szt. produktu {sys.argv[2]} o wartości {sys.argv[5]}gr/szt.')

print(logs)

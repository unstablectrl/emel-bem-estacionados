import requests

vouchers = set()

tries = {}
plates = set()
nifs = set()

with open('plates.txt', 'r') as f:
    for line in f:
        plates.add(line)

with open('nifs.txt', 'r') as f:
    for line in f:
        nifs.add(line)

dictionary = dict(zip(plates, nifs))


for key,val in dictionary.items():
    params = {'plate': key, 'nif': val}

    response = requests.post('http://bemestacionados.pt/Home/ConfirmPlate', data =params)
    voucher = response.json().get('voucher')
    print(voucher)
    if voucher:
        vouchers.add(voucher)

with open('vouchers.txt', 'a') as f:
    for v in vouchers:
        f.write(f'{v}\n')

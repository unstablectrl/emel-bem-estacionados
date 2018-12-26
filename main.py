import requests
from bs4 import BeautifulSoup
import string
import itertools

def generate_plates():
    alphabet = string.ascii_uppercase
    plates = []
    letters = list(map(lambda x: ''.join(x), itertools.product(string.ascii_uppercase, repeat=2)))
    numbers = list(map(lambda x: ''.join(str(y) for y in x) ,itertools.product(range(0, 10), repeat=4)))

    for i in range(3):
        for l in letters:
            for n in numbers:
                if i == 0:
                    plates.append(l+n)
                if i == 1:
                    plates.append(n[:2] + l + n[2:])
                if i == 2:
                    plates.append(n+l)

    with open('plates.txt', 'w') as f:
        for plate in plates:
            f.write(f'{plate}\n')



def nif_fresquinho():
    response = requests.get('https://nif.marcosantos.me/?i=2')
    content = response.content.decode('utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    nif = soup.find(id="nif").text
    return nif


def generate_nifs(n):
    nifs = []
    for i in range(n):
        nifs.append(nif_fresquinho())
    print(nifs)
    with open('nifs.txt', 'a') as f:
        for nif in nifs:
            f.write(f'{nif}\n')

def plate_quentinha():

    nif = '294382909'
    plate = '24BC01'
    response = requests.post('http://bemestacionados.pt/Home/ConfirmPlate', data = {'plate': plate, 'nif': nif})
    voucher = response.json().get('voucher')
    if voucher:
        voucher.append()

    with open('vouchers.txt', 'a') as f:
        for v in vouchers:
            f.write(f'{v}\n')


if __name__ == "__main__":
    pass

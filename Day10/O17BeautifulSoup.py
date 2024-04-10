
from bs4 import BeautifulSoup

with open("mypage.html", "r") as htmlFile:

    content = htmlFile.read()

    soup = BeautifulSoup(content, 'lxml')

    tag = soup.find('h5')
    print(tag)
    print("-" * 60)

    crdTitle= soup.findAll("h5")
    print(crdTitle)
    print("-" * 60)

    for ct in crdTitle:
        print(ct)

    print("-" * 60)
    cards = soup.findAll("div", class_="card")
    for card in cards:
        crd_title = card.h5.text
        price = card.a.text.split()[-1]
        print(f"Training on {crd_title} will cost {price}")
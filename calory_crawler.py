import requests
from lxml import html

from diet_planner import db
from models import *

for x in range(1, 10000):
    url = "https://kalkulatorkalorii.net/tabela-kalorii/{}/s-12".format(x)
    page = requests.get(url)
    tree = html.fromstring(page.content)
    products = tree.xpath(".//table/tbody/tr")
    if not products:
        break
    for product in products:
        name = product[0][0].text.strip()
        calories = int(product[1].text.strip())
        print("{} {}".format(name, calories))
        if not db.session.query(Product).filter_by(name=name).scalar():
            record = Product(
                name=name,
                calories=calories
            )
            db.session.add(record)
            db.session.commit()
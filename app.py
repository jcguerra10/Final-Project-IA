from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import copy
import re

app = Flask(__name__)

df = pd.read_excel("online_retail_II.xlsx")

products = df['Description'].tolist()
products = pd.DataFrame(products).drop_duplicates().values
products = products.tolist()
products = [item for sublist in products for item in sublist]
print(products)


@app.route('/')
def hello_world():
    q = request.args.get('search')
    print(q)
    if q:
        list_products = []
        for i in products:
            temp = str(i)
            if q in temp:
                list_products.append(temp)
    else:
        list_products = products[1:51]
    print(list_products)
    return render_template("home.html", len=len(list_products), products=list_products)


@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    print("----")
    prd = request.form['prd']
    print(prd)
    print("----")
    return render_template("recommendation.html", name_product=prd)


# @app.route('/search')
# def search():
#     txt_search = request.form['search']
#     list_products = list(filter(lambda x: txt_search in x, products))
#     if len(list_products) > 50:
#         list_products = list_products[1:51]
#     return render_template("home.html", len=len(list_products), products=list_products)


if __name__ == '__main__':
    app.run()

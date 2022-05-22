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
list_products: list
r_products = []


@app.route('/')
def hello_world():
    q = request.args.get('search')
    print(q)
    global list_products
    if q:
        list_products = []
        for i in products:
            temp = str(i)
            if q in temp:
                list_products.append(temp)
    else:
        list_products = products[0:50]
    print(list_products)
    return render_template("home.html", len=len(list_products), products=list_products)


@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    print("----")
    global list_products
    global r_products
    i = request.form['i']
    i = int(i)
    print(i)
    print("----")
    return render_template("recommendation.html", len=len(r_products), name_product=list_products[i], r_products=r_products)


if __name__ == '__main__':
    app.run()

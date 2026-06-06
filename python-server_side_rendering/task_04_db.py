from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# ---------- JSON ----------
def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

# ---------- CSV ----------
def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

# ---------- SQL ----------
def read_sql():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()

    return [
        {"id": r[0], "name": r[1], "category": r[2], "price": r[3]}
        for r in rows
    ]


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html',
                               error="Wrong source",
                               products=[])

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        try:
            data = read_sql()
        except:
            return render_template('product_display.html',
                                   error="Database error",
                                   products=[])

    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if p["id"] == product_id]
        except:
            data = []

        if not data:
            return render_template('product_display.html',
                                   error="Product not found",
                                   products=[])

    return render_template('product_display.html',
                           products=data,
                           error=None)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
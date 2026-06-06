from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# ---------- JSON reader ----------
def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

# ---------- CSV reader ----------
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


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # ---------- ERROR 1: invalid source ----------
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source", products=[])

    # ---------- load data ----------
    if source == 'json':
        data = read_json()
    else:
        data = read_csv()

    # ---------- filter by id ----------
    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if p["id"] == product_id]
        except:
            data = []

        if not data:
            return render_template('product_display.html', error="Product not found", products=[])

    return render_template('product_display.html', products=data, error=None)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
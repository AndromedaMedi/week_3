from app import app
from flask import render_template
from models.order_list import orders

@app.route('/')
def index():
    return "Welcome to bakery orders!"

@app.route('/orders')
def show_orders():
    return render_template('index.html', title="Bakery", orders=orders)

@app.route('/orders/<int:order_id>')
def show_single_order(order_id):
    chosen_order = orders[order_id]
    return render_template('order.html', order=chosen_order)
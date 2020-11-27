
from flask import Flask, request, jsonify
import  products_dao

app = Flask(__name__)

@app.route('/getProducts', methods=['GET'])
def get_products():



if __name__ == '__main__':
    print("Starting Python Flask Server for Grocery Management System")
    app.run(port=5000)

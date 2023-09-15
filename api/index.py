from flask import Flask, jsonify, request, make_response
from model import Data

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/get_company', methods=['GET'])
def get_company():
    
    company_id =  request.args.get("company_id")
    
    try:
        dt = Data()
        values = ()
        if request.method == "GET":
            if company_id:
                query = "SELECT * FROM company where company_id = %s"
                values = (company_id,)
            else:
                query =  "SELECT * FROM company"

        data = dt.get_data(query, values)
             

    except Exception as e:
        return make_response(jsonify({
            "status" : "FAILED",
            "error" : str(e)}), 400)
    
    return make_response(jsonify({
        "status" : "SUCCESS",
        "data" : str(data)}), 200)


@app.route('/add_company', methods=['POST'])
def add_company():
    
    dataInput = request.json
    

    companyName = dataInput["company_name"]
    
    try:
        dt = Data()
        values = ()
        if request.method == "POST":
            
                query = "INSERT INTO company (name) values (%s)"
                values = [companyName]

        dt.insert_data(query, values)
             

    except Exception as e:
        return make_response(jsonify({
            "status" : "FAILED",
            "error" : str(e)}), 400)
    
    return make_response(jsonify({
        "status" : "SUCCESS",
        "data" : "Berhasil Menambahkan company"}), 200)


@app.route('/delete_company', methods=['POST'])
def delete_company():
    
    company_id =  request.args.get("company_id")
    
    try:
        dt = Data()
        values = ()
        if request.method == "POST":
            if company_id:
                query = "DELETE FROM company where company_id = %s"
                values = (company_id,)
            else:
                return make_response(jsonify({
            "status" : "FAILED",
            "result" : "Company Id Kosong"}))

        dt.insert_data(query, values)    
             

    except Exception as e:
        return make_response(jsonify({
            "status" : "FAILED",
            "error" : str(e)}), 400)
    
    return make_response(jsonify({
        "status" : "SUCCESS",
        "data" : "Berhasil Menghapus Company"}))





@app.route('/get_product', methods=['GET'])
def get_product():
    
    product_id =  request.args.get("product_id")
    
    try:
        dt = Data()
        values = ()
        if request.method == "GET":
            if product_id:
                query = "SELECT * FROM product where product_id = %s"
                values = (product_id,)
            else:
                query =  "SELECT * FROM product"

        data = dt.get_data(query, values)
             

    except Exception as e:
        return make_response(jsonify({
            "status" : "FAILED",
            "error" : str(e)}), 400)
    
    return make_response(jsonify({
        "status" : "SUCCESS",
        "data" : str(data)}), 200)


@app.route('/add_product', methods=['POST'])
def add_product():
    
    dataInput = request.json
    

    productName = dataInput["product_name"]
    
    try:
        dt = Data()
        values = ()
        if request.method == "POST":
            
                query = "INSERT INTO product (name) values (%s)"
                values = [productName]

        dt.insert_data(query, values)
             

    except Exception as e:
        return make_response(jsonify({
            "status" : "FAILED",
            "error" : str(e)}), 400)
    
    return make_response(jsonify({
        "status" : "SUCCESS",
        "data" : "Berhasil Menambahkan product"}), 200)


@app.route('/delete_product', methods=['POST'])
def delete_product():
    
    product_id =  request.args.get("product_id")
    
    try:
        dt = Data()
        values = ()
        if request.method == "POST":
            if product_id:
                query = "DELETE FROM company where product_id = %s"
                values = (product_id,)
            else:
                return make_response(jsonify({
            "status" : "FAILED",
            "result" : "Product Id Kosong"}))

        dt.insert_data(query, values)    
             

    except Exception as e:
        return make_response(jsonify({
            "status" : "FAILED",
            "error" : str(e)}), 400)
    
    return make_response(jsonify({
        "status" : "SUCCESS",
        "data" : "Berhasil Menghapus Product"}))





app.run()
from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/get_company', methods=['GET'])
def get_company():
    
    company_id =  request.args.get("company_id")
    
    # try:
    #     dt = Data()
    #     values = ()
    #     if request.method == "GET":
    #         if company_id:
    #             query = "SELECT * FROM company where company_id = %s"
    #             values = (company_id,)
    #         else:
    #             query =  "SELECT * FROM company"

    #     data = dt.get_data(query, values)
             

    # except Exception as e:
    #     return make_response(jsonify({
    #         "status" : "FAILED",
            # "error" : str(e)}), 400)
    
    return make_response(jsonify({
        "status" : "SUCCESS",
        "data" : company_id}), 200)
from flask import Flask, request, make_response, jsonify

app = Flask(__name__, instance_relative_config=True)
from functools import reduce
import operator
import os
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('/add')
@api.param('a', "First Number", type = float)
@api.param('b', "Second Number", type = float)

class Add(Resource):
    def get(self):
        a = request.args.get('a', type=float)
        b = request.args.get('b', type=float)
        if a and b:
            return make_response(jsonify(s=a+b), 200) #HTTP 200 OK
        else:
            return make_response('Invalid input\n', 400) #HTTP 400 BAD REQUEST
        
    
@api.route('/upper')
@api.param('a', "The String", type=str)
class Upper(Resource):
    def get(self):
        a = request.args.get('a', type=str)
        if a:
            return make_response(jsonify(s=a.upper()), 200) 
        else: 
            return make_response('Invalid Input\n', 400)

# @api.route('/lower')
# def lower():
#     a = request.args.get('a', type=str)
#     if a:
#         return make_response(jsonify(a.lower()), 200) 
#     else: 
#         return make_response('Invalid Input\n', 400)
    
# @api.route('/concat')
# def concat():
#     a = request.args.get('a', type=str)
#     b = request.args.get('b', type=str)
#     if a and b:
#         return make_response(jsonify(a+b), 200) 
#     else: 
#         return make_response('Invalid Input\n', 400)
    
# @api.route('/reduce')
# def reduce_op():
#     op = request.args.get('op', type=str)
#     lst = request.args.get('lst', type=str)
    
#     if not op or not lst:
#         return make_response('Invalid Input\n', 400)
#     try:
#         # Example: 'lst=[2,1,3,4]' will become [2,1,3,4]
#         lst = eval(lst)
#         if not isinstance(lst, list):
#             raise ValueError
#     except:
#         return make_response('Invalid List Format\n', 400)

#     if op == "add":
#         result = reduce(operator.add, lst)
 
#     elif op == 'sub': 
#         result = reduce(operator.sub, lst)
        
#     elif op == 'mul': 
#         result = reduce(operator.mul, lst)
    
#     elif op == 'div': 
#         try:
#             result = reduce(operator.truediv, lst)
        
#         except ZeroDivisionError:
#             return make_response('Division by zero is not allowed\n', 400)
             
#     else:
#         return make_response('Invalid Operation\n', 400)
    
#     return make_response(jsonify(s=result), 200)

# @api.route('/crash/')
# def crash(): 
#     h = request.host
#     if h:
#         response=  make_response(jsonify(host=h), 200)

#         # time.sleep(30)

#         os._exit(0)

#         return response
#     else:
#         return make_response('Invalid Input\n', 400)
    
    

    
  

#Endpoint /sub for subtraction which takes a and b as query parameters.

#Endpoint /mul for multiplication which takes a and b as query parameters.

#Endpoint /div for division which takes a and b as query parameters. Returns HTTP 400 BAD REQUEST also for division by zero.

#Endpoint /mod for modulo which takes a and b as query parameters. Returns HTTP 400 BAD REQUEST also for division by zero.

#Endpoint /random which takes a and b as query parameters and returns a random number between a and b included. Returns HTTP 400 BAD REQUEST if a is greater than b.

if __name__ == '__main__':
    app.run(debug=True)
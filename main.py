import csv
from flask import Flask, jsonify, make_response
from flask_httpauth import HTTPBasicAuth
from io import StringIO

app = Flask(__name__)

auth = HTTPBasicAuth()

fruitlist = ['apple', 'banana', 'cherry']

with open('data/official_fruit_list.txt', 'r') as wikipedia_file:
    official_fruits = [str(i).lower()[:-1] for i in  # [:-1] to remove \n
                       wikipedia_file.readlines()]


@auth.get_password
def get_password( username ):
    if username == 'miguel':
        return 'python'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


@app.route('/showlist')
def show_list():
    # TODO: Add containing braces with 'Top Fruits' from requirements
    return jsonify(fruitlist)


@app.route('/add/<string:p_input>')
@auth.login_required
def add_fruit( p_input ):

    """ add fruit to list, either singleton or csv series """

    # iterate through comma-separated adds
    f = StringIO(p_input)
    reader = csv.reader(f, delimiter=',')
    _input_items = [i for i in reader]
    if len(_input_items) > 10:
        return 'Sorry. You can only add 10 comma-separated fruit names.' \
               'You entered ' + str(len(_input_items)) + '.'
    for item in _input_items:  # [0] to get inner nested list
        # TODO: add handling for case where item is already on list
        if str(item).lower() in official_fruits:
            fruitlist.append(str(item))
        else:
            return str(item) + ' is not an official fruit.<br />'

    return jsonify(fruitlist)

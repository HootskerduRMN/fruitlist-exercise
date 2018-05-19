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
print(official_fruits)

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
    print('input_items:', _input_items)
    if len(_input_items) > 10:
        return 'Sorry. You can only add 10 comma-separated fruit names.' \
               'You entered ' + str(len(_input_items)) + '.'
    for item in _input_items:  # [0] to get inner nested list
        # TODO: add handling for case where item is already on list
        print('item:', item)
        print('str(item[0]).lower() ', str(item[0]).lower())
        if str(item[0]).lower() in official_fruits:
            fruitlist.append(str(item))
        else:
            return str(item) + ' is not an official fruit.<br />'

    return jsonify(fruitlist)


@app.route('/delete/<string:p_input>')
@auth.login_required
def delete_fruit( p_input ):
    """ delete fruit item from list by name or index number """

    try:
        p_input_int = int(p_input)
        # handle index is out-of-bounds case
        if p_input_int < 1 or p_input_int > len(fruitlist):
            return 'Please enter a list number between 1 and ' + \
                   str(len(fruitlist)) + '.'
        else:  # valid index
            print('p_input_int', p_input_int)
            print('fruitlist[p_input_int - 1', fruitlist[p_input_int - 1])
            del fruitlist[p_input_int - 1]
    except (ValueError, TypeError):  # input not int, but string value
        try:
            fruitlist.remove(p_input)
        except(ValueError, TypeError):
            # entered fruitname not in list
            return 'Please enter the name of a fruit on  the list.'

    return jsonify(fruitlist)

"""
Script that uses the bottle microframework to show, add, and delete
individual fruit items from a list using API calls
"""

# TODO: add docstrings on class and functions
from bottle import route, run
import csv
from io import StringIO
import json

# TODO: Make script a class with separate main() and test() fns and exec as instance
# TODO: refactor to remove coupling by adding fruitlist as parameter passed in and reset; yes, I agree, this current global use of fruitlist is very suboptimal
# TODO: structure all error messages to render in same schema as show_list
# TODO: master opportunities to convert several for loops to comprehensions

# seed initial tightly-coupled list of fruit dictionary items with {rank: fruitname}
fruitlist = [{'1': 'Blackberry'}, {'2': 'Persimmon'}, {'3': 'Blueberry'}]


def format_json( p_json ):
    return json.dumps(p_json, sort_keys=True, indent=4,
                      separators=(',', ': '))


@route('/showlist')  # decorator for bottle to bind path to this function
def show_list():
    """returns ordered list of fruits as JSON"""
    _result = {"Top Fruits": fruitlist}
    return format_json(_result)


@route('/delete/<p_input>')  # bottle decorator allowing for variable input
def delete_fruit( p_input ):
    """ delete fruit item from list by name or index number """

    # create working copy of fruitlist
    global fruitlist
    _fruitlist = fruitlist

    # is the parameter a number?
    try:
        p_input_int = int(p_input)
        # handle index is out-of-bounds case
        if p_input_int < 1 or p_input_int > len(_fruitlist):
            return 'Please enter a list number between 1 and ' + \
                   str(len(_fruitlist)) + '.'
        else:  # valid index
            _scrubbed_fruitlist_by_number = []
            counter_number = 1
            for item in _fruitlist:
                for k, v in item.items():
                    if int(p_input) != int(k):  # only add ones not
                        # marked for deletion
                        _scrubbed_fruitlist_by_number.append(
                            {str(counter_number): v})
                        counter_number += 1
        _fruitlist = _scrubbed_fruitlist_by_number
    except (ValueError, TypeError):  # not deleting by index,
        # but by string of fruitname
        # generate list of fruit names
        _fruitnames = []
        for item in _fruitlist:
            for k, v in item.items():
                _fruitnames.append(v)
        if any(p_input.lower() == val.lower() for val in _fruitnames):
            _scrubbed_fruitlist_by_name = []
            counter = 1
            for item in _fruitlist:
                for k, v in item.items():
                    if p_input.lower() != v.lower():  # do not delete
                        _scrubbed_fruitlist_by_name.append({str(counter): v})
                        counter += 1
            _fruitlist = _scrubbed_fruitlist_by_name
        else:
            # entered fruitname not in list
            return 'Please enter the name of a fruit on  the list.'

    # assign working copy to global
    fruitlist = _fruitlist

    return 'The new list is now: ' + show_list()


@route('/add/<p_input>')
def add_fruit( p_input ):
    """ add fruit to list, either singleton or csv series """

    # create working copy of fruitlist
    global fruitlist
    _fruitlist = fruitlist

    # get fruit validator data
    official_fruits = []
    with open('data/official_fruit_list.txt', 'r') as wikipedia_file:
        official_fruits = [str(i).lower()[:-1] for i in  # [:-1] to remove \n
                           wikipedia_file.readlines()]

    # iterate through comma-separated adds
    f = StringIO(p_input)
    reader = csv.reader(f, delimiter=',')
    _input_items = [i for i in reader]
    if len(_input_items) > 10:
        return 'Sorry. You can only add 10 comma-separated fruit names.' \
               'You entered ' + str(len(_input_items)) + '.'
    _processing_output = ''
    for item in _input_items[0]:  # [0] to get inner nested list
        # TODO: add handling for case where item is already on list
        if str(item).lower() in official_fruits:
            _fruitlist_count = len(_fruitlist)
            _fruitlist.append({str(_fruitlist_count + 1): str(item)})
        else:
            _processing_output += str(item) + ' is not an official fruit.<br />'

    _processing_output += '<br />Current fruitlist is: ' + format_json(
        _fruitlist)

    fruitlist = _fruitlist
    return _processing_output


run()

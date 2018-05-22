## Fruitlist API ##

This API allows for the simple management of a list of fruits.

It runs using the flask microframework<sup>1</sup> on Python 3, and when app.py is run, you can access the API with `curl http://127.0.0.1:5000/showlist`

There are five calls you can make by suffixing the root:

1. **showlist** will return a list of all fruits in ranked order.
> `curl http://127.0.0.1:5000/showlist`

2. **add** will add a fruit to the bottom of the list. Note the following usages:
* only valid fruits<sup>2</sup> are allowed
* a single fruit can be added, e.g.:
> `curl http://127.0.0.1:5000/add/banana`
* up to ten multiple fruits can be added in csv format (no spaces), e.g.,:
> `curl http://127.0.0.1:5000/add/apple,banana,persimmon`

3. **delete** will remove a current fruit on the list, either by index number or by name. Thus for a three-item fruitlist of `['apple','banana', 'cantelope']`, one could remove `banana` either as:
> `curl http://127.0.0.1:5000/delete/banana`
or
> `curl http://127.0.0.1:5000/delete/2`

The `/documentation` directory contains formal requirements and deployment instructions.

For demonstration purposes only, the initial list is seeded with five fruits.


==========================

[1] http://flask.pocoo.org/

[2] per https://simple.wikipedia.org/wiki/List_of_fruits
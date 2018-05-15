## Fruitlist API ##

This API allows for the simple management of a list of fruits.

It runs using the bottle module[1] on Python 3, and when main.py is run, you can access the API at http://127.0.0.1.

There are three calls you can make by suffixing the root:

1. **showlist** will return a list of all fruits in ranked order.
> `http://127.0.0.1/showlist`

2. **add** will add a fruit to the bottom of the list. Note the following usages:
* only valid fruits[2] are allowed
* a single fruit can be added, e.g.:
> `http://127.0.0.1/add/banana`
* up to ten multiple fruits can be added in csv format (no spaces), e.g.,:
> `http://127.0.0.1/add/apple,banana,persimmon`

3. **delete** will remove a current fruit on the list, either by index number or by name. Thus for a three-item fruitlist of `{1: 'apple'},{2: 'banana'},{3: 'cantelope'}`, one could remove `banana` either as:
> `http://127.0.0.1/delete/banana`
or
> `http://127.0.0.1/delete/2`

The `/documentation` directory contains formal requirements and deployment instructions.

For demonstration purposes only, the initial list is seeded with three fruits.

There are many additional refactoring opportunities left unpursued at this point, due to time limits.

==========================

[1] http://bottlepy.com/docs/dev/
[2] per https://simple.wikipedia.org/wiki/List_of_fruits
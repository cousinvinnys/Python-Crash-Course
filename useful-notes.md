# Notes

## Chapter 2

- `print(f"String {variable}")`
- \n is newline, \t is tab
- `lstrip()` = left side of a string, `rstrip()` right side, and `strip()` both sides
- Exponents: `3 ** 2` = 9

## Chapter 3: Lists

- Index -1 means last element in the list. -2 is second to last, etc etc.
- Can modify items in a list `motorcycles[0] = 'ducati'`
- Append, add to end of list. `motorcycles.append('ducati')`
- Can insert and delete items at an index
- Can pop at an index: `mc = motorcycles.pop(1)`
- Can remove at a value: `motorcycles.remove('honda')`
- Sort reverse: `cars.sorted(reverse=True)`
- `sorted()`: temporary sort method

## Chapter 4: Working with Lists

- Subset of a list: `print(plyers[1:3])` prints the players from the first to the third index (by zero ofc)
- Copying a list: `friend_foods = my_foods[:]`
- **Immutable list**: Tuple
- Example tuple: set with parentheses, used for data that does not change. `dimensions = (100, 90)`

## Chapter 5: If statements

- `if elif else` structure
- Checking if something is in a list `if ___ in _list_`
- `for topping in requested_toppings: if topping in stock_toppings: do shit`

## Chapter 6: Dictionaries

- Simple Dictionary:
- `alien_0 = {'color': 'green', 'points': 5}`
- `print(alien_0['color'])`
- Can assign a variable the value of a dictionary
- Can add characteristics to a variable. `alien_0['x'] = 0`
- Can reassign value. `alien_0['x'] = 5`
-   `items()` returns a key-value pair. Can be used to loop through a dictionary.
- `for k, v in x.items()`
- If you want a list of unique values from a larger list, use the `set` keyword
- You can store a list inside of a dictionary
- `pizza['toppings': ['mushrooms', 'extra cheese']]`
- Can have a dictionary in a dictionary

## Chapter 7: User Input and While Loops

 - Can use `while(list)` is equivalent to while that list is not equal to empty
 - Can remove specific instances of a word. `while 'cat' in pets: pets.remove('cat')`

 ## Chapter 8: Functions

 - Dictionaries can be something that can be returned
 - Pass in a copy of a list to a function `func(list_name[:])`
 - Pass an arbitrary amount of arguments to the function: `func(*args)`
 - Double asteriks build a new dictionary for as many values passed in: `func(**args)`
 - Modules, just importing files. As in, `pizzas.py`, import pizzas, use pizzas.makePizza() etc
 - `from module_name import function_name` is useful
 - Import a function `as` something to assign an alias

## Chapter 9: Classes

 - To create a child class of a parent class, merely include the parent's name in parens. `class ElectricCar(Car)`
 - To inherit a parent's `init` function, use `super`. `super().__init__(make, model, year)`
 - Separate files out into separate modules with classes. Again, `from filename import class`
 - If you just import the module, you'll have to use `module.class.method` nomenclature instead of `class.method` if you import a specific class
- `choice()` is a Python standard library included function that takes in a list and returns a randomly selected element/
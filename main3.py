import types
from datetime import datetime

def decorator(old_function):
    def new_function(*args, **kwargs):
        with open('log.log', 'a', encoding='utf-8') as log_file:
            log_file.write(f'{datetime.now()} Function {old_function.__name__} started with arguments {args}, {kwargs}.\n')
            result = old_function(*args, **kwargs)
            log_file.write(f'{datetime.now()} Function {old_function.__name__} returned {result}.\n')
        return result
    return new_function

def flat_generator(list_of_lists):
	for i in list_of_lists:
		for el in i:
			yield el

@decorator
def hello_world():
    return 'Hello World'

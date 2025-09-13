ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

def all_thing_is_obj(object: any) -> int:
	if (type(object) == list):
		print("<class 'list'>")
	if (type(object) == tuple):
		print("<class 'tuple'>")
	if (type(object) == set):
		print("<class 'set'>")
	if (type(object) == dict):
		print("<class 'dict'>")
	if (type(object) == str): 
		print("<class 'str'>")
	return 42
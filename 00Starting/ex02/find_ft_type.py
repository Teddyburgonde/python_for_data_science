def all_thing_is_obj(object: any) -> int:
    if type(object) == list:
        print("List : <class 'list'>")
    elif type(object) == tuple:
        print("Tuple : <class 'tuple'>")
    elif type(object) == set:
        print("Set : <class 'set'>")
    elif type(object) == dict:
        print("Dict : <class 'dict'>")
    elif type(object) == str:
        print(object, "is in the kitchen : <class 'str'>")
    else:
        print("Type not found")
    return 42

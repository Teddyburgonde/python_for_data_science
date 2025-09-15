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
        if object == "Brian":
            print("Brian is in the kitchen : <class 'str'>")
        elif object == "Toto":
            print("Toto is in the kitchen : <class 'str'>")
        else:
            print("<class 'str'>")
    else:
        print("Type not found")
    return 42

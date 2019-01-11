"""
A dictionary is a type of data structure that is supported natively in all major interpreted languages such as JavaScript, Python, Ruby and PHP, where it's known as an Object, Dictionary, Hash and Array, respectively. In simple terms, a dictionary is a collection of unique keys and their values. The values can typically be of any primitive type (i.e an integer, boolean, double, string etc) or other dictionaries (dictionaries can be nested). However, for this exercise assume that values are either an integer, a string or another dictionary.

Given a dictionary dict, write a function flattenDictionary that returns a flattened version of it.

Example:

input:  dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }

output: {
            "Key1" : "1",
            "Key2.a" : "2",
            "Key2.b" : "3",
            "Key2.c.d" : "3",
            "Key2.c.e" : "1"
        }
"""


def flatten_dictionary(dictionary):
    result = {}
    flatten_dict_helper('', dictionary, result)

    return result


def flatten_dict_helper(init_key, dictionary, result):
    for key, value in dictionary.items():
        if not isinstance(value, dict):
            if init_key is None or init_key == "":
                result[key] = value
            else:
                concat = '' if key == '' else '.'
                result[init_key + concat + key] = value
        else:
            if init_key is None or init_key == "":
                flatten_dict_helper(key, value, result)
            else:
                flatten_dict_helper(init_key + '.' + key, value, result)


if __name__ == "__main__":
    d1 = {"Key1": "1", "Key2": {"a": "2", "b": "3", "c": {"d": "3", "e": "1"}}}
    d2 = {
        "Key1": "1",
        "Key2": {
            "a": "2",
            "b": "3",
            "c": {
                "d": "3",
                "e": {
                    "": "1"
                }
            }
        }
    }
    d3 = {"a": {"b": {"c": {"d": {"e": {"f": {"": "pramp"}}}}}}}
    print(flatten_dictionary(d1))
    print('\n')
    print(flatten_dictionary(d2))
    print(flatten_dictionary(d3))

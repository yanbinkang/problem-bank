=begin
A dictionary is a type of data structure that is supported natively in all major interpreted languages such as JavaScript, Python, Ruby and PHP, where it's known as an Object, Dictionary, Hash and Array, respectively.

In simple terms, a dictionary is a collection of unique keys and their values.

The values can typically be of any primitive type (i.e an integer, boolean, double, string etc) or other dictionaries (dictionaries can be nested).

However, for this exercise assume that values are either an integer, a string or another dictionary.

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
=end

def flatten_dictionary(dict)
  result = {}
  flatten_hash_helper('', dict, result)

  result
end

def flatten_hash_helper(init_key, dict, result)
  dict.each do |key, value|
    if !value.is_a?(Hash)
      if init_key.nil? || init_key.empty?
        result[key.to_s] = value
      else
        dot_or_str = key.empty? ? '' : '.'
        result[init_key + dot_or_str + key.to_s] = value
      end
    elsif init_key.nil? || init_key.empty?
      flatten_hash_helper(key.to_s, value, result)
    else
      flatten_hash_helper(init_key + '.' + key.to_s, value, result)
    end
  end
end

if $PROGRAM_NAME == __FILE__
  d1 = { 'Key1' => '1',
        'Key2' => { 'a' => '2', 'b' => '3',
                    'c' => { 'd' => '3', 'e' => '1' }
                  }
        }
  puts flatten_dictionary(d1)
end

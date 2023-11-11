from ast import literal_eval

def get_type(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        return str

num =input("Enter the value: ")
print(get_type(num))
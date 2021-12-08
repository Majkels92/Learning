"""Python file including functions that validates input data in monster.py file/app."""


# validate input value, value must be INT type and value > 0
def validate_int_value(int_value):
    if isinstance(int_value, int) and int_value > 0:
        return int_value
    else:
        if not isinstance(int_value, int):
            raise TypeError("Attribute must be integer type.")
        elif int_value <= 0:
            raise ValueError("Attribute must be greater than 0.")


# validate input value, value must be STR type
def validate_str_value(str_value):
    if isinstance(str_value, str):
        return str_value
    else:
        raise TypeError("Attribute must be string type.")




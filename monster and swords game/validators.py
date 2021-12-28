"""Python file including functions that validates input data in monster.py file/app."""


# validate input value, value must be INT type and value > 0
def validate_int_value(int_value):
    """Must be INT type and value > 0"""
    if isinstance(int_value, int) and int_value > 0:
        return int_value
    else:
        if not isinstance(int_value, int):
            raise TypeError("Attribute must be integer type.")
        elif isinstance(int_value, int) and int_value <= 0:
            raise ValueError("Attribute must be greater than 0.")


# validates input of gold sack, value must be number and value >=0
def validate_sack_number_value(value):
    """Should be INT and value >=0"""
    if isinstance(value, float) and value >= 0:
        sack_value = int(round(value, 0))
        return sack_value
    elif isinstance(value, int) and value >= 0:
        sack_value = value
        return sack_value
    else:
        if isinstance(value, float) or isinstance(value, int) and value < 0:
            raise ValueError("Attribute must be greater than 0.")
        elif not isinstance(value, int):
            raise TypeError("Attribute must be number type.")
        elif not isinstance(value, float):
            raise TypeError("Attribute must be number type.")


# validates value of weapon damage
def validate_int_weapon_dmg_value(int_value):
    """Must be int and 0 < int_value <= 100"""
    if isinstance(int_value, int) and 0 < int_value <= 100:
        return int_value
    else:
        if not isinstance(int_value, int):
            raise TypeError("Attribute must be integer type.")
        elif isinstance(int_value, int) and 0 < int_value <= 100:
            raise ValueError("Attribute must be greater than 0 and lower or equal of 100.")


# validates float value of weapon attack speed
def validate_float_weapon_att_spd_value(number_value):
    """Must be float value and 1.0 < int_value <= 4.0"""
    if isinstance(number_value, int):
        float_value = float(number_value)
    else:
        float_value = number_value
    if isinstance(float_value, float) and 1 <= float_value <= 4:
        return float_value
    else:
        if not isinstance(float_value, float):
            raise TypeError("Attribute must be integer type.")
        elif isinstance(number_value, int) or isinstance(number_value, float) and 1 < float_value <= 4:
            raise ValueError("Attribute must be greater or equal than 1 and lower or equal of 4.")


# validate input value, value must be STR type
def validate_str_value(str_value):
    if isinstance(str_value, str):
        return str_value
    else:
        raise TypeError("Attribute must be string type.")

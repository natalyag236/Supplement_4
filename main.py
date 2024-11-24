def next_ten_nums(num):
    """Given a number, returns a string contatinning the next 10 nums spearated by commaas

    Args:
        num (int): the starting number

    Returns:
        str: a comma-separated string of the next 10 numbers
    """
    numbers = []
    for i in range(1,11):
        numbers.append(num + i)
    return ', '.join(map(str, numbers)) 

def test_ten_nums():
    assert next_ten_nums(23) == "24, 25, 26, 27, 28, 29, 30, 31, 32, 33" 

def comma_delimited_string(string_list):
    return ', '.join(string_list) 

def test_comma_string():
    result = comma_delimited_string(["red", "pink", "purple"])
    assert result == "red, pink, purple" 
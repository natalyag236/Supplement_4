def next_ten_nums(num):
    numbers = []
    for i in range(1,11):
        numbers.append(num + i)
    return ', '.join(map(str, numbers)) 
def test_ten_nums():
    assert next_ten_nums(23) == "24, 25, 26, 27, 28, 29, 30, 31, 32, 33" 
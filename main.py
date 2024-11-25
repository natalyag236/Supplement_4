import csv
import os
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
    """Converts a list of strings into a single comma delimited string and 
    separates by a comma 

    Args:
        string_list (list): a list of string to be joined

    Returns:
        str: a single string with the list elements separated by commas.
    """
    return ', '.join(string_list) 

def test_comma_string():
    result = comma_delimited_string(["red", "pink", "purple"])
    assert result == "red, pink, purple" 

def headers_to_csv(filename, headers):
    """ Writes headers to CSV file.

    Args:
        filename (str): the name of the CSV file
        headers (list): a list of colum headers to be written as the first row 
    
    the file is oppened in write ('w') mode, 
    """
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

def data_to_csv(filename, data):
    """Appendes multipld rows of data to a CSV file

    Args:
        filename (str): the name of the CSV file 
        data (list of lists):  a list of rows where each row is a list of values to be written
    the file is openedf in append ('a') mode
    """
    with open(filename, mode='a', newline='') as file:  
        writer = csv.writer(file)
        writer.writerows(data)  

def test_write_to_csv():
    filename = "test_file.csv"
    
    headers = ["Birthday", "Horoscope Sign", "City"]
    data = [
        ["June 18, 2003", "Gemini", "Brooklyn"],
        ["October 27, 2021", "Scorpio", "Atlanta"],
        ["September 3, 1999", "Virgo", "Houston"]
    ]
    
    headers_to_csv(filename, headers)
    data_to_csv(filename, data)
    
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        content = list(reader)
    
    expected_content = [
        headers,
        ["June 18, 2003", "Gemini", "Brooklyn"],
        ["October 27, 2021", "Scorpio", "Atlanta"],
        ["September 3, 1999", "Virgo", "Houston"]
    ]
    
    assert content == expected_content

    


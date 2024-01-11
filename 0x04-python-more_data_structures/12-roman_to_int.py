#!/usr/bin/python3
def roman_to_int(roman_string):
    total_int = 0
    if (roman_string):
        if 'IV' in roman_string:
            total_int += 4
            roman_string = roman_string.replace('IV', '')
        if 'IX' in roman_string:
            total_int += 9
            roman_string = roman_string.replace('IX', '')
        if 'XL' in roman_string:
            total_int += 40
            roman_string = roman_string.replace('XL', '')
        if 'XC' in roman_string:
            total_int += 90
            roman_string = roman_string.replace('XC', '')
        if "CD" in roman_string:
            total_int += 400
            roman_string = roman_string.replace("CD", "")
        if "CM" in roman_string:
            total_int += 900
            roman_string = roman_string.replace("CM", "")
        for i in roman_string:
            if i == "I":
                total_int += 1
            elif i == "V":
                total_int += 5
            elif i == "X":
                total_int += 10
            elif i == "L":
                total_int += 50
            elif i == "C":
                total_int += 100
            elif i == "D":
                total_int += 500
            elif i == 'M':
                total_int += 1000
            else:
                total_int += 0
    return (total_int)

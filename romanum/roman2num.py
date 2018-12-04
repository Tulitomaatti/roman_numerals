def smallr2n(roman_str):
    roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, "": 0}
    # TODO: Could the roman symbol definitions be made package-wide instead of redefining them per module?
    # Parse roman numerals to 1-4999
    # Assume valid input
    num = 0
    aux = 0
    prev_c = ""

    for c in roman_str:
        if prev_c == "":
            prev_c = c
            aux += roman_nums[c]
            continue  # populate prev_c

        elif roman_nums[c] == roman_nums[prev_c]:  # Add up consecutive symbols
            aux += roman_nums[c]

        elif roman_nums[c] < roman_nums[prev_c]:  # Add encountered symbols to total if smaller one encountered.
            num += aux
            aux = roman_nums[c]

        elif roman_nums[c] > roman_nums[prev_c]:  # Larger symbol encountered: subtract & reset accumulated value
            num -= aux - roman_nums[c]
            aux = 0

        prev_c = c

    return num + aux


def r2n(roman_str):
    num = 0
    vin_mul = 1000
    vin_exp = 0
    starti = 0
    sign = 1

    if roman_str == "nulla":
        return 0

    if roman_str[0] == '-':  # Negative number encountered
        sign = -1
        roman_str = roman_str[1:]

    if roman_str[0] == '(':  # Encountered parens/vinculus notation
        for i, c in enumerate(roman_str):
            if c == '(':
                vin_exp += 1
                starti = i + 1
            elif c == ')':
                parse_s = roman_str[starti:i]
                num += vin_mul ** vin_exp * smallr2n(parse_s)
                vin_exp -= 1
                starti = i + 1
                if vin_exp == 0:
                    num += smallr2n(roman_str[i + 1:])  # Handle last block outside parens e.g.. ...)XII
                    break
            else:
                pass

        return sign * num
    else:  # Smaller number.
        return sign * smallr2n(roman_str)

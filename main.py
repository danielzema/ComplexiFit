from linear_regression import analyze_complexity

def parse_list(input_list):
    user_input = input(input_list) 
    numbers = user_input.split(",")
    values = []
    for number in numbers:
        values.append(float(number))
    return values 


from memory_profiler import profile

with open('Day_1/day_1_1_input.txt', 'r') as file:
    input_list = []
    for line in file:
        input_list.append(line.strip())

@profile
def grab_calibration(calibration_string):
    split_string = list(calibration_string)
    number_list = []
    calibration_numbers = []
    first_num = ""
    last_num = ""
    for char in split_string:
        if char.isnumeric():
            number_list.append(char)
    
    first_num = number_list[0]
    last_num = number_list[-1]
    final_num = int("".join(first_num+last_num))
    
    calibration_numbers.append(final_num)
    
    total = sum(calibration_numbers)
    
    return final_num

print(sum([grab_calibration(x) for x in input_list]))

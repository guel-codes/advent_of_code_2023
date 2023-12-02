from memory_profiler import profile

@profile
def get_calibration():
    with open('Day_1/day_1_2_input.txt', 'r') as file:
        input_2_list = []
        for line in file.readlines():
            line = line.replace("one", "o1ne")
            line = line.replace("two", "t2wo")
            line = line.replace("three", "t3hree")
            line = line.replace("four", "f4our")
            line = line.replace("five", "f5ive")
            line = line.replace("six", "s6ix")
            line = line.replace("seven", "s7even")
            line = line.replace("eight", "e8ight")
            line = line.replace("nine", "n9ine")
            line = line.replace("zero", "z0ero")
            
            character = []
            for char in line:
                if char>= '0' and char <= '9':
                        character.append(int(char))
            input_2_list.append(character)

            
    calibration_numbers = []
    input

    for item in input_2_list:
        first_num = item[0]
        last_num = item[-1]
        final_num = int("".join(str(first_num)+str(last_num)))

        calibration_numbers.append(final_num)
    
    return sum(calibration_numbers)

print(get_calibration())
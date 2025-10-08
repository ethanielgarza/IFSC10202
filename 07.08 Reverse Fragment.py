input_string = input('Enter a string: ')
first_h_index = input_string.find('h')
last_h_index = input_string.rfind('h')
start_part = input_string[:first_h_index + 1]
fragment_to_reverse = input_string[first_h_index + 1:last_h_index]
end_part = input_string[last_h_index:]
reversed_fragment = fragment_to_reverse[::-1]
final_string = start_part + reversed_fragment + end_part
print(final_string)
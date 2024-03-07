main_string = "олдос Хаксли родился в 1894 году"
name = main_string[0:6]
surname = main_string[6:11]
other = main_string[12:31]
main_string = name.capitalize() + surname.capitalize() + other
print(main_string)
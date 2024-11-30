from user_input_validator import UserInputValidator

# Create two instances of the UserInputValidator class
validator1 = UserInputValidator()
validator2 = UserInputValidator()

# Example input lists
input_list1 = ["10", "-5", "abc", "25"]
input_list2 = ["0", "15", "xyz", "100"]

# Validate input lists using both instances
valid_numbers1 = validator1.validate_positive_integers(input_list1)
validator1.display_validation_message()
print("Valid numbers from input_list1:", valid_numbers1)

valid_numbers2 = validator2.validate_positive_integers(input_list2)
validator2.display_validation_message()
print("Valid numbers from input_list2:", valid_numbers2)

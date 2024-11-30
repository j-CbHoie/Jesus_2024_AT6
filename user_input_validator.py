class UserInputValidator:
    def validate_positive_integers(self, input_list):
        """
        Validate and return a list of positive integers from the input list.
        """
        valid_numbers = []
        for item in input_list:
            if item.isdigit() and int(item) > 0:
                valid_numbers.append(int(item))
        return valid_numbers

    def display_validation_message(self):
        """
        Display a message after validating the list.
        """
        print("Validation complete. The list has been processed.")

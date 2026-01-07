# 3.Password Strength Validator
# Validate a password using rules:
# - min length
# - at least 1 uppercase, 1 lowercase, 1 digit, 1 special char
# - no repeated sequence longer than 2 chars

# 1. min length
def pass_len_check(password, min_length):
    if len(password) < min_length:
        return False
    return True


# Get characters Types Frequency
def char_type_frequency(password):
    char_types = {
        "lower case characters '[a-z]'": 0,
        "upper case characters '[A-Z]'": 0,
        "Digit characters '[0-9]'": 0,
        "Special characters '[@#$]'": 0,
    }
    for char in password:
        if char.islower():
            char_types["lower case characters '[a-z]'"] += 1
        elif char.isupper():
            char_types["upper case characters '[A-Z]'"] += 1
        elif char.isdigit():
            char_types["Digit characters '[0-9]'"] += 1
        else:
            char_types["Special characters '[@#$]'"] += 1
    return char_types


def char_type_check(password):
    char_type_fre = char_type_frequency(password)
    # at least 1 uppercase, 1 lowercase, 1 digit, 1 special char
    for k, v in char_type_fre.items():
        if v < 1:
            return f"The Password Should at least have 1 {k}."

    return True


# 3. no repeated sequence longer than 2 chars
def repeat_sequence_check(password):
    # no repeated sequence longer than 2 chars
    length = len(password)
    for idx in range(0, length - 2):
        if password[idx] == password[idx + 1] == password[idx + 2]:
            return True

    return False


#  Struggle here
def password_validator(password):
    min_length = 8
    if pass_len_check(password=password, min_length=min_length):
        for k, v in char_type_frequency(password).items():
            if v < 1:
                return f"The Password Should at least have 1 {k}."
        if repeat_sequence_check(password=password):
            return "No Repeated Sequence longer than 2 chars"
    else:
        return "Password Should be at lears 8 characters"


password_validator("13232321###0Mg")

# Functions with Outputs
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    format_f_name = f_name.title()
    format_l_name = l_name.title()
    print(f"Result: {format_f_name} {format_l_name}")


# Storing output in a variable
format_name(input("Your first name: "), input("Your last name: "))

# or printing output directly
format_name(input("What is your first name? "), input("What is your last name? "))

# Already used functions with outputs.
# length = len()


# # Return as an early exit
# def format_name(f_name, l_name):
#     """Take a first and last name and format it
#   to return the title case version of the name."""
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     format_f_name = f_name.title()
#     format_l_name = l_name.title()
#     return f"Result: {format_f_name} {format_l_name}"

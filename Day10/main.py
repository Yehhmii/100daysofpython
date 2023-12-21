# functions with output 

def format_name(f_name, l_name):
    """Docstrings that helps us define our code more"""
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name("kiKo", "myGuy"))
format_name()
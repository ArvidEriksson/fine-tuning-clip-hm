# This file is simply to demonstrate how the text field was generated from the tabular data

def generate_combined_string(row):
    first_sentence = row['detail_desc'].split('. ')[0]
    perceived_colour_master_name = row['perceived_colour_master_name'].lower()
    if perceived_colour_master_name.lower() in ['undefined', 'unknown']:
        colour_string = ""
    else:
        colour_string = f"{row['perceived_colour_value_name']} {perceived_colour_master_name}"
        first_sentence = first_sentence[0].lower() + first_sentence[1:]  # Convert first letter to lowercase
    return f"{colour_string} {first_sentence}"
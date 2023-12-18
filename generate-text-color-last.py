# This file is simply to demonstrate how the text field was generated from the tabular data

def generate_combined_string(row):
    first_sentence = row['detail_desc'].split('. ')[0]
    combined_string = f"Colour: {row['perceived_colour_value_name']} {row['perceived_colour_master_name']}"
    return f"{first_sentence} {combined_string}"

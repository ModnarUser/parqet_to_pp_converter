import pandas as pd
from dateutil import parser

def read_input_csv(file_path):
    return pd.read_csv(file_path, delimiter=';')

def convert_to_german_format(value):
    if pd.notna(value):
        return str(value).replace('.', ',')
    return value

def map_type_to_german(type_value):
    mapping = {
        'Buy': 'Kauf',
        'Sell': 'Verkauf',
        'Dividend': 'Dividende'
        # Add more mappings if necessary
    }
    return mapping.get(type_value, type_value)

def transform_data(input_df):
    columns = ['Datum', 'Typ', 'Wert', 'Buchungswährung', 'Bruttobetrag', 'Währung Bruttobetrag', 'Wechselkurs', 'Gebühren', 'Steuern', 'Stück', 'ISIN', 'WKN', 'Ticker-Symbol', 'Wertpapiername', 'Notiz']
    output_df = pd.DataFrame(columns=columns)

    for index, row in input_df.iterrows():
        # Parsing the 'datetime' field to handle the UTC format
        parsed_date = parser.parse(row['datetime'])
        datum = parsed_date.strftime('%Y-%m-%dT%H:%M')

        output_df = output_df.append({
            'Datum': datum,
            'Typ': map_type_to_german(row['type']),
            'Wert': convert_to_german_format(row['amount']),
            'Buchungswährung': row['currency'],
            'Bruttobetrag': convert_to_german_format(row['price']),
            'Währung Bruttobetrag': row['currency'],
            'Wechselkurs': convert_to_german_format(row['fxrate']),
            'Gebühren': convert_to_german_format(row['fee']),
            'Steuern': convert_to_german_format(row['tax']),
            'Stück': convert_to_german_format(row['shares']),
            'ISIN': row['identifier'],
            'WKN': row['wkn'],
            'Ticker-Symbol': '',
            'Wertpapiername': row['holdingname'],
            'Notiz': ''  
        }, ignore_index=True)

    return output_df

def write_output_csv(output_df, file_path):
    output_df.to_csv(file_path, index=False, sep=';', encoding='iso-8859-1')

# # Example usage
# input_file = 'Sample.csv'  # Replace with the path to your input CSV file
# output_file = 'Sample_output.csv'  # Replace with the path where you want to save the output CSV

# input_df = read_input_csv(input_file)
# transformed_df = transform_data(input_df)
# write_output_csv(transformed_df, output_file)

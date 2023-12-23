from flask import Flask, request, send_file, render_template, redirect, url_for
import pandas as pd
from io import BytesIO
from convert_csv import transform_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # HTML template for file upload

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))

    if file and file.filename.endswith('.csv'):
        input_df = pd.read_csv(file.stream, delimiter=';')
        transformed_df = transform_data(input_df)

        # Convert DataFrame to CSV and send as file
        stream = BytesIO()
        transformed_df.to_csv(stream, index=False, sep=';', encoding='iso-8859-1')
        stream.seek(0)
        return send_file(stream, as_attachment=True, attachment_filename='converted.csv')

    return send_file(stream, as_attachment=True, attachment_filename='converted.csv')

if __name__ == '__main__':
    app.run(debug=True)

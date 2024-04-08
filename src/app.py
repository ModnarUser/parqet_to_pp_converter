from flask import Flask, request, send_file, render_template, redirect, url_for, make_response
import pandas as pd
import webbrowser
from io import BytesIO
from convert_csv import transform_data  # Make sure this import matches your file structure

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

        # Convert DataFrame to CSV
        stream = BytesIO()
        transformed_df.to_csv(stream, index=False, sep=';', encoding='iso-8859-1')
        stream.seek(0)

        # Create a response and set a cookie
        response = make_response(send_file(stream, as_attachment=True, download_name='converted.csv'))
        response.set_cookie('fileDownload', 'true', max_age=60)  # Set a cookie for 60 seconds
        return response

    return redirect(url_for('index'))

if __name__ == '__main__':

    url = 'http://127.0.0.1:5000'
    webbrowser.open(url)
    app.run(debug=True)



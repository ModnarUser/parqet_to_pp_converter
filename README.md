# Parqet to Portfolio Performance Converter
![](example.PNG)

This project provides a simple web GUI to convert exported [**Parqet**](https://app.parqet.com/) activity data in CSV format 
to [**Portfolio Performance**](https://www.portfolio-performance.info/) compatible CSV format for easy migration. 
# Using It
To run the application locally, install the python requirements, start the python backend and click on the address displayed in the output (``Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)``)

```powershell
pip install -r requirements.txt

cd src
python app.py
```

# Buildung an Executable

```powershell
cd src
pyinstaller --add-data "templates;templates" --add-data "static;static" --hidden-import=flask --onefile app.py 
--icon=csv_converter_logo.ico
```
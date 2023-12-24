# Parqet to Portfolio Performance Converter
![](example.PNG)

This project provides a simple web GUI to convert exported [**Parqet**](https://app.parqet.com/) activity data in CSV format 
to [**Portfolio Performance**](https://www.portfolio-performance.info/) compatible CSV format for easy migration. 
# Using It
## From the executable 
If you don't want to install the dependencies and development environment locally on your PC, you can simply use the ``parqet_to_pp_converter.exe`` provided in the release package. 
Just download the ``exe`` and run it on your PC. It will start the backend for the conversion in a terminal window and open your webrowser to display the user interface. 
Once the backend is ready, the apps user inetrface will appear in your browser. Now you can simply select files to convert and click on the convert button. Everything will run locally on your PC. 
No personal data is shared with third parties, since all communication is running on your localhost. 

## With local Python
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

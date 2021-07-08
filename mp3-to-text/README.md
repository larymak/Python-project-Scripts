# mp3 to text

This Project converts mp3 files into text files.

## Getting started

* Clone this repo
* Install dependencies -- `poetry install`
    if you don't have poetry `pip install ibm-watson`
* Create IBM account to get the api key from this link [IBM-Watson speech-to-text](https://cloud.ibm.com/catalog/services/speech-to-text)
* You can choose the free version which gives you 500 minutes pre month to try the service.
* If you are using poetry, enter the virtual environment - `poetry shell`
* Add your api key in apikey variable line"4".
* Start the app - `python -m extract_text.py`
* Add the mp3 file path to the script and hit return.
* Your text file will be created in a file named output.txt.

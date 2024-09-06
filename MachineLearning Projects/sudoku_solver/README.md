# Sudoku Solver

* This app was built to allow users to solve their sudokus using a computer.
* There is a Flask based webserver `web_interface.py` which when run gives a web interface to upload an image of a sudoku to be solved. The response is a solved sudoku.
* There is a file `full_stack_http.py` which needs to be run alongside the webserver for the full app to run. This is in charge of opening multiple process channels to process the images that are sent to the webserver.
* The app relies of Pytesseract to identify the characters in the sudoku image.

# Operation

* The image is first stripped of color.
* It is then cropped to select the section of the sudoku. NOTE: This section is not dependent on the sudoku but has been hardcoded.
* The resulting image is passed to `Pytesseract` to extract the characters and their position.
* Using the characters and their position the grid size is determined.
* The appropriate grid is created and filled with the discovered characters.
* The grid is then solved with an algorithm contained in `sudoku.py`.
* A snapshot of the solved grid is then created and sent back to the user.
* The resultant snapshot is rendered on the browser page.

# To Run

* First install `Pytesseract`
* Install `Flask`
* Then run the `full_stack_http.py` file.
* Then run the `web_interface.py` file.
* Go to the browser and load the URL provided in the previous step.
* Click the upload button.
* Select your image and submit the form.
* Wait for the result to be loaded.
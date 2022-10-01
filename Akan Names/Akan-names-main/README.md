# Akan Birthday  Names


#### Created on 11th Feb 2022
#### By Dominic Yeboah

## Description 

It's a Web Application that uses the Ghanian Culture to Output the User's Birthday ghanian Name which is known as `AKAN NAME`. It works when the user inputs their Birth-Day and it Calculates the day of the Week they were born and depending on the gender of the User the respective name is Outputted to the Screen.

The Formula Used `(DD+(((MM+1)26)/10)+YY+(YY/4)+6*(YY/100)+(YY/400)-1)mod7;`

`DD` - Day    `MM` - Month   `YY` - Year


The Application
![Preview](./images/akan-name.png)

---

## Access the website
Need the latest browser to be able to View

Follow this link https://yeboahd24.github.io/Akan-names/

It is hosted by github.

---

### Setup
To access this project on your local files, you can clone it using these steps
1. Open your terminal
1. Use this command to clone `$ git clone https://github.com/yeboahd24/Akan-names.git`
1. This will clone the repositoty into your local folder
1. Run `index.html` with active internet
1. __Enjoy :)__

---

## Behaviour Driven Development

1. Displays Form For Entering Date and Gender
   - INPUT: User Enters Birth-Day via 3 inputs Day, Month, Year
   - INPUT: User chooses either Male or Female
   - OUTPUT: Akan Name is Diplayed According What the User as Entered and Choosed

2. Displays an Error Message if Date Input Left Blank
   - INPUT: ""
   - OUTPUT: Invalid Day, Enter Between 1 and 31

3. Displays an Error Message if Month Input is Left Blank
   - INPUT: ""
   - OUTPUT: Invalid Month, Enter Between 1 and 12

4. Displays an Error Message if Year Input is Left Blank
   - INPUT: ""
   - OUTPUT: Invalid Year, Enter Between 1950 and 2030

4. Displays an Error Message if One or All Inputs is Left Blank
   - INPUT: ""
   - OUTPUT: Empty Entry, Please Fill the Form

5. Displays an Error Message if Gender Not Chosen
   - INPUT: "" 
   - OUTPUT: Try Again. Select a gender 

6. Clears Form and Reset the Message on Click
   - INPUT: Click Reset Button
   - OUTPUT: Clears the Form Data

---

## Technologies Used
HTML

CSS

JAVASCRIPT

BOOTSTRAP

Git

---

## Contact Details
yeboahd24@gmail.com


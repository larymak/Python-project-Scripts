
# Driver Drowsiness Detection

A system that alarms the driver as soon as it detects that the driver is becoming drowsy to prevent any accidents.



## Quick Start 🚀

### Clone the Repository

```sh
git clone https://github.com/adityajai25/driver-drowsiness-detection.git
```
Then 

```sh
cd driver-drowsiness-detection
```


## Dataset

We used a dataset downloaded from Kaggle.
## Creating Virtual Environment

Using a virtual environment isolates dependencies, manages library versions, keeps the global Python environment clean, and ensures consistent setups.

### On Windows

#### Creating a virtual environment:

Open Command Prompt and navigate to the project directory

```sh
cd project/directory/

```
Create a Virtual Environment:
```sh
python -m venv env
```
To Activate the Virtual Environment:

```sh
.\env\Scripts\activate
```

### On mac/Linux

#### Creating a virtual environment:
Open terminal and navigate to the project directory

```sh
cd project/directory/

```
Create a Virtual Environment:
```sh
python -m venv env
```
To Activate the Virtual Environment:

```sh
source env/bin/activate
```


## Installing Required Packages

Once the virtual environment is activated, install the required packages using the following commands:

#### 1. Install pygame

```sh
pip install pygame==2.4.0
```
#### 2. Install openCV-Python

```sh
pip install opencv-python==4.6.0.66
```
#### 3. Install numpy

```sh
pip install numpy==1.23.0
```
#### 4. Install keras

```sh
pip install keras==2.12.0
```
#### 5. Install tensorflow

```sh
pip install tensorflow==2.13.0
```


## Execution
After installing the packages required, the project can be executed using the following command.

```sh
python main.py 
```

This will initiate the application, and it may take a few moments to activate the webcam and begin detection.
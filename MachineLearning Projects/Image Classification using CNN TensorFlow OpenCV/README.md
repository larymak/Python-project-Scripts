# CNN Image Classification using TensorFlow

This guide will help you navigate and learn CNN Image Classification using TensorFlow. 
This is an Introductory Codebase. For deeper knowledge visite [GitHub : DeepLearning-ImageClassification-Toolkit](https://github.com/iSiddharth20/DeepLearning-ImageClassification-Toolkit)

#### TensorFlow is Required to run this Code.
Install using [THIS](https://www.tensorflow.org/install/pip) Guide.
#### Make sure to inastall necessary dependencies by running this command :
pip install -r requirements.txt

## Understanding the Functionalities

### 1. PreProcessing
- Load Dataset from 'DATA_DIR' Directory
- Creates DataFrame containing Full Paths of Images and their Class Labels
- (Change as per Requirement) Rescale Images to Computationally Efficient Resolution
- (Optional but Recommended) Extracts Largest Object from Image using 'image_processing' Function
    - Leverages Parallel Processing for Faster Results
- Compares Original and Rescaled+Processed Image SIde-By-Side to make necessary changes
- Converts Processed Images to NumPy Array and Exports as Pickle File
    - Verifies If Exported Pickle File is Appropriate through 10 Random Samples
- (Optional) Merge Certain Class Lables Together
- Split Data for Training, Testing, Validation with Stratify to ensure data balancing
    - Verify if Split is Appropriate through 2 random samples
- (Optional) Perform Random Oversampling on Data to reduce Biasness
    - Verify if Oversampling is Appropriate through 2 random samples
- Perform One-Hot-Encoding of Class Labels
- Training, Testing, Validation Data and One-Hot-Encoding is Exported as Pickle Files
  
### 2. Training CNN ResNet50
- Training, Testing, Validation Data and One-Hot-Encoding are Imported
    - All Data is converted to TensorFlow Format
- Learning Rate Scheduler is Defined (Change If Desired) 
- Stochastic Gradient Descent with Momentum is Used as Optimizer  (Change If Desired) 
- Added Data Augmentation Techniques to improve Model Learning  (Change If Desired) 
- Base Model (CNN ResNet50) is Loded from TensorFlow Library
    - Custom Optimal Changes have been made to the Structure
    - Final Model is Compiled
- Final Model is Trained
    - Final Model with Lowest Validation Loss is Exported as a '.h5' file
- Traning Time (In Seconds) is Displayed
  
### 3. Verification and Confusion Matrix
- Trained Model and One-Hot-Encoding are Imported
- Entire Dataset is Run through the Trained Model to get Ground Truth of Accuracy
- (Optional) Incorrectly Classified Image Files will be copied to a seprate folder with detected class label
- Ground Truth Classification Confusion Matrix is Created
    - (Optional) Confusion Matrix can be Exported as a '.png' file
 
### HelperFunctions
- Function to display 2 images side-by-side on screen
- Function to Extract largest object from souruce image
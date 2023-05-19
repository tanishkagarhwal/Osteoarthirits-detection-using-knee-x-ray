# Osteoarthirits-detection-using-knee-x-ray
## DIAGNOSIS FOR PREDICTION OF KNEE OSTEOARTHRITIS USING DEEP LEARNING

### GOAL
The Goal of this project is to create a deep learning model that can detect if osteoarthritis 
is present or not along with this severity from a given  input of knee x-ray image.

### MODEL AND WORKING

#### Model:
![image](https://github.com/autesakshi/EditREADME/assets/96119061/92faa2bc-e657-4502-8216-9e7b133d157b)

The dataset consists of 1650 digital X-ray images of knee joint. The X-ray images are acquired using PROTEC PRS 500E X-ray machine. 
Original images are 8-bit grayscale image.  A novel approach has been developed to automatically extract the Cartilage region 
(region of interest) based on density of pixels. The target is to evaluate the performance of the deep learning algorithm to predict
per Kellgren and Lawrence grades.

#### Working:
Step1: Data Preprocessing: 
Convert image rgb to gray. 
Resizing the image using cv2.resize so that we get the fixed common size for all the images in the dataset.
Appending the image and the label (categorized) into the list (dataset) using data.append(resized) and label.append(label_dict[category]).
Step2: Convolutional Neural Network architectures.
Here from keras.models we import Sequential (data types that are an ordered set )
 From keras.layers import Conv2D (this creates a convolution kernel that is wind with layers input which helps produce a tensor of outputs), Activation (compares the input value to a threshold value), MaxPooling2D (calculates the largest or maximum value in every patch and the feature map), Dense, Flatten (returns a copy of the array in one dimensional rather than in 2-D or a multi-dimensional array).
Step3: Splitting data into training and testing
For splitting the data we import train_test_split from sklearn.model_selection.
Here we have split the data into 20% test and 80% train.
Get the visualization.
Split data for validation split.
In this we find the accuracy, loss through epochs.
Save the CNN model as model.h5
Randomly select data for text and check the loss and accuracy.
Then we import pyplot from matplotlib to plot the training loss and accuracy.
Plot the confusion matrix(to evaluate the performance and analyze the efficiency of the model) by importing confusion_matrix from sklearn.metrices.


#### DEPENDENCY
Total no of files: The total number of files required to create this model are 6 files.
![image](https://github.com/autesakshi/EditREADME/assets/96119061/b7012d28-4404-4e7a-8e27-238146b8222d)

1]Static file:
This file is consist of 2 sub files which are 
          - .Css file
          - .js file
CSS and js files are used to define styles for your web pages, including the design, layout and variations 
in display for different devices and screen sizes.

2]Templete file:
This file is consist of 2 sub files which are 
          - index.html file
          - base.html file
we have created this HTML file for creating Web pages
HTML file describes the structure of a Web page
HTML files are consists of a series of elements
HTML file elements tell the browser how to display the content

3]Test sample file:
This file is consist of different knee image of several type sech as doutfull,moderate,mild,etc 
we are using this images to predict the output weather the person is suffering from the dignosis or not
and at what stage

4]app file:
* The app.py file typically begins by importing the necessary dependencies
* The app.py file defines the routes for the application, which determine how incoming requests are processed
* This file also defines the functions that will handle the incoming requests.
* Finally, the app.py file includes code to start the application and listen for incoming requests. 

5]Model file:
The model file typically contains the code for the machine learning model itself. The model file is responsible 
for loading and preprocessing the data, training the model on that data, and generating predictions for new data.

#### PERFORMANCE ANALYSIS:
![Uploading image.png…]()


![Uploading image.png…]()



![image](https://github.com/tanishkagarhwal/Osteoarthirits-detection-using-knee-x-ray/assets/113787863/5eb4f381-4e2e-404a-8933-c91cc9015218)


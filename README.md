# Cars24_2021

### Introduction:
This code gives you the price of a preowned car from the site Cars24. I found this beautiful dataset in Kaggle which consists of 5900 records of used cars data. This includes all types of cars from hatchback to lux_sedan ranging from 1.2L to 65L rupees. But I have only considered the data ranging from the lowest to 15L only considering the availability of data as it leads to better accuracy. Also I am not that type of person who risks to invest such huge amout of money in a preowned car. These factors made this model more practical. I achieved a cross validation score of 89.12% accuracy. 

### Input:
This model takes 9 inputs whose data types are specified in the model. The inputs are most obvious things which a normal person look for. Make sure you give the right input with no spelling mistakes and no extra spaces. Price in the output can be anything as it will be updated by the predicted value in the end and it doesnot affect your training/test data or you model.

#### Brands and Models:
Below are the Brands we have considered in the model. The code for this goes like data["Car Brand"].unique()
'Hyundai', 'Maruti', 'Tata', 'Honda', 'Renault', 'Volkswagen', 'Ford', 'Toyota', 'Mahindra', 'Nissan', 'Skoda', 'Audi', 'Chevrolet', 'Datsun', 'KIA', 'MG', 'Volvo', 'Mercedes', 'Fiat', 'Landrover', 'BMW', 'ISUZU', 'Ssangyong', 'Mitsubishi', 'Jeep', 'Jaguar', 'TOYOTA'.

Code for models of a brand goes like:

data[data["Car Brand"] == 'Hyundai']['Model'].unique()

Here you can replace "Hyundai" with the brand you would like to predict and look for all the available models in it.

#### Location, Gear & Fuel:
Execute this to get the locations and fuel type available in the dataset

data["Location"].unique()

data["Gear"].unique()

data["Fuel"].unique()

### Result and Output:
Result gives you a dataframe comparing the actual and predicted values along with the percentage of residuals for each sample.
Output is the the prediction you are looking for.

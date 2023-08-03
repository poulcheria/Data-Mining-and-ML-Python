# Data-Mining-and-ML-Python


# Project Overview

This repository showcases a Python-based data analysis project that explores a dataset and utilizes two key components: DBSCAN clustering and LSTM (Long Short-Term Memory) neural network. The project explores a dataset containing the electrical energy needs of the State of California and the sources from which they are met. The dataset covers each day of the year from 1st January 2019 to 31st December 2021, recorded at a five-minute time resolution.


## Data Preprocessing & Analysis:

In this section of the project, the electrical energy dataset for the State of California is subjected to comprehensive data analysis and preprocessing to ensure its suitability for further exploration and modeling. The key steps involved in the data analysis are as follows:

1. File Renaming and Data Consolidation: To simplify the management of CSV files containing energy demand and sources data, the files are renamed with sequential names from 0 to the total number of files in each folder. Before consolidation, blank values in some columns are replaced with their respective averages, ensuring the presence of statistical values essential for subsequent analysis.

2. Merging Similar Columns: During data consolidation, it was observed that some columns contained similar data but with different capitalization, such as "Natural gas," "Natural Gas," "Large hydro," and "Large Hydro." To avoid redundancy and improve data consistency, these similar columns were merged into "Natural Gas" and "Large Hydro," respectively.

3. Descriptive Statistics: The function describe() is employed to extract essential descriptive statistics from the dataset. This includes measures like the mean, standard deviation (std), maximum (max), and minimum (min) values of the observations. 


## Data Clustering using DBSCAN for Identifying Days-Outliers:

In the DBSCAN.py file, a data analysis task is performed to identify days-outliers based on the prices of electrical energy demand and available energy resources for each day. The main goal is to detect days with abnormal price patterns or unexpected fluctuations in demand or production.

### Advantages of DBSCAN:
DBSCAN's ability to handle clusters of arbitrary shapes and effectively identify points as outliers without predefined cluster numbers makes it well-suited for detecting days-outliers in our energy price dataset. This data-driven analysis can provide valuable insights into potential issues or exceptional events related to energy demand or production.

## Neural Network using LSTM for Time-Series Prediction:

In the LSTM.py file Long Short-Term Memory (LSTM) neural network is implemented for time-series prediction. LSTM is a type of recurrent neural network (RNN) that excels at learning patterns and dependencies over time, making it suitable for time-series data analysis and forecasting.

**Neural Network Architecture**:
The LSTM neural network is designed with three layers: a visible layer with 1 input (time-step), a hidden layer with 32 LSTM blocks, and an output layer that generates a single value prediction.

**Data Preprocessing**:
Before training the neural network, the data is preprocessed to ensure optimal model performance. The values are normalized to a range of 0 to 1 to prevent the network from being sensitive to the magnitude of the data. This normalization ensures a consistent scale across different features and enhances convergence during training.

**Training and Hyperparameters**:
The LSTM neural network is trained for 300 epochs, meaning it goes through the entire dataset 300 times during training. A batch size of 100 is used, which means the network updates its weights after processing 100 data points.

**Model Evaluation**:
After training, the LSTM model is evaluated by comparing the actual values (in blue) with the predicted values (in orange). The figure shows the model's ability to capture the patterns and trends present in the time-series data. The closer the orange line aligns with the blue line, the more accurate the model's predictions are.


## Technologies Used

The project is implemented in Python, utilizing popular libraries for data analysis and machine learning, including:
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- TensorFlow
- NLTK
- Gensim

## Installation and Usage

To run this project locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required Python libraries using the following command:

``
pip install matplotlib \
pip install numpy  
pip install turtle  
pip install pydoc  
pip install cProfile  
pip install scikit-learn  
pip install tensorflow  
pip install nltk  
pip install genism  
``

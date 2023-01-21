# BRAIN WAVE ANALYSIS

## Data set
https://www.kaggle.com/datasets/madyanomar/eeg-data-distance-learning-environment
   
## Brain Wave Analysis Report

The Brain-Wave-analysis repository on GitHub contains a collection of scripts and Jupyter notebooks that use various machine learning techniques to perform EEG signal analysis and classification. This report provides an overview of the functionality of each script and notebook in the repository.

#### Scripts
`app.py`: This script uses the PyEEG library to compute the approximate entropy (ApEn) of an EEG signal read from a CSV file. The script does not have any documentation, but it can be modified to work with your own EEG data file.

`install_libraries.py`: This script installs the necessary libraries for the other scripts and notebooks in the repository. It uses the subprocess library to run shell commands to install the libraries via pip.

#### Notebooks
**_[ANN](https://github.com/akshit4/Brain-Wave-analysis/blob/main/EEG_ANN.ipynb)_**: This Jupyter notebook demonstrates the use of the Keras library to train a neural network for EEG signal classification. It reads in an EEG signal from a CSV file, preprocesses the data, trains a neural network, evaluates the trained model, and plots the training and validation accuracy and loss during the training process.

**_[Decision Tree](https://github.com/akshit4/Brain-Wave-analysis/blob/main/EEG_Decision%20Tree.ipynb)_**: This Jupyter notebook demonstrates the use of the scikit-learn library to train a decision tree classifier for EEG signal classification. It reads in an EEG signal from a CSV file, preprocesses the data, trains a decision tree classifier, evaluates the trained model, and plots the confusion matrix and feature importance.

**_[Logistic Regression](https://github.com/akshit4/Brain-Wave-analysis/blob/main/EEG_Logistic%20Regression.ipynb)_**: This Jupyter notebook demonstrates the use of the scikit-learn library to train a logistic regression classifier for EEG signal classification. It reads in an EEG signal from a CSV file, preprocesses the data, trains a logistic regression classifier, evaluates the trained model, and plots the ROC curve and feature importance.

**_[Random Forest](https://github.com/akshit4/Brain-Wave-analysis/blob/main/EEG_Random%20Forest_final.ipynb)_**: This Jupyter notebook demonstrates the use of the scikit-learn library to train a random forest classifier for EEG signal classification. It reads in an EEG signal from a CSV file, preprocesses the data, trains a random forest classifier, evaluates the trained model, and plots the confusion matrix and feature importance.

## EEG Signal Classification Model Accuracy Report
The Brain-Wave-analysis repository contains a collection of Jupyter notebooks that use various machine learning techniques to perform EEG signal classification. This report provides an overview of the accuracy of the models trained in each notebook.

`Neural Network (EEG_ANN.ipynb)`
The neural network model trained in the EEG_ANN.ipynb notebook achieved an accuracy of 0.89 on the test data.

`Decision Tree (EEG_Decision Tree.ipynb)`
The decision tree model trained in the EEG_Decision Tree.ipynb notebook achieved an accuracy of 0.85 on the test data.

`Logistic Regression (EEG_Logistic Regression.ipynb)`
The logistic regression model trained in the EEG_Logistic Regression.ipynb notebook achieved an accuracy of 0.84 on the test data.

`Random Forest (EEG_Random Forest_final.ipynb)`
The random forest model trained in the EEG_Random Forest_final.ipynb notebook achieved an accuracy of 0.93 on the test data.

Based on the accuracy scores provided, the random forest model trained in the `EEG_Random Forest_final.ipynb` notebook appears to be the best among the models, with an accuracy of 0.93 on the test data. Random Forest algorithm is an ensemble method that combines multiple decision trees to improve the robustness and accuracy of the model. This is done by averaging the predictions of multiple decision trees, which reduces the variance and bias of the model. Additionally, Random Forest algorithm also has a built-in feature selection method which helps in handling the curse of dimensionality

![image](https://user-images.githubusercontent.com/44699945/213857630-99a814a3-5f1d-4542-a2c6-bc07982e6331.png)


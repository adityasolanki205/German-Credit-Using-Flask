# Supervised Learning on German Credit Data

This is a **Supervised Learning Project on German Credit Data**. In this repository a complete process of Supervised Learning is explained. Here are the steps followed to perform this analysis :

1. **Data Loading**
2. **Data Exploration**
3. **Data Preprocessing**
4. **Model Selection**
5. **Model Evaluation**
6. **Conclusion**


## Motivation
For the last one year, I have been part of a great learning curve wherein I have upskilled myself to move into a Machine Learning and Cloud Computing. This project was practice project for all the learnings I have had. This is first of the many more to come. 
 

## Libraries/framework used

<b>Built with</b>
- [scikit-learn](https://scikit-learn.org/stable/)
- [seaborn](https://seaborn.pydata.org/)
- [matplotlib.pyplot](https://matplotlib.org/api/pyplot_api.html)
- [Pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)


## Code Example

```bash
    # clone this repo, removing the '-' to allow python imports:
    git clone https://github.com/adityasolanki205/German-Credit.git
```

## Installation

Below are the steps to setup the enviroment and run the codes:

1. **Data Setup**: First the data setup has to be done. Download the [German Credit Risk](https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)). Refined data is also present [here](https://www.kaggle.com/uciml/german-credit) 

2. **Exploratory Data Analysis**: Now we need check if the data is clean, how is the data in the dataset, what features require more refining and better representation. Using visualization and python's data analysis libraries we will try to extract hidden details from the data.

```python
    # All the codes are written in Jupyter Notebooks

    # Checking if there are any missing values
    customers.isnull().sum()
     
    # Checking how skewed is the data in the two classes of credit worthy and non credit worthy customers
    classification_count = customers.groupby('Classification').count()
    classification_count['Existing account']
    
    # Using group by we will try to capture various hidden details in the data
    grouped_data = df.groupby([column]).get_group(value)
    
    # Using various graphs we will try to see the details of the data
    sns.factorplot(data=customers, 
                   col='Number of credits', 
                   x='Credit history', 
                   y='Age', 
                   hue='Classification', 
                   kind='swarm', size=11, aspect=0.4, s=7)
```

3. **Data Wrangling**:  Now we will clean the data to be used by the Machine learning algorithms. Using Logrithmic transforms, Min Max Scaling and One Hot Encoding we will make the data machine readable and more relavant,

```python
    # Logrithmic transform to remove the outliers
    customers[numeric_columns].apply(lambda x: np.log(x + 1))
    
    # Min Max scaling to normalize the data
    customers_log_transformed[numeric_columns] = scaler.fit_transform(customers_log_transformed[numeric_columns])
    
    # One Hot Encoding for the Data becomes machine readable
    customers_final = pd.get_dummies(customers_log_transformed)
```

4. **Model Selection**: Now we will train 3 different types of Models and see which one is preforming better.

```python
    # First is Random Forest Algorithm
    Randon_forest_pred  = RandomForestClassifier().fit(X_train, y_train).predict(X_test)
    
    # Second is Logistic Regression Algorithm
    Logistic_regression_pred   = LogisticRegression().fit(X_train, y_train).predict(X_test)
    
    # Third is Support Vector Machine
    SVC_pred  = SVC(kernel = 'linear',probability = True).fit(X_train, y_train).predict(X_test)
```

5. **Model Evaluation**: After selecting top 2 models we will try to evaluate which one is better on the given model.

```python
    
```

## Tests
To test the code we need to do the following:

    1. Copy the photo to be tested in 'Test' subfolder of 'Data' folder. 
    Here I have used a photo of Elton John and Madonna
![](data/test/singers.jpg)
    
    2. Goto the 'Predict face in a group' folder.
    
    3. Open the 'Predict from a group of faces.ipynb'
    
    4. Goto filename variable and provide the path to your photo. Atlast run the complete code. 
    The recognised faces would have been highlighted and a photo would be saved by the name 'Highlighted.jpg'
![](final.jpg)

**Note**: The boundary boxes are color coded:

    1. Aditya Solanki  : Yellow
    2. Ben Affleck      : Blue   
    3. Elton John      : Green
    4. Jerry Seinfield : Red
    5. Madonna         : Aqua
    6. Mindy Kaling    : White
    
## How to use?
To run the complete code, follow the process below:

    1. Create Data Folder. 
    
    2. Create Sub folders as Training and Validation Dataset
    
    3. Create all the celebrity folders with all the required photos in them. 
    
    4. Run the Train and Test Data.ipynb file under Training Data Creation folder
    
    5. Save the output as numpy arrays
    
    6. Run the Face embedding using FaceNet.ipynb under the same folder name. This will create training data for SVM model
    
    7. Run the Predict from a group of faces.ipynb to recognise a familiar face

## Credits
1. David Sandberg's facenet repo: [https://github.com/davidsandberg/facenet](https://github.com/davidsandberg/facenet)
2. Tim Esler's Git repo:[https://github.com/timesler/facenet-pytorch](https://github.com/timesler/facenet-pytorch)
3. Akash Nimare's README.md: https://gist.github.com/akashnimare/7b065c12d9750578de8e705fb4771d2f#file-readme-md
4. [Machine learning mastery](https://machinelearningmastery.com/how-to-develop-a-face-recognition-system-using-facenet-in-keras-and-an-svm-classifier/)

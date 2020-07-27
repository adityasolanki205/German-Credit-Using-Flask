# Deep Learning on German Credit Data

This is a **Supervised Learning Project on German Credit Data**.In this repository we will just implement this application using Flask Architecture to run it on Google Cloud. The complete process to Train and test is present [here](https://github.com/adityasolanki205/German-Credit).This model is trained to detect if the transaction is Fraud or not. In this repository a complete process of Supervised Learning is explained. This Repository is divided into 2 parts:

1. **Setting up the application on Google Cloud**
2. **Create a POST request to Detect Fraud Transactions**


## Motivation
For the last one year, I have been part of a great learning curve wherein I have upskilled myself to move into a Machine Learning and Cloud Computing. This project was practice project for all the learnings I have had. This is first of the many more to come. 
 

## Libraries/framework used

<b>Built with</b>
- [Pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [Keras](https://keras.io/)
- [TensorFlow](https://www.tensorflow.org/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)


## Code Example

```bash
    # clone this repo, removing the '-' to allow python imports:
    git clone https://github.com/adityasolanki205/German-Credit-Using-Flask.git
```

## Installation

Below are the steps to setup the enviroment and run the codes:

1. **Cloud account Setup**: First we will have to setup free google cloud account which can be done [here](https://cloud.google.com/free). 

2. **Creating a Google Compute instance**: Now we have to create a Compute Engine Instance to deploy the app. To do that we will use **n1-standard-8** as it has larger processing power. For Boot Disk we will select **Ubuntu 18.04 LTS**. Also tick on the Allow Http traffic label to send/receive requests. At last click on create button.

![](images/compute_instance.gif)

3. **Create Firewall policy to allow Flask to access GCP**: For Local host to access google cloud we will have to
create a firewall rule to let port 5000 access Compute instance. To do that go to VPC/Firewall tool on google Console and create a new firewall rule.

![](images/firewall.gif)

4. **Deploying the App on Compute Engine**: After creating the instance, we will deploy the code on the instance using SSH. So click on the SSH button to create a session to deploy our code.

```bash
    # update system packages and install the required packages
    sudo apt-get update
    sudo apt-get install bzip2 libxml2-dev libsm6 libxrender1 libfontconfig1
    
    # clone the project repo
    git clone https://github.com/adityasolanki205/German-Credit-Using-Flask.git
    
    # download and install miniconda
    wget https://repo.anaconda.com/miniconda/Miniconda3-4.7.10-Linux-x86_64.sh
    bash Miniconda3-4.7.10-Linux-x86_64.sh
    
    export PATH=/home/<your name here>/miniconda3/bin:$PATH
    
    rm Miniconda3-4.7.10-Linux-x86_64.sh
    
    # confirm installation
    which conda
```
![](images/startup.jpg)

5. **Running the App**:  Now we will run the app on the instance

```bash
    # Goto the Flask Folder
    cd German-Credit-Using-Flask
    
    # Installing all the dependencies
    pip install -r requirements.txt
    
    # Running the app 
    python app.py
```
![](images/application.jpg)

6. **Creating a POST request from Local**: After this we will create a POST request from the local. To do that we will just run request.py from local. There is one thing that has to be changed in the request.py file i.e. the IP address of the instance. Copy the external IP of the instance from Google cloud Console and paste in the request.py file. The X_test_json file was already created [here](https://github.com/adityasolanki205/German-Credit-Using-Flask/blob/master/German%20Credit-TensorFlow.ipynb)

```python
    import requests
    import json

    url = "http://<External IP address>:5000/predict"
    headers={"content-type": "application/json"}

    # send HTTP request to the server
    response = requests.post(url, data=open('json/X_test_json.json', 'rb'), headers=headers)
    predictions = response.json()
```
![](images/request.jpg)

6. **See the magic happen**: Run Request.py file and see detected labels for each request received backfrom Google Cloud. The output received will be in the form of Json which could be used in anywhere .



## Repository Content

    1. German Credit-Tensorflow.ipynb

    2. app.py
    
    3. german_credit.h5    
    
    4. request.py
    
    5. german_credit.py
    
    6. requirements.txt
    

## Credits
1. Akash Nimare's [README.md](https://gist.github.com/akashnimare/7b065c12d9750578de8e705fb4771d2f#file-readme-md)
2. [Machine Learning Mastery](https://machinelearningmastery.com/imbalanced-classification-of-good-and-bad-credit/)
3. Special thanks to [Deploying ML Model](https://towardsdatascience.com/deploying-a-custom-ml-prediction-service-on-google-cloud-ae3be7e6d38f)

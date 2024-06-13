# Project Report

## Source Data and Statistics

### Data Overview

**Project goal**: to develop a model which will predict prices for monthly rent of the flats using historical data

We have data from [Yandex.Realty](https://realty.yandex.ru) classified  containing real estate listings for apartments in St. Petersburg and Leningrad Oblast from 2016 till the middle of August 2018. There are different datatypes in the dataset including integers, floating points, strings and booleans. The initial dataset has information about flats for sell and for rent. It has 429 187 rows and 17 columns.

### Data Types

- integer: 6 columns (offer_id, floor, rooms, offer_type, category_type, building_id)
- bool: 2 columns (open_plan, studio)
- float: 6 columns (last_price, area, kitchen_area, living_area, agent_fee, renovation)
- object: 3 columns (first_day_exposition, last_day_exposition, unified_address)

### Data Visualization


## Information about model, choosen framework, hyperparams 
**Features:** floor,	open_plan,	rooms,	area,	renovation

**Target variable:** last_price

Were developed 5 models: LinearRegressor, DecisionTreeRegressor, RandomForestRegressor, CatBoostRegressor and GradientBoostingRegressor. The models were developed with sklearn library which is quiet commonly used for building machine learning models. The best results in terms of metrics were demonstrated by GBRegressor.


**Chosen model:** GradientBoostingRegressor

**Hyperparameters** were tuned using GridSearch with cross-validation (GridSearchCV).

The parameters:
- n_estimators: [50, 100, 150], 
- learning_rate: [0.05, 0.1, 0.15] 
- max_depth: [None, 3, 5, 7, 10,] 


## Installation and Running Instructions With Virtual Environment
Creating and activating virtual environment

`python3 -m venv .venv
source .venv/bin/activate`

List of all the insatlled packages can be found in the file requirements.txt. All the necessary packages can be insatlled using the following command:

`pip insatll -r requirements.txt`

Run the app using the following command:

`python3 app.py`

## Information About Dockerfile and It’s Content

```
FROM ubuntu:20.04
MAINTAINER Amina Uzdenova
RUN apt-get update -y
COPY . /opt/gsom_predictor
WORKDIR /opt/gsom_predictor
RUN apt install -y python3-pip
RUN pip3 install -r requirements.txt
CMD python3 app.py
```

### This Dockerfile creates a Docker image that:

- Uses Ubuntu 20.04 as the base image.
- Updates the package list.
- Copies the current directory's contents into /opt/gsom_predictor inside the image.
- Sets /opt/gsom_predictor as the working directory.
- Installs python3-pip for managing Python packages.
- Installs the necessary Python packages listed in requirements.txt.
- Runs the Python application app.py when the container starts.

## How to open the port in your remote VM
To open the port on remote VM use the following command

`ssh <login>@<your_vm_address>` 

## How to run app using docker and which port it uses

```
docker run --network host -d aminauzdenova/gsom_e2e24:v.0.1
sudo ufw allow 7778
python3 app.py
```
# car-rental-api

Car rental api was built on django restframework for developers,companies and users to have easy usability to renting out their stuff mainly cars.

## Table of Contents

1.[Prerequisites](#Prerequisites)
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Features](#features)
5. [Contributing](#contributing)
6. [License](#license)
7. [Authors](#authors)
8. [Acknowledgments](#acknowledgments)

#### Prerequisites
Before using the RentalApi,you need to have a fair idea on how to integrate apis into your system in any programming langugae.If not,there's a documentation for you at :[Car Rental Api](https://rentalapi.onrender.com)

## Installation
If you want to run the system on your localhost,follow these steps:
You can skip to the next section [Usage](#usage) to use the hosted system [Car Rental Api](https://rentalapi.onrender.com)
1. clone this github repository using the command:
`git clone https://github.com/Silas003/car-rental-api`
2. create a virtual environment inside the main folder by running:
`python -m venv virtual-env` after you have installed the virtual enviroment package through `pip install venv`
3. run the command: `<your-virtual-env-name>/Scripts/activate` to activate the virtual environment
4. run `pip install -r requirements.txt` which would install all the packages needed to run the system smoothly without any hassle
5. run `python manage.py makemigrations ` to acknowlege the creation of new models
6. run `py manage.py migrate` to move all the data into the database
7. finally,run `py manage.py runserver` to start the localhost server for development


## Usage

### Base URL/Endpoint
The base URl for this is API is `https://rentalapi.onrender.com/api/v1/`

##  Endpoints

### GET / list of all vehicles
- **Description:** Get list of all vehicles no matter their status being it `[available/unavailable]`
`https://rentalapi.onrender.com/api/v1/list-vehicles`


## Example Usage
GET `https://rentalapi.onrender.com/api/v1/list-vehicles?car_brand=toyota&car_model=highlander&prod_year=2020`
This request will fetch a vehicle called toyota highlander produced in the year 2020

GET `https://rentalapi.onrender.com/api/v1/list-vehicles?search=toyota`
This request will search all vehicles called toyota and return their data to the consumer
## How to Use the API Documentation (/docs)

1. Open a web browser.
2. Visit the URL: [Car Rental Api](https://rentalapi.onrender.com)
3. Explore the available endpoints, parameters, and schemas.
4. Test the API by providing parameters and making requests directly from the browser interface.

Feel free to explore the interactive API documentation to understand the available endpoints and how to interact with them.
# Food Order Delivery (Microservice)
Multiple Services with Django App and Kafka 

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Application has been  devided into 3 microservices using Kafka for Event sharing.
For Backend Services Django Framework has been used and Database has been sepated. For Kafka running Docker has been used. For getting data as a consumer service multithreading has been implemented inside all Django applications.


To run application clone the source and install all required dependencies

## Installation

### Application requires [Python](https://www.python.org/) v3.8+ to run.

Install the dependencies and devDependencies and start the server.

```sh

pip install requirements.txt

```

In order to run multithreading script open new terminal and run following script

```sh

python3 manage.py run_script

```


The following script has been added inside app folder 

```sh

project/app/management/commands --> run_script.py

```

### explanation
<p float="left">
  <img src="https://github.com/barkhayot/food-microservice/blob/main/rer.jpg" alt="Markdown Monster icon" style="width:100%"/>
  </p>


### scree of usage

<p float="left">
  <img src="https://github.com/barkhayot/food-microservice/blob/main/screeeb.png" alt="Markdown Monster icon" style="width:100%"/>
  </p>
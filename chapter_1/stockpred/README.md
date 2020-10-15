# bitpred
Open source bitcoin price movement prediction engine.

V0.01 - Features
* Is it "going down" - tomorrow ( within 24hours) api backend classifier
* Get data from public sources (yahoo)
* Combine data with relevant influencers data ( Twitter for ) now
* Create a complete e2e backend classifier and ML pipeline

# data 
Currently using live streams from : Yahoo 

## How to run training

### Install MLFlow locally
`$ pip install mlflow`


### From mlflow 

Locally:
`$ mlflow run .`

From github:
`$ mlflow run https://github.com/nlauchande/bitpred/ `



## How to run a listening prediction api
Using the id of the model and the model name you can run the following commnad :

`$  mlflow models serve -m ./mlruns/0/b9ee36e80a934cef9cac3a0513db515c/artifacts/model_random_forest/ `


## How to run a prediction

`curl http://127.0.0.1:5000/invocations -H 'Content-Type: application/json' -d '{"data":[[1,1,1,1,0,1,1,1,0,1,1,1,0,0]]}'                                                                                                            
[1]%`

## How to monitor experiments with MLFlow

### Run the server



## How to add a new algorithm
You can modify the train.py file .

=======
Currently using live streams from Yahoo.
 
## GitHub Issues


### Features

We also use the issue tracker to track features. If you have an idea for a feature, or think you can help kops become even more awesome follow the steps below.

- Open a [new issue](https://github.com/nlauchande/bitpred/issues/new).
- Remember users might be searching for your issue in the future, so please give it a meaningful title to help others.
- Clearly define the use case, using concrete examples. EG: I type `this` and kops does `that`.
- Some of our larger features will require some design. If you would like to include a technical design for your feature please include it in the issue.
- After the new feature is well understood, and the design agreed upon we can start coding the feature. We would love for you to code it. So please open up a **WIP** *(work in progress)* pull request, and happy coding.

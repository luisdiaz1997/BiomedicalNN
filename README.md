## Our Website

* [BAD DATA HEALTH](http://baddatahealth.com)

------------------------------------------------------------

## Built With

* [FastAI](https://www.fast.ai) - Deep Learning library for [Pytorch](https://pytorch.org)
* [create-react-app](https://github.com/facebook/create-react-app) - Used to build our [front end](https://github.com/eramos4/csc821-finalproject)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Used to serve as REST API server to communicate our model and front-end
* [Gunicorn](https://gunicorn.org) - Used to handle our HTTP server
* [NGINX](https://nginx.org/en/) - Used to handle out HTTP proxy server

------------------------------------------------------------------------

# Deploy on your computer

## Instalation
Install anaconda 3 in your system
https://www.anaconda.com/products/individual

Then create new environment

```
conda create --name fast python=3.6
```

Activate the environment
```
conda activate fast
```

Then install packages
```
conda install pytorch=1.4 torchvision -c pytorch
conda install -c fastai fastai
conda install flask gunicorn
```
---------------------------------------
## Test run

```
python model.py sample/NORMAL2-IM-1427-0001.jpeg | python model.py sample/person1947_bacteria_4876.jpeg
```

<p float="center">
  <img src="https://github.com/luisdiaz1997/BiomedicalNN/blob/master/predictions/NORMAL2-IM-1427-0001.jpeg?raw=true" width="200" />
  <img src="https://github.com/luisdiaz1997/BiomedicalNN/blob/master/predictions/person1947_bacteria_4876.jpeg?raw=true" width="200" />
</p>

---------------------------------------
## Changing the paths
You can change the paths of where the model is located
And where the predictions will be sent
by changing the following in [model.py](https://github.com/luisdiaz1997/BiomedicalNN/blob/master/model.py)

```
model_path = 'models/'
output_path = 'predictions/'
```

make sure that the path of the models
always contains the file "dense"

---------------------------------------
## Deployment

```
gunicorn --bind 0.0.0.0:5000 wsgi:app
```

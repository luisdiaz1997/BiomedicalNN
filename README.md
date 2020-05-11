
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
python model.py sample/NORMAL2-IM-0832-0001-0002.jpeg
python model.py sample/person469_bacteria_1993.jpeg
```
That should create files with same name in ./predictions, they will contain a green title with the prediction
model.py just takes the path of an image as argument, this path can be anywhere in the computer

---------------------------------------
## Changing the paths
You can change the paths of where the model is located
And where the predictions will be sent
by changing the following in model.py

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

----------------------------------------
## Built With

* [FastAI](https://www.fast.ai) - Deep Learning library for [Pytorch](https://pytorch.org)
* [create-react-app](https://github.com/facebook/create-react-app) - Used to build our [front end](https://github.com/eramos4/csc821-finalproject)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Used to serve as REST API server to communicate our model and front-end

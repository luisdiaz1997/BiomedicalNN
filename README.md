
Install anaconda 3 in your system
https://www.anaconda.com/products/individual

--Then create new environment

```
conda create --name fast python=3.6
```

--Activate the environment
conda activate fast

Then install packages
conda install pytorch=1.4 torchvision -c pytorch
conda install -c fastai fastai
conda install flask gunicorn

---------------------------------------
--Test run

python model.py sample/NORMAL2-IM-0832-0001-0002.jpeg
python model.py sample/person469_bacteria_1993.jpeg

--That should create files with same name in ./predictions
--They will contain a green title with the prediction
--model.py just takes the path of an image as argument
--this path can be anywhere in the computer
---------------------------------------
--Changing the paths
--You can change the paths of where the model is located
--And where the predictions will be sent
--by changing the following in model.py

model_path = 'models/'
output_path = 'predictions/'

--make sure that the path of the models
--always contains the file "dense"

---------------------------------------
--Run server

gunicorn --bind 0.0.0.0:5000 wsgi:app

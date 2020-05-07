import io
import model
import os
from flask import Flask, request,\
render_template,jsonify

#from flask_assets import Bundle, Environment

dir_path = os.path.dirname(os.path.realpath(__file__))


app = Flask(__name__)


'''
js = Bundle('like_button.js', output = 'main.js')
assets = Environment(app)
assets.register('main_js', js)
'''


@app.route('/predict', methods = ['POST','GET'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        im = model.image_from_bytes(file.read())
        category, predictions = model.predict(im)
        fig = model.fig_from_pred(im, category, predictions)
        fig.savefig(model.output_path + file.filename , bbox_inches='tight')
        return jsonify({'class_id': category,\
        'class_name': model.label_dict[category],\
        'class_probability': float(predictions[category]),
        'results': os.path.join(dir_path, 'predictions', file.filename)})
    return render_template('file_upload.html')


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)

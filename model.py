import fastai
from fastai.vision import *
import matplotlib as mpl
mpl.use('Agg')
import sys
import io
import PIL


def image_from_bytes(image_bytes):
    im = PIL.Image.open(io.BytesIO(image_bytes))
    im = pil2tensor(im.convert("RGB"), np.float32).div_(255)
    im = Image(im)
    return im

def predict(im, p_name = 'prediction.png'):
    model_path = 'models/'
    output_path = 'predictions/'
    label_dict = {0: 'NORMAL', 1: 'PNEUMONIA'}
    learn = load_learner(path = model_path, file = 'dense')
    fig = plot_class_pred(learn, im, label_dict)
    fig.savefig(output_path + p_name, bbox_inches='tight')



def predict_from_path(im_path):
    im = open_image(im_path)
    predict(im, im_path.split('/')[-1])

def plot_class_pred(learner, im, label_dict):

    category, category_t, preds = learner.predict(im)
    fig = plt.figure(1)
    plt.imshow(im.data.detach().numpy().transpose(1, 2, 0))
    plt.gca().set_title('{0}, {1:.1f}%'.format(
        label_dict[int(category_t)],
        preds[int(category_t)].detach().numpy() * 100),
        color=("green")
    )

    plt.axis('off')
    return fig



if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Please input the path of the image')
    else:
        predict_from_path(sys.argv[1])

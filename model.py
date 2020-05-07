import fastai
from fastai.vision import *
import matplotlib as mpl
mpl.use('Agg')
import sys
import io
import PIL

model_path = 'models/'
output_path = 'predictions/'
label_dict = {0: 'NORMAL', 1: 'PNEUMONIA'}
learner = load_learner(path = model_path, file = 'dense')

def image_from_bytes(image_bytes):
    im = PIL.Image.open(io.BytesIO(image_bytes))
    im = pil2tensor(im.convert("RGB"), np.float32).div_(255)
    im = Image(im)
    return im

def predict(im):
    category, category_t, preds = learner.predict(im)
    return int(category_t), preds

def fig_from_pred(im, category_t, preds):
    fig = plt.figure(1)
    plt.imshow(im.data.detach().numpy().transpose(1, 2, 0))
    plt.gca().set_title('{0}, {1:.1f}%'.format(
        label_dict[category_t],
        preds[category_t].detach().numpy() * 100),
        color=("green")
    )
    plt.axis('off')
    return fig

def predict_from_path(im_path, savefig = True):
    im = open_image(im_path)
    category_t, preds = predict(im)
    if savefig:
        fig = fig_from_pred(im, category_t, preds)
        fig.savefig(output_path + im_path.split('/')[-1], bbox_inches='tight')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Please input the path of the image')
    else:
        predict_from_path(sys.argv[1])

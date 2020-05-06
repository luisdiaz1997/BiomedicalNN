import fastai
from fastai.vision import *
import sys

def predict_from_dir(im_dir):

    model_path = 'models/'
    output_path = 'predictions/'


    label_dict = {0: 'NORMAL', 1: 'PNEUMONIA'}
    learn = load_learner(path = model_path, file = 'dense')
    fig = plot_class_pred(learn, im_dir, label_dict)
    fig.savefig(output_path + im_dir.split('/')[-1], bbox_inches='tight')


def plot_class_pred(learner, im_path, label_dict):
    im = open_image(im_path)
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
        predict_from_dir(sys.argv[1])

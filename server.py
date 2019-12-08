from __future__ import division, print_function
import os
import numpy as np
import requests
from PIL import Image
import torch.nn.functional as F
from torchvision import models, transforms

from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
from flask import request, Flask, render_template
import time


# labels for image net classification
LABELS_URL = 'https://s3.amazonaws.com/mlpipes/pytorch-quick-start/labels.json'
labels = {int(key):value for (key, value)
          in requests.get(LABELS_URL).json().items()}

# Data preprocess
preprocess = transforms.Compose([
   transforms.Resize(256),
   transforms.CenterCrop(224),
   transforms.ToTensor(),
   transforms.Normalize(
     mean=[0.485, 0.456, 0.406],
     std=[0.229, 0.224, 0.225])
])

# ResNet initialization
model = models.resnet18(pretrained=True).eval()


# web servers
app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Receive the file
        start_time = time.time()
        f = request.files['image']

        # Save the file
        root = os.path.dirname(__file__)
        img_folder = os.path.join(root, 'images')
        if not os.path.exists(img_folder):
            os.makedirs(img_folder)

        img_path = os.path.join(img_folder, secure_filename(f.filename))
        f.save(img_path)

        # Recognize the image
        img_pil = Image.open(img_path)
        img_tensor = preprocess(img_pil)
        img_tensor.unsqueeze_(0)
        fc_out = model(img_tensor)
        fc_out = F.softmax(fc_out)
        lbl_out = np.argsort(fc_out[0].data.numpy())[-1]
        result = " Top-1 prediction:\"" + str(labels[lbl_out]) + " \";  Confidence: %.3f" % (fc_out[0].data.numpy()[lbl_out]) + ", Response Time: %.3f s" % (time.time() - start_time)
        return result
    return None


if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 13456), app)
    http_server.serve_forever()

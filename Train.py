import numpy as np
import os

from tflite_model_maker.config import ExportFormat
from tflite_model_maker import model_spec
from tflite_model_maker import object_detector

import tensorflow as tf
assert tf.__version__.startswith('2')

tf.get_logger().setLevel('ERROR')
from absl import logging
logging.set_verbosity(logging.ERROR)

label_map = {1: 'player', 2: 'goalkeeper', 3:'referee', 4: 'ball'} 

train_images_dir = '/content/dataset/train_image'
train_annotations_dir = '/content/dataset/train_label'
val_images_dir = '/content/dataset/valid_image'
val_annotations_dir = '/content/dataset/valid_label'
test_images_dir = '/content/dataset/test_image'
test_annotations_dir = '/content/dataset/test_label'

train_data = object_detector.DataLoader.from_pascal_voc(
    train_images_dir, train_annotations_dir, label_map=label_map)

validation_data = object_detector.DataLoader.from_pascal_voc(
    val_images_dir, val_annotations_dir, label_map=label_map)

test_data = object_detector.DataLoader.from_pascal_voc(
    test_images_dir, test_annotations_dir, label_map=label_map)

spec = model_spec.get('efficientdet_lite2')

model = object_detector.create(train_data=train_data, 
                               model_spec=spec, 
                               validation_data=validation_data, 
                               epochs=50, 
                               batch_size=64,
                               train_whole_model=True)

model.evaluate(test_data)

TFLITE_FILENAME = 'trained_model.tflite'
LABELS_FILENAME = 'model-labels.txt'

model.export(export_dir='.', tflite_filename=TFLITE_FILENAME, label_filename=LABELS_FILENAME,
             export_format=[ExportFormat.TFLITE, ExportFormat.LABEL])

'''
# download vgg16 trained parameters from ftp://mi.eng.cam.ac.uk/pub/mttt2/models/vgg16.npy

reference
https://github.com/machrisaa/tensorflow-vgg
https://github.com/MarvinTeichmann/tensorflow-fcn
'''

import numpy as np
import tensorflow as tf

import scipy as scp
import scipy.misc
import os
from images_labels_1000 import labels

os.environ['CUDA_VISIBLE_DEVICES'] = '2'

VGG_MEAN = [103.939, 116.779, 123.68]

def get_paras(name, paras_name, data_dict):

    paras = []
    for i in range(len(paras_name)):
        init = tf.constant_initializer(value=data_dict[name][i], dtype=tf.float32)
        shape = data_dict[name][i].shape

        var = tf.get_variable(name=paras_name[i], initializer=init, shape=shape)
        paras.append(var)

    return paras

def conv2d(input, name, data_dict):
    paras_name = ['filter', 'bias']
    filter, bias = get_paras(name, paras_name, data_dict)

    res = tf.nn.conv2d(input, filter, [1, 1, 1, 1], padding='SAME')
    res = tf.nn.bias_add(res, bias)
    res = tf.nn.relu(res)

    return res


def maxPooling(input):
    pool = tf.nn.max_pool(input, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    return pool


def fully_connected(input, name, data_dict):
    paras_name = ['weight', 'bias']
    weight, bias = get_paras(name, paras_name, data_dict)

    res = tf.matmul(input, weight)
    res = tf.nn.bias_add(res, bias)
    res = tf.nn.relu(res)

    return res


def vgg16(rgb):

    data_dict = np.load('./vgg16.npy', encoding='latin1').item()

    red, green, blue = tf.split(rgb, 3, 3)
    input = tf.concat([
                blue - VGG_MEAN[0],
                green - VGG_MEAN[1],
                red - VGG_MEAN[2],
            ], 3)

    names = ['conv1_1', 'conv1_2', 'conv2_1', 'conv2_2', 'conv3_1', 'conv3_2', 'conv3_3', 'conv4_1', 'conv4_2', 'conv4_3',
             'conv5_1', 'conv5_2', 'conv5_3', 'fc6', 'fc7', 'fc8']

    res = [input]
    pre = ''

    for name in names:
        if 'con' in pre and pre.split('_')[0] != name.split('_')[0]:
            res[-1] = maxPooling(res[-1])

        with tf.variable_scope(name) as scope:
            if 'con' in name:
                tmp = conv2d(res[-1], name, data_dict)
            else:
                if name == 'fc6':
                    shape = res[-1].shape
                    flatten = shape[1] * shape[2] * shape[3]
                    res[-1] = tf.reshape(res[-1], [-1, flatten])

                tmp = fully_connected(res[-1], name, data_dict)

            res.append(tmp)
        print('after {0}, shape: {1}'.format(name, res[-1].shape))
        pre = name

    classifier = tf.argmax(res[-1], dimension=1)

    return classifier

if __name__ == '__main__':

    img_path = ['./tabby_cat.png', './kobe.jpg']
    vec = []
    for path in img_path:
        img = scp.misc.imread(path)
        skip = 0
        img = img[0:224, skip:224+skip, :]
        img = np.expand_dims(img, 0)
        vec.append(img)

    imgs = np.concatenate(vec, 0)
    rgb = tf.placeholder('float', shape=[None, 224, 224, 3])
    classifier = vgg16(rgb)
    
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)
    
    res = sess.run(classifier, feed_dict={rgb : imgs})
    #print(res)

    for i in range(len(res)):
        print('{0} is classified to "{1}"'.format(img_path[i], labels[res[i]]))


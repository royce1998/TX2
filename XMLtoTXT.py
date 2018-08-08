import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import subprocess

classes = ["chairs", "gym_bike", "person", "yogaball"]

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

wd = getcwd()

if not os.path.exists('image_data/labels'):
    os.makedirs('image_data/labels')

list_file = open('imagelist.txt', 'w')

for image_id in os.listdir('image_data/images'):
    list_file.write('%s/image_data/images/%s\n' % (wd, image_id))
    try: in_file = open('image_data/annotations/%s.xml' % os.path.splitext(image_id)[0])
    except FileNotFoundError:
        subprocess.check_output(['mv', 'image_data/images/%s' % image_id, 'image_data/useless'])
        continue
    out_file = open('image_data/labels/%s.txt' % os.path.splitext(image_id)[0], 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text

        if cls not in classes or int(difficult) == 1:
            continue

        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

list_file.close()

import os
from PIL import Image
import pandas as pd
import numpy as np
import pickle
import torch
from torch.utils import data
import torchvision.transforms as transforms

from utils.dataset import AVADataset

if __name__ == "__main__":
    root = './AVA/images'
    pickle_file = './train.pickle'
    train_transform = transforms.Compose([
        transforms.Resize(256), 
        transforms.RandomCrop(224), 
        transforms.RandomHorizontalFlip(), 
        transforms.ToTensor(), 
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
    dataset = AVADataset(pickle_file=pickle_file, root_dir=root, transform=train_transform)
    train_loader = data.DataLoader(dataset, batch_size=4, shuffle=True, num_workers=4)
    for i, data in enumerate(train_loader):
        images = data['image']
        print(images.size())
        labels = data['annotations']
        print(labels.size())
        print(labels)
        print(data['img_id'])
        print(data['score'])


        exit()
    
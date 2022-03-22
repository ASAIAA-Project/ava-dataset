import os
from PIL import Image
import pandas as pd
import numpy as np
import pickle
from torch.utils import data
import torchvision.transforms as transforms

class AVADataset(data.Dataset):
    """AVA dataset
    Args:
        pickle_file: a 12-column pickle_file
            column one contains the names of image files
            column 2-11 contains the empiricial distributions of ratings
            column 12 contains the score
        root_dir: directory to the images
        transform: preprocessing and augmentation of the training images
    """

    def __init__(self, pickle_file, root_dir, transform=None):
        with open(pickle_file, 'rb') as handle:
            self.annotations = pickle.load(handle)
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.annotations)

    def __getitem__(self, idx):
        img_name = os.path.join(self.root_dir, f'{int(self.annotations[idx][0])}.jpg')
        image = Image.open(img_name).convert('RGB')
        annotations = self.annotations[idx][1:11]
        annotations = annotations.astype('float').reshape(-1, 1)
        score = self.annotations[idx][11]
        sample = {
            'img_id': img_name,
            'image': image,
            'annotations': annotations,
            'score' : score}

        if self.transform:
            sample['image'] = self.transform(sample['image'])

        return sample
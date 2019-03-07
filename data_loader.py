from torch.utils import data
from torchvision import transforms as T
from torchvision.datasets import ImageFolder
from PIL import Image
import torch
import os


class PokemonDataset(data.Dataset):
    def __init__(self, root, transform):

        self.transform = transform

        # Get img paths
        for root, dirs, files in os.walk(root):
            print(root)
            # print(files)
            self.imgs_path = []
            for f in files:
                self.imgs_path.append(root + f)

    def __getitem__(self, index):
        img = self.imgs_path[index]
        img = Image.open(img).convert('RGB')
        img = self.transform(img)

        return img

    def __len__(self):
        return len(self.imgs_path)


        
"""This code is to verify the image dataset and check that all the labels of the grid location are in the correct place.
"""

import PIL.Image as Image
from matplotlib import pyplot as plt
import numpy as np
from image import SudokuDataset, get_dataset, tqdm, Model
import torch

img_size = (300,300)

def mark(positions, image, color_value):
    print(positions)
    print(image.shape)
    x0,y0,x1,y1,x2,y2,x3,y3 = positions
    image = image.transpose()
    grad = (y1 - y0)/(x1 - x0)
    if x1 > x0:
        for i in range(x1 - x0):
            image[x0 + i, int(y0 + i * grad)] = color_value
    else:
        for i in range(x0 - x1):
            image[x0 - i, int(y0 - i * grad)] = color_value
    
    grad = (y2 - y1)/(x2 - x1)
    if x2 > x1:
        for i in range(x2 - x1):
            image[x1 + i, int(y1 + i * grad)] = color_value
    else:
        for i in range(x1 - x2):
            image[x1 - i, int(y1 - i * grad)] = color_value
    
    grad = (y3 - y2)/(x3 - x2)
    if x3 > x2:
        for i in range(x3 - x2):
            image[x2 + i, int(y2 + i * grad)] = color_value
    else:
        for i in range(x2 - x3):
            image[x2 - i, int(y2 - i * grad)] = color_value
    
    grad = (y0 - y3)/(x0 - x3)
    if x0 > x3:
        for i in range(x0 - x3):
            image[x3 + i, int(y3 + i * grad)] = color_value
    else:
        for i in range(x3 - x0):
            image[x3 - i, int(y3 - i * grad)] = color_value
    return image.transpose()

# dataset = SudokuDataset("./archive/outlines_sorted.csv", img_size)
# for item in dataset:
#     try:
#         image = item['image']
#         grid = item['grid']
#         x0,y0,x1,y1,x2,y2,x3,y3 = list(grid.numpy())
#         x0 = int(x0 * img_size[0])
#         x1 = int(x1 * img_size[0])
#         x2 = int(x2 * img_size[0])
#         x3 = int(x3 * img_size[0])
#         y0 = int(y0 * img_size[1])
#         y1 = int(y1 * img_size[1])
#         y2 = int(y2 * img_size[1])
#         y3 = int(y3 * img_size[1])
#         image = mark((x0,y0,x1,y1,x2,y2,x3,y3), image.numpy()[0], 0.7)
#         plt.imshow(image)
#         plt.colorbar()
#         plt.show()
#     except KeyboardInterrupt:
#         break

def test(config:dict, model_filename:str):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = torch.load(model_filename).to(device)
    model.eval()
    loss = torch.nn.MSELoss().to(device)
    dataset = get_dataset(config['filename'], config['input_shape'], config['batch_size'])
    batch_iterator = tqdm(dataset)
    for batch in batch_iterator:
        x = batch['image'].to(device)
        y_true = batch['grid'].to(device)
        # print(batch['grid'])
        # return
        y_pred = model(x)
        error = loss(y_true, y_pred)
        batch_iterator.set_postfix({"loss":f"Loss: {error.item():6.6f}"})
        x0,y0,x1,y1,x2,y2,x3,y3 = list(y_pred.detach().numpy()[1])
        print(x0,y0,x1,y1,x2,y2,x3,y3)
        x0 = int(x0 * img_size[0])
        x1 = int(x1 * img_size[0])
        x2 = int(x2 * img_size[0])
        x3 = int(x3 * img_size[0])
        y0 = int(y0 * img_size[1])
        y1 = int(y1 * img_size[1])
        y2 = int(y2 * img_size[1])
        y3 = int(y3 * img_size[1])
        image = mark((x0,y0,x1,y1,x2,y2,x3,y3), x.detach().numpy()[0][0], 0.7)
        plt.imshow(image)
        plt.colorbar()
        plt.show()

config = {
    "input_shape": (300,300),
    "filename": "archive/outlines_sorted.csv",
    "number_of_layers": 4,
    "dims": 3,
    "batch_size": 8,
    "lr": 1e-5
}
# model = train(50, config)
test(config, "model.pt")
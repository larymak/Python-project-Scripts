import torch
from torch.utils.data import Dataset, DataLoader
import PIL.Image as Image
import pandas as pd
from tqdm import tqdm
import numpy as np


class SudokuDataset(Dataset):
    def __init__(self, grid_locations_file:str, input_shape:tuple[int, int]) -> None:
        super().__init__()
        self.grid_locations = []
        self.image_filenames = []
        self.input_shape = input_shape
        self.all_data = pd.read_csv(grid_locations_file, header=0)
        self.image_filenames = list(self.all_data['filepath'].to_numpy())
        self.grid_locations = [list(a[1:]) for a in self.all_data.values]
        to_pop = []
        for i,file in enumerate(self.image_filenames):
            try:
                Image.open(file)
            except FileNotFoundError:
                to_pop.append(i)
                print(f"{file} not found.")
        for i in reversed(to_pop):
            self.image_filenames.pop(i)
            self.grid_locations.pop(i)
        # print(self.all_data.columns)
        # print(self.grid_locations)
    
    def __len__(self) -> int:
        return len(self.image_filenames)

    def __getitem__(self, index) -> dict[str, torch.Tensor]:
        image = Image.open(self.image_filenames[index]).convert("L")
        size = image.size
        image = image.resize(self.input_shape)
        image = np.array(image)
        image = image.reshape((1,*image.shape))
        location = self.grid_locations[index]
        for i in range(len(location)):
            if i%2:
                location[i] /= size[1]
            else:
                location[i] /= size[0]
        return {
            "image": torch.tensor(image, dtype=torch.float32)/255.,
            "grid": torch.tensor(location, dtype=torch.float32)
        }

class Model(torch.nn.Module):
    def __init__(self, input_shape:tuple[int,int], number_of_layers:int, dims:int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.input_shape = input_shape
        self.conv_layers:list = []
        self.conv_layers.append(torch.nn.Conv2d(1, dims, (3,3), padding='same'))
        for _ in range(number_of_layers-1):
            self.conv_layers.append(torch.nn.Conv2d(dims, dims, (3,3), padding='same'))
            self.conv_layers.append(torch.nn.LeakyReLU(negative_slope=0.01))
            self.conv_layers.append(torch.nn.MaxPool2d((2,2)))
            self.conv_layers.append(torch.nn.BatchNorm2d(dims))
        self.flatten = torch.nn.Flatten()
        self.location = [
            torch.nn.Linear(4107, 8),
            torch.nn.Sigmoid()
        ]
        self.conv_layers = torch.nn.ModuleList(self.conv_layers)
        self.location = torch.nn.ModuleList(self.location)
    
    def forward(self, x:torch.Tensor) -> torch.Tensor:
        for layer in self.conv_layers:
            x = layer(x)
        x = self.flatten(x)
        location = x
        for layer in self.location:
            location = layer(location)
        return location
    
def create_model(input_shape:tuple[int,int], number_of_layers:int, dims:int):
    model = Model(input_shape, number_of_layers, dims)
    for p in model.parameters():
        if p.dim() > 1:
            torch.nn.init.xavier_uniform_(p)
    return model

def get_dataset(filename:str, input_shape:tuple[int,int], batch_size:int) -> DataLoader:
    train_dataset = SudokuDataset(filename, input_shape)
    train_dataloader = DataLoader(train_dataset, batch_size, shuffle=True)
    return train_dataloader

def train(epochs:int, config:dict, model:None|Model = None) -> Model:
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    if not model:
        print("========== Using new model =========")
        model = create_model(config['input_shape'], config['number_of_layers'], config['dims']).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=config['lr'])
    loss = torch.nn.MSELoss().to(device)
    dataset = get_dataset(config['filename'], config['input_shape'], config['batch_size'])
    prev_error = 0
    try:
        for epoch in range(1, epochs+1):
            batch_iterator = tqdm(dataset, f"Epoch {epoch}/{epochs}:")
            for batch in batch_iterator:
                x = batch['image'].to(device)
                y_true = batch['grid'].to(device)
                # print(batch['grid'])
                # return
                y_pred = model(x)
                error = loss(y_true, y_pred)
                batch_iterator.set_postfix({"loss":f"Loss: {error.item():6.6f}"})
                error.backward()
                optimizer.step()
                # optimizer.zero_grad()
            if abs(error-0.5) < 0.05:# or (prev_error-error)<0.000001:
                del(model)
                model = create_model(config['input_shape'], config['number_of_layers'], config['dims']).to(device)
                print("New model created")
            prev_error = error
    except KeyboardInterrupt:
        torch.save(model, "model.pt")
    return model

def test(config:dict, model_filename:str):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = torch.load("model.pt").to(device)
    loss = torch.nn.MSELoss().to(device)
    dataset = get_dataset(config['filename'], config['input_shape'], config['batch_size'])
    

if __name__ == '__main__':
    config = {
        "input_shape": (300,300),
        "filename": "archive/outlines_sorted.csv",
        "number_of_layers": 4,
        "dims": 3,
        "batch_size": 8,
        "lr": 1e-5
    }
    # model = train(50, config)
    model = torch.load("model.pt")
    test(config, model)
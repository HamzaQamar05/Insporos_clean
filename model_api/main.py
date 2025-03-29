
from fastapi import FastAPI
from pydantic import BaseModel
import torch
import torch.nn as nn

app = FastAPI()

# Define the model structure (same as training)
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        return self.fc(x)

# Load the model
model = SimpleModel()
model.load_state_dict(torch.load("simple_model.pth"))
model.eval()

class InputData(BaseModel):
    data: list  

@app.post("/predict")
def predict(input: InputData):
    input_tensor = torch.tensor(input.data, dtype=torch.float32).unsqueeze(0)  # [1, 10]
    with torch.no_grad():
        output = model(input_tensor)
    return {"prediction": output.item()}


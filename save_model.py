
import torch
import torch.nn as nn


class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 1)  # Simple linear layer

    def forward(self, x):
        return self.fc(x)

model = SimpleModel()
torch.save(model.state_dict(), "simple_model.pth")
print("Model saved as simple_model.pth")

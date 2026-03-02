import torch
import torch.nn as nn

class NoiseRegressor(nn.Module):
    def _init_(self):
        super(NoiseRegressor, self)._init_()
        self.network = nn.Sequential(
            nn.Linear(8, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1)
        )

    def forward(self, x):
        return self.network(x)

import torch
import torch.nn as nn


class {{ cookiecutter.model_name }}(nn.Module):
    def __init__(self, n_classes):
        super().__init__()

        self.n_classes = n_classes
        self.model = nn.Sequential(
            ...
        )

    def forward(self, input):
        x = self.model(input)

        return x

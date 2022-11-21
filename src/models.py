from typing import List

import torch
import torch.nn as nn
import torch.functional as F


class FCNN(nn.Module):
    def __init__(
        self, input_dim: int, output_dim: int, dim_list: List[int], p: float
    ) -> None:
        super().__init__()
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.dim_list = [input_dim] + dim_list + [output_dim]
        self.p = p

        layers = []
        for i in range(len(self.dim_list) - 2):
            layers.append(nn.Linear(self.dim_list[i], self.dim_list[i + 1]))
            layers.append(nn.ReLU())
            layers.append(nn.BatchNorm1d(self.dim_list[i + 1]))
            layers.append(nn.Dropout1d(self.p))
        self.net = nn.Sequential(*layers)

    def forward(self, input):
        return self.net(input)

    @staticmethod
    def weights_init(layer):
        classname = layer.__class__.__name__
        if classname.find("Linear") != -1:
            nn.init.xavier_uniform_(layer.weight)


class SeqModel(nn.Module):
    def __init__(
        self, input_dim: int, output_dim: int, dim_list: List[int], p: float
    ) -> None:
        super().__init__()

        self.adpooling = nn.AdaptiveMaxPool1d(1)
        self.fcnn = FCNN(input_dim, output_dim, dim_list, p)

    def forward(self, input):
        out = input.T
        out = self.adpooling(out)
        out = out.ravel()
        out = self.fcnn(out)
        return out

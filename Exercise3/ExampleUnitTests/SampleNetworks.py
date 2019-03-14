import torch
import torch.nn as nn
import torch.nn.functional as F

class ValueNetwork(nn.Module):
    def __init__(self,inputDims, layerDims, outputDims):

        super(ValueNetwork, self).__init__()

        self.processingLayers = []
        self.layerDims = layerDims
        self.layerDims.insert(0,inputDims)
        self.layerDims.append(outputDims)

        for idx in range(len(self.layerDims)-1):
            self.processingLayers.append(nn.Linear(self.layerDims[idx], self.layerDims[idx+1]))

        list_param = []
        for a in self.processingLayers:
            list_param.extend(list(a.parameters()))

        self.LayerParams = nn.ParameterList(list_param)

    def forward(self, inputs):

        out = inputs
        for layers in self.processingLayers[:-1]:
            out = layers(out)
            out = F.relu(out)

        out = self.processingLayers[-1](out)

        return out

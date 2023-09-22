#Linear State Space Model

import numpy as np
import torch
import random

class LinearStateSpaceModel:
    def __init__(self, A, B, C, D, initial_state):
        self.A = A #State transition matrix
        self.B = B #Input matrix
        self.C = C #Output matrix
        self.D = D #Feedthrough matrix
        self.state = initial_state #Initial state

    def update(self, input_signal):
        input_signal = input_signal.float()
        self.state = torch.matmul(self.A, self.state) + torch.matmul(self.B, input_signal)

    def get_output(self):
        output = torch.matmul(self.C.float(), self.state.float())
        return output
    
A = torch.tensor([[round(random.uniform(0, 1), 1), round(random.uniform(0, 1), 1)],
                [round(random.uniform(0, 1), 1), round(random.uniform(0, 1), 1)]], dtype=torch.float) #Random state transitions

B = torch.tensor([[round(random.uniform(0, 1), 1)],
                [round(random.uniform(0, 1), 1)]], dtype=torch.float) #Random inputs

C = torch.tensor([[1.0, 0.0]], dtype=torch.float) #Output is the first state variable

D = torch.tensor([[0.0]], dtype=torch.float) #No direct feedthrough

initial_state = torch.tensor([[0.0],
                              [0.0]], dtype=torch.float)

print(A, B, C, D, initial_state)

model = LinearStateSpaceModel(A, B, C, D, initial_state)

T = 10 #No. of discrete time steps
for t in range(T):
    input_signal = torch.tensor([[t + 1]])
    model.update(input_signal)
    output = model.get_output()
    print(f"t{t+1}, Output: {output.item()}")
     
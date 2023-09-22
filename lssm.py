#Linear State Space Model

import numpy as np
import torch
import random

class LinearStateSpaceModel:
    def __init__(self, A, B, C, D, initial_state, tau):
        self.A = A #State transition matrix
        self.B = B #Input matrix
        self.C = C #Output matrix
        self.D = D #Feedthrough matrix
        self.state = initial_state #Initial state
        self.tau = tau #Fixed time constant

    def update(self, input_signal):
        input_signal = input_signal.float()
        self.state = torch.matmul(torch.exp(-1/self.tau * self.A), self.state) + torch.matmul(1 - torch.exp(-1/self.tau * self.B), input_signal)

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

tau = random.uniform(1,3) #Random fixed time constant between (1, 3) (no specific reason for the range)

print("A =", A,"\nB =", B,"\nC = ", C,"\nD = ", D,"\nIni. state = ", initial_state,"\nτ = ", tau)

model = LinearStateSpaceModel(A, B, C, D, initial_state, tau)

T = 10 #No. of discrete time steps
for t in range(T):
    input_signal = torch.tensor([[t + 1]])
    model.update(input_signal)
    output = model.get_output()
    print(f"t{t+1}, Output: {output.item()}")
     

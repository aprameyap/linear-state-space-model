import numpy as np
import torch
import random

class KalmanFilter:
    def __init__(self, A, B, C, D, initial_state, tau, Q, R):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.state = initial_state
        self.tau = tau
        self.Q = Q
        self.R = R
        self.P = torch.eye(A.shape[0])

    def update(self, input_signal):
        predicted_state = torch.matmul(torch.exp(-1/self.tau * self.A), self.state) + torch.matmul(1 - torch.exp(-1/self.tau * self.B), input_signal)
        predicted_P = torch.matmul(torch.matmul(torch.exp(-2/self.tau * self.A), self.P), torch.exp(-2/self.tau * self.A).t()) + self.Q

        innovation = input_signal - torch.matmul(self.C, predicted_state)
        innovation_covariance = torch.matmul(torch.matmul(self.C, predicted_P), self.C.t()) + self.R
        Kalman_gain = torch.matmul(torch.matmul(predicted_P, self.C.t()), torch.inverse(innovation_covariance))
        self.state = predicted_state + torch.matmul(Kalman_gain, innovation)
        self.P = predicted_P - torch.matmul(torch.matmul(Kalman_gain, self.C), predicted_P)

    def get_output(self):
        output = torch.matmul(self.C, self.state)
        return output

A = torch.tensor([[round(random.uniform(0, 1), 1), round(random.uniform(0, 1), 1)],
                [round(random.uniform(0, 1), 1), round(random.uniform(0, 1), 1)]], dtype=torch.float) #Random state transitions

B = torch.tensor([[round(random.uniform(0, 1), 1)],
                [round(random.uniform(0, 1), 1)]], dtype=torch.float) #Random inputs

C = torch.tensor([[1.0, 0.0]], dtype=torch.float) #Output is the first state variable

D = torch.tensor([[0.0]], dtype=torch.float) #No direct feedthrough

initial_state = torch.tensor([[0.0], [0.0]], dtype=torch.float) #Initial at (0,0)

tau = 1.0

Q = torch.eye(A.shape[0]) * 0.01
R = torch.eye(C.shape[0]) * 0.1

model = KalmanFilter(A, B, C, D, initial_state, tau, Q, R)

T = 10
for t in range(T):
    input_signal = torch.tensor([[t + 1]], dtype=torch.float)
    model.update(input_signal)
    output = model.get_output()
    print(f"t{t+1}, Output: {output.item()}")

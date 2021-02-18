#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pennylane as qml
from pennylane import numpy as np
import sys

def simple_circuits_30(angle):
    x_expectation = 0.0
    num_wires = 1
    dev =  qml.device("default.qubit", wires= num_wires)
    @qml.qnode(dev)

    def circuit(angle):
        qml.RY(angle, wires = 0)
        return qml.expval(qml.PauliX(0))

    #result =  circuit()
    x_expectation = circuit(angle)

    return x_expectation



if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block

    # Load and process input
    angle_str = sys.stdin.read()
    angle = float(angle_str)

    ans = simple_circuits_30(angle)

    if isinstance(ans, np.tensor):
        ans = ans.item()

    if not isinstance(ans, float):
        raise TypeError("the simple_circuits_30 function needs to return a float")

    print(ans)


# In[ ]:





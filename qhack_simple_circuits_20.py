import pennylane as qml
from pennylane import numpy as np
import sys

def simple_circuits_20(angle):
    prob =0.0
    num_wires =1
    dev = qml.device("defalut.qubit", wires=num_wires)
    @qml.qnode(dev)
    def circuit (angle):
        qml.RX(angle, wires=0)
        return qml.probs(wires=0)
    result =circuit(angle)
    prob=result[0]
    return prob

if _name_ == "_main_":
    angle_str = sys.stdin.read()
    angle = float (angle_str)
    ans = simple_circuits_20(angle)
    if isinstance (ans,np.tensor):
        ans  =ans.item()
    if not isintance (ans, float):
        raise TypeError("the simple_circuits_20 function needs to return a float")
    print(ans)
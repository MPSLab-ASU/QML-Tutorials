import pennylane as qml
import matplotlib.pyplot as plt
import numpy as np

dev = qml.device("default.qubit",wires=1)

def output_and_draw(gates):
    print(f"Output of the circuit {circuit(gates)}")
    qml.draw_mpl(circuit)(gates)
    plt.show()

def draw_and_get_state(gates):
    qml.draw_mpl(probelm_circuit)(gates)
    state = probelm_circuit(gates)
    print(f"State created: \n {state}")
    plt.show()

@qml.qnode(dev)
def circuit(gates:list):
    for g in gates:
        g(0)
    return qml.probs(0)

@qml.qnode(dev)
def probelm_circuit(gates:list):
    for g in gates:
        g(0)
    return qml.state()


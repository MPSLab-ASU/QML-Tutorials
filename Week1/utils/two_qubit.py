import pennylane as qml
import matplotlib.pyplot as plt
import numpy as np

dev = qml.device("default.qubit",wires=2)


def draw_and_get_state(gates):
    """2 qubit function to draw and get states.
        gates [list] : instantiated gates with the wires defined eg. qml.CNOT([0,1])
    """
    qml.draw_mpl(probelm_circuit,decimals=2)(gates)
    state = probelm_circuit(gates)
    print(f"State created: \n {state}")
    plt.show()

@qml.qnode(dev,grad_on_execution=False,diff_method=None)
def probelm_circuit(gates:list):
    for g in gates:
        qml.apply(g)
    return qml.state()

def decompose_and_plot(gate):
    """2 qubit function to decompose gates into Pauli + CNOT and draw the result
        gates : instantiated gates with the wires defined eg. qml.CNOT([0,1])
    """
    gate=gate([0,1])
    gates= qml.ops.two_qubit_decomposition(gate.matrix(),wires=[0,1])
    qml.draw_mpl(probelm_circuit,decimals=2)(gates)
    state = probelm_circuit(gates)
    states_formatted = ['{:.2f}'.format(i) for i in state]
    plt.show()
    print(f"Output State:\n {states_formatted}")
    print(f"Decomposition:\n {gates}")



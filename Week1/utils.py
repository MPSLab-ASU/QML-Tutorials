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

@qml.qnode(dev,grad_on_execution=False,diff_method=None)
def circuit(gates:list):
    for g in gates:
        g(0)
    return qml.probs(0)

@qml.qnode(dev,grad_on_execution=False,diff_method=None)
def probelm_circuit(gates:list):
    for g in gates:
        g(0)
    return qml.state()

# Lecture 2
@qml.qnode(dev,grad_on_execution=False,diff_method=None)
def circuit_ops(ops):
    for op in ops:
        qml.apply(op)
    return qml.state()

def apply_ops_and_draw(ops):
    print(f"State Created by Decomposition:\n {circuit_ops(ops)}")
    qml.draw_mpl(circuit_ops)(ops)
    plt.show()

def decompose_and_plot(gate):
    gate_wire=gate(0)
    draw_and_get_state([gate])
    print(f"Decomposition:\n {gate_wire.decomposition()}")
    apply_ops_and_draw(gate_wire.decomposition())
import pennylane as qml
import matplotlib.pyplot as plt
import numpy as np

dev = qml.device("default.qubit",wires=1)

def output_and_draw(gates):
    print(f"Output of the circuit {circuit(gates)}")
    qml.draw_mpl(circuit,decimals=2)(gates)
    plt.show()

def draw_and_get_state(gates):
    qml.draw_mpl(probelm_circuit,decimals=2)(gates)
    state = probelm_circuit(gates)
    states_formatted = ['{:.2f}'.format(i) for i in state]
    print(f"State created: \n {states_formatted}")
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
    states_formatted = ['{:.2f}'.format(i) for i in circuit_ops(ops)]
    print(f"State Created by Decomposition:\n {states_formatted}")
    qml.draw_mpl(circuit_ops,decimals=2)(ops)
    plt.show()

def decompose_and_plot(gate):
    gate_wire=gate(0)
    draw_and_get_state([gate])
    print(f"Decomposition:\n {gate_wire.decomposition()}")
    apply_ops_and_draw(gate_wire.decomposition())


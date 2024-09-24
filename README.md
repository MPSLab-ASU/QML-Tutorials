# Quantum Machine Learning Tutorials [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/vinayak19th/QML-Tutorials/master?labpath=Explicit%2520Model.ipynb)

This repository contains tutorials on Quantum Machine Learning. The tutorials are written in Jupyter Notebooks and are intended to be run on Google Colab. 

**Table of Contents**
- [Quantum Machine Learning Tutorials ](#quantum-machine-learning-tutorials-)
  - [Folder Structure:](#folder-structure)
  - [Colab Links:](#colab-links)
- [Training Performance:](#training-performance)
  - [Explicit Model:](#explicit-model)


## Folder Structure:
The folder structure for demos follows the following pattern:
* [`logs/`](logs/) : Contains the logs from [tensorboard](https://www.tensorflow.org/tensorboard).
*  [`Saved_vars/`](Saved_vars/) : Contains the saved data sets to train the models on
*  **Notebooks**:
   *  [`ExplicitModel.ipynb`](ExplicitModel.ipynb) : This notebook contains the implementation of the explicit model for the XOR gate.
   *  [`ImplicitModel.ipynb`](ImplicitModel.ipynb) : This notebook contains the implementation of the implicit model for the XOR gate.
   *  [`Data_Reuploading.ipynb`](Data_Reuploading.ipynb) : This notebook contains the implementation of the Quantum Neural Network for the XOR gate.
   *  [`DataGenerator.ipynb`](DataGenerator.ipynb) : This notebook creates a random quantum circuit from which we sample to create our dataset.
* [`Media/`](Media/) : Contains the images from training. 

## Colab Links:
The notebooks can be run on Google Colab by clicking on the following links:

| **Notebook**                                       | **Colab**                                                                                                                                                                                                                                         |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`ExplicitModel.ipynb`](ExplicitModel.ipynb)       | <a target="_blank" style="display: inline" href="https://colab.research.google.com/github/vinayak19th/QML-Tutorials/blob/master/ExplicitModel.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>    |
| [`ImplicitModel.ipynb`](ImplicitModel.ipynb)       | <a target="_blank" style="display: inline" href="https://colab.research.google.com/github/vinayak19th/QML-Tutorials/blob/master/ImplicitModel.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>    |
| [`Data_Reuploading.ipynb`](Data_Reuploading.ipynb) | <a target="_blank" style="display: inline" href="https://colab.research.google.com/github/vinayak19th/QML-Tutorials/blob/master/Data_Reuploading.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> |
| [`DataGenerator.ipynb`](DataGenerator.ipynb)       | <a target="_blank" style="display: inline" href="https://colab.research.google.com/github/vinayak19th/QML-Tutorials/blob/master/DataGenerator.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>    |

# Training Performance:

## Explicit Model:
![Explicit Model](Media/ExplicitModel_labelled.png)

<table>
<tr>
  <td> <img src="Media/Explicit_3L_3R.gif" alt="Explicit Model" style="width: 90%;"/> </td>
  <td>  
    Training Loss is good
  </tr>
</table>

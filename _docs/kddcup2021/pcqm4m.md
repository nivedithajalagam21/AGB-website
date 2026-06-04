---
title: OGB-LSC @ KDD Cup 2021
permalink: /kddcup2021/pcqm4m/
layout: kdd_pcqm4m
---
#### **Important: PCQM4M has been deprecated. Use [PCQM4Mv2](/docs/lsc/pcqm4mv2/) instead.**
#### **Learn about PCQM4M-LSC and Python package**
- **[Dataset](#dataset): Learn about the dataset and the prediction task.**
- **Python package tutorial**
    - **[Install `rdkit`](https://www.rdkit.org/docs/Install.html): You will need `rdkit>=2019.03.1` package to create molecular graphs.**
    - **[Dataset object](#dataset_object): Learn about how to prepare and use the dataset with our package.**
    - **[Performance evaluator](#evaluator): Learn about how to evaluate models and save test submissions with our package.**
    - **[Initial baseline code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/pcqm4m): Learn about our initial baseline experiments.**
    - **[DGL's baseline code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb_lsc/PCQM4M): [DGL](https://www.dgl.ai/)-based implementation.**
- **[Discussion forum](https://github.com/snap-stanford/ogb/discussions/categories/pcqm4m-lsc): Ask questions and make discussion about the dataset.**

<a name="dataset"/>

------
##### **Dataset: Predicting a quantum property of molecular graphs**

**Practical Relevance:**
Density Functional Theory (DFT) is a powerful and widely-used quantum physics calculation that can accurately predict various molecular properties such as the shape of molecules, reactivity, responses by electromagnetic fields. 
However, DFT is time-consuming and takes up to several hours per small molecule.
Using fast and accurate ML models to approximate DFT enables diverse downstream applications, such as property prediction for organic photovaltaic devices and structure-based virtual screening for drug discovery.

**Overview:**
PCQM4M-LSC is a quantum chemistry dataset originally curated under the PubChemQC project [1].
Based on the PubChemQC, we define a meaningful ML task of predicting DFT-calculated HOMO-LUMO energy gap of molecules given their 2D molecular graphs.
The HOMO-LUMO gap is one of the most practically-relevant quantum chemical properties of molecules since it is related to reactivity, photoexcitation, and charge transport.
Moreover, predicting the quantum chemical property only from 2D molecular graphs without their 3D equilibrium structures is also practically favorable. This is because obtaining 3D equilibrium structures requires DFT-based geometry optimization, which is expensive on its own.

**Graph:**
We provide molecules as the **[SMILES strings](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system)**, from which 2D molecule graphs (nodes are atoms and edges are chemical bonds) as well as molecular fingerprints (hand-engineered molecular feature developed by the chemistry community) can be obtained. 
The conversion requires **[`rdkit` Python package](https://www.rdkit.org/docs/Install.html)** to be installed.
By default, we follow OGB to convert the SMILES string into a molecular graph representation (see code **[here](https://github.com/snap-stanford/ogb/blob/master/ogb/utils/mol.py#L6)**), where each node is associated with a 9-dimensional feature (e.g., atomic number, chirality) and each edge comes with a 3-dimensional feature (e.g., bond type, bond stereochemistry), although the optimal set of input graph features remains to be explored.

**Prediction task and evaluation metric:**
The task is graph regression: predicting the HOMO-LUMO energy gap in electronvolt (eV) given 2D molecular graphs. Mean Absolute Error (MAE) is used as evaluation metric.

**Data split:**
We split molecules by their PubChem ID (CID) with ratio 80/10/10. 
Our original intention was to provide the scaffold split [2], but the provided data turns out to be split by the CID due to some pre-processing bug (pointed out [here](https://github.com/snap-stanford/ogb/discussions/162)).
The CID number itself does not indicate particular meaning about the molecule, but splitting by CID may provide a moderate distribution shift (most likely not as severe as the scaffold split). [Here](https://github.com/snap-stanford/ogb/discussions/162#discussioncomment-637529), we provide some analysis, comparing the CID and scaffold splits.
Overall, we found the model performances were consistent between the two splits.
<!-- Specifically, we split the molecules based on their 2D structural frameworks, resulting in validation and test molecules that are structurally very different from training ones.
Prediction over out-of-distribution molecular structure is commonplace in ML-based virtual screening. This is because training molecules represent an extremely tiny and biased subset of the entire chemical space (estimated to be around 10^60 molecules), to which fast ML models are applied for virtual screening. -->

###### **References**
[1] Nakata, M., & Shimazaki, T. (2017). PubChemQC project: a large-scale first-principles electronic structure database for data-driven chemistry. Journal of chemical information and modeling, 57(6), 1300-1308. <br/>
[2] Wu, Z., Ramsundar, B., Feinberg, E. N., Gomes, J., Geniesse, C., Pappu, A. S., Leswing, K. & Pande, V. (2018). MoleculeNet: a benchmark for molecular machine learning. Chemical science, 9(2), 513-530.

##### License: CC BY 4.0


---------------

<a name="dataset_object"/>
-------

##### **Python package: Dataset object**
The dataset object handles downloading, preprocessing, and access to the graph and its features. Below we go though basic usage.

###### **- Download and extract data**
The molecules are provided as SMILES strings (sequence representation of molecules), and we provide two options for our dataset object.
Both options download and process dataset under the specified `ROOT` directory (default to `dataset/`).

**(1) SMILES dataset**
The first option directly provides the raw SMILES string.
```python
from ogb.lsc import PCQM4MDataset
dataset = PCQM4MDataset(root = ROOT, only_smiles = True)

# get i-th molecule and its target value (nan for test data)
i = 1234
print(dataset[i]) # ('O=C1C=CC(O1)C(c1ccccc1C)O', 5.292614392225)
```

**(2) Molecular graph dataset**
<br/>
The second option provides a molecular graph object constructed from the SMILES string.
After preprocessing, the file size will be around 8GB.
<a name="evaluator"/>
```python
from ogb.lsc import PCQM4MDataset
from ogb.utils import smiles2graph

# smiles2graph takes a SMILES string as input and returns a graph object
# requires rdkit to be installed.
# You can write your own smiles2graph
graph_obj = smiles2graph('O=C1C=CC(O1)C(c1ccccc1C)O')

# convert each SMILES string into a molecular graph object by calling smiles2graph
# This takes a while (a few hours) for the first run
dataset = PCQM4MDataset(root = ROOT, smiles2graph = smiles2graph)

# get i-th molecule and its target value (nan for test data)
i = 1234
print(dataset[i]) # (graph_obj, 5.292614392225)
```
Here graph object (`graph_obj` above) is a Python dictionary containing the following keys: `edge_index`, `edge_feat`, `node_feat`, and `num_nodes`.
- `edge_index`: numpy ndarray of shape `(2, num_bonds)`, representing chemical bond connections. Each column represents a chemical bond edge. As chemical bond is undirected, our edges are represented by bi-directional edges (double-counting each chemical bond).
- `edge_feat`: numpy ndarray of shape `(num_bonds, bondfeat_dim)`, representing chemical bond features. `bondfeat_dim` is the dimensionality of bond features and `i`-th row represents the feature of `i`-th chemical bond edge (corresponding to `edge_index[:,i]`). 
- `node_feat`: numpy ndarray of shape `(num_atomss, atomfeat_dim)`, representing atom features. `atomfeat_dim` is the dimensionality of atom features and i-th row represents the feature of i-th atom. 
- `num_nodes`: number of atoms in the molecular graph.

We additionally provide the dataset objects that are fully compatible to **[Pytorch Geometric](https://pytorch-geometric.readthedocs.io/en/latest/)** and **[DGL](https://www.dgl.ai/)**.
```python
from ogb.utils import smiles2graph

# if you use Pytorch Geometric (requires torch_geometric to be installed)
from ogb.lsc import PygPCQM4MDataset
pyg_dataset = PygPCQM4MDataset(root = ROOT, smiles2graph = smiles2graph)

# if you use DGL (requires dgl to be installed)
from ogb.lsc import DglPCQM4MDataset
dgl_dataset = DglPCQM4MDataset(root = ROOT, smiles2graph = smiles2graph)
```


If you use our default `smiles2graph` (`from ogb.utils import smiles2graph`) to convert each SMILES string into a molecular graph, you can map input atom/bond features into fixed-dimensional dense embeddings as follows. This is convenient to connect the input features into your subsequent deep learning architecture.
```python
from ogb.graphproppred.mol_encoder import AtomEncoder, BondEncoder
atom_encoder = AtomEncoder(emb_dim = 100) # Pytorch Module class w/ learnable parameters
bond_encoder = BondEncoder(emb_dim = 100) # Pytorch Module class w/ learnable parameters

atom_emb = atom_encoder(node_feat) # node_feat is input atom feature in Pytorch Tensor
edge_emb = bond_encoder(edge_feat) # edge_feat is input edge feature in Pytorch Tensor
```

###### **- Get data splits**
```python
split_dict = dataset.get_idx_split()
train_idx = split_dict['train'] # numpy array storing indices of training molecules
valid_idx = split_dict['valid'] # numpy array storing indices of validation molecules
test_idx = split_dict['test'] # numpy array storing indices of testing molecules
```
If you use `PygPCQM4MDataset` or `DglPCQM4MDataset`, `{train,valid,test}_idx` will be `torch` tensors.

<a name="evaluator"/>

--------------

##### **Python package: Performance evaluator**
We provide an evaluator to evaluate and save model's prediction in a standardized way.
To evaluate train/validation performance, first prepare 
- `y_pred`: `np.array` or `torch.Tensor` of shape `(num_data,)`. `i`-th element stores the predicted value (type: `float`) of `i`-th data.
- `y_true`: `np.array` of `torch.Tensor` of shape `(num_data,)`. `i`-th element stores the ground-truth value (type: `float`) of `i`-th data.

```python
from ogb.lsc import PCQM4MEvaluator

evaluator = PCQM4MEvaluator()
input_dict = {'y_pred': y_pred, 'y_true', y_true}
result_dict = evaluator.eval(input_dict)
print(result_dict['mae']) # get MAE
```

To save your test submission, first prepare 
- `y_pred`: `np.array` or `torch.Tensor` of shape `(num_test_data,)`. `i`-th element stores the predicted value (type: `float`) of `i`-th test data (i.e., having index of `test_idx[i]`).
- `dir_path`: directory path (type: `str`) to save the test file (our package will create the directory if it does not exist). Test file `y_pred_pcqm4m.npz` will be saved under the directory `dir_path`.

```python
input_dict = {'y_pred': y_pred}
evaluator.save_test_submission(input_dict = input_dict, dir_path = dir_path)
```
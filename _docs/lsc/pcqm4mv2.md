---
title: PCQM4Mv2
permalink: /docs/lsc/pcqm4mv2/
---

#### **Learn about PCQM4Mv2 and Python package**
- **[Dataset](#dataset): Learn about the dataset and the prediction task.**
- **Python package tutorial**
    - **[Install `rdkit`](https://pypi.org/project/rdkit-pypi/): You will need `rdkit>=2019.03.1` package to create molecular graphs.**
    - **[Dataset object](#dataset_object): Learn about how to prepare and use the dataset with our package.**
    - **[Performance evaluator](#evaluator): Learn about how to evaluate models and save test submissions with our package.**
    - **[Initial baseline code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/pcqm4m-v2): Learn about our initial baseline experiments.**
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
PCQM4Mv2 is a quantum chemistry dataset originally curated under the PubChemQC project [1].
Based on the PubChemQC, we define a meaningful ML task of predicting DFT-calculated HOMO-LUMO energy gap of molecules given their 2D molecular graphs.
The HOMO-LUMO gap is one of the most practically-relevant quantum chemical properties of molecules since it is related to reactivity, photoexcitation, and charge transport.
Moreover, predicting the quantum chemical property only from 2D molecular graphs without their 3D equilibrium structures is also practically favorable. This is because obtaining 3D equilibrium structures requires DFT-based geometry optimization, which is expensive on its own.

**2D Graph:**
We provide molecules as the **[SMILES strings](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system)**, from which 2D molecule graphs (nodes are atoms and edges are chemical bonds) as well as molecular fingerprints (hand-engineered molecular feature developed by the chemistry community) can be obtained. 
The conversion requires **[`rdkit` Python package](https://www.rdkit.org/docs/Install.html)** to be installed.
By default, we follow OGB to convert the SMILES string into a molecular graph representation (see code **[here](https://github.com/snap-stanford/ogb/blob/master/ogb/utils/mol.py#L6)**), where each node is associated with a 9-dimensional feature (e.g., atomic number, chirality) and each edge comes with a 3-dimensional feature (e.g., bond type, bond stereochemistry), although the optimal set of input graph features remains to be explored.

**3D Graph:**
We further provide the equilibrium 3D graph structure for training molecules in the form of the **[SDF format](https://en.wikipedia.org/wiki/Chemical_table_file#SDF)**. The compressed SDF can be downloaded **[here](http://ogb-data.stanford.edu/data/lsc/pcqm4m-v2-train.sdf.tar.gz)** (1.5GB). The single SDF contains 3D information of all the 3,378,606 training molecules. First download and decompress the file as follows.
```bash
wget http://ogb-data.stanford.edu/data/lsc/pcqm4m-v2-train.sdf.tar.gz
md5sum pcqm4m-v2-train.sdf.tar.gz # fd72bce606e7ddf36c2a832badeec6ab
tar -xf pcqm4m-v2-train.sdf.tar.gz # extracted pcqm4m-v2-train.sdf
```
Then, use `rdkit` to extract molecule information as follows.
```python
from rdkit import Chem

suppl = Chem.SDMolSupplier('pcqm4m-v2-train.sdf')
for idx, mol in enumerate(suppl):
    print(f'{idx}-th rdkit mol obj: {mol}')
```
The community should feel free to exploit 3D structural information to improve their model performance. Note that 3D information is *not* provided for validation and test molecules, and test-time inference needs to be performed without explicit 3D information.
**Known issue**: A very small number of training molecules (around 46 out of 3,378,606) have 2D graph structures that are inconsistent with the ones calculated from SMILES. These molecules often involve Si atom(s). For the rest of the training molecules, the 2D graphs constructed from SDF and SMILES are identical (even though the atom-to-atom correspondence is not available).

**Prediction task and evaluation metric:**
The task is graph regression: predicting the HOMO-LUMO energy gap in electronvolt (eV) given 2D molecular graphs. Mean Absolute Error (MAE) is used as evaluation metric.

**Data split:**
We split molecules by their PubChem ID (CID) with ratio 90/2/4/4 for train/validation/test-dev/test-challenge. 
Our original intention was to provide the scaffold split [2], but the provided data turns out to be split by the CID due to some pre-processing bug (pointed out [here](https://github.com/snap-stanford/ogb/discussions/162)).
The CID number itself does not indicate particular meaning about the molecule, but splitting by CID may provide a moderate distribution shift (most likely not as severe as the scaffold split). [Here](https://github.com/snap-stanford/ogb/discussions/162#discussioncomment-637529), we provide some analysis, comparing the CID and scaffold splits.
Overall, we found the model performances were consistent between the two splits.

**Updates from PCQM4M:**
Below we summarize the updates we have made to the original PCQM4M.
- **3D molecular structures provided.** We additionally provide 3D structures for training molecules. These structures are calculated by DFT and are obtained together with the HOMO-LUMO gap.
- **SMILES strings are partly updated.** In the process of preparing the 3D structures, we found a subtle mismatch between SMILES strings (i.e., 2D molecular graphs) and the HOMO-LUMO gap for about 10% of the entire molecules. 
Specifically, the SMILES strings can be changed in the course of DFT's geometry optimization, but in PCQM4M, we provided the *initial* SMILES strings. In the updated PCQM4Mv2, we provide SMILES strings corresponding to the *final* optimized 3D structures. Note that the HOMO-LUMO gap was calculated by DFT based on the final 3D structures; hence, it makes more sense to correspond the HOMO-LUMO gap with the SMILES string associated with the final 3D structures. 
- **Number of molecules decreased slightly.** As a result of the SMILES update, some molecules can no longer be parsed by the commonly-used chemistry toolkit, i.e., rdkit. As a result, the total number of molecules has been slightly reduced to 3,746,619. 
- **Split ratio changed.** For PCQM4Mv2, we set the split ratio for train/validation/test-dev/test-challenge to 90/2/4/4. The split is still done by PubChem compound ID so that there is no test label leakage, i.e., all the test molecules in PCQM4Mv2 is in the test split of PCQM4M.

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
from ogb.lsc import PCQM4Mv2Dataset
dataset = PCQM4Mv2Dataset(root = ROOT, only_smiles = True)

# get i-th molecule and its target value (nan for test data)
i = 1234
print(dataset[i]) # ('CC(NCC[C@H]([C@@H]1CCC(=CC1)C)C)C', 6.811009678015001)
```

**(2) Molecular graph dataset**
<br/>
The second option provides a molecular graph object constructed from the SMILES string.
After preprocessing, the file size will be around 8GB.
<a name="evaluator"/>
```python
from ogb.lsc import PCQM4Mv2Dataset
from ogb.utils import smiles2graph

# smiles2graph takes a SMILES string as input and returns a graph object
# requires rdkit to be installed.
# You can write your own smiles2graph
graph_obj = smiles2graph('CC(NCC[C@H]([C@@H]1CCC(=CC1)C)C)C')

# convert each SMILES string into a molecular graph object by calling smiles2graph
# This takes a while (a few hours) for the first run
dataset = PCQM4Mv2Dataset(root = ROOT, smiles2graph = smiles2graph)

# get i-th molecule and its target value (nan for test data)
i = 1234
print(dataset[i]) # (graph_obj, 6.811009678015001)
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
from ogb.lsc import PygPCQM4Mv2Dataset
pyg_dataset = PygPCQM4Mv2Dataset(root = ROOT, smiles2graph = smiles2graph)

# if you use DGL (requires dgl to be installed)
from ogb.lsc import DglPCQM4Mv2Dataset
dgl_dataset = DglPCQM4Mv2Dataset(root = ROOT, smiles2graph = smiles2graph)
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
testdev_idx = split_dict['test-dev'] # numpy array storing indices of test-dev molecules
testchallenge_idx = split_dict['test-challenge'] # numpy array storing indices of test-challenge molecules
```
If you use `PygPCQM4MDataset` or `DglPCQM4MDataset`, `{train,valid,testdev,testchallenge}_idx` will be `torch` tensors.

<a name="evaluator"/>

--------------

##### **Python package: Performance evaluator**
We provide an evaluator to evaluate and save model's prediction in a standardized way.
To evaluate train/validation performance, first prepare 
- `y_pred`: `np.array` or `torch.Tensor` of shape `(num_data,)`. `i`-th element stores the predicted value (type: `float`) of `i`-th data.
- `y_true`: `np.array` of `torch.Tensor` of shape `(num_data,)`. `i`-th element stores the ground-truth value (type: `float`) of `i`-th data.

```python
from ogb.lsc import PCQM4Mv2Evaluator

evaluator = PCQM4Mv2Evaluator()
input_dict = {'y_pred': y_pred, 'y_true', y_true}
result_dict = evaluator.eval(input_dict)
print(result_dict['mae']) # get MAE
```

To save your test-dev submission, first prepare 
- `y_pred`: `np.array` or `torch.Tensor` of shape `(num_test_data,)`. `i`-th element stores the predicted value (type: `float`) of `i`-th test data (i.e., having index of `testdev_idx[i]`).
- `dir_path`: directory path (type: `str`) to save the test file (our package will create the directory if it does not exist). Test file `y_pred_pcqm4m-v2_test-dev.npz` will be saved under the directory `dir_path`.
- `mode`: either `test-dev` or `test-challenge` (type: `str`).

```python
input_dict = {'y_pred': y_pred}
evaluator.save_test_submission(input_dict = input_dict, dir_path = dir_path, mode = 'test-dev')
```

You can similarly prepare the test-challenge submission by preparing the corresponding `y_pred` and set `mode` to be `test-challenge`.

---------

#### **Explore [PCQM4Mv2 leaderboard](/docs/lsc/leaderboards/#pcqm4mv2)!**
---
title: Get Started
permalink: /docs/home/
redirect_from: /docs/index.html
---

-----

### Overview

OGB contains graph datasets that are managed by data loaders. The loaders handle downloading and pre-processing of the datasets.
Additionally, OGB has standardized evaluators and leaderboards to keep track of state-of-the-art results.

<p align = "center">
<img width="90%" src="{{ "/assets/img/ogb_overview.png" | relative_url }}" class="img-responsive">
</p>

The OGB components are closely tied to OGB Python package, as detailed below.

-------

### Package Installation

You can install OGB using Python package manager pip.

```bash
pip install ogb
```

Please check the version is `1.3.6`.
```bash
python -c "import ogb; print(ogb.__version__)"
# Otherwise, please update the version by running
pip install -U ogb
```

#### Requirements
 - Python>=3.6
 - PyTorch>=1.6
 - DGL>=0.5.0 or torch-geometric>=1.6.0
 - Numpy>=1.16.0
 - pandas>=0.24.0
 - urllib3>=1.24.0
 - scikit-learn>=0.20.0
 - outdated>=0.2.0

------

### Package Usage

Next, we outline two key features of the OGB package, easy-to-use data loaders, and standardized model evaluators. <br/>
Please also refer to our [example code](https://github.com/snap-stanford/ogb/tree/master/examples) for how the package can be used in practice.

<a name="dataloader"/>

#### Data Loaders

We prepare easy-to-use [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/en/latest/) and [DGL](https://www.dgl.ai/) data loaders that handle dataset downloading and standardized dataset splits.

Following is an example in PyTorch Geometric showing that a few lines of code are sufficient to prepare and split the dataset. You can enjoy the same convenience for DGL. We also prepare library-agnostic dataset loaders that can be used with any other deep learning libraries such as [Tensorflow](https://www.tensorflow.org/) and [MxNet](https://mxnet.apache.org/).


```python
from ogb.graphproppred import PygGraphPropPredDataset
from torch_geometric.data import DataLoader

# Download and process data at './dataset/ogbg_molhiv/'
dataset = PygGraphPropPredDataset(name = "ogbg-molhiv", root = 'dataset/')

 
split_idx = dataset.get_idx_split() 
train_loader = DataLoader(dataset[split_idx["train"]], batch_size=32, shuffle=True)
valid_loader = DataLoader(dataset[split_idx["valid"]], batch_size=32, shuffle=False)
test_loader = DataLoader(dataset[split_idx["test"]], batch_size=32, shuffle=False)
```

**Mapping:** The nodes/edges/graphs in OGB are mapped to real entities in the world, e.g., each drug node in the [drug-drug interaction network](../linkprop/#ogbl-ddi) is mapped to a unique drug ID in [DrugBank](https://www.drugbank.ca/). The mapping information is provided in `mapping/` directory of the downloaded dataset folder, and is meant to allow researchers to draw scientific insight from model's prediction and to potentially augment the given graphs with richer information.

<a name="evaluator"/>

#### Evaluators

We prepare standardized evaluators for testing and comparing different methods. The evaluator takes `input_dict` (a dictionary whose format is specified in `evaluator.expected_input_format`) as input and returns a dictionary storing performance metric, which is appropriate for a particular dataset.

```python
from ogb.graphproppred import Evaluator

evaluator = Evaluator(name = "ogbg-molhiv")
# You can learn the input and output format specification of the evaluator as follows.
# print(evaluator.expected_input_format) 
# print(evaluator.expected_output_format) 
input_dict = {"y_true": y_true, "y_pred": y_pred}
result_dict = evaluator.eval(input_dict) # E.g., {"rocauc": 0.7321}
```

------

### Citing OGB

If you use OGB datasets in your work, please cite [our paper](https://arxiv.org/abs/2005.00687) (Bibtex below).

```
@article{hu2020ogb,
  title={Open Graph Benchmark: Datasets for Machine Learning on Graphs},
  author={Hu, Weihua and Fey, Matthias and Zitnik, Marinka and Dong, Yuxiao and Ren, Hongyu and Liu, Bowen and Catasta, Michele and Leskovec, Jure},
  journal={arXiv preprint arXiv:2005.00687},
  year={2020}
}
```



--------
### You are ready to explore OGB [datasets](../dataset_overview/)!

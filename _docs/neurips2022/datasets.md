---
title: OGB-LSC @ NeurIPS 2022
permalink: /neurips2022/datasets
layout: neurips2022_datasets
---

#### **Learn about the datasets**  
- **Please learn about the datasets and their usage.**  


---------------

#### **Installing Python Package**
First, please install our [`ogb` Python package](https://github.com/snap-stanford/ogb), as all of our datasets are downloaded and prepared using the package.
The model evaluation and test submission file preparation are also handled by our package.
Please install/update it by:
```bash
pip install -U ogb
```

-------

#### **Summary of Datasets**
OGB-LSC provides three large-scale datasets.
The dataset statistics as well as basic information are summarized below.
Each dataset is described in detail in the dataset page (jump to the links).

Task category | Name      | Package      |  #Graphs      | #Total nodes  | #Total edges  | Task Type   | Metric  | Download size | 
|:---------:|:--------|-----:|-----:|----------------:|----------------------:|:---------------|:-------|:---------|---------:|
Node-level | **[MAG240M](/docs/lsc/mag240m/)** | >=1.3.2 | 1 | 244,160,499  | 1,728,364,232 |  Multi-class classification | Accuracy | 167GB |
Link-level | **[WikiKG90Mv2](/docs/lsc/wikikg90mv2/)** |  >=1.3.3  | 1 | 91,230,610 | 601,062,811 |   KG completion | MRR | 89GB | 
Graph-level | **[PCQM4Mv2](/docs/lsc/pcqm4mv2/)** |  >=1.3.2  | 3,746,619  | 52,970,652 | 54,546,813   |  Regression | MAE | 59MB**&Dagger;**  | 

**&Dagger;**: The PCQM4Mv2 dataset is provided in the SMILES strings. After processing them into graph objects, the eventual file size will be around 8GB.

**Important: Make sure below prints the required package version for the dataset you are working on.**
```bash
python -c "import ogb; print(ogb.__version__)"
```

-----------

#### **Baselines**

In our **[paper](https://arxiv.org/pdf/2103.09430.pdf)**, we further perform an extensive baseline analysis on each dataset, implementing simple baseline models as well as advanced expressive models at scale.
We find that advanced expressive models, despite requiring more efforts to scale up, do benefit from large data and significantly outperform simple baseline models that are easy to scale.
All of our baseline code is made **[publicly available](https://github.com/snap-stanford/ogb/tree/master/examples/lsc)** to facilitate public research.
Please also check out [public leaderboards](/docs/lsc/leaderboards/) (evaluated on `test-dev` set) for state-of-the-art submissions.

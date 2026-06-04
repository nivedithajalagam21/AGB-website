---
title: MAG240M
permalink: /docs/lsc/mag240m/
---

#### **Learn about MAG240M and Python package**
- **[Dataset](#dataset): Learn about the dataset and the prediction task.**
- **Python package tutorial**
    - **[Dataset object](#dataset_object): Learn about how to prepare and use the dataset with our package.**
    - **[Performance evaluator](#evaluator): Learn about how to evaluate models and save test submissions with our package.**
    - **[Initial baseline code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m): Learn about our initial baseline experiments.**
    - **[DGL's baseline code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb_lsc/MAG240M): [DGL](https://www.dgl.ai/)-based implementation.**
- **Text data**
    - **[Download (33GB)](http://snap.stanford.edu/ogb/data/lsc/mapping/mag240m_mapping.zip)** md5sum: fc345d28b45808a2fa280ce6cbbfd198
- **[Discussion forum](https://github.com/snap-stanford/ogb/discussions/categories/mag240m-lsc): Ask questions and make discussion about the dataset.**


<a name="dataset"/>

------
##### **Dataset: Predicting papers' subject areas in a heterogeneous academic graph**

**Practical Relevance:**
The volume of scientific publication has been increasing exponentially, doubling every 12 years.
Currently, subject areas of arXiv papers are manually determined by the paper's authors and arXiv moderators.
An accurate automatic predictor of papers' subject categories not only reduces the significant burden of manual labeling, 
but can also be used to classify the vast number of non-arXiv papers, thereby allowing better search and organization of academic papers.

**Overview:**
MAG240M-LSC is a heterogeneous academic graph extracted from the Microsoft Academic Graph (MAG) [1].
Given arXiv papers situated in the heterogeneous graph, whose schema diagram is illustrated below, we aim to automatically annotating their topics, i.e., predicting the primary subject area of each arXiv paper.

<p align = "center">
<img width="50%" src="{{ "/assets/img/mag_schema.png" | relative_url }}" class="img-responsive">
</p>

**Graph:**
We extract 121M academic papers in English from MAG to construct a heterogeneous academic graph. The resultant paper set is written by 122M author entities, who are affiliated with 26K institutes. 
Among these papers, there are 1.3B citation links captured by MAG. 
Each paper is associated with its natural language title and most papers' abstracts are also available. 
We concatenate the title and abstract by period and pass it to a RoBERTa sentence encoder [2,3], generating a 768-dimensional vector for each paper node. 
Among the 121M paper nodes, approximately 1.4M nodes are arXiv papers annotated with 153 arXiv subject areas, e.g., cs.LG (Machine Learning).

**Prediction task and evaluation metric:**
The task is to predict the primary subject areas of the given arXiv papers, which is cast as an ordinary multi-class classification problem. The metric is the classification accuracy.

**Data split:**
We split the data according to time. Specifically, we train models on arXiv papers published until 2018, validate the performance on the 2019 papers, and finally test the performance on the 2020 papers. The split reflects the  practical scenario of helping the authors and moderators annotate the subject areas of the newly-published arXiv papers.

###### **References**
[1] Wang, K., Shen, Z., Huang, C., Wu, C. H., Dong, Y., & Kanakia, A. (2020). Microsoft Academic Graph: when experts are not enough. Quantitative Science Studies, 1(1), 396-413. <br/>
[2] Liu, Y., Ott, M., Goyal, N., Du, J., Joshi, M., Chen, D., Levy, O., Lewis, M., Zettlemoyer, L. & Stoyanov, V. (2019). RoBERTa: A Robustly Optimized BERT Pretraining Approach. arXiv preprint arXiv:1907.11692. <br/>
[3] Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence embeddings using siamese BERT-networks. arXiv preprint arXiv:1908.10084.

##### License: ODC-BY

---------------

<a name="dataset_object"/>
-------

##### **Python package: Dataset object**
The dataset object handles downloading and easy access to the graph and its features. Below we go through its basic usage.

###### **- Download and extract data**
Download and process dataset under the specified `ROOT` directory (default to `dataset/`).
This takes a while (several hours to a day) in the first run, so please be patient.
After decompression, the file size will be around 202GB.
```python
from ogb.lsc import MAG240MDataset
dataset = MAG240MDataset(root = ROOT)
```

###### **- Get basic dataset statistics**
```python
print(dataset.num_papers) # number of paper nodes
print(dataset.num_authors) # number of author nodes
print(dataset.num_institutions) # number of institution nodes
print(dataset.num_paper_features) # dimensionality of paper features
print(dataset.num_classes) # number of subject area classes
```

###### **- Get heterogeneous edges**
```python
'''
edge_index is numpy.ndarray of shape (2, num_edges).
- first row: indices of source nodes (indexed by source node types)
- second row: indices of target nodes (indexed by target node types)
In other words, i-th edge connects from edge_index[0,i] to edge_index[1,i].
'''
edge_index_writes = dataset.edge_index('author', 'writes', 'paper') 
edge_index_writes = dataset.edge_index('author', 'paper') # edge type can be omitted and inferred by our package.
edge_index_cites = dataset.edge_index('paper', 'paper')
edge_index_affiliated_with = dataset.edge_index('author', 'institution')
```

###### **- Get paper features**
Papers' features are extremely large (768-dimensional vectors for the 121M papers).
The features are saved as `numpy`'s **[`.npy` format](https://numpy.org/doc/stable/reference/generated/numpy.save.html)** in half precision (`np.float16`). The raw file is available at `ROOT/mag240m_kddcup2021/processed/paper/node_feat.npy` and has 175GB.

In our package, we use **[`numpy`'s read-only `memmap` mode](https://numpy.org/doc/stable/reference/generated/numpy.memmap.html)** so that the features can be loaded in a CPU-memory-efficient way.
In the [`memmap`]((https://numpy.org/doc/stable/reference/generated/numpy.memmap.html)) mode, each paper feature is not loaded into CPU memory from disk until it is explicitly accessed by your program.
Below are examples.

```python
# get i-th paper feature
i = 1234
print(dataset.paper_feat[i]) # only i-th data is loaded into memory

# get the feature matrix storing features of papers in idx_arr
idx_arr = np.array([1,10,100,1000,10000])
print(dataset.paper_feat[idx_arr]) # only the 5 data is loaded into memory
```

Here each data access is a disk access, which could be a bit slow. If you have sufficient CPU memory, you could also load the entire feature matrix into CPU memory at the beginning and enjoy fast RAM data access from there.
**Note: Do not run the following unless you have 200GB+ CPU memory!**

```python
# load the entire data (175GB) into CPU memory 
feat_in_memory = dataset.all_paper_feat # this takes a while

# Fast RAM access.
print(feat_in_memory[i])
print(feat_in_memory[idx_arr]) 
```


###### **- Get data splits**
```python
split_dict = dataset.get_idx_split()
train_idx = split_dict['train'] # numpy array storing indices of training paper nodes
valid_idx = split_dict['valid'] # numpy array storing indices of validation paper nodes
testdev_idx = split_dict['test-dev'] # numpy array storing indices of test-dev paper nodes
testchallenge_idx = split_dict['test-challenge'] # numpy array storing indices of test-challenge paper nodes

# alternatively, you can do the following.
train_idx = dataset.get_idx_split('train')
valid_idx = dataset.get_idx_split('valid')
testdev_idx = dataset.get_idx_split('test-dev')
testchallenge_idx = dataset.get_idx_split('test-challenge')
```

###### **- Get paper labels**
```python
print(dataset.paper_label) # numpy array of shape (num_papers, ), storing target labels of papers.
```
Note that **not all nodes are associated with labels**: Non-arXiv papers and test arXiv papers do *not* have labels.
Hence, for non-arXiv papers, we set their labels to `nan` (indicating that there is no label), while for test arXiv papers, we set their labels to `-1` (indicating that they are hidden).

###### **- Get paper years**
As an extra information, we provide a year in which each paper is published.
```python
print(dataset.paper_year[train_idx]]) # all elements < 2019
print(dataset.paper_year[val_idx]) # all elements are 2019
print(dataset.paper_year[testdev_idx]) # all elements are 2020
print(dataset.paper_year[testchallenge_idx]) # all elements are 2020
```


<a name="evaluator"/>

--------------

##### **Python package: Performance evaluator**
We provide an evaluator to evaluate and save model's prediction in a standardized way.
To evaluate train/validation performance, first prepare 
- `y_pred`: `np.array` or `torch.Tensor` of shape `(num_data,)`. `i`-th element stores the predicted label (type: `int`) of `i`-th data.
- `y_true`: `np.array` of `torch.Tensor` of shape `(num_data,)`. `i`-th element stores the ground-truth label (type: `int`) of `i`-th data.

```python
from ogb.lsc import MAG240MEvaluator

evaluator = MAG240MEvaluator()
input_dict = {'y_pred': y_pred, 'y_true', y_true}
result_dict = evaluator.eval(input_dict)
print(result_dict['acc']) # get accuracy
```

To save your test-dev submission, first prepare 
- `y_pred`: `np.array` or `torch.Tensor` of shape `(num_test_data,)`. `i`-th element stores the predicted label (type: `int`) of `i`-th test data (i.e., having index of `testdev_idx[i]`).
- `dir_path`: directory path (type: `str`) to save the test file (our package will create the directory if it does not exist). Test file `y_pred_mag240m_test-dev.npz` will be saved under the directory `dir_path`.
- `mode`: either `test-dev` or `test-challenge` (type: `str`).

```python
input_dict = {'y_pred': y_pred}
evaluator.save_test_submission(input_dict = input_dict, dir_path = dir_path, mode = 'test-dev')
```

You can similarly prepare the test-challenge submission by preparing the corresponding `y_pred` and set `mode` to be `test-challenge`.

---------

#### **Explore [MAG240M leaderboard](/docs/lsc/leaderboards/#mag240m)!**

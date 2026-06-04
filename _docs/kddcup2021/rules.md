---
title: OGB-LSC @ KDD Cup 2021
permalink: /kddcup2021/rules/
layout: kdd_rules
---

#### **Learn about the rules of the competition**  
- **Please read carefully about what are/aren't allowed in the competition.**  

-------


##### **Data Split**
We allow our participants to use training and validation sets in any ways. For example, there is no need to use the validation set only for model selection (you can directly train your model on the validation set if you find useful).
Also, the validation data can be defined by contestants themselves (you can use larger/smaller validation set if you find useful.
In OGB-LSC, we still provide the "standardized" validation sets since they have particular practical meaning (e.g., time splits in MAG240M-LSC and WikiKG90M-LSC) and can be used as a way for participants to understand how test submissions are evaluated.

For the test data, you should only use them for your model inference (make prediction and save it for your test submissions). In other words, your model should be developed only based on training and validation sets and should not touch the test data except for the final inference.
The only exception is the MAG240M-LSC, where you can use the test nodes in any ways, since the dataset is modeled as a transductive prediction task (i.e., test nodes are part of the entire graph).

------

##### **Use of External Data**
During the KDD Cup, we **do not** allow the use of any external datasets to train models. For each dataset, models need to be developed only using the provided data.

<a name="pcqm4m_time"/>

-----------

##### **Test Inference Time for [PCQM4M-LSC](/kddcup2021/pcqm4m/)**
**Note: The motivation behind the rules here can be better understood after you read the description of the [`PCQM4M-LSC`](/kddcup2021/pcqm4m/) dataset.**

For the [`PCQM4M-LSC`](/kddcup2021/pcqm4m/) dataset, the goal is to use ML to *accelerate* expensive DFT calculations (which takes up to a few hours per molecule!).
In order for the model to be practically useful, the inference time of the ML model must be fast enough.
**Therefore, for `PCQM4M-LSC` only, we limit the computational budget for the test-time inference.**
The specific rules are as follows:

- The total inference time over the 377,423 test molecules (i.e., time to predict target values of the test molecules **from their raw SMILES strings**) should not exceed **12 hours, using a single GPU and single CPU.****\*1**
 Note that multi-threading on a multi-core CPU is allowed.
 Once you win the contest, you will need to provide the inference code (example [here](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/pcqm4m/test_inference_gnn.py)) that takes the 377,423 test SMILES strings as input and saves 377,423 prediction values within 12 hours with single GPU and CPU.
- The 12-hour budget does *not* need to include the time to train your model(s). There is no budget limitation during training.
- You are allowed to use the following chemistry packages to process molecules from their SMILES strings: **[rdkit](https://www.rdkit.org/docs/GettingStartedInPython.html)**, **[Open Babel](https://open-babel.readthedocs.io/en/latest/UseTheLibrary/Python.html)**, and **[pyscf](http://pyscf.org/)**. **The 12-hour budget must include the pre-processing time of test molecules using these packages**, e.g., transforming test SMILES strings into graphs. This means that you cannot use the expensive (quantum) calculations to do feature engineering for your input test graphs, while you may include many more cheap features in your graphs.

For your reference, the test inference time for our baseline GNN takes about 3 minutes (you can run the code [here](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/pcqm4m/test_inference_gnn.py)) on a single GeForce RTX 2080 GPU and an Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz.
Hence, the above 12-hour budget is quite generous for an ordinary GNN model applied to our default molecular graphs. However, the 12-hour budget could be the limiting factor, if you want to apply expensive feature engineering to obtain your input test graphs.
Note that from the quantum chemistry point of view, making predictions over the 377,423 molecules in 12 hours (or 0.1 second per molecule) is about four-orders-of-magnitude faster than the original DFT calculations, making the ML-based approach practically fast and useful.

**\*1** Ideally, we would like our participants to use the GPU/CPU with the same specs as ours (GeForce RTX 2080 GPU, and an Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz.). 
However, as it is hard to enforce the hardware constraint, we also allow the use of other GPU/CPU specs (the 12-hour budget stays the same for simplicity). We will require you to report the hardware specs in the final test submission. 

 If you need any clarifications about the rules, please feel free to make posts at **[PCQM4M's discussion forum](https://github.com/snap-stanford/ogb/discussions/categories/pcqm4m-lsc).**

---------

<a name="code"/>
##### **Code Submission by Awardees**
For the awardees of the contest, we require public code submission through Github repo. The repo should follow the format of our baseline code (e.g., [MAG240M](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m), [WikiKG90M](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/wikikg90m), [PCQM4M](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/pcqm4m)) and contain
- All the code to reproduce your results (including data pre-processing and model training/inference) and save the test submission.
- `README.md` that contains all the instructions to run the code (from data pre-processing to model inference on test data).

The Github repo will be publicized on our webpage and need to remain public even after the KDD Cup.
Our goals are two-fold:
- To make it easier for the community to follow and build on top of the strong solutions.
- To incentivize the participants to follow the rules described above. Otherwise, the community would be able to find any misconduct by scrutinizing the code. The awardees will be disqualified if there is any misconduct found in the code.

---------

##### **Public Data Source**
All of our datasets are constructed from public database.
To avoid trivial test label leakage, we have anonymized the data as much as we can, removing any obvious clues (e.g., data identifier, raw text information) that can be used to map nodes or graphs into the entities in the public database. At the same time, to keep our datasets practically-relevant and realistic, our anonymization may not be perfect (e.g., we need to provide the real graph connectivity, node features, and SMILES strings). Although we believe it is nearly impossible to recover ground-truth test labels, we still significantly discourage the participants to try to de-anonymize the datasets during the competition.
Keep in mind that once you win the contest, you will need to share all the code to reproduce your solution through public Github repository. 
This means that any obvious misconduct (e.g., training or doing early stopping on test labels, directly using the test labels as predictions) will be revealed.

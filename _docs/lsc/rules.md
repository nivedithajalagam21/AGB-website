---
title: Rules for OGB-LSC Leaderboards
permalink: /docs/lsc/rules/
---

##### **Please read carefully about what are/aren't allowed in the OGB-LSC leaderboard submissions.**  

-------


##### **Data Split**
We allow you to use training and validation sets in any ways. For example, there is no need to use the validation set only for model selection, and you can directly train your model on the validation set if you find useful.
Nevertheless, it is often helpful for the community to know the validation performance reported on the standardized validation split.
Therefore, we still provide the official validation set and **require every leaderboard submission to report the validation performance on it.**

For the test data, you should only use them for your model inference (make prediction and save it for your test submissions). In other words, your model should be developed only based on training and validation sets and should not touch the test data except for the final inference.
The only exception is the MAG240M, where you can use the test nodes in any ways, since the dataset is modeled as a transductive prediction task (i.e., test nodes are part of the entire graph).

------


<a name="code"/>
##### **Code and Technical Report Submissions**
For every leaderboard submission, we require public code submission through Github repo. The repo should follow the format of our baseline code (e.g., [MAG240M](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m), [WikiKG90Mv2](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/wikikg90m-v2), [PCQM4Mv2](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/pcqm4m-v2)) and contain
- All the code to reproduce your results (including data pre-processing and model training/inference) and save the test submission.
- `README.md` that contains all the instructions to run the code (from data pre-processing to model inference on test data).

In addition, we require a short technical report that describes your approach. The link can be either Arxiv or PDF uploaded to your Github repository. You are free to update the report once the test-dev performance is announced.

As examples, please refer to the **[KDD Cup winners' code/reports](https://ogb.stanford.edu/kddcup2021/results/)**. For the Latex style file, we recommend using the **[arxiv-style](https://github.com/kourgeorge/arxiv-style)**.

------

##### **Use of External Data: Not allowed**
We **do not** allow the use of any external datasets to train models. 
<!-- For PCQM4Mv2 only, we allow the use of *unlabeled* molecules (primarily for unsupervised learning and self-training). However, any expensive calculation (i.e., taking more than 10 seconds per molecule) should not be performed on the unlabeled molecules in order to augment the dataset. -->

<a name="text"/>
--------

##### **Use of Text data: Not allowed**
Based on the request from the community, we have released text data for MAG240M (**[Download (33GB)](http://snap.stanford.edu/ogb/data/lsc/mapping/mag240m_mapping.zip)**) and WikiKG90Mv2 (**[Download (2.4GB)](http://snap.stanford.edu/ogb/data/lsc/mapping/wikikg90mv2_mapping.zip)**). The text data can be used in various purposes, such as analyzing model's predictions, improving model performance, and pre-training models.
**However, for the purpose of this leaderboard, we do not allow the models to use the text data**. This is because when LLMs are used, they may leak our test set information by being trained on our test data (which is publicly available). In the future, we plan to set up a new specialized leaderboard where the use of LLMs and text data is allowed. We welcome suggestions from the community.

Moreover, since text data is now released, it becomes easier to reveal hidden test labels by accessing the public database. We ask the community not to do it.
Keep in mind that you will need to share all the code to reproduce your solution through public Github repository. 
This means that any obvious misconduct (e.g., training or doing early stopping on test labels, directly using the test labels as predictions) will be revealed.

<a name="pcqm4m_time"/>

-----------

##### **Test Inference Time for [PCQM4Mv2](/docs/lsc/pcqm4mv2/)**
**Note: The motivation behind the rules here can be better understood after you read the description of the [`PCQM4Mv2`](/docs/lsc/pcqm4mv2/) dataset.**

For the [`PCQM4Mv2`](/docs/lsc/pcqm4mv2/) dataset, the goal is to use ML to *accelerate* expensive DFT calculations (which takes up to a few hours per molecule!).
In order for the model to be practically useful, the inference time of the ML model must be fast enough.
**Therefore, for `PCQM4Mv2` only, we limit the computational budget for the test-time inference.**
The specific rules are as follows:

- The total inference time over the ~147K test-dev/test-challenge molecules (i.e., time to predict target values of the test molecules **from their raw SMILES strings**) should not exceed **4 hours, using a single GPU/TPU/IPU and single CPU.****\*1**
 Note that multi-threading on a multi-core CPU is allowed.
 Once you win the contest, you will need to provide the inference code (example [here](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/pcqm4m-v2/test_inference_gnn.py)) that takes the ~147K test SMILES strings as input and saves ~147K prediction values within 4 hours with single GPU and CPU.
- You are allowed to use the following chemistry packages to process molecules from their SMILES strings: **[rdkit](https://www.rdkit.org/docs/GettingStartedInPython.html)**, **[Open Babel](https://open-babel.readthedocs.io/en/latest/UseTheLibrary/Python.html)**, and **[pyscf](http://pyscf.org/)**. **The 4-hour budget must include the pre-processing time of test molecules using these packages**, e.g., transforming test SMILES strings into graphs. This means that you cannot use the expensive (quantum) calculations to do feature engineering for your input test graphs, while you may include many more cheap features in your graphs.

For your reference, the test inference time for our baseline GNN takes about 1 minute (you can run the code [here](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/pcqm4m-v2/test_inference_gnn.py)) on a single GeForce RTX 2080 GPU and an Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz.
Hence, the above 4-hour budget is quite generous for an ordinary GNN model applied to our default molecular graphs. However, the 4-hour budget could be the limiting factor, if you want to apply expensive feature engineering to obtain your input test graphs.
Note that from the quantum chemistry point of view, making predictions over the ~147K molecules in 4 hours (or ~0.1 second per molecule) is about four-orders-of-magnitude faster than the original DFT calculations, making the ML-based approach practically fast and useful.

**\*1** Ideally, we would like our participants to use the GPU/CPU with the same specs as ours (GeForce RTX 2080 GPU, and an Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz.). 
However, as it is hard to enforce the hardware constraint, we also allow the use of other GPU/CPU specs (the 4-hour budget stays the same for simplicity). We will require you to report the hardware specs in the final test submission. 

 If you need any clarifications about the rules, please feel free to make posts at **[PCQM4Mv2's discussion forum](https://github.com/snap-stanford/ogb/discussions/categories/pcqm4m-lsc).**


---------

<!-- ##### **Public Data Source** -->
<!-- All of our datasets are constructed from public database.
To avoid trivial test label leakage, we have anonymized the data as much as we can, removing any obvious clues (e.g., data identifier, raw text information) that can be used to map nodes or graphs into the entities in the public database. At the same time, to keep our datasets practically-relevant and realistic, our anonymization may not be perfect (e.g., we need to provide the real graph connectivity, node features, and SMILES strings). Although we believe it is nearly impossible to recover ground-truth test labels, we still significantly discourage the participants to try to de-anonymize the datasets during the competition. -->


##### **Honor Code**
All the information provided in the **[leaderboard submission page](https://ogb-save.stanford.edu/leaderboard/)** must be correct and follows the above rules of OGB-LSC. The leaderboard submission cannot be deleted once it is public. Whenever you are contacted by the OGB-LSC Team, you need to provide information to verify the correctness of the information. Otherwise, the submission may be deleted, and future submissions may be prohibited.
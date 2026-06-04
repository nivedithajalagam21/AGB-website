---
title: WikiKG90Mv2
permalink: /docs/lsc/wikikg90mv2/
---
#### **Learn about WikiKG90Mv2 and Python package**

- **[Dataset](#dataset): Learn about the dataset and the prediction task.**
- **Python package tutorial**
    - **[Dataset object](#dataset_object): Learn about how to prepare and use the dataset with our package.**
    - **[Performance evaluator](#evaluator): Learn about how to evaluate models and save test submissions with our package.**
    - **[Initial baseline code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/wikikg90m-v2): Learn about our initial baseline experiments.**
- **Text data**
    - **[Download (2.4GB)](http://snap.stanford.edu/ogb/data/lsc/mapping/wikikg90mv2_mapping.zip)** md5sum: 2f0e3178a5e201bd1ab59a81f2dcba72
- **[Discussion forum](https://github.com/snap-stanford/ogb/discussions/categories/wikikg90m-lsc): Ask questions and make discussion about the dataset.**

<a name="dataset"/>

---------
##### **Dataset: Predicting missing facts in a knowledge graph**

**Practical Relevance:**
Large encyclopedic Knowledge Graphs (KGs), such as Wikidata [1] and Freebase [2], represent factual knowledge about the world through triples connecting different entities, e.g., (`Geoffrey Hinton`, `citizen of`, `Canada`). They provide rich structured information about many entities, aiding a variety of knowledge-intensive downstream applications such as information retrieval, question answering, and recommender systems.
However, these large KGs are known to be far from complete, missing many relational information between entities.
Using ML to automatically impute missing triples significantly reduces the manual curation of knowledge and provides a more comprehensive KG, which in turn improves the aforementioned downstream applications.

**Overview:**
WikiKG90Mv2 is a Knowledge Graph (KG) extracted from the *entire* Wikidata knowledge base. The task is to automatically impute missing triples that are not yet present in the current KG. Accurate imputation models can be readily deployed on the Wikidata to improve its coverage.

**Graph:**
Each triple (`head`, `relation`, `tail`) in WikiKG90Mv2 represents an Wikidata claim, where `head` and `tail` are the Wikidata items, and `relation` is the Wikidata predicate. We extracted triples from the public Wikidata dump downloaded at three time-stamps: May 17th, June 7th, and June 28th of 2021, for training, validation, and testing, respectively.
We retain all the entities and relations in the earliest May dump, resulting in 91,230,610 entities, 1,387 relations, and 601,062,811 triples in total.
In addition to extracting triples, we provide text features for entities and relations. Specifically, each entity/relation in Wikidata is associated with a title and a short description, e.g., one entity is associated with the title `Geoffrey Hinton` and the description `computer scientist and psychologist`.
We provide the MPNet embeddings [4,5] for all the entities and relations, which was the best-performing sentence embedding model [3] at the time of our dataset creation.

**Prediction task and evaluation metric:**
The task is the KG completion, i.e., given a set of training triples, predict a set of new test triples. 
For evaluation, for each test triple, (`head`, `relation`, `tail`), the model is asked to predict `tail` entity from (`head`, `relation`). Please assume that every validation/test triple is not present during training, so training triples should not be predicted even if they are correct.
More specifically, for each (`head`, `relation`), the model is asked to predict the top 10 tail entities that are most likely to be positive. The goal is to rank the ground-truth tail entity as high in the rank as possible within the top 10, which is measured by Mean Reciprocal Rank (MRR).

**Data split:**
We split the triples according to time, simulating a realistic KG completion scenario of imputing missing triples not present at a certain timestamp.
Specifically, we construct KGs using the aforementioned three timestamps,  where we only retain entities and relation types that appear in the earliest KG.
We use the triples in the earlies KG for training, and use the additional triples in the subsequent KGs for validation and test, respectively.

**Updates from WikiKG90M:** Below we summarize the updates we have made to the original WikiKG90M.
- **No candidate tails provided.** The most important update is that we do not provide any candidate tail entities for validation/test triples. Hence, a model needs to predict the target tail entity out of all the entities in Wikidata.
- **Created from more recent Wikidata.** The WikiKG90Mv2 is based on the public Wikidata dump downloaded at three time-stamps: May 17th, June 7th, and June 28th of 2021, for training, validation, and testing, respectively. We retain all the entities and relations in the September dump, resulting in 91,230,610 entities, 1,387 relations, and 601,062,811 triplets in total.
- **A better text encoder used.** The text features of WikiKG90Mv2 are obtained by using MPNet [4], which is shown to be significantly better sentence encoder [3].
- **Balancing relation types in validation/test triples.** On the new Wikidata dumps, we found the relation types of the raw validation/test triples are highly-skewed; the most frequent relation, "cites work (P2860)", occupies 60% and 8% of the entire validation and test triples, respectively. To test a model's capability to perform well across all types of relations, we subsample 15,000/10,000 triples from the entire test-dev/test-challenge triples such that the resulting relation counts are proportional to the cubic-root of the original relation counts.

###### **References**
[1] Vrandečić, D., & Krötzsch, M. (2014). Wikidata: a free collaborative knowledgebase. Communications of the ACM, 57(10), 78-85. <br/>
[2] Bollacker, K., Evans, C., Paritosh, P., Sturge, T., & Taylor, J. (2008, June). Freebase: a collaboratively created graph database for structuring human knowledge. In Proceedings of the 2008 ACM SIGMOD international conference on Management of data (pp. 1247-1250). <br/>
[3] Reimers, N., & Gurevych, I. (2019). Sentence-bert: Sentence embeddings using siamese bert-networks. arXiv preprint arXiv:1908.10084. <br/>
[4] Song, K., Tan, X., Qin, T., Lu, J., & Liu, T. Y. (2020). Mpnet: Masked and permuted pre-training for language understanding. arXiv preprint arXiv:2004.09297. <br/>

##### License: CC-0

---------------

<a name="dataset_object"/>
-------

##### **Python package: Dataset object**
The dataset object handles downloading and easy access to the graph and its features. Below we go through its basic usage.

###### **- Download and extract data**
Download and process dataset under the specified `ROOT` directory (default to `dataset/`).
This takes a while (several hours to a day) in the first run, so please be patient.
After decompression, the file size will be around 159GB.
```python
from ogb.lsc import WikiKG90Mv2Dataset
dataset = WikiKG90Mv2Dataset(root = ROOT)
```

###### **- Get basic dataset statistics**
```python
print(dataset.num_entities) # number of entities
print(dataset.num_relations) # number of relation types
print(dataset.num_feat_dims) # dimensionality of entity/relation features.
```

###### **- Get training triples**
Each triple consists of (`head`, `relation`, `tail`). In the following, we abbreviate it as (`h`, `r`, `t`).
Training triples can be obtained as follows.
```python
train_hrt = dataset.train_hrt # numpy ndarray of shape (num_triples, 3)
i = 1234
print(train_hrt[i]) # get i-th training triple (h[i], r[i], t[i])
```

###### **- Get entity features**
Entity features are extremely large (768-dimensional vectors for the 91M entities).
The features are saved as `numpy`'s **[`.npy` format](https://numpy.org/doc/stable/reference/generated/numpy.save.html)** in half precision (`np.float16`). The raw file is available at `ROOT/wikikg90m-v2/processed/entity_feat.npy` and has 131GB.

In our package, we use **[`numpy`'s read-only `memmap` mode](https://numpy.org/doc/stable/reference/generated/numpy.memmap.html)** so that the features can be loaded in a CPU-memory-efficient way.
In the `memmap` mode, each entity feature is not loaded into CPU memory from disk until it is explicitly accessed by your program.
Below are examples.
```python
# get i-th entity feature
i = 1234
print(dataset.entity_feat[i]) # only i-th data is loaded into memory

# get the feature matrix storing features of entities in idx_arr
idx_arr = np.array([1,10,100,1000,10000])
print(dataset.entity_feat[idx_arr]) # only the 5 data is loaded into memory
```

Here each data access is a disk access, which could be a bit slow. If you have sufficient CPU memory, you could also load the entire feature matrix into CPU memory at the beginning and enjoy fast RAM data access from there.
**Note: Do not run the following unless you have 200GB+ CPU memory!**

```python
# load the entire data (131GB) into CPU memory 
feat_in_memory = dataset.all_entity_feat # this takes a while

# Fast RAM access.
print(feat_in_memory[i])
print(feat_in_memory[idx_arr]) 
```

###### **- Get relation features**
```python
# both read the entire relation features (only 2MB) into CPU memory
print(dataset.relation_feat)
print(dataset.all_relation_feat)
```

###### **- Get a prediction task**
For validation and testing, the goal is to predict the correct `tail` given `head` and `relation`. Hence, the prediction can be written as `head,relation->tail`, or `h,r->t` in short.

Below we illustrate how we set up the `h,r->t` prediction task from the original validation/test triples (on the very left of the figure).

<p align = "center">
<img width="95%" src="{{ "/assets/img/wikikg2_task_illustration.png" | relative_url }}" class="img-responsive">
</p>

As illustrated, we convert the original `hrt` matrix into `hr`, `t`, as defined below.

- `hr`: numpy ndarray of shape (num_validation_triples, 2)
    - `i`-th row stores (`h[i]`, `r[i]`)
- `t`: numpy ndarray of shape (num_validation_triples, )
    - `i`-th row stores `t[i]`.

The task is for the model to accurately predict `t` given `hr`. Specifically, the model predicts `t_pred_top10`, defined as follows.

- `t_pred_top10`: numpy ndarray of shape `(num_validation_triples, 10)`
    -  `t_pred_top10[i][rank]` stores the `rank`-th predicted entity index of the tail entity.
    - In other words, the model predicts that (`h[i]`, `r[i]`, `t_pred_top10[i][rank]`) as the `rank`-th likely new triples, involving (`h[i]`, `r[i]`). 
    - You can assume that (`h[i]`, `r[i]`, `t[i]`) does not appear in training triples; therefore, the model should *not* re-predict training triples even if it assigns high scores (which is most likely the case as the model is directly trained on training triples).

The goal is for the model to rank `t[i]` as high as possible within `t_pred_top10[i]`, which is **measured by Reciprocal Rank (i.e., inverse of the rank).** If `t[i]` is not ranked within `t_pred_top10[i]`, the model receives the score of 0. The Overall performance is measured by **Mean Reciprocal Rank (MRR)**, which is commonly-used in the KG completion literature.

**For validation**, we provide all `hr` and `t`, which can be accessed as follows.
```python
valid_task = dataset.valid_dict['h,r->t'] # get a dictionary storing the h,r->t task.
hr = valid_task['hr']
t = valid_task['t']
```

**For test-dev and test-challenge**, we only provide `hr`, and `t` is hidden.
```python
testdev_task = dataset.test_dict(mode = 'test-dev')['h,r->t'] # get a dictionary storing the h,r->t task.
hr = testdev_task['hr']
# testdev_task['t'] is hidden and not provided
```


<a name="evaluator"/>

--------------

##### **Python package: Performance evaluator**
We provide an evaluator to evaluate and save model's prediction in a standardized way.
To evaluate train/validation performance, first prepare 
- `t_pred_top10`: numpy array of shape `(num_validation_triples, 10)`, defined above.
- `t`: numpy array of shape `(num_validation_triples, )`, defined above.

```python
from ogb.lsc import WikiKG90Mv2Evaluator

evaluator = WikiKG90Mv2Evaluator()
input_dict = {}
input_dict['h,r->t'] = {'t_pred_top10': t_pred_top10, 't', t}
result_dict = evaluator.eval(input_dict)
print(result_dict['mrr']) # get mrr
```

To save your test-dev submission, first prepare 
- `t_pred_top10`: `np.array` or `torch.Tensor` of shape `(num_test_triples, 10)`, defined above. The prediction is made over the `test-dev` set.
- `dir_path`: directory path (type: `str`) to save the test file (our package will create the directory if it does not exist). Test file `t_pred_wikikg90m-v2_test-dev.npz` will be saved under the directory `dir_path`.
- `mode`: either `test-dev` or `test-challenge` (type: `str`).

```python
input_dict = {}
input_dict['h,r->t'] = {'t_pred_top10': t_pred_top10}
evaluator.save_test_submission(input_dict = input_dict, dir_path = dir_path, mode = 'test-dev')
```

You can similarly prepare the test-challenge submission by preparing the corresponding `t_pred_top10` and set `mode` to be `test-challenge`.

---------

#### **Explore [WikiKG90Mv2 leaderboard](/docs/lsc/leaderboards/#wikikg90mv2)!**
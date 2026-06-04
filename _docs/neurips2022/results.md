---
title: OGB-LSC @ NeurIPS 2022
permalink: /neurips2022/results/
layout: neurips2022_results
---

#### **Learn about competition results and winning solutions**  

- **[Winners](#winners)**
    - **[MAG240M track](#winners_mag240m)**
    - **[WikiKG90Mv2 track](#winners_wikikg90mv2)**
    - **[PCQM4Mv2 track](#winners_pcqm4mv2)**

- **[NeurIPS workshop](/neurips2022/workshop/)**
- **[Leaderboards for test submissions](#leaderboards)**
    - **[MAG240M leaderboard](#leaderboard_mag240m)**
    - **[WikiKG90Mv2 leaderboard](#leaderboard_wikikg90mv2)**
    - **[PCQM4Mv2 leaderboard](#leaderboard_pcqm4mv2)**

-------

<a name="winners"/>

<a name="winners_mag240m"/>

#### **Winners of [MAG240M](/docs/lsc/mag240m/) Track ([Leaderboard](#leaderboard_mag240m))**

###### **1st place: ComeAgain ([contact](mailto:huangzhengjie@baidu.com))**
- **Team members**: Zhe Dong (Baidu Inc./Tianjin University), Hongwei Chen (Baidu Inc.), Siming Dai (Baidu Inc.), Yunsheng Shi (Baidu Inc.), Weibin Li (Baidu Inc.), Zhengjie Huang (Baidu Inc.), Mingguo He (Baidu Inc./Renmin University of China), Zeyang Fang (Baidu Inc.), Zeyu Chen (Baidu Inc.), Shikun Feng (Baidu Inc.)
- **Method**: Fastest R-UniMP (160 Ensemble)
- **Short summary**: We upgrade the R-UniMP with PEG and GPR methods.  And we train it with a much faster graph neural network training optimization using 8 A100 GPU with total 640G gpu memory, making it possible to train R-UniMP to reach SOTA in almost 1 hour in the fastest mode.
- **Learn more: [Technical report](/paper/neurips2022/mag240m_ComeAgain.pdf), [code](https://github.com/PaddlePaddle/PGL/tree/main/examples/NeurIPS2022-OGB-Challenge/MAG240M)**
- **Test accuracy**: 0.7570

###### **2nd place: DSE-node ([contact](mailto:wenhongz@msu.edu))**
- **Team members**: Hang Li (Michigan State University), Haoyu Han (Michigan State University), Hongzhi Wen (Michigan State University), Wei Jin (Michigan State University), Feng Shi (TigerGraph Company), Victor Lee (TigerGraph Company), Jiliang Tang (Michigan State University)
- **Method**: Inverse APPNP + R-UNIMP
- **Short summary**: Inverse APPNP stacking with R-GAT. 5 Inverse APPNP and 5 R-GAT models trained on different folds are ensembled.
- **Learn more: [Technical report](/paper/neurips2022/mag240m_DSE-node.pdf), [code](https://github.com/hzlihang99/NeurIPS2022-MAG240M)**
- **Test accuracy**: 0.7522

###### **3rd place: CogDL ([contact](mailto:cenyk1230@gmail.com))**
- **Team members**: Yufei He (Beijing Institute of Technology/Zhipu AI), Zhenyu Hou (Tsinghua University), Huanjing Zhao (Anhui University/Zhipu AI), Xiao Liu (Tsinghua University), Yukuo Cen (Tsinghua University), Xu Cheng (Tsinghua University)
- **Method**: MDGNN
- **Short summary**: A decoupled graph neural network with metapath-based features and other effective features. 15 models with different configurations are ensembled. 
- **Learn more: [Technical report](/paper/neurips2022/mag240m_CogDL.pdf), [code](https://github.com/cenyk1230/MDGNN_MAG240M)**
- **Test accuracy**: 0.7506

---------

<a name="winners_wikikg90mv2"/>

#### **Winners of [WikiKG90Mv2](/docs/lsc/wikikg90mv2/) Track ([Leaderboard](#leaderboard_wikikg90mv2))**

###### **1st place: wikiwiki ([contact](mailto:douglas.orr99@gmail.com))**
- **Team members**: Douglas Orr (Graphcore), Alberto Cattaneo (Graphcore), Daniel Justus (Graphcore), Harry Mellor (Graphcore), Jerome Maloberti (Graphcore), Zhenying Liu (Graphcore), Thorin Farnsworth (Graphcore), Andrew Fitzgibbon (Graphcore), Blazej Banaszewski (Graphcore), Carlo Luschi (Graphcore)
- **Method**: BESS + diverse shallow KGE ensemble (85 models)
- **Short summary**: An ensemble of 85 shallow KGE models combining five different scoring functions (TransE, TransH, RotatE, DistMult, ComplEx) and two different loss functions (log-sigmoid, sampled softmax cross-entropy), using a new distribution framework, BESS (Balanced Entity Sampling and Sharing).
- **Learn more: [Technical report](/paper/neurips2022/wikikg90mv2_wikiwiki.pdf), [code](https://github.com/graphcore/distributed-kge-poplar/tree/2022-ogb-submission)**
- **Test MRR**: 0.2562

###### **2nd place: DNAKG ([contact](mailto:xu.chen@microsoft.com))**
- **Team members**: Xu Chen (Microsoft Research Asia), Lun Du (Microsoft Research Asia), Xiaojun Ma (Microsoft Research Asia), Yue Fan (Peking University), Jiayi Liao (University of Science and Technology of China), Qiang Fu (Microsoft Research Asia), Shi Han (Microsoft Research Asia), Chongjian Yue (Peking University)
- **Method**: DNAKG
- **Short summary**: We generate candidates using a structure-based strategy and rule mining, and score them by 13 knowledge graph embedding models and 10 manual features. Finally we adopt the ensemble method to assemble the scores given by 13 knowledge graph embedding models and 10 manual features. 
- **Learn more: [Technical report](/paper/neurips2022/wikikg90mv2_DNAKG.pdf), [code](https://github.com/AprLie/DNAKG.git)**
- **Test MRR**: 0.2514

###### **3rd place: TIEG-Youpu ([contact](mailto:fengniesysu@gmail.com))**
- **Team members**: Feng Nie (Tencent), Zhixiu Ye (Tencent), Sifa Xie (Tencent), Shuang Wu (Tencent), Xin Yuan (Tencent), Liang Yao (Tencent), Jiazhen Peng (Tencent)
- **Method**: Structure enhanced retrieval and re-rank
- **Short summary**: Semantic&Structure enhanced retrieval with TransE+ComplEx+NOTE 6 model ensemble
- **Learn more: [Technical report](/paper/neurips2022/wikikg90mv2_TIEG-Youpu.pdf), [code](https://github.com/CoderMusou/NeurIPS_2022_WikiKG90Mv2_TIEG-Youpu)**
- **Test MRR**: 0.2309

---------

<a name="winners_pcqm4mv2"/>

#### **Winners of [PCQM4Mv2](/docs/lsc/pcqm4mv2/) Track ([Leaderboard](#leaderboard_pcqm4mv2))**

###### **1st place: WeLoveGraphs ([contact](mailto:dominic.masters.gc@gmail.com))**
- **Team members**: Dominic Masters (Graphcore), Kerstin Klaser (Graphcore), Josef Dean (Graphcore), Hatem Helal (Graphcore), Adam Sanders (Graphcore), Sam Maddrell-Mander (Graphcore), Zhiyi Li (Graphcore), Deniz Beker (Graphcore), Dominique Beaini (Valence Discovery/Universite de Montreal/Mila Quebec), Ladislav Rampasek (Universite de Montreal/Mila Quebec)
- **Method**: GPS++ (112 model ensemble)
- **Short summary**: We use GPS++, a hybrid message passing neural network (MPNN) and transformer that builds on the General, Powerful, Scalable (GPS) framework presented by Rampášek et al. [2022]. Specifically, this combines a large and expressive message passing module with a biased self-attention layer to maximise the benefit of local inductive biases while still allowing for effective global communication. Furthermore, we integrate a grouped input masking method to exploit available 3D positional information and use a denoising loss to alleviate oversmoothing.
- **Learn more: [Technical report](/paper/neurips2022/pcqm4mv2_WeLoveGraphs.pdf), [code](https://github.com/graphcore/ogb-lsc-pcqm4mv2)**
- **Test MAE**: 0.0719

###### **2nd place\*: ViSNet ([contact](mailto:watong@microsoft.com))**
- **Team members**: Tong Wang (MSR AI4Science), Yusong Wang (Xi`an Jiaotong University, MSR AI4Science), Shaoning Li (MSR AI4Science), Zun Wang (MSR AI4Science), Xinheng He (MSR AI4Science), Bin Shao (MSR AI4Science), Tie-Yan Liu (MSR AI4Science)
- **Method**: 20 Transformer-M-ViSNet + 2 Pretrained-3D-ViSNet 
- **Short summary**: We designed two kinds of models: Transformer-M-ViSNet which is a geometry-enhanced graph neural network for fully connected molecular graphs and Pretrained-3D-ViSNet which is a pretrained ViSNet by distilling geometric information from optimized structures. 22 models with different settings are ensembles.
- **Learn more: [Technical report](https://arxiv.org/abs/2211.12791), [code](https://github.com/microsoft/ViSNet/tree/OGB-LSC%40NIPS2022)**
- **Test MAE**: 0.0723

###### **2nd place\*: NVIDIA-PCQM4Mv2 ([contact](mailto:jeanfrancoispuget@gmail.com))**
- **Team members**: Jean-Francois Puget (NVIDIA), Jiwei Liu (NVIDIA), Gilberto Titericz Junior (NVIDIA), Sajad Darabi (NVIDIA), Alexandre Milesi (NVIDIA), Pawel Morkisz (NVIDIA), Shayan Fazeli (UCLA)
- **Method**: Heterogenous Ensemble of Models
- **Short summary**: Our method combines variants of the recent TransformerM architecture with Transformer, GNN, and ResNet backbone architectures. Models are trained on the 2D data, 3D data, and image modalities of molecular graphs. We ensemble these models with a HuberRegressor. The models are trained on 4 different train/validation splits of the original train + valid datasets.
- **Learn more: [Technical report](/paper/neurips2022/pcqm4mv2_NVIDIA-PCQM4Mv2.pdf), [code](https://github.com/jfpuget/NVIDIA-PCQM4Mv2)**
- **Test MAE**: 0.0723

\*: **Indicates the tied 2nd place.**

-------

<a name="leaderboards"/>

<a name="leaderboard_mag240m"/>
#### **Leaderboard for [MAG240M](/docs/lsc/mag240m/)**
##### Classification accuracy. The higher, the better.

| Rank  | Team | Test-challenge Accuracy 
|:----:|:-----:|:------:|
|  1  |  ComeAgain  | 0.7570  |
|  2  |  DSE-node  | 0.7522  |
|  3  |  CogDL  | 0.7506  |
|  4  |  xNetOO7  | 0.7419  |
|  5  |  ZHUQUE  | 0.7393  |
|  6  |  mycelia  | 0.7388  |
|  7  |  ICT-GIMLab  | 0.7386  |
|  8  |  Team Park  | 0.7293  |


-------

<a name="leaderboard_wikikg90mv2"/>
#### **Leaderboard for [WikiKG90Mv2](/docs/lsc/wikikg90mv2/)**
##### Mean Reciprocal Rank (MRR). The higher, the better.

| Rank  | Team | Test-challenge MRR 
|:----:|:-----:|:------:|
|  1  |  wikiwiki  | 0.2562  |
|  2  |  DNAKG  | 0.2514  |
|  3  |  TIEG-Youpu  | 0.2309  |
|  4  |  CogDL-kgTransformer  | 0.2292  |
|  5  |  USTCWiki  | 0.2279  |
|  6  |  GraphLARS  | 0.2185  |
|  7  |  GraphPKU  | 0.2178  |
|  8  |  AgainCome  | 0.2153  |
|  9  |  KnowledgeIsPower  | 0.1242  |
|  10  |  Big Smarted  | 0.0167  |


-------

<a name="leaderboard_pcqm4mv2"/>
#### **Leaderboard for [PCQM4Mv2](/docs/lsc/pcqm4mv2/)**
##### Mean Absolute Error (MAE). The lower, the better.

| Rank  | Team | Test-challenge MAE 
|:----:|:-----:|:------:|
|  1  |  WeLoveGraphs  | 0.0719  |
|  2  |  ViSNet  | 0.0723  |
|  2  |  NVIDIA-PCQM4Mv2  | 0.0723  |
|  4  |  YouGraph  | 0.0734  |
|  5  |  DIVE-TAMU  | 0.0746  |
|  6  |  polixir.ai  | 0.0752  |
|  7  |  PhiNeurons  | 0.0755  |
|  8  |  GraphLARS  | 0.0756  |
|  9  |  CogDL  | 0.0758  |
|  10  |  The Graphoppers  | 0.0899  |
|  11  |  Zhuque Zhejianglab  | 0.1008  |
|  12  |  Mingdu Zeeta  | 0.1202  |
|  13  |  GraFactored  | 0.2224  |

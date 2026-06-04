---
title: OGB-LSC @ KDD Cup 2021
permalink: /kddcup2021/results/
layout: kdd_results
---

#### **Learn about competition results and winning solutions**  

- **[Awardees](#awardees)**
    - **[MAG240M-LSC track](#awardees_mag240m)**
    - **[WikiKG90M-LSC track](#awardees_wikikg90m)**
    - **[PCQM4M-LSC track](#awardees_pcqm4m)**

- **[Final test submission](#final): Evaluated on the entire test data**
    - **[Final MAG240M-LSC leaderboard](#final_mag240m)**
    - **[Final WikiKG90M-LSC leaderboard](#final_wikikg90m)**
    - **[Final PCQM4M-LSC leaderboard](#final_pcqm4m)**

- **[Initial test submission](#initial): Evaluated on 5% of test data (same across submissions)**
    - **[Initial MAG240M-LSC leaderboard](#initial_mag240m)**
    - **[Initial WikiKG90M-LSC leaderboard](#initial_wikikg90m)**
    - **[Initial PCQM4M-LSC leaderboard](#initial_pcqm4m)**

-------

<a name="awardees"/>

<a name="awardees_mag240m"/>

#### **Awardees of [MAG240M-LSC](/kddcup2021/mag240m/) Track ([Leaderboard](#final_mag240m))**
##### **Winners**
###### **1st place: BD-PGL ([contact](mailto:shiyunsheng01@baidu.com))**
- **Team members**: Yunsheng Shi (Baidu), Zhengjie Huang (Baidu), Weibin Li (Baidu), Weiyue Su (Baidu), Shikun Feng (Baidu)
- **Method**: R-UNIMP
- **Short summary**: We adopt the recent advanced technique UniMP which proposes to incorporate feature and label propagation at both training and inference time, making significant improvements across several node classification tasks. And we modify it into an R-UniMP version for a heterogeneous graph with "R" stands for "Relational". Besides, we provide a detailed recall of our key strategies and valuable findings during the en- tire competition. 30 models with different initialization are ensembled.
- **Learn more: [Technical report](/paper/kddcup2021/mag240m_BD-PGL.pdf), [code](https://github.com/PaddlePaddle/PGL/tree/main/examples/kddcup2021/MAG240M/r_unimp)**
- **Test accuracy**: 0.7549

###### **2nd place: Academic ([contact](mailto:petarv@google.com))**
- **Team members**: Petar Velickovic (DeepMind), Peter Battaglia (DeepMind), Jonathan Godwin (DeepMind), Alvaro Sanchez (DeepMind), David Budden (DeepMind), Shantanu Thakoor (DeepMind), Jacklynn Stott (DeepMind), Ravichandra Addanki (DeepMind), Thomas Keck (DeepMind), Andreea Deac (DeepMind)
- **Method**: MPNN Ensemble with BGRL fine-tuning
- **Short summary**: MPNN over subsampled patches, fine-tuned by BGRL (bootstrapped graph latents) self-supervised objective. 20 models with different initialisation and validation split are ensembled.
- **Learn more: [Technical report](/paper/kddcup2021/mag240m_Academic.pdf), [code](https://github.com/deepmind/deepmind-research/tree/master/ogb_lsc/mag)**
- **Test accuracy**: 0.7519

###### **3rd place: Synerise AI ([contact](mailto:jack.dabrowski@synerise.com))**
- **Team members**: Michal Daniluk (Synerise), Jacek Dabrowski (Synerise), Konrad Goluchowski (Synerise), Barbara Rychalska (Warsaw University of Technology/Synerise)
- **Method**: Cleora + EMDE
- **Short summary**: We tackle the task with an efficient model based on our previously introduced algorithms: EMDE and Cleora, on top of a simplistic feed-forward neural network.  We use EMDE to represent nodes in the form of sketches -- structures representing local similarity, which additionally allow for easy accumulation of multiple object values. We use Cleora for label propagation, i.e. representing nodes with sets of labels observed in the training data. To achieve maximal performance, we train 60 independent ensemble models.
- **Learn more: [Technical report](/paper/kddcup2021/mag240m_SyneriseAI.pdf), [code](https://github.com/Synerise/kdd-cup-2021)**
- **Test accuracy**: 0.7460

##### **Runner-ups**
###### **4th place: Topology_mag ([contact](mailto:caowencai@oppo.com))**
- **Team members**: Qiuying Peng (OPPO Research), Wencai Cao (OPPO Research), Zheng Pan (OPPO Research)
- **Method**: MPLP + finetune (40 ensemble)
- **Short summary**: Metapath-based Label Propagation with fine-tuning using latest year samples. models from 5-fold cross-validation in 8 random seeds are ensembled.
- **Learn more: [Technical report](/paper/kddcup2021/mag240m_Topology_mag.pdf), [code](https://github.com/qypeng-ustc/mplp)**
- **Test accuracy**: 0.7447

###### **5th place: passages ([contact](mailto:tsotfsk@bupt.edu.cn))**
- **Team members**: Bole Ai (Nanjing University), Xiang Long (Beijing University of Posts and Telecommunications), Kaiyuan Li (Beijing University of Posts and Telecommunications), Quan Lin (Huazhong University of Science and Technology), Xiaofan Liu (Beijing University of Posts and Telecommunications), Pengfei Wang (Beijing University of Posts and Telecommunications), Mingdao Wang (Beijing University of Posts and Telecommunications), Zhichao Feng (Beijing University of Posts and Telecommunications), Kun Zhao (Nanjing University)
- **Method**: SGC + R-GAT + Finetune
- **Short summary**: Our method can be largely summarized in two main stages: a pretraining stage is designed to explore heterogeneous academic networks for better node embeddings; and a transfer learning stage is used to alleviate differences of label distributions and node representations between training and test set.
- **Learn more: [Technical report](/paper/kddcup2021/mag240m_passages.pdf), [code](https://github.com/passages-kddcup2021/KDDCUP2021_OGB_LSC_MAG240M)**
- **Test accuracy**: 0.7381

###### **6th place: DeeperBiggerBetter ([contact](mailto:guohao.li@kaust.edu.sa))**
- **Team members**: Guohao Li (KAUST), Hesham Mostafa (Intel Corporation), Jesus Alejandro Zarzar Torano (KAUST), Sami Abu-El-Haija (USC), Marcel Nassar (Intel Labs), Daniel Cummings (Intel Corporation), Sohil Shah (Intel Corporation), Matthias Mueller (Intel Labs), Bernard Ghanem (KAUST)
- **Method**: GNN180M
- **Short summary**: We train two R-GAT models, one with 2 layers and another with 3 layers for a total of 180M parameters. We utilize author labels as extra regularization, conduct multiple inference passes with proportional neighborhood sizes, aggregate their results by ensembling and then apply a label smoothing trick on model's predictions with author labels for post-processing. 
- **Learn more: [Technical report](/paper/kddcup2021/mag240m_DeeperBiggerBetter.pdf), [code](https://github.com/zarzarj/DeeperBiggerBetter_KDDCup)**
- **Test accuracy**: 0.7353

---------

<a name="awardees_wikikg90m"/>

#### **Awardees of [WikiKG90M-LSC](/kddcup2021/wikikg90m/) Track ([Leaderboard](#final_wikikg90m))**

##### **Winners**
###### **1st place: BD-PGL ([contact](mailto:weiyue.su@gmail.com))**
- **Team members**: Weiyue Su (Baidu), Shikun Feng (Baidu), Zeyang Fang (Baidu), Huijuan Wang (Baidu), Siming Dai (Baidu), Hui Zhong (Baidu), Yunsheng Shi (Baidu), Zhengjie Huang (Baidu)
- **Method**: NOTE + Feature
- **Short summary**: We modified OTE into NOTE for better performance and use the post-smoothing technique to capture the graph structure for supplementation. Feature engineering further improves the results.
- **Learn more: [Technical report](/paper/kddcup2021/wikikg90m_BD-PGL.pdf), [code](https://github.com/PaddlePaddle/PGL/tree/main/examples/kddcup2021/WikiKG90M)**
- **Test MRR**: 0.9727
- **Note:** The solution explictly makes use of val/test tail candidate entities provided by the organizer. In practice, those candidates are not provided, and a model needs to rank among all entities.

###### **2nd place: OhMyGod ([contact](mailto:pengwh.hit@gmail.com))**
- **Team members**: Weihua Peng (Harbin Institute of Technology)
- **Method**: TransE, CompIEx, DistMult, and SimplE (9 ensemble)
- **Short summary**: a) more powerful representation vector learning, b) the complementarity between different models, c) candidate filtering based on the aggregated statistics of the validation/test tail candidates.
- **Learn more: [Technical report](/paper/kddcup2021/wikikg90m_OhMyGod.pdf), [code](https://github.com/biandh/KDDCup2021_WikiKG90M_OhMyGod/tree/master/examples/lsc/wikikg90m)**
- **Test MRR**: 0.9712
- **Note:** The solution explictly makes use of val/test tail candidate entities provided by the organizer. In practice, those candidates are not provided, and a model needs to rank among all entities.

###### **3rd place: GraphMIRAcles ([contact](mailto:jycai@mail.ustc.edu.cn))**
- **Team members**: Jianyu Cai (University of Science and Technology of China), Jiajun Chen (University of Science and Technology of China), Taoxing Pan (University of Science and Technology of China), Zhanqiu Zhang (University of Science and Technology of China), Jie Wang (University of Science and Technology of China)
- **Method**: ComplEx-CMRC + Rule + KD (15 ensemble)
- **Short summary**: Encoder: Concat-MLP with Residual Connection (CMRC). Decoder: ComplEx. Rule mining for data augmentation. Knowledge distillation to improve single models. 15 models with different random seeds are ensembled.
- **Learn more: [Technical report](/paper/kddcup2021/wikikg90m_GraphMIRAcles.pdf), [code](https://github.com/MIRALab-USTC/KDDCup2021_WikiKG90M_GraphMIRAcles)**
- **Test MRR**: 0.9707
- **Note:** The solution explictly makes use of val/test tail candidate entities provided by the organizer. In practice, those candidates are not provided, and a model needs to rank among all entities.

##### **Runner-ups**
###### **4th place: littleant ([contact](mailto:kexi.ys@antgroup.com))**
- **Team members**: Shuo Yang (Ant Group), Daixin Wang (Ant Group), Dingyuan Zhu (Ant Group), Yakun Wang (Ant Group), Borui Ye (Ant Group)
- **Method**: AntLinkPred
- **Short summary**: 1. Heuristic features extraction. 2. Decoder (TransE, AutoSF, PariRE, RotatE,. etc) selection and model ensemble. 3. Model fine-tuning with low-confidence samples. 4. Generate a smaller candidates list with a recall model. 5. Generate final results by a re-ranking model.  
- **Learn more: [Technical report](/paper/kddcup2021/wikikg90m_littleant.pdf), [code](https://github.com/herrkun/ogb/tree/master/examples/lsc/wikikg90m/dgl-ke-ogb-lsc/python)**
- **Test MRR**: 0.9511

---------

<a name="awardees_pcqm4m"/>

#### **Awardees of [PCQM4M-LSC](/kddcup2021/pcqm4m/) Track ([Leaderboard](#final_pcqm4m))**

##### **Winners**
###### **1st place: MachineLearning ([contact](mailto:yingchengsyuan@gmail.com))**
- **Team members**: Chengxuan Ying (Dalian University of Technology), Mingqi Yang (Dalian University of Technology), Shengjie Luo (Peking University), Tianle Cai (Princeton University), Guolin Ke (MSRA), Di He (MSRA), Shuxin Zheng (MSRA), Chenglin Wu (Xiamen University), Yuxin Wang (Dalian University of Technology), Yanming Shen (Dalian University of Technology)
- **Method**: Graphormer (10 ensemble) + ExpC (8 ensemble)
- **Short summary**: We adopt Graphormer and ExpC as our basic models. We train each model by 8-fold cross-validation, and additionally train two Graphormer models on the union of training and validation sets with different random seeds. For final submission, we use a naive ensemble for these 18 models by taking average of their outputs.
- **Learn more: [Technical report](https://arxiv.org/pdf/2106.08279.pdf), [code](https://github.com/microsoft/Graphormer/tree/ogb-lsc)**
- **Test MAE**: 0.1200

###### **2nd place: SuperHelix ([contact](mailto:zhangshanzhuo@baidu.com))**
- **Team members**: Shanzhuo Zhang (Baidu), Lihang Liu (Baidu), Sheng Gao (Baidu), Donglong He (Baidu), Weibin Li (Baidu), Zhengjie Huang (Baidu), Weiyue Su (Baidu), Wenjin Wang (Baidu)
- **Method**: LiteGEM
- **Short summary**: Deep graph neural network with self-supervised tasks on topology and geometry information. 73 models with different tasks and hyper-parameters are ensembled.
- **Learn more: [Technical report](/paper/kddcup2021/pcqm4m_SuperHelix.pdf), [code](https://github.com/PaddlePaddle/PaddleHelix/tree/dev/competition/kddcup2021-PCQM4M-LSC)**
- **Test MAE**: 0.1204

###### **3rd place: Quantum ([contact](mailto:petarv@google.com))**
- **Team members**: Petar Velickovic (DeepMind), Peter Battaglia (DeepMind), Jonathan Godwin (DeepMind), Alvaro Sanchez (DeepMind), David Budden (DeepMind), Shantanu Thakoor (DeepMind), Jacklynn Stott (DeepMind), Ravichandra Addanki (DeepMind), Sibon Li (DeepMind), Andreea Deac (DeepMind)
- **Method**: Very Deep GN Ensemble + Conformers + Noisy Nodes
- **Short summary**: A combination of a 32-layer deep Graph Network over RDKit conformer features, and 50-layer deep Graph Network for molecules for which conformers cannot be computed. Denoising regularisation with Noisy Nodes was applied. 20 models with different initialisation and validation splits are ensembled.
- **Learn more: [Technical report](/paper/kddcup2021/pcqm4m_Quantum.pdf), [code](https://github.com/deepmind/deepmind-research/tree/master/ogb_lsc/pcq)**
- **Test MAE**: 0.1205

##### **Runner-ups**
###### **4th place: DIVE@TAMU ([contact](mailto:hao.yuan@tamu.edu))**
- **Team members**: Meng Liu (Texas A&M University), Cong Fu (Texas A&M University), Xuan Zhang (Texas A&M University), Limei Wang (Texas A&M University), Yaochen Xie (Texas A&M University), Hao Yuan (Texas A&M University), Youzhi Luo (Texas A&M University), Zhao Xu (Texas A&M University), Shenglong Xu (Texas A&M University), Shuiwang Ji (Texas A&M University)
- **Method**: 2D Deep GNNs + 3D low-cost conformer GNNs
- **Short summary**: (1) 2D Deeper GNN with larger receptive fields (over 20 layers) and more expressivity over 2D molecular graphs.
(2) 3D GNN over low-cost conformer sets, which can be obtained by RDKit with an affordable budget.
- **Learn more: [Technical report](/paper/kddcup2021/pcqm4m_DIVE.pdf), [code](https://github.com/divelab/MoleculeX)**
- **Test MAE**: 0.1235

###### **5th place: no_free_lunch ([contact](mailto:zouxiaochuan1984@gmail.com))**
- **Team members**: Xiaochuan Zou (AntGroup), Ruofan Wu (AntGroup), Baokun Wang (AntGroup), Sheng Tian (AntGroup), Yifei Hu (AntGroup), Liang Zhu (AntGroup), Peixuan Chen (AntGroup), MengjiaoZ hang (AntGroup), Yuhao Zhang (AntGroup)
- **Method**: Ensemble MolNet
- **Short summary**: Tansformer with graph structure features. 6 models with different initialization and running epochs are ensembled
- **Learn more: [Technical report](/paper/kddcup2021/pcqm4m_no_free_lunch.pdf), [code](https://github.com/zouxiaochuan/molnet_kddcup2021)**
- **Test MAE**: 0.1244

###### **6th place: GNNLearner ([contact](mailto:yinxia@microsoft.com))**
- **Team members**: Yingce Xia (Microsoft Research Asia), Lijun Wu (Microsoft Research Asia), Shufang Xie (Microsoft Research Asia), Jinhua Zhu (University of Science and Technology of China), Yang Fan (University of Science and Technology of China), Yutai Hou (Harbin Institute of Technology), Tao Qin (Microsoft Research Asia)
- **Method**: Transformers(standard x4,two-branch x8) + GIN (x5)
- **Short summary**: (1) Transformer with two branches, where one for regression and the other for classification. Two branches learn from each other; (2) Standard Transformer; (3) GIN; Models with different initialization are aggregated.
- **Learn more: [Technical report](/paper/kddcup2021/pcqm4m_GNNLearner.pdf), [code](https://github.com/TransfromerMeetsGraph/GNNLearner)**
- **Test MAE**: 0.1253

-------

<a name="final"/>

<a name="final_mag240m"/>
#### **Final leaderboard for [MAG240M-LSC](/kddcup2021/mag240m/)**
##### Classification accuracy. The higher, the better.

| Rank  | Team | Test Accuracy 
|:----:|:-----:|:------:|
|  1  |  BD-PGL  | 0.7549  |
|  2  |  Academic  | 0.7519  |
|  3  |  Synerise AI  | 0.7460  |
|  4  |  Topology_mag  | 0.7447  |
|  5  |  passages  | 0.7381  |
|  6  |  DeeperBiggerBetter  | 0.7353  |
|  7  |  paper2paper  | 0.7292  |
|  8  |  NTT DOCOMO LABS  | 0.7290  |
|  9  |  GraphAI  | 0.7278  |
|  10  |  MC-AiDA  | 0.7274  |
|  11  |  yangxc  | 0.7273  |
|  12  |  AntAntGraph  | 0.7272  |
|  13  |  IF-bigdata  | 0.7271  |
|  14  |  antkg  | 0.7260  |
|  15  |  LEEXY  | 0.7254  |
|  16  |  PKUDB3  | 0.7250  |
|  17  |  PM-TEAM  | 0.7239  |
|  18  |  Euler  | 0.7233  |
|  19  |  UVA-PolyU-MAG  | 0.7218  |
|  20  |  hust-tigergraph  | 0.7196  |
|  21  |  nvsac  | 0.7165  |
|  22  |  Abearcomes  | 0.7161  |
|  23  |  MSRA DKI  | 0.7118  |
|  24  |  Ikigai  | 0.7113  |
|  25  |  Graph@PKU  | 0.7076  |
|  26  |  Fireside Coding Club  | 0.7035  |
|  27  |  bjtuxingyuan  | 0.7030  |
|  28  |  mtMAG  | 0.7027  |
|  29  |  CogDL  | 0.7018  |
|  30  |  VCGroup  | 0.7001  |
|  31  |  UCLA-Graph  | 0.6988  |
|  32  |  University of Macau  | 0.6946  |
|  33  |  FreedomDancer  | 0.6925  |
|  34  |  ALGRUC  | 0.6921  |
|  35  |  jianmohuo  | 0.6905  |
|  36  |  zjuainet  | 0.6897  |
|  37  |  fanfanman  | 0.6821  |
|  38  |  GoBruins  | 0.6517  |
|  39  |  HUNGraphs  | 0.6517  |
|  40  |  Four Colors  | 0.6466  |
|  41  |  Oxtest  | 0.6408  |
|  42  |  TPA FDU  | 0.6400  |
|  43  |  dascim  | 0.5898  |
|  44  |  Rotopia  | 0.5783  |
|  45  |  Binary Bird  | 0.0218  |
|  46  |  BU-LISP  | 0.0009  |


-------

<a name="final_wikikg90m"/>
#### **Final leaderboard for [WikiKG90M-LSC](/kddcup2021/wikikg90m/)**
##### Mean Reciprocal Rank (MRR). The higher, the better.

| Rank  | Team | Test MRR 
|:----:|:-----:|:------:|
|  1  |  BD-PGL  | 0.9727  |
|  2  |  OhMyGod  | 0.9712  |
|  3  |  GraphMIRAcles  | 0.9707  |
|  4  |  littleant  | 0.9511  |
|  5  |  vcdbro  | 0.9489  |
|  6  |  JohnZheng  | 0.9465  |
|  7  |  VCGroup  | 0.9432  |
|  8  |  USTC-HNT-1  | 0.9324  |
|  9  |  USTC-HNT  | 0.9311  |
|  10  |  CogDL  | 0.9275  |
|  11  |  RelAix  | 0.9184  |
|  12  |  Neural Bellman-Ford Networks  | 0.9178  |
|  13  |  mtWIKIKG  | 0.9081  |
|  14  |  cciiplab  | 0.9058  |
|  15  |  Heads and Tails  | 0.9047  |
|  16  |  Hello KG  | 0.8945  |
|  17  |  NTT DOCOMO INC  | 0.8935  |
|  18  |  迷路的小叮当  | 0.8761  |
|  19  |  HET-TigerGraph  | 0.8720  |
|  20  |  antkg  | 0.8712  |
|  21  |  AJ Team  | 0.8688  |
|  22  |  UVA-PolyU-Wiki  | 0.8653  |
|  23  |  TransCendence  | 0.8252  |
|  24  |  NiuBiP  | 0.7425  |
|  25  |  XJTUGNN  | 0.6597  |
|  26  |  WashuLink  | 0.4791  |
|  27  |  BU-LISP  | 0.0629  |
|  28  |  SUFE-OXAI  | 0.0029  |


-------

<a name="final_pcqm4m"/>
#### **Final leaderboard for [PCQM4M-LSC](/kddcup2021/pcqm4m/)**
##### Mean Absolute Error (MAE). The lower, the better.

| Rank  | Team | Test MAE 
|:----:|:-----:|:------:|
|  1  |  MachineLearning  | 0.1200  |
|  2  |  SuperHelix  | 0.1204  |
|  3  |  Quantum  | 0.1205  |
|  4  |   DIVE@TAMU  | 0.1235  |
|  5  |  no_free_lunch  | 0.1244  |
|  6  |  GNNLearner  | 0.1253  |
|  7  |  RelAix  | 0.1273  |
|  8  |  VCGroup  | 0.1281  |
|  9  |  pauli  | 0.1293  |
|  10  |  mtPCQM  | 0.1298  |
|  11  |  NTT DOCOMO LABS  | 0.1298  |
|  12  |  Schrodinger  | 0.1305  |
|  13  |  Ant-AGL-Chem  | 0.1306  |
|  14  |  AI Winter is Coming  | 0.1324  |
|  15  |  HUNGraphs  | 0.1327  |
|  16  |  PreferredSmile  | 0.1328  |
|  17  |  ADVERSARIES  | 0.1328  |
|  18  |  MoleculeHunter  | 0.1338  |
|  19  |  KAICD  | 0.1344  |
|  20  |  CogDL  | 0.1346  |
|  21  |  MLCollective  | 0.1358  |
|  22  |  Team IC1101  | 0.1398  |
|  23  |  DeepBlueAI  | 0.1414  |
|  24  |  So Vegetable  | 0.1415  |
|  25  |  USTC-DLC  | 0.1416  |
|  26  |  Autobot  | 0.1418  |
|  27  |  DeeperBiggerBetter  | 0.1420  |
|  28  |  Topology_pcq  | 0.1421  |
|  29  |  The_Sky_Is_Blue  | 0.1423  |
|  30  |  DeepBlueAI  | 0.1429  |
|  31  |  The Graphinators  | 0.1432  |
|  32  |  JustDoIt  | 0.1434  |
|  33  |  CUNY KDD Cup  | 0.1435  |
|  34  |  THUMLP  | 0.1443  |
|  35  |  Danhuangpai  | 0.1447  |
|  36  |  The Long and Winding Node  | 0.1457  |
|  37  |  dminers  | 0.1467  |
|  38  |  RiseLab  | 0.1469  |
|  39  |  FudanGWX  | 0.1501  |
|  40  |  USTC-MO  | 0.1536  |
|  41  |  braino  | 0.1537  |
|  42  |  IITD-GPU-GO-BRRR  | 0.1544  |
|  43  |  USTC-MO-1  | 0.1568  |
|  44  |  Celestial Being  | 0.1589  |
|  45  |  kojimar  | 0.1590  |
|  46  |  BUPTTDCS-TG  | 0.1606  |
|  47  |  CIML at UniPI  | 0.2105  |
|  48  |  yfishlab  | 0.2202  |
|  49  |  GraLITIS  | 0.9393  |


-------

<a name="initial"/>

<a name="initial_mag240m"/>
#### **Initial leaderboard for [MAG240M-LSC](/kddcup2021/mag240m/)**
##### Classification accuracy. The higher, the better.

| Rank  | Team | Test Accuracy (subset) 
|:----:|:-----:|:------:|
|  1  |  Synerise AI  | 0.7454  |
|  2  |  BD-PGL  | 0.7339  |
|  3  |  antkg  | 0.7241  |
|  4  |  DeeperBiggerBetter  | 0.7132  |
|  5  |  passages  | 0.7113  |
|  6  |  Academic  | 0.7082  |
|  7  |  PKUDB3  | 0.7067  |
|  8  |  Graph@PKU  | 0.7049  |
|  9  |  the-stone-story  | 0.7045  |
|  10  |  NTT DOCOMO LABS  | 0.7020  |
|  11  |  Abearcomes  | 0.7008  |
|  12  |  winone  | 0.7003  |
|  13  |  Ikigai  | 0.6984  |
|  14  |  AntAntGraph  | 0.6975  |
|  15  |  MSRA DKI  | 0.6974  |
|  16  |  hust-tigergraph  | 0.6967  |
|  17  |  mtMAG  | 0.6958  |
|  18  |  VCGroup  | 0.6936  |
|  19  |  Topology_mag  | 0.6925  |
|  20  |  luke28  | 0.6922  |
|  21  |  MindGMP  | 0.6920  |
|  22  |  PM-TEAM  | 0.6918  |
|  23  |  LEEXY  | 0.6913  |
|  24  |  Susanna  | 0.6901  |
|  25  |  HJYgotoPLAY  | 0.6892  |
|  26  |  CogDL  | 0.6884  |
|  27  |  IF-bigdata  | 0.6877  |
|  28  |  Fightfightfight  | 0.6875  |
|  29  |  bjtuxingyuan  | 0.6871  |
|  30  |  KAICD  | 0.6868  |
|  31  |  GraphAI  | 0.6864  |
|  31  |  overwatch  | 0.6864  |
|  32  |  TheAIDivision  | 0.6849  |
|  33  |  fanfanman  | 0.6811  |
|  34  |  zjuainet  | 0.6798  |
|  35  |  UVA-PolyU-MAG  | 0.6782  |
|  36  |  no_free_lunch  | 0.6781  |
|  37  |  UCLA-Graph  | 0.6771  |
|  38  |  Fireside Coding Club  | 0.6751  |
|  39  |  nvsac  | 0.6729  |
|  40  |  PAHT-AI  | 0.6631  |
|  41  |  ALGRUC  | 0.6629  |
|  42  |  yangxc  | 0.6557  |
|  43  |  Binary Bird  | 0.6504  |
|  44  |  Mojito  | 0.6366  |
|  45  |  ANTKCC  | 0.5304  |
|  46  |  XJTUGNN  | 0.5264  |
|  47  |  Four Colors  | 0.5241  |
|  48  |  UPSIDE-DOWN  | 0.5233  |
|  49  |  MC-AiDA  | 0.5210  |
|  50  |  DeepBlueTechnology  | 0.4653  |
|  51  |  BU-LISP  | 0.3920  |
|  52  |  dascim  | 0.0582  |
|  53  |  paper2paper  | 0.0213  |
|  54  |  Rookie  | 0.0202  |
|  55  |  lleb-mag  | 0.0067  |


-------

<a name="initial_wikikg90m"/>
#### **Initial leaderboard for [WikiKG90M-LSC](/kddcup2021/wikikg90m/)**
##### Mean Reciprocal Rank (MRR). The higher, the better.

| Rank  | Team | Test MRR (subset) 
|:----:|:-----:|:------:|
|  1  |  JohnZheng  | 0.9405  |
|  2  |  OhMyGod  | 0.9401  |
|  3  |  vcdbro  | 0.9291  |
|  4  |  littleant  | 0.9261  |
|  5  |  GraphMIRAcles  | 0.9223  |
|  6  |  sanwenaoteman  | 0.9088  |
|  7  |  esther  | 0.9087  |
|  8  |  mtWIKIKG  | 0.9035  |
|  9  |  RelAix  | 0.9027  |
|  10  |  yeyeye  | 0.8967  |
|  11  |  cciiplab  | 0.8944  |
|  12  |  迷路的小叮当  | 0.8938  |
|  13  |  GNNIAUN  | 0.8877  |
|  14  |  BD-PGL  | 0.8858  |
|  15  |  Neural Bellman-Ford Networks  | 0.8792  |
|  16  |  VCGroup  | 0.8722  |
|  17  |  CogDL  | 0.8705  |
|  18  |  TheAIDivision  | 0.8690  |
|  19  |  AJ Team  | 0.8681  |
|  20  |  GreatTeam  | 0.8675  |
|  21  |  GalaxyX  | 0.8647  |
|  22  |  Synerise AI  | 0.8606  |
|  23  |  abcdef  | 0.8513  |
|  24  |  UVA-PolyU-Wiki  | 0.8498  |
|  25  |  TransCendence  | 0.8154  |
|  26  |  spoer  | 0.8131  |
|  27  |  迪迦奥特曼  | 0.7847  |
|  28  |  MorningStar  | 0.7775  |
|  29  |  USTC-HNT  | 0.7356  |
|  30  |  Knowledgeable  | 0.7347  |
|  31  |  HET-TigerGraph  | 0.7344  |
|  32  |  BU-LISP  | 0.7280  |
|  33  |  NTT DOCOMO INC  | 0.7199  |
|  34  |  The A-Team  | 0.6708  |
|  35  |  Heads and Tails  | 0.4346  |
|  36  |  XJTUGNN  | 0.0825  |
|  37  |  antkg  | 0.0104  |
|  38  |  no_free_lunch  | 0.0030  |
|  39  |  fastretrieve.ai  | 0.0030  |


-------

<a name="initial_pcqm4m"/>
#### **Initial leaderboard for [PCQM4M-LSC](/kddcup2021/pcqm4m/)**
##### Mean Absolute Error (MAE). The lower, the better.

| Rank  | Team | Test MAE (subset) 
|:----:|:-----:|:------:|
|  1  |  SuperHelix  | 0.1294  |
|  2  |  MachineLearing  | 0.1328  |
|  3  |  Autobot  | 0.1338  |
|  4  |  Quantum  | 0.1352  |
|  5  |  no_free_lunch  | 0.1356  |
|  6  |   DIVE@TAMU  | 0.1363  |
|  7  |  RelAix  | 0.1366  |
|  8  |  NTT DOCOMO LABS  | 0.1369  |
|  9  |  mtPCQM  | 0.1370  |
|  10  |  Ant-AGL-Chem  | 0.1394  |
|  11  |  the-stone-story  | 0.1403  |
|  12  |  Team IC1101  | 0.1406  |
|  13  |  overwatch  | 0.1408  |
|  14  |  TongJing  | 0.1413  |
|  15  |  VCGroup  | 0.1416  |
|  16  |  Schrodinger  | 0.1425  |
|  17  |  CUNY KDD Cup  | 0.1443  |
|  18  |  MLCollective  | 0.1456  |
|  19  |  GNNLearner  | 0.1474  |
|  20  |  So Vegetable  | 0.1486  |
|  21  |  The_Sky_Is_Blue  | 0.1492  |
|  22  |  yangxc  | 0.1497  |
|  23  |  Topology_pcq  | 0.1498  |
|  24  |  WBMSDU  | 0.1504  |
|  25  |  CogDL  | 0.1510  |
|  26  |  braino  | 0.1511  |
|  27  |  kojimar  | 0.1565  |
|  28  |  HUNGraphs  | 0.1572  |
|  29  |  PreferredSmile  | 0.1614  |
|  30  |  pauli  | 0.1673  |
|  31  |  Tardigrades  | 0.1717  |
|  32  |  DBSISDM  | 0.1755  |
|  33  |  AI Winter is Coming  | 0.1793  |
|  34  |  USTC-MO  | 0.1803  |
|  35  |  IITD-GPU-GO-BRRR  | 0.1826  |
|  36  |  NO HUMO NO LUMO BRO  | 0.1880  |
|  37  |  USTC-MO-1  | 0.1927  |
|  38  |  DeepBlueAI  | 0.2090  |
|  39  |  MoleculeHunter  | 0.2171  |
|  40  |  Family Business  | 0.2215  |
|  41  |  USTC-DLC  | 0.2223  |
|  42  |  dminers  | 0.2382  |
|  43  |  yfishlab  | 0.2865  |
|  44  |  KAICD  | 0.3466  |
|  45  |  DeepBlueAI  | 0.3694  |
|  46  |  GLab-graph  | 0.6404  |
|  47  |  shadoks  | 1.1089  |
|  48  |  GraLITIS  | 1.3002  |
|  49  |  FocusMind  | 5.0008  |


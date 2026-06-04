---
title: OGB-LSC @ NeurIPS 2022
permalink: /neurips2022/
layout: neurips2022_overview
---

#### **Why 2nd OGB-LSC?**
Machine learning (ML) over large-scale graph data (e.g., graphs with billions of edges) has a huge impact.
[At KDD Cup 2021](/kddcup2021/), we organized the 1st OGB Large-Scale Challenge (OGB-LSC), where we provided large and realistic graph ML tasks. Our KDD Cup attracted huge attention from graph ML community (more than 500 team registrations across the globe, ~150 teams participated), facilitating innovative methods being developed to yield significant performance breakthrough.
However, the problem of machine learning over large graphs is not solved yet, and it is important for the community to engage in a focused multi-year effort in this area (like ImageNet and MS-COCO). 

For the NeurIPS 2022 competition track, we organize the 2nd OGB-LSC (referred to as OGB-LSC 2022) around the OGB-LSC datasets, which will drive forward method development and allow for tracking progress
Importantly, we have updated two out of the three datasets based on the lessons learned from our KDD Cup, so that the resulting datasets are more challenging and realistic.

------------

#### **Overview of OGB-LSC 2022**

We provide three OGB-LSC datasets that are unprecedentedly large in scale and cover prediction at the level of nodes, links, and graphs, respectively. An illustrative overview of the three OGB-LSC datasets is provided below.
<p align = "center">
<img width="90%" src="{{ "/assets/img/ogb-lsc-task-overview2.png" | relative_url }}" class="img-responsive">
</p>
- **[MAG240M](/docs/lsc/mag240m/)** is a heterogeneous academic graph, and the task is to predict the subject areas of papers situated in the heterogeneous graph (node classification). 
- **[WikiKG90Mv2](/docs/lsc/wikikg90mv2/)** is a knowledge graph, and the task is to impute missing triplets (link prediction). 
- **[PCQM4Mv2](/docs/lsc/pcqm4mv2/)** is a quantum chemistry dataset, and the task is to predict an important molecular property, the HOMO-LUMO gap, of a given molecule (graph regression).


There are two kinds of test sets: `test-dev` and `test-challenge`. **For this NeurIPS challenge, please use `test-challenge`.** The `test-dev` is used for the [public leaderboards](/docs/lsc/leaderboards/), where the community can evaluate their model performance throughout the year. We encourage `test-dev` submissions even during the NeurIPS competition, but in order to be qualified for the leaderboards, we require public code and technical report. 
More details can be found [here](/docs/lsc/leaderboards/).

-----------

#### **[Paper](https://arxiv.org/pdf/2103.09430.pdf)**

Details about our datasets and our initial baseline analysis are described in our **[OGB-LSC paper](https://arxiv.org/pdf/2103.09430.pdf)**.
If you use OGB-LSC in your work, please cite our paper (Bibtex below)

```
@article{hu2021ogblsc,
  title={OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs},
  author={Hu, Weihua and Fey, Matthias and Ren, Hongyu and Nakata, Maho and Dong, Yuxiao and Leskovec, Jure},
  journal={arXiv preprint arXiv:2103.09430},
  year={2021}
}
```

--------

#### **OGB-LSC Team and Contact**

The OGB-LSC team can be reached at **<ogb-lsc@cs.stanford.edu>**. 
For discussion or general questions about the datasets, use **[our Github discussion](https://github.com/snap-stanford/ogb/discussions)**.
For questions about our code, use **[our Github issues](https://github.com/snap-stanford/ogb/issues)**. Subscribe to **[our Google group](https://groups.google.com/forum/#!forum/open-graph-benchmark)** to keep yourself updated with any changes and updates from us.

We acknowledge **[Adrijan Bradaschia](https://www.linkedin.com/in/adrijan-bradaschia-7b58ba8a/)** (Stanford) for setting up the server and the test submission page.
We also acknowledge the **[DGL Team](https://www.dgl.ai/)** for helping us host our datasets on AWS, which allows much faster downloading of the datasets.

<table style="background-color:#FDFEFE; border:none;">
  <tr>
    <td>
    <div style="margin: 0 auto; width: 150px; text-align: center">
      <img src="{{ "/assets/img/portrait/weihua.png" | relative_url }}" class="img-responsive">
      <strong><a href="https://weihua916.github.io/">Weihua Hu</a></strong> <br/> Stanford University
      </div>
    </td>
    <td>
    <div style="margin: 0 auto; width: 150px; text-align: center">
      <img src="{{ "/assets/img/portrait/matthias.png" | relative_url }}" class="img-responsive">
      <strong><a href="https://rusty1s.github.io/#/">Matthias Fey</a></strong> <br/> Kumo AI
      </div>
    </td>
    <td>
    <div style="margin: 0 auto; width: 150px; text-align: center">
      <img src="{{ "/assets/img/portrait/hongyu.png" | relative_url }}" class="img-responsive">
      <strong><a href="http://hyren.me/">Hongyu Ren</a></strong> <br/> Stanford University
      </div>
    </td>
    <td>
    <div style="margin: 0 auto; width: 150px; text-align: center">
      <img src="{{ "/assets/img/portrait/maho.png" | relative_url }}" class="img-responsive">
      <strong><a href="http://nakatamaho.riken.jp/">Maho Nakata</a></strong> <br/> RIKEN
      </div>
    </td>
    <td>
    <div style="margin: 0 auto; width: 150px; text-align: center">
      <img src="{{ "/assets/img/portrait/yuxiao.png" | relative_url }}" class="img-responsive">
      <strong><a href="https://keg.cs.tsinghua.edu.cn/yuxiao/">Yuxiao Dong</a></strong> <br/> Tsinghua University
      </div>
    </td>
    <td>
    <div style="margin: 0 auto; width: 150px; text-align: center">
      <img src="{{ "/assets/img/portrait/jure.png" | relative_url }}" class="img-responsive">
      <strong><a href="https://cs.stanford.edu/people/jure/">Jure Leskovec</a></strong> <br/> Stanford University
      </div>
    </td>
  </tr> 
</table>

<!-- #### **Partners**
<table style="background-color:#FDFEFE; border:none;">
  <tr>
    <td>
    <div style="margin: 0 auto; width: 150px; text-align: center">
      <img src="{{ "/assets/img/portrait/amit.png" | relative_url }}" class="img-responsive">
      <strong>Amit Bleiweiss</strong> <br/> Intel
      </div>
    </td>
    <td>
    <div style="margin: 0 auto; width: 150px; text-align: center">
      <img src="{{ "/assets/img/portrait/benjamin.png" | relative_url }}" class="img-responsive">
      <strong>Benjamin Braun</strong> <br/> Intel
      </div>
    </td>
  </tr> 
</table> -->

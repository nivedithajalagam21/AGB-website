---
title: OGB-LSC @ NeurIPS 2022
permalink: /neurips2022/participate/
layout: neurips2022_participate
---

#### **Learn about team registration and test submissions**  
- **All the deadlines are on 11:59pm PDT.** 

<a name="registration"/>

-------

#### **Team registration**: Deadline September 2nd, 2022
##### **[Google form (closed)](https://docs.google.com/forms/d/e/1FAIpQLSe0-xCtMm5fe87WEwFOn9M75Y5vI1Cq73PZ9TURyF4Og1hxuw/viewform)**
**Every team must be registered through the Google form in order to be eligible for the subsequent test submissions.** 
Each team can have at most 10 members. If a group of people wants to work on multiple datasets, they should register a separate team for each dataset. A person cannot be on multiple teams that are competing on the same dataset, but a person can be on multiple teams as long as those teams are competing on different datasets. So in other words, for each email address, please do NOT register more than once per dataset. 
In the Google form, you will need to provide the following information. 

- **Email:** Your own email address that you check daily. **Please avoid using an enterprise email, as it sometimes completely blocks an email from the Google form. Gmail/QQ/academic emails should work.**
- **Dataset:** MAG240M, WikiKG90Mv2, or PCQM4Mv2.
- **Team name:** Try to come up with a unique name!
- **Password:** Come up with a complex password (minimum 10 characters) that cannot be guessed easily. This password will be used to verify that you (not others) are making the test submissions with your email address.
    - **Important: Please do NOT use your personal password as we won't hash it!** 
    - **Note:** This password can be as random as it can be. You will get a response receipt email recording this password, so you do not need to memorize it (as long as you keep the receipt email).
- **Google group subscription**: From each team, we require at least one email address to be subscribed to our **[Google group](https://groups.google.com/g/open-graph-benchmark)**. We will use the group to make any announcements.
- **Team member information:** For each member, we require the following information. Note that you can register at most 10 members per team.
    - Full real name
    - Institution
    - Email address
- **Rules**: Promise to follow the [rules](../rules).
- **Honor code**: I acknowledge that the email address is my own and all the information written here is correct and finalized. Whenever I am asked to prove them, I can immediately respond through the indicated email address. If not, I understand that I will be disqualified from the competition.

**Important: After the registration, you will receive a response receipt email with all the above information on it (in case you didn't get it, please check your spam folder as well). Please keep the receipt email for your subsequent test submissions.**
As you see below, you will need to enter the information you have registered here.

------------

<a name="submit"/>

#### **Test-challenge submission**: Deadline November 1st, 2022
##### **[Submission website (closed)](https://ogb-save.stanford.edu/neurips2022/)**
**Each team makes its own test-challenge submission.**
First, please have your registration receipt email with you.
Then, provide the following information.
You can submit the test files multiple times under the same team, but we will only keep your latest submission. The submission website will automatically close at the deadline; there won’t be any extension.

- **Email:** As registered in the receipt.
- **Dataset:** As registered in the receipt.
- **Team name**: As registered in the receipt.
- **Password**: As registered in the receipt.
- **Package version**: OGB package version used for experiments. Must match the required package for the dataset.
- **Prediction file**: Upload the model's prediction on the **test-challenge set**. **The file must be the one directly saved by the Evaluator---any modification (including filename) is not allowed and disqualifies the submission.**
- **Extra information (irrelevant to winner decision)**:
    - **Validation performance** (if you use our official validation set for model selection).
    - **Training hardware and time**
        - Ex) 24 hours on a GeForce RTX 2080 GPU (11GB memory) and an Intel(R) Xeon(R) Gold 6148 CPUs @ 2.40GHz (512GB memory).
    - **Test inference hardware and time**
        - Ex) 1 hour on a GeForce RTX 2080 GPU (11GB memory) and an Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz (512GB memory).
    - **List of optimized hyper-parameters**
        - Ex) lr: [0.001\*, 0.01], num_layers: [4, 5\*], hidden_channels: [128, 256\*], dropout: [0, 0.5\*], epochs: early-stop\*
        - The asterisks \* denotes the hyper-parameters you eventually selected.
    - **Number of models ensembled**
    - **Number of learnable parameters**
        - In Pytorch, it can be calculated by `sum(p.numel() for p in model.parameters())`. If you use model ensemble, please report the parameter count of **a single model**.
    - **Availability of the pre-trained model**
        - We encourage you to save the best pre-trained model that you use to make the final prediction.

The prediction will be evaluated over the **test-challenge data**. The winners as well as all the submitted performance will be publicly announced.
import pandas as pd 
import numpy as np
import os

nodeprop_dataset_list = ['ogbn-products', 'ogbn-proteins', 'ogbn-arxiv', 'ogbn-papers100M', 'ogbn-mag']
linkprop_dataset_list = ['ogbl-ppa', 'ogbl-collab', 'ogbl-ddi', 'ogbl-citation2', 'ogbl-wikikg2', 'ogbl-biokg', 'ogbl-vessel']
graphprop_mol_dataset_list = ['ogbg-molhiv', 'ogbg-molpcba', 'ogbg-ppa', 'ogbg-code2']
deprecated_dataset_list = ['ogbl-wikikg', 'ogbl-citation', 'ogbg-code']

dataset2metric = {}
dataset2metric['ogbn-products'] = 'Accuracy'
dataset2metric['ogbn-proteins'] = 'ROC-AUC'
dataset2metric['ogbn-arxiv'] = 'Accuracy'
dataset2metric['ogbn-papers100M'] = 'Accuracy'
dataset2metric['ogbn-mag'] = 'Accuracy'
dataset2metric['ogbl-ppa'] = 'Hits@100'
dataset2metric['ogbl-collab'] = 'Hits@50'
dataset2metric['ogbl-ddi'] = 'Hits@20'
dataset2metric['ogbl-citation2'] = 'MRR'
dataset2metric['ogbl-citation'] = 'MRR'
dataset2metric['ogbl-wikikg2'] = 'MRR'
dataset2metric['ogbl-wikikg'] = 'MRR'
dataset2metric['ogbl-biokg'] = 'MRR'
dataset2metric['ogbl-vessel'] = 'ROC-AUC'
dataset2metric['ogbg-molhiv'] = 'ROC-AUC'
dataset2metric['ogbg-molpcba'] = 'AP'
dataset2metric['ogbg-ppa'] = 'Accuracy'
dataset2metric['ogbg-code'] = 'F1 score'
dataset2metric['ogbg-code2'] = 'F1 score'

month_dict = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

def round_float(num):
    return round(num*10000)/10000

def convert_date_to_str(date):
    # '2/8/2020 23:07:08' -> 'Feb 8, 2020'
    temp = date.split(' ')[0]
    splitted = temp.split('/')
    month = month_dict[int(splitted[0])]
    day = int(splitted[1])
    year = int(splitted[2])
    return '{} {}, {}'.format(month, day, year)

def process_submissions(submissions, metric):

    if len(submissions) > 0:
        avg_list = []
        std_list = []
        for submission in submissions:
            splitted = submission['Test Performance'].split(',')
            avg_list.append(round_float(float(splitted[0])))
            std_list.append(round_float(float(splitted[1])))

        avg_list = np.array(avg_list)

        if metric == 'RMSE':
            ## from small to large
            sorted_ind_list = np.argsort(avg_list)
        else:
            ## from large to small
            sorted_ind_list = np.argsort(-avg_list)
            
        header = '| Rank  | Method | Ext. data | Test {} | Validation {} | Contact | References | #Params | Hardware | Date \n'.format(metric, metric)
        header += '|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|\n'

        current_ranking = 1

        for i, ind in enumerate(sorted_ind_list):
            submission = submissions[ind]
            if submission['Official'] == 'Official':
                header += '|  {}  |  **{}**  | {} | {:.4f} ± {:.4f}   | {} |[{}](mailto:{}) | [Paper]({}), [Code]({}) | {} | {} | {} |\n'.\
                            format(current_ranking, submission['Method'], submission['External data'], avg_list[ind], std_list[ind], submission['Validation Performance'], submission['Primary contact person'],
                                submission['Primary contact email'], submission['Paper'], submission['Code'], submission['#Params'], submission['Hardware'], convert_date_to_str(submission['Timestamp']))
            else:
                header += '|  {}  |  {}  | {} | {:.4f} ± {:.4f}   | {} | [{}](mailto:{}) | [Paper]({}), [Code]({}) | {} | {} | {} |\n'.\
                            format(current_ranking, submission['Method'], submission['External data'], avg_list[ind], std_list[ind], submission['Validation Performance'], submission['Primary contact person'],
                                submission['Primary contact email'], submission['Paper'], submission['Code'], submission['#Params'], submission['Hardware'], convert_date_to_str(submission['Timestamp']))
            
            if i < len(sorted_ind_list) - 1 and avg_list[ind] != avg_list[sorted_ind_list[i+1]]:
                current_ranking += 1
    else:
        header = '| Rank  | Method | Test {} | Validation {} | Contact | References | #Params | Hardware | Date \n'.format(metric, metric)

    return header

def insert_leaderboard(source_file, dest_file, leaderboard_dict):
    PATH = '_docs/leaderboard'
    with open(os.path.join(PATH, source_file), 'r') as f:
        source = f.read().split('\n')

    dest = []
    for line in source:
        ### line = '#ogbg-mol-cls'
        ### line[1:] = 'ogbg-mol-cls'
        if line[1:] in leaderboard_dict:
            dest.append(leaderboard_dict[line[1:]])
        else:
            dest.append(line)

    with open(os.path.join(PATH, dest_file), 'w') as f:
        f.write('\n'.join(dest))


if __name__ == '__main__':
    url = 'https://docs.google.com/spreadsheets/d/1m9NWfmzxNqoNhX46LGbFLk7NPHWrBSVa73WKP4ObpTQ/export?format=csv&gid=516823038'
    df = pd.read_csv(url)

    dataset2submissions = {dataset: [] for dataset in dataset2metric.keys()}

    for index, submission in df.iterrows():
        ### only consider the approved entry

        if submission['Approved'] == 'Y':
            # get dataset name
            dataset = submission['Dataset']
            # print(submission)

            ### Request additional information
            if np.isnan(submission['#Params']):
                submission['#Params'] = '[Please tell us](mailto:ogb@cs.stanford.edu)'
            else:
                submission['#Params'] = '{:,}'.format(int(submission['#Params']))
            try:
                if np.isnan(submission['Hardware']):
                    submission['Hardware'] = '[Please tell us](mailto:ogb@cs.stanford.edu)'
            except:
                pass

            if not isinstance(submission['Validation Performance'], str):
                submission['Validation Performance'] = '[Please tell us](mailto:ogb@cs.stanford.edu)'
            else:
                splitted = submission['Validation Performance'].split(',')
                submission['Validation Performance'] = '{:.4f} ± {:.4f}'.format(round_float(float(splitted[0])),round_float(float(splitted[1])))
                
            if submission['External data'] != 'Yes':
                submission['External data'] = 'No'

            dataset2submissions[dataset].append(submission)

    dataset2leaderboard = {}

    for dataset, submissions in dataset2submissions.items():
        # converting a list of submissions to a leaderboard
        dataset2leaderboard[dataset] = process_submissions(submissions, metric = dataset2metric[dataset])


    insert_leaderboard('_leader_graphprop_scaf.md', 'leader_graphprop.md', dataset2leaderboard)
    insert_leaderboard('_leader_nodeprop_scaf.md', 'leader_nodeprop.md', dataset2leaderboard)
    insert_leaderboard('_leader_linkprop_scaf.md', 'leader_linkprop.md', dataset2leaderboard)
    insert_leaderboard('_leader_deprecated_scaf.md', 'leader_deprecated.md', dataset2leaderboard)


    ### make leaderboards for graph property prediction. Currently, we only have molecule data.
    # graph_leaderboard_dict = get_default_leaderboard(graphprop_valid_submission_list)


    # insert_leaderboard('_leader_graphprop_scaf.md', 'leader_graphprop.md', graph_leaderboard_dict)

    # ### make leaderboards for node property prediction
    # node_leaderboard_dict = dict()
    # for dataset in nodeprop_dataset_list:
    #     leaderboard = get_default_leaderboard(dataset, nodeprop_valid_submission_list, dataset2metric[dataset])
    #     node_leaderboard_dict[dataset] = leaderboard

    # insert_leaderboard('_leader_nodeprop_scaf.md', 'leader_nodeprop.md', node_leaderboard_dict)

    # ### make leaderboards for link property prediction
    # link_leaderboard_dict = dict()
    # for dataset in linkprop_dataset_list:
    #     leaderboard = get_default_leaderboard(dataset, linkprop_valid_submission_list, dataset2metric[dataset])
    #     link_leaderboard_dict[dataset] = leaderboard

    # insert_leaderboard('_leader_linkprop_scaf.md', 'leader_linkprop.md', link_leaderboard_dict)



import pandas as pd 
import numpy as np
import math
import os

lsc_dataset_list = ['MAG240M', 'WikiKG90Mv2', 'PCQM4Mv2']

dataset2metric = {}
dataset2metric['MAG240M'] = 'Accuracy'
dataset2metric['WikiKG90Mv2'] = 'MRR'
dataset2metric['PCQM4Mv2'] = 'MAE'

month_dict = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

def round_float(num):
    return round(num*10000)/10000

def convert_date_to_str(date):
    # '9/8/2021' -> 'Sep 8, 2021'
    splitted = date.split('/')
    month = month_dict[int(splitted[0])]
    day = int(splitted[1])
    year = int(splitted[2])
    return '{} {}, {}'.format(month, day, year)

def process_submissions(submissions, metric):

    if len(submissions) > 0:
        perf_list = []
        for submission in submissions:
            perf_list.append(round_float(float(submission['test_performance'])))

        perf_list = np.array(perf_list)

        if metric == 'MAE':
            ## from small to large
            sorted_ind_list = np.argsort(perf_list)
        else:
            ## from large to small
            sorted_ind_list = np.argsort(-perf_list)
            
        header = '| Rank  | Method | Ensemble | Test-dev {} | Validation {} | Team | Contact | References | #Params | Hardware | Date \n'.format(metric, metric)
        header += '|:----:|:-----:|:------:|:-----:|:-----:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|\n'

        current_ranking = 1

        for i, ind in enumerate(sorted_ind_list):
            submission = submissions[ind]
            if submission['val_performance'] == 'N/A':
                header += '|  {}  |  **{}**  | {} | {:.4f}  | {} | {} | [{}](mailto:{}) ({}) | [Paper]({}), [Code]({}) | {} | {} | {} |\n'.\
                            format(current_ranking, submission['method'], submission['ensemble'], perf_list[ind], submission['val_performance'], submission['team'], submission['contact_name'],
                                submission['contact_email'], submission['affiliations'], submission['paper'], submission['code'], submission['params'], submission['hardware_gputpu'], convert_date_to_str(submission['time']))
            else:
                header += '|  {}  |  **{}**  | {} | {:.4f}  | {:.4f} | {} | [{}](mailto:{}) ({}) | [Paper]({}), [Code]({}) | {} | {} | {} |\n'.\
                            format(current_ranking, submission['method'], submission['ensemble'], perf_list[ind], submission['val_performance'], submission['team'], submission['contact_name'],
                                submission['contact_email'], submission['affiliations'], submission['paper'], submission['code'], submission['params'], submission['hardware_gputpu'], convert_date_to_str(submission['time']))
                        
            if i < len(sorted_ind_list) - 1 and perf_list[ind] != perf_list[sorted_ind_list[i+1]]:
                current_ranking += 1
    else:
        header = '| Rank  | Method | Ensemble | Test-dev {} | Validation {} | Team | Contact | References | #Params | Hardware | Date \n'.format(metric, metric)

    return header

def insert_leaderboard(source_file, dest_file, leaderboard_dict):
    PATH = '_docs/lsc'
    with open(os.path.join(PATH, source_file), 'r') as f:
        source = f.read().split('\n')

    dest = []
    for line in source:
        if line[1:] in leaderboard_dict:
            dest.append(leaderboard_dict[line[1:]])
        else:
            dest.append(line)

    with open(os.path.join(PATH, dest_file), 'w') as f:
        f.write('\n'.join(dest))


if __name__ == '__main__':
    df = pd.read_csv('test-dev_master.csv')

    dataset2submissions = {dataset: [] for dataset in dataset2metric.keys()}

    for index, submission in df.iterrows():
        ### only consider the approved entry

        if submission['approved'] == 'Yes':
            for key in submission.keys():
                try:
                    if math.isnan(submission[key]):
                        submission[key] = 'N/A'
                except:
                    pass
            
            # get dataset name
            dataset = submission['dataset']
            try:
                submission['params'] = '{:,}'.format(int(submission['params']))
            except:
                submission['params'] = 'N/A'
    
            
            dataset2submissions[dataset].append(submission)

    dataset2leaderboard = {}

    for dataset, submissions in dataset2submissions.items():
        # converting a list of submissions to a leaderboard
        dataset2leaderboard[dataset] = process_submissions(submissions, metric = dataset2metric[dataset])

    insert_leaderboard('_leaderboards_scaf.md', 'leaderboards.md', dataset2leaderboard)




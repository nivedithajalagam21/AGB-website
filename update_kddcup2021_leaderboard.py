import numpy as np
import os
from ogb.lsc import WikiKG90MEvaluator

wikikg_evaluator = WikiKG90MEvaluator()

init_dir = 'lsc_submission/initial/'
final_dir = 'lsc_submission/final/'
test_label_dir = '/dfs/scratch1/weihuahu/ogb-lsc/testset'
dataset_list = ['mag240m', 'wikikg90m', 'pcqm4m']
dataset_mapping = {'mag240m': 'MAG240M-LSC', 'wikikg90m': 'WikiKG90M-LSC', 'pcqm4m': 'PCQM4M-LSC'}
filename_mapping = {'mag240m': 'y_pred_mag240m.npz', 'wikikg90m': 't_pred_wikikg90m.npz', 'pcqm4m': 'y_pred_pcqm4m.npz'}
test_filename_mapping = {'mag240m': 'node_label_test.npy', 'wikikg90m': 'test_t_correct_index.npy', 'pcqm4m': 'homolumogap_test.npy'}
metric_mapping = {'mag240m': 'Accuracy', 'wikikg90m': 'MRR', 'pcqm4m': 'MAE'}

np.random.seed(42)
mag240m_len = 146818
mag240m_subset_idx = np.random.permutation(mag240m_len)[:int(0.05*mag240m_len)]
wikikg90m_len = 1359303
wikikg90m_subset_idx = np.random.permutation(wikikg90m_len)[:int(0.05*wikikg90m_len)]
pcqm4m_len = 377423
pcqm4m_subset_idx = np.random.permutation(pcqm4m_len)[:int(0.05*pcqm4m_len)]

def eval_mag240m(pred_filename, y_true, eval_subset = False):
    try:
        y_pred = np.load(pred_filename)['y_pred']
    except e:
        # print(pred_filename)
        # print(e)
        return 0
    if eval_subset:
        return (y_true[mag240m_subset_idx] == y_pred[mag240m_subset_idx]).sum() / y_true[mag240m_subset_idx].shape[0]
    else:
        return (y_true == y_pred).sum() / y_true.shape[0]

def eval_wikikg90m(pred_filename, test_t_correct_index, eval_subset = False):
    try:
        pred = np.load(pred_filename)['t_pred_top10']
    except:
        # print(pred_filename)
        # print(e)
        return 0
    if eval_subset:
        pred_dict = {'h,r->t': {'t_pred_top10': pred[wikikg90m_subset_idx], 't_correct_index': test_t_correct_index[wikikg90m_subset_idx]}}
    else:
        pred_dict = {'h,r->t': {'t_pred_top10': pred, 't_correct_index': test_t_correct_index}}
    metrics = wikikg_evaluator.eval(pred_dict)
    return metrics['mrr']

def eval_pcqm4m(pred_filename, y_true, eval_subset = False):
    try:
        y_pred = np.load(pred_filename)['y_pred']
    except e:
        # print(pred_filename)
        # print(e)
        return 12345
    if eval_subset:
        return np.average(np.absolute(y_true[pcqm4m_subset_idx] - y_pred[pcqm4m_subset_idx]))
    else:
        return np.average(np.absolute(y_true - y_pred))

def eval_wrapper(dataset, pred_filename, label_true, eval_subset = False):
    if dataset == 'mag240m':
        return eval_mag240m(pred_filename, label_true, eval_subset)
    elif dataset == 'wikikg90m':
        return eval_wikikg90m(pred_filename, label_true, eval_subset)
    elif dataset == 'pcqm4m':
        return eval_pcqm4m(pred_filename, label_true, eval_subset)

def get_info(dataset, stage = 'init'):
    # get performance, team name and email address
    dir = init_dir if stage == 'init' else final_dir
    eval_subset = True if stage == 'init' else False
    label_true = np.load(os.path.join(test_label_dir, dataset, test_filename_mapping[dataset]))

    perf_list = []
    team_list = []
    email_list = []

    for folder in os.listdir(os.path.join(dir, dataset_mapping[dataset])):
        if '@' not in folder:
            continue
        pred_filename = os.path.join(dir, dataset_mapping[dataset], folder, filename_mapping[dataset])
        info_filename = os.path.join(dir, dataset_mapping[dataset], folder, 'info.txt')
        with open(info_filename, 'r') as f:
            for line in f.read().split('\n'):
                if 'Team name:' in line:
                    team_name = line[11:]
        perf = eval_wrapper(dataset, pred_filename, label_true, eval_subset)

        perf_list.append(perf)
        team_list.append(team_name)
        email_list.append(folder)

    return perf_list, team_list, email_list

def process_submissions(perf_list, team_list, dataset, stage):
    
    if len(perf_list) > 0:
        perf_list = np.array(perf_list)
        metric = metric_mapping[dataset]
        if metric == 'MAE':
            ## from small to large
            sorted_ind_list = np.argsort(perf_list)
        else:
            ## from large to small
            sorted_ind_list = np.argsort(-perf_list)
            
        if stage == 'init':
            header = f'| Rank  | Team | Test {metric} (subset) \n'
        else:
            header = f'| Rank  | Team | Test {metric} \n'
        header += '|:----:|:-----:|:------:|\n'

        current_ranking = 1

        for i, ind in enumerate(sorted_ind_list):
            perf = float(perf_list[ind])
            team = team_list[ind]
            if perf == 0 or perf == 12345:
                header += '|  {}  |  {}  | Invalid  |\n'.format(current_ranking, team, perf)
            else:
                header += '|  {}  |  {}  | {:.4f}  |\n'.format(current_ranking, team, perf)  

            if i < len(sorted_ind_list) - 1 and perf_list[ind] != perf_list[sorted_ind_list[i+1]]:
                current_ranking += 1
    else:
        if stage == 'init':
                header = f'| Rank  | Team | Test {metric} (subset) \n'
        else:
            header = f'| Rank  | Team | Test {metric} \n'

    return header


def main(dir, coming_soon_initial = False, coming_soon_final = True):

    ### create leaderboard_dict
    ### initial
    leaderboard_dict = {}
    for dataset in dataset_list:
        print()
        print(dataset)
        key = f'initial_{dataset}'
        if coming_soon_initial:
            leaderboard_dict[key] = '##### Coming soon...'
        else:
            perf_list, team_list, email_list = get_info(dataset, stage = 'init')
            header = process_submissions(perf_list, team_list, dataset, stage = 'init')
            leaderboard_dict[key] = header
    
    for dataset in dataset_list:
        key = f'final_{dataset}'
        if coming_soon_final:
            leaderboard_dict[key] = '##### Coming soon...'
        else:
            perf_list, team_list, email_list = get_info(dataset, stage = 'final')
            header = process_submissions(perf_list, team_list, dataset, stage = 'final')
            leaderboard_dict[key] = header

    # source scaffold file
    with open('_docs/kddcup2021/_leaderboard.md', 'r') as f:
        source = f.read().split('\n')

    dest = []
    for line in source:
        if line[1:] in leaderboard_dict:
            dest.append(leaderboard_dict[line[1:]])
        else:
            dest.append(line)

    # destination file
    with open('_docs/kddcup2021/results.md', 'w') as f:
        f.write('\n'.join(dest))


if __name__ == '__main__':
    # first copy from the public submission
    # scp -r weihuahu@ogb-save:/opt/ogb-lsc/data/initial lsc_submission/
    main(dir)
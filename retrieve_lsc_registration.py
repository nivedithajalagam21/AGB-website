import pandas as pd
import numpy as np

url = 'https://docs.google.com/spreadsheets/d/1JEPvB62RJ1w15b4VAclWQcyNSOjrPVmBW68EyYT0Q00/export?format=csv&gid=1188631267'
df = pd.read_csv(url)

winning_teams_dict = {}
winning_teams_dict['MAG240M-LSC'] = ['BD-PGL', 'Academic', 'Synerise AI', 'Topology_mag', 'passages', 'DeeperBiggerBetter']
winning_teams_dict['WikiKG90M-LSC'] = ['BD-PGL', 'OhMyGod', 'GraphMIRAcles', 'littleant', 'vcdbro', 'JohnZheng']
winning_teams_dict['PCQM4M-LSC'] = ['MachineLearning', 'SuperHelix', 'Quantum', 'DIVE@TAMU', 'no_free_lunch', 'GNNLearner']

dataset_list = ['MAG240M-LSC', 'WikiKG90M-LSC', 'PCQM4M-LSC']

for dataset in dataset_list:
    print('=======', dataset)
    for team in winning_teams_dict[dataset]:
        print(team)
        tf = np.logical_and(df['Dataset'] == dataset, df['Team name'] == team)
        tf = np.logical_and(df['Ignore'] != df['Ignore'], tf)
        idx = tf.to_numpy().nonzero()[0]
        assert len(idx) == 1
        idx = idx[0]

        contact = df['Email Address'][idx]
        name_list = []
        
        for i in range(1, 11):
            info = df[f'Team member ({i})'][idx]
            if info != info:
                break
            name = info.split(',')[0]
            aff = info.split(',')[1]
            name_list.append(f'{name} ({aff})')

        print('Contact: ', contact)
        print(', '.join(name_list))
        print('')
            
        

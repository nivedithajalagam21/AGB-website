import os
import pandas as pd

def extract_date(raw):
    # 2021-09-08 23:11:44 --> 2021/09/08
    return raw.split(' ')[0].replace('-', '/')
    

def main():
    # Retrieve from the server
    os.system('scp weihuahu@ogb-save.stanford.edu:/opt/ogb-leaderboard/leaderboard_sample/test-dev_leaderboard.csv .')

    # Merge test-dev_leaderboard.csv into test-dev_master.csv
    leaderboard_df = pd.read_csv('test-dev_leaderboard.csv', index_col = 'unique_identifier')
    leaderboard_df['time'] = leaderboard_df['time'].map(extract_date)

    merged_df = pd.read_csv('test-dev_master.csv')

    print(leaderboard_df)
    print(merged_df)

    leaderboard_entry = leaderboard_df.index.tolist()
    existing_entry = merged_df['unique_identifier'].tolist()

    new_entry = sorted(list(set(leaderboard_entry) - set(existing_entry)))
    # new_entry = leaderboard_entry
    print('New entries added: ', new_entry)

    new_entry_df = leaderboard_df.loc[new_entry]
    # print(leaderboard_df)
    # print(new_entry)
    # new_entry_df['unique_identifier'] = new_entry_df.index
    new_entry_df.reset_index(level = 0, inplace=True)
    
    updated_df = pd.concat([merged_df, new_entry_df])
    updated_df.to_csv('test-dev_master.csv', index = None)



if __name__ == '__main__':
    main()

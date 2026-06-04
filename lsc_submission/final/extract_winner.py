from ogb.lsc import MAG240MEvaluator
import numpy as np
import os


email_list = [
    'shiyunsheng01@baidu.com',
    'jacklynnstott@google.com',
    'jack.dabrowski@synerise.com',
    'caowencai@oppo.com',
    'tsotfsk@bupt.edu.cn',
    'guohao.li@kaust.edu.sa',
]


evaluator = MAG240MEvaluator()

for email in email_list:
    res = np.load(os.path.join('MAG240M-LSC', email, 'y_pred_mag240m.npz'))['y_pred']
    num_test = len(res)
    idx = np.arange(num_test)
    dev_idx = np.nonzero(idx % 5 < 3)[0]
    
    res_testdev = res[dev_idx]
    
    evaluator.save_test_submission(
        input_dict = {
        'y_pred': res_testdev, 
        },
        dir_path = os.path.join('MAG240M-testdev', email),
        mode = 'test-dev'
    )
    
    
    


#!usr/bin/python
#coding=utf-8

# importing the basic library
from __future__ import print_function
import sys, os

sys.path.append(os.path.abspath(''))   # 把当前目录设为引用模块的地址之一

from utils import *
from data_utils import *
# from models.solver_cnn import *
from models.solver_cnn_ import *
from models.ConvNet import *

import numpy as np
import pandas as pd
from itertools import product, permutations

import matplotlib.pyplot as plt
print()
test_ctx()
print()


### Load Data ####
GW_address = '/floyd/input/waveform/'
# GW_address = './data/'

data = pd.DataFrame(np.load(GW_address+'GW_H1.npy'), index=np.load(GW_address+'GW_H1_index.npy'))
print('Raw data: ', data.shape)
peak_samppoint = data.values.argmax(axis=1)
peak_samppoint = int(peak_samppoint.sum() / peak_samppoint.shape[0])
peak_time = peak_samppoint/data.shape[-1]
peak_time = float('{:.2f}'.format(peak_time))
print('Peak sampling point at %dth (%.2fs).' %(peak_samppoint, peak_time))
print()

### Split the Data
print('总波形数目：', data.index.shape)
train_masses = [(float(masses.split('|')[0]), float(masses.split('|')[1])) for masses in data.index if float(masses.split('|')[0]) % 2 != 0]
test_masses = [(float(masses.split('|')[0]), float(masses.split('|')[1])) for masses in data.index if float(masses.split('|')[0]) % 2 == 0]
print('训练集波形数目：', len(train_masses))
print('测试集波形数目：', len(test_masses))
print()

# 做好训练集和测试集的分割~
test_masses = [masses for masses in data.index if float(masses.split('|')[0]) % 2 == 0]
train_masses = [masses for masses in data.index if float(masses.split('|')[0]) % 2 != 0]
train_data = nd.array(data.loc[train_masses], ctx=mx.cpu())
test_data = nd.array(data.loc[test_masses], ctx=mx.cpu())

b = nd.array(pre_fir().reshape((-1,1)), ctx=ctx)

mx.random.seed(1)  # fix the random seed
stacking_size = 256
rand_times = 5
num_noise = stacking_size * rand_times * 2 +2
pp = pre_fftfilt(b, shape = (num_noise, train_data.shape[-1]), nfft=None)
localnoise = GenNoise_matlab_nd(shape = (num_noise, train_data.shape[-1]), params = pp)


## Training
params_tl  = None
# for snr in list([1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]):
# params_tl  = nd.load('/floyd/input/pretrained/PRL/snr_8_best_params_epoch@26.pkl')
# params_tl  = nd.load('/floyd/input/pretrained/PRL/snr_5_best_params_epoch@22.pkl')
# params_tl  = nd.load('/floyd/input/pretrained/pretrained_models/PRL/snr_10_best_params_epoch@31.pkl')

SNR_list = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
# SNR_list = (np.array([0.01]+np.arange(0.05,1.04,0.05).tolist()))[::-1]
i = 0
while True:
    try:
        snr = SNR_list[i]
    except IndexError:
        break

    PRL = ConvNet(conv_params = {'kernel': ((1,64), (1,32), (1,32), (1,16),(1,16),(1,16)), 
                                'num_filter': (8, 8, 16, 16, 32, 32),
                                'stride': ((1,1), (1,1), (1,1),(1,1),(1,1),(1,1),),
                                'padding': ((0,0), (0,0), (0,0),(0,0),(0,0),(0,0),),
                                'dilate': ((1,1), (1,1), (1,1),(1,1),(1,1),(1,1),)},
                    act_params = {'act_type': ('elu', 'elu', 'elu', 'elu','elu','elu','elu','elu')},
                    pool_params = {'pool_type': ('max', 'max', 'max','max','max','max',),
                                'kernel': ((1,1), (1,8), (1,1),(1,6),(1,1),(1,4)),
                                'stride': ((1,2), (1,2), (1,2),(1,2),(1,2),(1,2)),
                                'padding': ((0,0),(0,0), (0,0), (0,0),(0,0),(0,0)),
                                'dilate': ((1,1), (1,1), (1,1),(1,1),(1,1),(1,1))},
                    fc_params = {'hidden_dim': (64,64)}, drop_prob = 0.5, 
#                         input_dim = (2,1,8192)
                    input_dim = (1,1,8192)
                        )

    Solver = Solver_nd(model = PRL, 
                    train = train_data,
                    test = test_data,
                    SNR = snr,   params = params_tl,
                    num_epoch=30, rand_times = rand_times,
                    batch_size = 256, stacking_size = stacking_size,
                    lr_rate=0.0001, localnoise = localnoise
                    ,save_checkpoints_address = './pretrained_models/PRL/'
                    ,checkpoint_name = 'snr_%s' %int(snr*100),floydhub_verbose =True, )
    try:
        Solver.Training()
    except mx.MXNetError as e:
        print(e)
        print('Rerunning...')
        continue

    params_tl = Solver.best_params
    i += 1


# floyd run --gpu \
# --data wctttty/datasets/gw_waveform/1:waveform \
# -m "PRL_old" \
# "bash setup_floydhub.sh && python run_PRL.py"
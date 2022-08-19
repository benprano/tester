# -*- coding: utf-8 -*-
"""TEST .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wxcpYMRUihi6UbWpVtO1C1c1ZmFpoA5e
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
# creating a DataFrame
from matplotlib.axes._axes import _log as matplotlib_axes_logger
matplotlib_axes_logger.setLevel('ERROR')
import math
import re
import itertools  
from tabulate import tabulate
import datetime
from collections import namedtuple
from tqdm import tqdm
from itertools import groupby
from operator import itemgetter
from functools import partial
from itertools import combinations
#define a function to fit the model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
# %matplotlib inline
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('pdf')
import matplotlib.patches as patches
from collections import defaultdict
from collections import Counter
import seaborn as sns
from time import perf_counter
from IPython.display import HTML
from matplotlib import animation
import plotly.graph_objects as go
import plotly.express as px
from itertools import cycle
import plotly
import gzip
import numpy as np
import pandas as pd
import multiprocessing as mp
import seaborn as sns
sns.set()
from tqdm import tqdm
import datetime
import datetime as dt
from scipy.stats import mstats
sns.set(rc={'figure.figsize':(18,10)})
from matplotlib.ticker import PercentFormatter
import matplotlib.ticker as mticker
from csv import DictWriter
import warnings
warnings.filterwarnings('ignore')
import io, os, sys, types
from IPython import get_ipython
from nbformat import current
from IPython.core.interactiveshell import InteractiveShell
from IPython.core.display import display, HTML
from functools import reduce
from scipy.interpolate import griddata
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import plotly.graph_objects as go
from scipy import stats
from datetime import datetime
from scipy.stats import norm, skew #for some statistics
import pickle
def ignore_warn(*args, **kwargs):
    pass
warnings.warn = ignore_warn #ignore annoying warning from sklearn and seaborn

# %matplotlib inline
plt.style.use('seaborn')
from sklearn.model_selection import TimeSeriesSplit
from sklearn.model_selection import StratifiedKFold, train_test_split
from keras.models import Model
from numpy import array
from numpy import hstack
from keras.models import Sequential
from keras.layers import LSTM, GRU, Bidirectional, Masking,  Layer
from keras.layers import RepeatVector, Concatenate, concatenate, Lambda
from keras.layers import TimeDistributed, Flatten
from keras.layers import Input
from keras.layers.core import Dense
from keras import models, layers, optimizers, regularizers
from sklearn import model_selection, preprocessing
import tensorflow as tf
from tqdm import tqdm
import matplotlib.pyplot as plt
from keras.layers.core import Dense, Dropout, Flatten, Activation
from keras.layers import BatchNormalization
from keras.layers import multiply , Reshape, Lambda, RepeatVector

#from keras.layers.recurrent import LSTM, GRU 
from keras.models import model_from_json, Sequential
from tensorflow.keras.optimizers import RMSprop
from sklearn.model_selection import StratifiedKFold
import theano
from keras import initializers as initializers, regularizers, constraints
from keras.callbacks import CSVLogger
#from keras.utils.vis_utils import plot_model
from keras.callbacks import EarlyStopping,ModelCheckpoint
import seaborn as sns
from keras.models import load_model
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import precision_recall_curve ,roc_auc_score, roc_curve, average_precision_score,auc, recall_score,precision_score
from collections import Counter
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
sys.path.append("..\..")
sns.set()
import os
import warnings
import sys
warnings.filterwarnings("ignore")
import random as rn
from keras import backend as K
import keras
#from tensorflow.keras.callbacks import Callback
from sklearn.metrics import precision_recall_curve
from keras.callbacks import Callback
from keras.callbacks import CSVLogger
from string import ascii_uppercase
from random import choice
random_str = ''.join(choice(ascii_uppercase) for i in range(12))
#session_conf = tf.compat.v1.ConfigProto(intra_op_parallelism_threads=num_cores,
#                                      inter_op_parallelism_threads=num_cores, 
#                                      allow_soft_placement=True,
#                                      device_count = {'CPU' : num_CPU, 'GPU' : num_GPU})

#sess = tf.compat.v1.Session(graph=tf.compat.v1.get_default_graph(), config=session_conf)
#K.set_session(sess)

config =  tf.compat.v1.ConfigProto( device_count = {'GPU': 0 , 'CPU': 4} ) 
config.gpu_options.allow_growth = True
sess = tf.compat.v1.Session(config=config) 
keras.backend.set_session(sess)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
# Remise à zéro des états du modèle
from timeit import default_timer as timer
#tf.keras.backend.clear_session()

print(tf.__version__)
import distutils
if distutils.version.LooseVersion(tf.__version__) < '1.14':
    raise Exception('This notebook is compatible with TensorFlow 1.14 or higher, for TensorFlow 1.13 or lower please use the previous version at https://github.com/tensorflow/tpu/blob/r1.13/tools/colab/classification_iris_data_with_keras.ipynb')

# It is the official metric used in this competition
# below is the declaration of a function used inside the keras model, calculation with K (keras backend / thensorflow)
def matthews_correlation(y_true, y_pred):
    '''Calculates the Matthews correlation coefficient measure for quality
    of binary classification problems.
    '''
    y_pred_pos = K.round(K.clip(y_pred, 0, 1))
    y_pred_neg = 1 - y_pred_pos

    y_pos = K.round(K.clip(y_true, 0, 1))
    y_neg = 1 - y_pos

    tp = K.sum(y_pos * y_pred_pos)
    tn = K.sum(y_neg * y_pred_neg)

    fp = K.sum(y_neg * y_pred_pos)
    fn = K.sum(y_pos * y_pred_neg)

    numerator = (tp * tn - fp * fn)
    denominator = K.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))

    return numerator / (denominator + K.epsilon())

def attention_3d_block(inputs, name):
    # inputs.shape = (batch_size, time_steps, input_dim)
    TIME_STEPS = inputs.shape[1]
    SINGLE_ATTENTION_VECTOR = False
    
    input_dim = int(inputs.shape[2])
    a = tf.keras.layers.Permute((2, 1))(inputs)
    a = tf.keras.layers.Reshape((input_dim, TIME_STEPS))(a) # this line is not useful. It's just to know which dimension is what.
    a = tf.keras.layers.Dense(TIME_STEPS, activation='softmax')(a)
    if SINGLE_ATTENTION_VECTOR:
        a = tf.keras.layers.Lambda(lambda x: K.mean(x, axis=1))(a)
        a = tf.keras.layers.RepeatVector(input_dim)(a)
    a_probs = tf.keras.layers.Permute((2, 1), name=name)(a)
    output_attention_mul = tf.keras.layers.Multiply()([inputs, a_probs])
    return output_attention_mul

def channel_attention_module(x, ratio=8):
    batch, _, _, channel = x.shape

    ## Shared layers
    l1 = tf.keras.layers.Dense(channel//ratio, activation="relu", use_bias=False)
    l2 = tf.keras.layers.Dense(channel, use_bias=False)

    ## Global Average Pooling
    x1 = tf.keras.layers.GlobalAveragePooling2D()(x)
    x1 = l1(x1)
    x1 = l2(x1)

    ## Global Max Pooling
    x2 = tf.keras.layers.GlobalMaxPooling2D()(x)
    x2 = l1(x2)
    x2 = l2(x2)

    ## Add both the features and pass through sigmoid
    feats = x1 + x2
    feats = tf.keras.layers.Activation("sigmoid")(feats)
    feats = tf.keras.layers.Multiply()([x, feats])

    return feats

def spatial_attention_module(x):
    ## Average Pooling
    x1 = tf.reduce_mean(x, axis=-1)
    x1 = tf.expand_dims(x1, axis=-1)

    ## Max Pooling
    x2 = tf.reduce_max(x, axis=-1)
    x2 = tf.expand_dims(x2, axis=-1)

    ## Concatenat both the features
    feats = tf.keras.layers.Concatenate()([x1, x2])
    ## Conv layer
    feats = tf.keras.layers.Conv2D(1, kernel_size=7, padding="same", activation="sigmoid")(feats)
    feats = tf.keras.layers.Multiply()([x, feats])

    return feats

def cbam(x):
    x = channel_attention_module(x)
    x = spatial_attention_module(x)
    return x

def benchmarking_models(recur_input, ffn_in, gru_dim_mask=False,concat_vect = False, lstm_dim=256, appl_mask_layer=False):

    input_ffn = tf.keras.layers.Input(shape=ffn_in, name="ffn_input")
    x_ffn = tf.keras.layers.BatchNormalization()(input_ffn)
    x_ffn = tf.keras.layers.Dense(lstm_dim//2, activation="sigmoid")(x_ffn)
    x_ffn = tf.keras.layers.Dropout(0.2 ,name="ffn_dropout_1")(x_ffn)
    x_ffn = tf.keras.layers.Dense(lstm_dim//4, activation="sigmoid")(x_ffn)
    x_ffn = tf.keras.layers.Dropout(0.2 ,name="ffn_dropout_2")(x_ffn)
    
    
        
    inp_gru = tf.keras.layers.Input(shape=recur_input, name="input_shape_gru")
    if appl_mask_layer:
      x_gru = tf.keras.layers.Masking(mask_value=0, input_shape=recur_input, name="masking_layer")(inp_gru)
    else:
      x_gru = inp_gru
    g =  channel_attention_module(x_gru, ratio=8)
    z =  spatial_attention_module(x_gru)
    att = cbam(x_gru)
    print("channel_attention_module", g.shape)
    print("spatial_attention_module", z.shape)
    x_gru = tf.keras.layers.BatchNormalization()(att)
    x_gru = tf.keras.layers.TimeDistributed(tf.keras.layers.Bidirectional(LSTM(lstm_dim, 
                                                                          input_shape=recur_input, 
                                                                          return_sequences=True, 
                                                                          kernel_regularizer=tf.keras.regularizers.l2(0.001)), 
                                                                          name="gru_layer_1"))(x_gru)
    x_gru = tf.keras.layers.BatchNormalization()(x_gru)
    x_gru = tf.keras.layers.TimeDistributed(tf.keras.layers.Bidirectional(LSTM(lstm_dim, 
                                                                          input_shape=recur_input, 
                                                                          return_sequences=False, 
                                                                          kernel_regularizer=tf.keras.regularizers.l2(0.001)), 
                                                                          name="gru_layer_2"))(x_gru)
    #x_gru = tf.keras.layers.TimeDistributed(Flatten(), name="flatten_layer_1")(x_gru)
    if gru_dim_mask:
        gru_mask_input =tf.keras.layers.Input(shape=gru_dim_mask, name="LSTM_INPUT_MASK")
        #x_gru_mask   = attention_block(gru_mask_input, "attention_vec_mask_vector")
        x_gru_mask   = tf.keras.layers.TimeDistributed(tf.keras.layers.Bidirectional(LSTM(lstm_dim, 
                                                                                     return_sequences=True, 
                                                                                     kernel_regularizer=tf.keras.regularizers.l2(0.001)), 
                                                                                      name="LSTM_MASK"))(gru_mask_input)
        x_gru_mask = tf.keras.layers.TimeDistributed(tf.keras.layers.Bidirectional(LSTM(lstm_dim, 
                                                                                   input_shape=gru_dim_mask, 
                                                                                   return_sequences=False,
                                                                                   kernel_regularizer=tf.keras.regularizers.l2(0.001)),
                                                                                   name="LSTM_MASK_2"))(x_gru_mask)
        x_gru_mask   = attention_3d_block(x_gru_mask, "attention_vec_mask_vector")
        mul_layer = tf.keras.layers.Add()([x_gru, x_gru_mask])
        inp =mul_layer
        print("mul_layer", mul_layer.shape)
    else:
        inp = x_gru
        print("x_gru", inp.shape)
   
    x =  attention_3d_block(inp, "attention_vec_1")
   
    x = tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(recur_input[-1]*2,
                                                           return_sequences=True, 
                                                           name="gru_layer_3"))(x)
    x = tf.keras.layers.Dropout(0.2, name="dropout_0")(x)
    x = tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(recur_input[-1]))(x)
    #x_gru = NonMasking()(x_gru)
    # x_gru = tf.keras.layers.Flatten(name="flatten_layer_2")(x_gru)
    x = tf.keras.layers.Dropout(0.2, name="dropout_1")(x)
    

    combined_features = tf.keras.layers.concatenate([x_ffn, x], axis=1)
    out = tf.keras.layers.Dense((recur_input[-1]+ffn_in[-1])*2)(combined_features)
    out = tf.keras.layers.Dropout(0.2, name="dropout_2")(out)
    output = tf.keras.layers.Dense(64, activation="relu")(out)
    outputs = tf.keras.layers.BatchNormalization()(output)
    outputs = tf.keras.layers.Dense(1, activation="sigmoid", 
                                    name="output_layer")(outputs)
    if concat_vect: 
        model_gru = tf.keras.models.Model([inp_gru,gru_mask_input,input_ffn], outputs)
    else:
        model_gru = tf.keras.models.Model([inp_gru,input_ffn], outputs)
    model_gru.compile(optimizer =tf.keras.optimizers.Adam(learning_rate=0.0001), 
                     loss='binary_crossentropy', metrics=['accuracy', matthews_correlation])
    model_gru.summary()
    tf.keras.utils.plot_model(model_gru, to_file="GRU_MASKING_MODEL_ATT_GPU_0.png",
                              show_shapes=True, show_layer_names=True)
    
    return model_gru

network = benchmarking_models((24,1,62), (4,),gru_dim_mask=False,concat_vect=False, lstm_dim=256, appl_mask_layer=True)



n_samples = 2000
time_step = 24
n_features = 62

X = np.random.randint(0, 1000, size=(n_samples, time_step, n_features))
M = np.random.randint(2, size=(n_samples, time_step, n_features))
stats = np.random.randint(0, 100, size=(n_samples, 3))
target = np.random.randint(2, size=n_samples)
X= np.expand_dims(X, axis=2)
M= np.expand_dims(M, axis=2)

data= np.load("/content/drive/MyDrive/COHORT/subjects_cohort.npz",allow_pickle=True )

data.files

timeseries=data["timeseries"]
masked_vectors=data["masked_vectors"] 
statics=data["statics"] 
labels=data["labels"]
target_hor_mor = labels[:,:,0]
target_hor_icu = labels[:,:,1]

timeseries.shape, masked_vectors.shape, statics.shape, labels.shape



timeseries= np.expand_dims(timeseries, axis=2)
masked_vectors= np.expand_dims(masked_vectors, axis=2)
statics = np.squeeze(statics, axis=1)



def train_model_wt_transformer_with_masking(X_train, X_train_stats,Y_train, X_test, X_test_stats, Y_test, seed, label_task, 
                                            X_train_mask=False , X_test_mask=False, concatenate_vect =False, mask_model=False,
                                            EPOCHS=50, BATCH_SIZE=64, applied_mask_layer=True):
    # CREATE CALLBACKS poids_train.hdf5  patience=20
    early_stopping = EarlyStopping(monitor='val_loss', mode='min', 
                               patience=5,verbose=2)
    checkpoint = ModelCheckpoint(f"{label_task}_{seed}.h5", monitor='val_matthews_correlation', 
                             verbose=1, save_best_only=True, mode='max')
    model = None
    score_folds = []
    strategy = tf.distribute.MirroredStrategy()
    print("Number of devices: {}".format(strategy.num_replicas_in_sync))
    # LR SCHEDULE 
    reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(monitor = 'val_loss', factor=0.1,
                      patience=3, min_lr=1e-6,verbose =2) 
    
    EPOCHS = EPOCHS
    BATCH_SIZE = BATCH_SIZE * strategy.num_replicas_in_sync
    STEPS_PER_EPOCH = (len(X_train) + len(X_test)) // BATCH_SIZE
    LR = 1e-3
    steps = STEPS_PER_EPOCH * EPOCHS
    
    # Open a strategy scope.([X_test, X_test_stats], Y_test) validation_data=([X_test, X_test_stats],Y_test) , lr_schedule_rc ,build_transformer_model_ , build_transformer_model_tune
    # gru_masking_model_attention
    with strategy.scope():
        #print(X_train_mask.shape)
        if mask_model:
            print("applied_mask_layer", applied_mask_layer)
            print("gru_dim_mask", X_train_mask.shape[1:])
            print("concat_vect", concatenate_vect)
           
            model = benchmarking_models(X_train.shape[1:],X_train_stats.shape[1:],
                                                           gru_dim_mask=X_train_mask.shape[1:],
                                                           concat_vect= concatenate_vect,
                                                           appl_mask_layer=applied_mask_layer)
        else:
            print("applied_mask_layer", applied_mask_layer)
            print("gru_dim", X_train.shape[1:])
            model = benchmarking_models(X_train.shape[1:],X_train_stats.shape[1:],
                                        appl_mask_layer=applied_mask_layer)
    # , lr_schedule    
    if concatenate_vect:
        results = model.fit([X_train,X_train_mask, X_train_stats,],Y_train, epochs=EPOCHS, 
                         batch_size=BATCH_SIZE, callbacks=[checkpoint, early_stopping], 
                         verbose=2, validation_split=0.2)  
        print("Val Score: ", model.evaluate([X_test,X_test_mask, X_test_stats], Y_test))
    
        score_folds.append([average_precision_score(Y_test,model.predict([X_test, X_test_mask, X_test_stats])),
                           roc_auc_score(Y_test,model.predict([X_test,X_test_mask, X_test_stats])),
                           (Y_test,model.predict([X_test,X_test_mask, X_test_stats]))])
    else:
        results = model.fit([X_train,X_train_stats],Y_train, epochs=EPOCHS, 
                             batch_size=BATCH_SIZE, callbacks=[checkpoint, early_stopping], 
                             verbose=2, validation_split=0.2)  
        print("Val Score: ", model.evaluate([X_test, X_test_stats], Y_test))

        score_folds.append([average_precision_score(Y_test,model.predict([X_test, X_test_stats])),
                           roc_auc_score(Y_test,model.predict([X_test, X_test_stats])),
                           (Y_test,model.predict([X_test, X_test_stats]))])
    return results, (results , score_folds), model

DATA = [('MASKING',timeseries, True),]

FOLDS_SCORE =[]
FOLDS_SCORE_RESULTS =[]
size_batch=32
data_hrs = 24
TASK = "ICU_MORTALITY"
main_path ="/content/PAPER_TASK_THESIS"
dn = os.path.join(main_path, f"{TASK}_{str(data_hrs)}_DATA")
try:
    os.makedirs(dn)
except:
    pass
for inputation_type,data_type, mask_layer in DATA:
    print(inputation_type, mask_layer)
    seed = 42
    NUM_FOLDS = 5
    from sklearn.model_selection import KFold
    from sklearn.model_selection import StratifiedKFold
    label_task=f"{TASK}_{data_hrs}_HRS_DATA_{inputation_type}"
    kf = StratifiedKFold(n_splits=NUM_FOLDS, shuffle=True, random_state=seed)
    model_history = []
    test_data = []
    score_folds_=[]
    histories = []
    for index, (train_index, test_index) in enumerate(kf.split(data_type, target_hor_icu)):
        print('<------- fold', index + 1, '------->')
        x_train, x_test = data_type[train_index], data_type[test_index]
        x_train_mask, x_test_mask = masked_vectors[train_index], masked_vectors[test_index]
        print(x_train.shape)
        x_train_stats, x_test_stats = statics[train_index], statics[test_index]
        print(x_train_stats.shape)
        label_train, label_test = target_hor_icu[train_index], target_hor_icu[test_index]
        print(f'Fold:{index+1}, Train set: {len(train_index)}, Test set:{len(test_index)}')
        if inputation_type !='MASKING':
            historique, results , model = train_model_wt_transformer_with_masking(x_train,x_train_stats,label_train, x_test,
                                                                     x_test_stats, label_test,index,label_task, BATCH_SIZE=size_batch, applied_mask_layer=mask_layer)
            test_data.append([x_test, x_test_stats, label_test])
            score_folds_.append([average_precision_score(label_test,model.predict([x_test,x_test_stats])),
                                        roc_auc_score(label_test,model.predict([x_test,x_test_stats]))])
        else:
            historique, results , model = train_model_wt_transformer_with_masking(x_train,x_train_stats,label_train, x_test, x_test_stats, 
                                                                     label_test,index,label_task, X_train_mask=x_train_mask ,
                                                                     X_test_mask=x_test_mask, concatenate_vect =True, 
                                                                     mask_model=True, BATCH_SIZE=size_batch, applied_mask_layer=mask_layer)
            score_folds_.append([average_precision_score(label_test,model.predict([x_test, x_test_mask,x_test_stats])),
                                        roc_auc_score(label_test,model.predict([x_test, x_test_mask,x_test_stats]))])
            test_data.append([x_test, x_test_mask, x_test_stats, label_test])
            
            
       
        #model.save_weights(os.path.join("PAPER_TASK_THESIS/Mortality_hos/" ,f'TRANSFORMERS_HOS_MOR_ALL_ICU_{index+1}_{label_task}.h5'))
        
        
        print(f" Performance model PR and AUC on test data: {score_folds_}")
        print("======="*12, end="\n\n\n")
        histories.append(historique)
        model_history.append(results)
    FOLDS_SCORE_RESULTS.append((inputation_type, [model_history,test_data,score_folds_]))
    FOLDS_SCORE.append((inputation_type, [model_history,test_data,score_folds_,histories]))
    model_results = [model_history[i][1] for i in range(len(model_history))]
    #np.savez(os.path.join(dn,f"{inputation_type}_model.npz"),result_folds=model_results, data_test=test_data)
import re
import scipy
import math
from scipy.stats import skew, kurtosis, t, norm, sem
import numpy as np
import pandas as pd
import statistics

#dataset = [10.22, 4.12, 8.58, 14.79, 2.88, 7.24, 9.67, 10.45, 10.48]
## dataset = [float(x) for x in input('Enter a number: ').split()]



def statistic(dataset):
    dataset = [x for x in dataset if str(x) != 'nan']
    dataset = list(filter(None, dataset))
    mean = statistics.mean(dataset)
    median = statistics.median(dataset)
    quant25 = statistics.quantiles(dataset)[0]
    quant75 = statistics.quantiles(dataset)[2]
    maximum = max(dataset)
    minimum = min(dataset)
    skewness = skew(dataset)
    kurt = kurtosis(dataset)
    blowout_min = quant25 - 1.5 * (quant75 - quant25)
    blowout_max = quant75 + 1.5 * (quant75 - quant25)
    dataset_clean = dataset.copy()
    for val in dataset:
        if blowout_min > val or blowout_max < val:
            dataset_clean.remove(val)
    if blowout_min > min(dataset_clean) or blowout_max < max(dataset_clean):
        blowout = 1
    else:
        blowout = 0

    '''
    Проверка на нормальность
    '''
    n = len(dataset)
    A = skewness
    E = kurt
    D_A = 6*(n-1)/((n+1)*(n+3))
    D_E = 24*(n-2)*(n-3)*n/((n+5)*(n+3)*(n-1)*(n-1))
    if (abs(A) < 3 * math.sqrt((D_A))) and (abs(E) < 3 * math.sqrt((D_E))):
        # print("Данные распределены нормально")
        res = 1
    else:
        # print('Данные НЕ распределены нормально')
        res = 0

    '''
    Доверительный интервал = x(+/-) t *(s/√n)
    '''
    alpha = 0.95
    d = 0
    for i in range(len(dataset)):
        d = d + (dataset[i] - mean)**2
    se_true = np.sqrt(d/(n-1))/((n-1)**0.5)
    lower = mean - 1.96*se_true
    upper = mean + 1.96*se_true
    
    # data = {'Среднее':mean, 'Медиана':median, 'Верхний квартиль': quant25, 'Нижний квантиль':quant75, 'Максимум':maximum, 'Минимум':minimum, 'Асимметрия':skewness, 
    # 'Эксцесс':kurt, 'Нормальное распределение':res, 'Нижняя граница доверительного интервала':lower, 'Верхняя граница доверительного интервала':upper}

    return skewness, kurt, res, lower, upper, blowout_min, blowout_max, blowout
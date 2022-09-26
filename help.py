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
    mean = statistics.mean(dataset)
    # print("Среднее:", mean)
    median = statistics.median(dataset)
    # print("Медиана:", median)
    quant25 = statistics.quantiles(dataset)[0]
    # print("Верхний квартиль:", quant25)
    quant75 = statistics.quantiles(dataset)[2]
    # print("Нижний квантиль:", quant75)
    maximum = max(dataset)
    # print("Максимум:",maximum)
    minimum = min(dataset)
    # print('Минимум:', minimum)
    skewness = skew(dataset)
    # print("Асимметрия:", skewness)
    kurt = kurtosis(dataset)
    # print("Эксцесс:", kurt)

    '''
    Проверка на нормальность
    '''
    n = len(dataset)
    A = skewness
    E = kurt
    D_A = 6*(n-1)/((n+1)*(n+3))
    D_E = 24*(n-2)*(n-3)*n/((n+5)*(n+3)*(n-1)*(n-1))
    if (abs(A) <= 3 * math.sqrt((D_A))) and (abs(E) <= 3 * math.sqrt((D_E))):
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
    global df
    # print(f"{alpha*100} confidence interval {lower} and {upper}")

    # data = {'Среднее':mean, 'Медиана':median, 'Верхний квартиль': quant25, 'Нижний квантиль':quant75, 'Максимум':maximum, 'Минимум':minimum, 'Асимметрия':skewness, 
    # 'Эксцесс':kurt, 'Нормальное распределение':res, 'Нижняя граница доверительного интервала':lower, 'Верхняя граница доверительного интервала':upper}

    return skewness, kurt, res, lower, upper


df = pd.read_csv("folders/dataset/diabetes.csv")
# columns = ['Среднее', 'Медиана', 'Верхний квартиль', 'Нижний квантиль', 'Максимум', 'Минимум', 'Асимметрия', 'Эксцесс', 'Нормальное распределение', 'Нижняя граница дов. интервала', 'Верхняя граница дов. интервала']
columns = ['Асимметрия', 'Эксцесс', 'Нормальное распределение (1-да, 0-нет)', 'Нижняя граница доверительного интервала', 'Верхняя граница доверительного интервала']
dataframe = pd.DataFrame(columns = columns)
for col in df.columns:
    to_append = list(df[col])
    dataframe = dataframe.append(pd.DataFrame([list(statistic(to_append))], columns=columns), ignore_index=True)
print(dataframe)
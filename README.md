## ОПИСАНИЕ 
Данный проект – простая система искусственного интеллекта с автоматизацией анализа данных, основанная на библиотеках pandas, stats, statsmodels и scikit-learn.
Система автоматизирует проверку гипотез, предоставление описательных статистик и выводов, которые могут помочь аналитику.
Функции машинного обучения автоматизируют некоторые из распространенных шагов, связанных с применением scikit-learn к бизнес-задачам.
На вход принимает файл csv/xlsx с численными данными или список (list) чисел.

***Предупреждение***: если загрузить файл с другими колонками, то не будет работать блок prediction и analysis/eda


## ФУНКЦИОНАЛ
1. **ML**: LogisticRegression, LinearRegression (с округлением до ближайшего предсказанного класса), DecisionTreeClassifier

2. **Statistics**: Mode, Median and Mean, Interquartile Range and Box Plot, Variance and Standard deviation, Z-scores, Contingency Table, Pearson’s, Distribution (Normal/Binomial/Poisson), Inferential Statistics, Confidence Intervals, Hypothesis Testing

3. **Analytics**: Summarizing and Visualizing Data (graphs, matrix)

![screenshot](https://user-images.githubusercontent.com/81550686/196056168-8d274b39-2dd2-4746-b996-f97c8bb1aa8b.jpg)


## ТРЕБОВАНИЯ
(создали виртуальную среду и находимся в ней)
1. Скачиваем необходимые библиотеки

pip install -r requirements.py 
2. Запускаем веб-приложение

py -m streamlit run C:\Users\Sveta\projects\BI_system\BI-system.py

**ИЛИ**

streamlit run C:\path\to\BI_system\BI-system.py 

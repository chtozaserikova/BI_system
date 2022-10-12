## ОПИСАНИЕ 
Данный проект - простая система искусственного интеллекта с автоматизацией анализа данных, основанная на библиотеках pandas, stats, statsmodels и scikit-learn.
Система автоматизирует проверку гипотез, предоставление описательных статистик и выводов, которые могут помочь аналитику.
Функции машинного обучения автоматизируют некоторые из распространенных шагов, связанных с применением scikit-learn к бизнес-задачам.


## ФУНКЦИОНАЛ
1. **ML**: LogisticRegression, LinearRegression (с округлением до ближайшего предсказанного класса), DecisionTreeClassifier

2. **Statistics**: Mode, Median and Mean, Interquartile Range and Box Plot, Variance and Standard deviation, Z-scores, Contingency Table, Pearson’s, Distribution (Normal/Binomial/Poisson), Inferential Statistics, Confidence Intervals, Hypothesis Testing

3. **Analytics**: Summarizing and Visualizing Data (graphs, matrix)
![экран веб-приложения]("https://github.com/chtozaserikova/BI_system/blob/master/folders/home/screenshot.jpg")

## ТРЕБОВАНИЯ
(создали виртуальную среду и находимся в ней)
1. Скачиваем необходимые библиотеки

pip install -r requirements.py 
2. Запускаем веб-приложение

py -m streamlit run C:\path\to\BI_system\BI-system.py 

**ИЛИ**

streamlit run C:\path\to\BI_system\BI-system.py 


## НУЖНО ДОРАБОТАТЬ
1. проверить показ фотки в гитхабе 
2. прописать исключения в функциях с учетом пропущенных значених и cat_columns
3. переписать вывод графиков и диаграмм с учетом того, что мы не знаем название колонок (или их вообще может не быть)
4. улучшить метрики в предикшенах (точность 90+)
5. если 3) сделано, то аналогично переписать функцию start_prediction()
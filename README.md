# Lowess и Надарай-Ватсон
(алгоритмы для моделирования и сглаживания двумерных данных )

полное описание можно прочесть здесь [здесь]( http://www.machinelearning.ru/wiki/index.php?title=%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_LOWESS)


# классический Loweless

можно посчитать новые Y по формуле Надарая-Ватсона:
![](https://raw.githubusercontent.com/okiochan/Lowess/master/h1.gif)

формула Lowess выглядит так (добавляются настраевыемые gamma): 
![](https://raw.githubusercontent.com/okiochan/Lowess/master/h2.gif)

код программы в **lowess.py**

Вызываемый метод, принимает X,Y - выборку, MAX - кол-во итераций, h - коэф. сглаживание, ro - метрику
```
lowess(X,Y, MAX=2, h=0.9, ro=euclidean):
```
выборки содержатся в файле **data.py**, для вызова - воспользуйтесь командой 
```
X,Y = data.DataBuilder().Build("имя выборки")
```
имена выборок: "poisson", "wavelet",degenerate"

Посмотрим как отрабатывают оба алгоритма:

Пример работы на выборке "degenerate"
![](https://raw.githubusercontent.com/okiochan/Lowess/master/Figure_11.png)
Среднеквадратичная ошибка
![](https://raw.githubusercontent.com/okiochan/Lowess/master/ssse.png)

Пример работы на выборке "wavelet"
![](https://raw.githubusercontent.com/okiochan/Lowess/master/Figure_12.png)

Среднеквадратичная ошибка
![](https://raw.githubusercontent.com/okiochan/Lowess/master/ssse1.png)

Пример работы на выборке "poisson"
![](https://raw.githubusercontent.com/okiochan/Lowess/master/Figure_13.png)

Среднеквадратичная ошибка
![](https://raw.githubusercontent.com/okiochan/Lowess/master/ssse2.png)

# пример Loweless со взвешенной регрессией

код программы  в **LowessGood.py**

Взвешенная регрессия сглаживает выборку так: 
![](https://raw.githubusercontent.com/okiochan/Lowess/master/Figure_1.png)
![](https://raw.githubusercontent.com/okiochan/Lowess/master/Figure_2.png)



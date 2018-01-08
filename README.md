# Lowess и Надарай-Ватсон
(алгоритмы для моделирования и сглаживания двумерных данных )

полное описание можно прочесть здесь [здесь]( http://www.machinelearning.ru/wiki/index.php?title=%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_LOWESS)

Рассматриваемые ниже выборки содержатся в файле **data.py**, для вызова - воспользуйтесь командой 
```
X,Y = data.DataBuilder().Build("имя выборки")
```
имена выборок: "poisson", "wavelet",degenerate"


# метод Надарая-Ватсона

Реализована основная формула Надарая-Ватсона:
![](https://raw.githubusercontent.com/okiochan/Lowess/master/formula/h1.gif)

код программы в **lowess.py**

Нужно вызвать метод Надарая-Ватсона, он принимает: X,Y - выборку, h - коэф. сглаживания, ro - метрику, K - функцию ядра
```
nadaray(X,Y, h, K, ro=euclidean)
```

Примеры работы программы с гауссовским	и	квартическим	ядрами (был взят h = 0.6).

![](https://raw.githubusercontent.com/okiochan/Lowess/master/img/nad1.png)

на выборке "poisson", ошибка:
![](https://raw.githubusercontent.com/okiochan/Lowess/master/img/nad11.png)

![](https://raw.githubusercontent.com/okiochan/Lowess/master/img/nad2.png)

на выборке "wavelet", ошибка:
![](https://raw.githubusercontent.com/okiochan/Lowess/master/img/nad22.png)

Также, мы видим, что чем выше h, тем лучше сглаживание:

**h = 0.9**

![](https://raw.githubusercontent.com/okiochan/Lowess/master/img/hbig.png)

**h = 0.2**

![](https://raw.githubusercontent.com/okiochan/Lowess/master/img/hsmall.png)

Вот еще интересный пример:

![](https://raw.githubusercontent.com/okiochan/Lowess/master/img/nad3.png)

на выборке "degenerate", ошибка:
![](https://raw.githubusercontent.com/okiochan/Lowess/master/img/nad33.png)

# Loweless

можно посчитать новые Y по формуле Надарая-Ватсона:
![](https://raw.githubusercontent.com/okiochan/Lowess/master/formula/h1.gif)

формула Lowess выглядит так (добавляются настраевыемые gamma): 
![](https://raw.githubusercontent.com/okiochan/Lowess/master/formula/h2.gif)

код программы в **lowess.py**

Lowess метод, принимает X,Y - выборку, MAX - кол-во итераций, h - коэф. сглаживания, ro - метрику, K и K1 - функции ядер
```
lowess(X,Y, MAX, h, K, K1, ro=euclidean)
```

Посмотрим как отрабатывают оба алгоритма:

![](https://raw.githubusercontent.com/okiochan/Lowess/master/img/Figure_11.png)

на выборке "degenerate", Среднеквадратичная ошибка
![](https://raw.githubusercontent.com/okiochan/Lowess/master/img/ssse.png)

![](https://raw.githubusercontent.com/okiochan/Lowess/master/img/Figure_12.png)

выборке "wavelet", cреднеквадратичная ошибка
![](https://raw.githubusercontent.com/okiochan/Lowess/master/img/ssse1.png)

![](https://raw.githubusercontent.com/okiochan/Lowess/master/img/Figure_13.png)

на выборке "poisson", cреднеквадратичная ошибка
![](https://raw.githubusercontent.com/okiochan/Lowess/master/img/ssse2.png)


# Loweless со взвешенной регрессией

код программы  в **LowessGood.py**

Взвешенная регрессия сглаживает выборку так: 
![](https://raw.githubusercontent.com/okiochan/Lowess/master/img/Figure_1.png)
![](https://raw.githubusercontent.com/okiochan/Lowess/master/img/Figure_2.png)



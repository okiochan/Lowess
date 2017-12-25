# Lowess
(алгоритм для моделирования и сглаживания двумерных данных )

полное описание алгоритма [здесь]( http://www.machinelearning.ru/wiki/index.php?title=%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_LOWESS)

(выборки содержатся в файле **data.py**, для вызова - воспользуйтесь командой *X,Y = data.DataBuilder().Build("имя выборки")* )
(имена выборок: "poisson", "wavelet",degenerate")

# классический Loweless

можно посчитать новые Y по формуле Надарая-Ватсона:
![](https://raw.githubusercontent.com/okiochan/Lowess/master/h1.gif)

формула Lowess выглядит так (добавляются настраевыемые gamma): 
![](https://raw.githubusercontent.com/okiochan/Lowess/master/h2.gif)

код программы [здесь]( https://github.com/okiochan/Lowess/blob/master/lowess.py)

![](https://raw.githubusercontent.com/okiochan/Lowess/master/Figure_11.png)
![](https://raw.githubusercontent.com/okiochan/Lowess/master/Figure_12.png)

# пример Loweless со взвешенной регрессией
(выборка содержится в файле **data.py**, для вызова - воспользуйтесь командой *X,Y = data.DataBuilder().Build("poisson")* )

код программы [здесь]( https://github.com/okiochan/Lowess/blob/master/LowessGood.py)

![](https://raw.githubusercontent.com/okiochan/Lowess/master/Figure_1.png)
![](https://raw.githubusercontent.com/okiochan/Lowess/master/Figure_2.png)



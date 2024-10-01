# Практическая работа №2

## Численные методы решения нелинейных уранвений.

</br></br></br></br>


Студент: Кайков Дмитрий Алексеевич  
Преподаватель: Лычёв Андрей Владимирович  
Группа: БИВТ-23-9 
Вариант: 7  
Подпись:
<img src="подпись.bmp" alt="подпись" width="100"/> 

</br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br>


<center>Москва, 2024</center>

<div class="page"/>
<div style-"page-break-after: always;"></div>

**Цель работы:**  
Приобретение практических навыков для поиска решения нелинейных уравнений численными  методами.  
**Задача:**  
Требуется найти один из нулей функции *f(x)* на отрезке *[a, b]*, где функция
является непрерывной. То есть решить уравнение *f(x) = 0* и найти такую точку
*x<sup>∗</sup> ∈ [a, b], что f(x<sup>∗</sup>) = 0.*

**1 Аналитический вид функции**  
*f(x) = -2 + sin(x) + cos<sup>2</sup>(x) + log(|x|)*

**2 График функции**  
<img src="Figure_1.png" alt="подпись" width="1000"/> 

**3 Алгоритм**
X0 - начальное приблежение


**3 Листинг программы в виде текста**
```python
import matplotlib.pyplot as plt
import numpy as np 
import time


f = lambda x: -2 + np.sin(x) + np.cos(x)**2 + np.log(abs(x))
g = lambda x: np.e**(2 - np.sin(x) - np.cos(x)**2)


def method_simple_iteration(x0, f, g, is_show=False):
    a, b = 5, 7
    q = 5
    a -= q 
    b += q

    x = np.arange(a, b, 0.1)
    y = f(x)

    history = [x0]
    history_y = [f(x0)]
    colors = [1 / history_y[-1]]
    c_op = 0
    start_t = time.time()
    for i in range(47):
        xn1 = g(history[-1])
        history.append(xn1)
        history_y.append(f(history[-1]))
        colors.append(1 /history_y[-1])
        c_op += 6

    if is_show:
        plt.xlim(a, b)
        plt.ylim(-4, 4)
        plt.plot(x, y)
        plt.scatter(history, history_y, s=30, c=colors)
        plt.plot([a, b], [0, 0])
        plt.plot([history[-1], history[-1]], [-100, 100], c='red')
        plt.show()

    return history[-1], history_y[-1]


def method_secant(x0, f, g, is_show=False):
    a, b = 5, 7
    q = 5
    a -= q 
    b += q

    x = np.arange(a, b, 0.1)
    y = f(x)

    history = [x0, x0 - 1]
    history_y = [f(history[0]), f(history[-1])]
    colors = [1 / history_y[-2], 1 / history_y[-1]]
    c_op = 0
    start_t = time.time()
    for i in range(11):
        xn1 = history[-1] - (history[-1] - history[-2]) * f(history[-1]) / (f(history[-1]) - f(history[-2]))
        history.append(xn1)
        history_y.append(f(history[-1]))
        colors.append(1 /history_y[-1])
        c_op += 5

    if is_show:
        plt.xlim(a, b)
        plt.ylim(-4, 4)
        plt.plot(x, y)
        plt.scatter(history, history_y, s=30, c=colors)
        plt.plot([a, b], [0, 0])
        plt.plot([history[-1], history[-1]], [-100, 100], c='red')
        plt.show()

    return history[-1], history_y[-1]


def method_dichotomy(f, g, is_show=False):
    a, b = 5, 7
    q = 5
    a -= q 
    b += q
    a_border = a
    b_border = b
    print(a, b)

    x = np.arange(a, b, 0.1)
    y = f(x)

    history = []
    history_y = []
    colors = []
    c_op = 0
    start_t = time.time()
    for i in range(100):
        c = (a + b) / 2
        if f(b) * f(c) < 0:
            a = c
        else:
            b = c
        history.append(c)
        history_y.append(f(c))
        colors.append(1 /history_y[-1])
        c_op += 3

    if is_show:
        plt.xlim(a_border, b_border)
        plt.ylim(-4, 4)
        plt.plot(x, y)
        plt.scatter(history, history_y, s=30, c=colors)
        plt.plot([a_border, b_border], [0, 0])
        plt.plot([history[-1], history[-1]], [-100, 100], c='red')
        plt.show()

    return history[-1], history_y[-1]


x, y = method_simple_iteration(9, f, g, 1)
print(x, y)
```

**4 Результаты вычислений.**  
**Метод простых итераций**
| Этап | Кол-во сложений | Кол-во умножений | Кол-во делений | Кол-во ар. оп. |
|--------------|-----------|------------|------------|------------|


**5 Вывод**

Метод простых итераций позволяет найти достаточно точное решение заданной функции за маленькое количество времени, и кол-во операций равному кол-ву операций вычисления функции. Но в сравнении с методом дихотомии и секущих сходимость метода хуже.
# Практическая работа №1

## Представление вещественных чисел

</br></br></br></br>


Студент: Кайков Дмитрий Алексеевич  
Преподаватель: Лычёв Андрей Владимирович  
Группа: БИВТ-23-9 
Вариант: 7  
Подпись:
<img src="подпись.bmp" alt="подпись" width="100"/> 

</br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br>


<center>Москва, 2024</center>

<div class="page"/>
<div style-"page-break-after: always;"></div>

**Цель работы:**  
Закрепить теоретические знания и формирование практических навыков представления чисел с плавающей запятой.
**Задача:**  
На основе спецификации IEEE 754 описать представление в памяти чисел с плавающей запятой с количеством бит знака S = 1, порядка *E = 11* и мантиссы *T = 12*. Число *F = pi / 7*.

**1 Представление числа** 
В памяти число представляется следующим образом:


<table border="1px solid black;">
    <tbody>
        <tr>
            <td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td>
        </tr>
        <tr>
            <td>S</td>
            <td colspan=11 align="center">E</td>
            <td colspan=12 align="center">T</td>
        </tr>
    </tbody>
</table>

S(1 бит) - знак числа.  
E(11 бит) - экспонента e со смещением bias. (bias = 2<sup>11 - 1</sup> - 1 = 1023)
T(12 бит) - мантиса с неявно заданной целой частью.


**2 Формула**  
Если *E != 0*  
*F = (-1)<sup>S</sup> * 2<sup>E - bias</sup> * (1 + 2<sup>-p</sup> * T)*

Если *E = 0*  
*F = (-1)<sup>S</sup> * 2<sup>E - bias</sup> * (0 + 2<sup>-p</sup> * T)*


**3 Представление чисел**

3.1 Минимальное положительное число
<table border="1px solid black;">
    <tbody>
        <tr>
            <td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td>
        </tr>
        <tr>
            <td>S</td>
            <td colspan=11 align="center">E</td>
            <td colspan=12 align="center">T</td>
        </tr>
        <tr>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
        </tr>
    </tbody>
</table>

*F = (-1)<sup>0</sup> * 2<sup>-1023</sup> * (0 + 2<sup>-12</sup>) = 2.716154612436 * 10<sup>-312</sup>*

3.2 Максимальное положительное число
<table border="1px solid black;">
    <tbody>
        <tr>
            <td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td>
        </tr>
        <tr>
            <td>S</td>
            <td colspan=11 align="center">E</td>
            <td colspan=12 align="center">T</td>
        </tr>
        <tr>
            <td>0</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
        </tr>
    </tbody>
</table>

*F = (-1)<sup>0</sup> * 2<sup>2047 - 1023</sup> * (1 + 2<sup>-12</sup> * 1023) =...<sup></sup>*

3.3 Наименьшее из чисел больше единицы
<table border="1px solid black;">
    <tbody>
        <tr>
            <td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td>
        </tr>
        <tr>
            <td>S</td>
            <td colspan=11 align="center">E</td>
            <td colspan=12 align="center">T</td>
        </tr>
        <tr>
            <td>0</td>
            <td>0</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
        </tr>
    </tbody>
</table>

*F = (-1)<sup>0</sup> * 2<sup>1023 - 1023</sup> * (0 + 2<sup>-12</sup> * 1) =1.000244140625<sup></sup>*

3.4 Положительный ноль
<table border="1px solid black;">
    <tbody>
        <tr>
            <td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td>
        </tr>
        <tr>
            <td>S</td>
            <td colspan=11 align="center">E</td>
            <td colspan=12 align="center">T</td>
        </tr>
        <tr>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
        </tr>
    </tbody>
</table>
3.5 Отрицательный ноль
<table border="1px solid black;">
    <tbody>
        <tr>
            <td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td>
        </tr>
        <tr>
            <td>S</td>
            <td colspan=11 align="center">E</td>
            <td colspan=12 align="center">T</td>
        </tr>
        <tr>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
        </tr>
    </tbody>
</table>
3.6 Плюс бесконечность
<table border="1px solid black;">
    <tbody>
        <tr>
            <td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td>
        </tr>
        <tr>
            <td>S</td>
            <td colspan=11 align="center">E</td>
            <td colspan=12 align="center">T</td>
        </tr>
        <tr>
            <td>0</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
        </tr>
    </tbody>
</table>
3.7 Минус бесконечность
<table border="1px solid black;">
    <tbody>
        <tr>
            <td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td>
        </tr>
        <tr>
            <td>S</td>
            <td colspan=11 align="center">E</td>
            <td colspan=12 align="center">T</td>
        </tr>
        <tr>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
        </tr>
    </tbody>
</table>
3.8 NaN
<table border="1px solid black;">
    <tbody>
        <tr>
            <td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td>
        </tr>
        <tr>
            <td>S</td>
            <td colspan=11 align="center">E</td>
            <td colspan=12 align="center">T</td>
        </tr>
        <tr>
            <td>0</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
        </tr>
    </tbody>
</table>

3.9 Машинный эпсилон

e = 2<sup>-12</sup> = 0.000244140625

**4 Представление заданного числа**  
*F = pi / 7 = 0.4487989505128276*  

```python
import math 

n = math.pi / 7

n2 = n / 0.25 - 1

for i in range(12):
    n2 *= 2 
    if n2 >= 1:
        print(1, end=" ")
        n2 -= 1
    else:
        print(0, end=" ")
```

<table border="1px solid black;">
    <tbody>
        <tr>
            <td>0</td>
            <td>1</td>
            <td>2</td>
            <td>3</td>
            <td>4</td>
            <td>5</td>
            <td>6</td>
            <td>7</td>
            <td>8</td>
            <td>9</td>
            <td>10</td>
            <td>11</td>
            <td>12</td>
            <td>13</td>
            <td>14</td>
            <td>15</td>
            <td>16</td>
            <td>17</td>
            <td>18</td>
            <td>19</td>
            <td>20</td>
            <td>21</td>
            <td>22</td>
            <td>23</td>
        </tr>
        <tr>
            <td>S</td>
            <td colspan=11 align="center">E</td>
            <td colspan=12 align="center">T</td>
        </tr>
        <tr>
            <td>0</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
            <td>0</td>
            <td>1</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
        </tr>
    </tbody>
</table>

**5 Вывод**

Кодирование дробных чисел согласно стандарту IEEE-754 является интерпритируемым и распростронёным способом кодирования, но имеет недостатки точночти. Объём памяти следует увеличить при использовании в точных рассчётах или же использовать только для постых вычислений.
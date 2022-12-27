# Code Style
---

## Самое главное: соблюдать CRUD (create, read, update, delete) для таблиц 
---


## Variables (переменные)
#### Не делать:
``` python
x = 0 # неясно что значит
X = 0 # нет, просто нет
cnt = 0 # здесь лучше будет написать count = 0
```
#### Вот так можно
``` python
count = 0
i = 0 # только в цикле

```
 ---
## Functions names (имена функций)

#### НЕ ДЕЛАТЬ:

``` python
def sdfldfslksdflkjsdfalkj(): # просто не надо 
    pass

def pls_work(): # непонятная запись, неясно что она делает
    pass

def damag(): # грамматическая ошибка
    pass

def damageToPacman: # camelcase, в питоне пишем через нижнее подчеркивание
    pass
```
#### Вот так можно:
``` python
def damage_to_pacman:
    pass
```

---
## Classes (классы)
#### Не делать:
``` python
class Ldsfkjajlkdfs: # неясно, кто это
    pass
class pacman: # с маленькой буквы
    pass
```
#### Вот так можно:
``` python
class Pacman:
    pass
```
---

## Мотивационная цитата Игоря
>Быстро и легко можно получить только при***лей, для остального наберись терпения  
c. Игорь
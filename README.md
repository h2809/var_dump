# var_dump
Python3で、PHPのvar_dump()に近い事をやりたい

```
# foo.py
import vd;

list = ['yoshida', 42]
vd.var_dump(list)
```

```
$ python foo.py
[list(2)]:
    (str) yoshida
    (int) 42
```

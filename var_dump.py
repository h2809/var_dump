# -*- coding: utf-8 -*-

def var_dump(var, prefix=''):
    if type(var) in (int, float, str, complex):
        print(prefix, '(', var.__class__.__name__, ') ', var, sep='')
    else:
        my_type = '[' + var.__class__.__name__ + '(' + str(len(var)) + ')]:'
        print(prefix, my_type, sep='')
        prefix += '    '
        for i in var:
            if type(i) in (list, tuple, dict, set):
                var_dump(i, prefix)
            else:
                if isinstance(var, dict):
                    print(prefix, i, ': (', var[i].__class__.__name__, ') ', var[i], sep='')
                else:
                    print(prefix, '(', i.__class__.__name__, ') ', i, sep='')

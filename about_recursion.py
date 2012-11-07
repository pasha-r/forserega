#!/usr/bin/env python
# -*- coding: utf-8 -*-

# одна и та же рекурсивная функция, но первая по следам всего что делает пишет всякое на экран
def func(a):
    print "a", a
    next_step = a - 2
    print "next_step", next_step
    if next_step < 0:
        print "    return 0"
        return 0
    print "    call func(", next_step, ") + 1"
    counter = func(next_step) + 1
    print "    return counter", counter
    return counter

# а вторая просто красивая и по ней видно, за что рекурсию некоторые программисты любят :)
def func(a):
    return (func(a - 2) + 1) if a >= 2 else 0

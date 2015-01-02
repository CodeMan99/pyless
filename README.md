pyless
======

Page the output of anything using `less`.

Example
-------

This will create a pager, and on exit send its own content to `less`.

```python
>>> from pyless import Pager
>>> with Pager() as p:
...     print("Hello", file=p)
```

This will create a pager that sets itself to sys.stdout.

```python
>>> from pyless import StdoutPager
>>> with StdoutPager():
...    print("Hello")
```

###Lisense###
[LGPL v3](http://www.gnu.org/licenses/lgpl-3.0.txt)

*Disclaimer: Only tested on python 3.4*

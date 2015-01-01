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

*Only tested on python 3.4*

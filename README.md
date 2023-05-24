# pytube-win-wrapper

## Quickfixes

### RegexMatchError: __init__: could not find match for ^\w+\W

If you get the following error output:

```
  File "C:\Python311\Lib\site-packages\pytube\cipher.py", line 33, in __init__
    raise RegexMatchError(
pytube.exceptions.RegexMatchError: __init__: could not find match for ^\w+\W
```

edit `line 30` in `YOUR_PYTHON_DIR\Lib\site-packages\pytube\cipher.py`

Replace `var_regex = re.compile(r"^\w+\W")`

with `var_regex = re.compile(r"^\$*\w+\W")`

# the data science toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> your person python toolkit for data science.

_This is part of a blog post series on [the personal data science toolkit](http://www.alexfranz.com/data-science-toolkit-part-1) 🛠_


## Usage 

You can clone this repo or install it via pip with

```
pip install git+http://github.com/alfranz/... 
```

After the installation, you can start using the package and its functions in your re-curring analytics tasks. 

```python
import frnz

df = frnz.data.cities

print(frnz.analytics.count_missing(df))
```


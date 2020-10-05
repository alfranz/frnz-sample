# The Personal Python Data Science Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

_This is part of a blog post series on [the personal python data science toolkit](http://www.alexfranz.com/posts/personal-python-data-science-toolkit-part-1/) 🛠_


## Usage 

You can clone this repo or install it via pip with

```
pip install -e git+https://github.com/alfranz/frnz-sample.git@master#egg=frnz
```

After the installation, you can start using the package and its functions in your re-curring analytics tasks. 

```python
import frnz

df = frnz.data.cities

print(frnz.analytics.count_missing(df))
```


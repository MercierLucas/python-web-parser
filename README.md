# python-web-parser

Simple web scrapper that will retrieve every elements ( outer_element) and their childs (inner_elements) inside:


Usage


```python
outer_element = scrapper.Element("zg-item-immersion",property="class",tag="li")

inner_elements = [
    scrapper.Element("p13n-sc-truncate-desktop-type2",property="class",tag="div"),
    scrapper.Element("p13n-sc-price",property="class",tag="span"),
]
headers = ["Product","Price"]

amazon = scrapper.Scrapper(
    outer_element,
    headers,
    inner_elements
)
```

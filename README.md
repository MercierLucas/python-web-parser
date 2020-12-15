# python-web-parser

Simple web scrapper that will retrieve every elements ( outer_element) and their childs (inner_elements) inside:

## Elements:

Elements are objects that we want to target in pages. We distinguish two type of elements:
- outer_element: to identify each product on the page
- inner_elements: that allows to target specific tags in our products, for example price, title etc.

## Example
Initialize:

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

Use:

```python
url = "https://www.amazon.fr/gp/bestsellers/grocery/ref=zg_bs_nav_0"
df_amazon = amazon.parse_and_get(url,"BEST BUYS",add_scroll=False)
```


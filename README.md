# python-web-parser

Simple web scrapper that will retrieve every elements ( outer_element) and their childs (inner_elements) inside:


Usage


```python
# define all
outer_element = scrapper.Element("product-thumbnail",property="class",tag="article")

inner_elements = [
    scrapper.Element("product-thumbnail__description",property="class",tag="p"),
    scrapper.Element("GROCERY",property="data-seller-type",tag="span"),
    scrapper.Element("product-price",property="class",tag="div")
]
headers = ["Product","Price","Size"]

auchan_fetes = "https://www.auchan.fr/joyeuses-fetes/plats-accompagnements-fromages/poissons-crustaces/ca-b202011041112?page=1"
auchan_viande = "https://www.auchan.fr/boucherie-volaille-poissonnerie/ca-n02?page=1"
auchan_scrap = scrapper.Scrapper(
    outer_element,
    headers,
    inner_elements
)
```

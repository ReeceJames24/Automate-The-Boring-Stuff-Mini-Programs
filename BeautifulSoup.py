Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #parsing html with bs4
>>> 
>>> import requests
>>> import bs4
SyntaxError: invalid syntax
>>> import bs4
>>> res = requests.get('https://shopee.ph/63-pcs-1x1-or-20-pcs-2x2-Personalized-Sticker-Label-i.81465298.1555807819?gclid=CjwKCAjwtajrBRBVEiwA8w2Q8CjubzzCYtuHbr4lAtymH8pAgTSKDjfHka3CLgx1Gj6jTwEkoK1-ahoCAxcQAvD_BwE')
>>> res.raise_for_status()
>>> #NICE it worked
>>> 
>>> #now we pass the html text to the bs4 module
>>> shopee = bs4.BeautifulSoup(res.text)
>>> #we then use soup.select and then get the css path/selector of whatever we want to parse from a webpage. the soup.select will return a list of al the element objects for all the matching elements
>>> soup.select('#main > div > div.shopee-page-wrapper > div.page-product > div.container > div.product-briefing.flex.card._2cRTS4 > div.flex.flex-auto.k-mj2F > div > div.flex._32fuIU > div.flex.SbDIui > div.ilat8Wv')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    soup.select('#main > div > div.shopee-page-wrapper > div.page-product > div.container > div.product-briefing.flex.card._2cRTS4 > div.flex.flex-auto.k-mj2F > div > div.flex._32fuIU > div.flex.SbDIui > div.ilat8Wv')
NameError: name 'soup' is not defined
>>> #OOPS it should be shopee.select
>>> shopee.select('#main > div > div.shopee-page-wrapper > div.page-product > div.container > div.product-briefing.flex.card._2cRTS4 > div.flex.flex-auto.k-mj2F > div > div.flex._32fuIU > div.flex.SbDIui > div.ilat8W')
[]
>>> #LETS REDO THIS WITH ANOTHER PAGE
>>> 
>>> 
>>> import requests
>>> import bs4
>>> res = requests.get('https://www.amazon.com/Impractical-Python-Projects-Programming-Activities/dp/159327890X/ref=pd_lpo_14_t_2/140-4977272-3862923?_encoding=UTF8&pd_rd_i=159327890X&pd_rd_r=9a5d9e29-154d-404c-8796-1808ecf64fa6&pd_rd_w=5pkQ1&pd_rd_wg=61R7Q&pf_rd_p=7b36d496-f366-4631-94d3-61b87b52511b&pf_rd_r=3T0APTGH3Q06J3PYK7A4&psc=1&refRID=3T0APTGH3Q06J3PYK7A4')
>>> res.raise_for_status()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    res.raise_for_status()
  File "/opt/anaconda3/lib/python3.8/site-packages/requests/models.py", line 941, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 503 Server Error: Service Unavailable for url: https://www.amazon.com/Impractical-Python-Projects-Programming-Activities/dp/159327890X/ref=pd_lpo_14_t_2/140-4977272-3862923?_encoding=UTF8&pd_rd_i=159327890X&pd_rd_r=9a5d9e29-154d-404c-8796-1808ecf64fa6&pd_rd_w=5pkQ1&pd_rd_wg=61R7Q&pf_rd_p=7b36d496-f366-4631-94d3-61b87b52511b&pf_rd_r=3T0APTGH3Q06J3PYK7A4&psc=1&refRID=3T0APTGH3Q06J3PYK7A4
>>> #SHUCKS OKAY LETS USE ANTHER ONE AGAIN
>>> 
>>> 
>>> 
>>> res = requests.get('https://www.bestbuy.com/site/naruto-shippuden-ultimate-ninja-storm-4-road-to-boruto-standard-edition-xbox-one/5705543.p?skuId=5705543')
>>> res.raise_for_status()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    res.raise_for_status()
  File "/opt/anaconda3/lib/python3.8/site-packages/requests/models.py", line 941, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 403 Client Error: Forbidden for url: https://www.bestbuy.com/site/naruto-shippuden-ultimate-ninja-storm-4-road-to-boruto-standard-edition-xbox-one/5705543.p?skuId=5705543
>>> res=requests.get('https://www.lazada.com.ph/products/mamypoko-easy-to-wear-medium-6-11-kg-50-pcs-x-1-pack-50-pcs-diaper-pants-i147295386-s172403101.html?clickTrackInfo=bf224b9c-e15c-4b8c-bcf4-a111df31387e__147295386__5399__hot__171996__0.31546035__0.31451362__0.0__0.0__0.0__0.31451362__8__null__null__null__null__null__null____410.0__0.03170731707317076__4.869284357188094__7895__397.0__12005%2C12018%2C12027%2C12035%2C12040%2C12044%2C14001%2C16001%2C20001%2C23008%2C23083%2C23084%2C24085%2C38009%2C54853%2C71029%2C73206%2C73210%2C80976%2C82420%2C85112__null__null__null')
>>> res.raise_for_status()
>>> diaper = bs4.BeautifulSoup(res.text)
>>> diaper.select('#module_product_title_1 > div > div > span')
[]
>>> diaper.select('//*[@id="module_product_title_1"]/div/div/span/text()')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    diaper.select('//*[@id="module_product_title_1"]/div/div/span/text()')
  File "/opt/anaconda3/lib/python3.8/site-packages/bs4/element.py", line 1864, in select
    results = soupsieve.select(selector, self, namespaces, limit, **kwargs)
  File "/opt/anaconda3/lib/python3.8/site-packages/soupsieve/__init__.py", line 98, in select
    return compile(select, namespaces, flags, **kwargs).select(tag, limit)
  File "/opt/anaconda3/lib/python3.8/site-packages/soupsieve/__init__.py", line 62, in compile
    return cp._cached_css_compile(pattern, namespaces, custom, flags)
  File "/opt/anaconda3/lib/python3.8/site-packages/soupsieve/css_parser.py", line 208, in _cached_css_compile
    CSSParser(pattern, custom=custom_selectors, flags=flags).process_selectors(),
  File "/opt/anaconda3/lib/python3.8/site-packages/soupsieve/css_parser.py", line 1043, in process_selectors
    return self.parse_selectors(self.selector_iter(self.pattern), index, flags)
  File "/opt/anaconda3/lib/python3.8/site-packages/soupsieve/css_parser.py", line 894, in parse_selectors
    key, m = next(iselector)
  File "/opt/anaconda3/lib/python3.8/site-packages/soupsieve/css_parser.py", line 1036, in selector_iter
    raise SelectorSyntaxError(msg, self.pattern, index)
soupsieve.util.SelectorSyntaxError: Invalid character '/' position 0
  line 1:
//*[@id="module_product_title_1"]/div/div/span/text()
^
>>> 
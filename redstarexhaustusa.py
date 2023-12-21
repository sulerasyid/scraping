import requests
import bs4


def call_brands():
    url='https://redstarexhaustusa.com/vehicle-make'
    contents = requests.get(url)
    respond = bs4.BeautifulSoup(contents.text, 'html.parser')
    headlines = respond.find(attrs={'class' : 'center_bg'})
    subCategory  = headlines.find(attrs={'id':'subcategories'})
    subcategoryImages = subCategory.find_all(attrs={'class' : 'subcategory-image'})
    brands = []

    for subcategoryImage in subcategoryImages :
        url = subcategoryImage.find('a')['href']
        title = subcategoryImage.find('a')['title']
        item = {
        'url': url,
        'title': title
        }
        brands.append(item)
    return brands

def call_list():
    url='https://redstarexhaustusa.com/aston-martin'
    contents = requests.get(url)
    respond = bs4.BeautifulSoup(contents.text, 'html.parser')
    grids = respond.find_all('ul', {'class': 'product_list grid row'})
    for grid in grids :
        for litag in grid.find_all('li'):
            url = litag.find('a')['href']
            print (url)

# brands = call_brands()
# print(brands)
# list_data = call_list()
#https://redstarexhaustusa.com/porsche-992-911-turbo-headers
# https://redstarexhaustusa.com/aston-martin-db11-40-primary-downpipes
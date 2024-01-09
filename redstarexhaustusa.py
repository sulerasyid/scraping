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
def is_checked(tag):
    return tag.has_attr('checked')

def detail_url():
    url="https://redstarexhaustusa.com/aston-martin-db11-40-primary-downpipes"
    htmlPage = get_html(url=url)
    referenceHtml = htmlPage.find(attrs={'id':'product_reference'})
    ProductReference= referenceHtml.find(attrs={'class':'editable'})['content']
    productNameHtml = htmlPage.find(attrs={'class':'pb-center-column'})
    productName = productNameHtml.find('h1').string
    brand  = productNameHtml.find(attrs={'id':'product_manufacturer'}).find('a')['title']
    # specificOne = boxProductHtml.find(attrs={'class':'attribute_label'}).string
    # specificOneValueHtml = boxProductHtml.find(attrs={'class':'attribute_list'}).find('input',attrs={'name':'group_6'}).has_attr('checked')
    ShortDescription = htmlPage.find(attrs={'id':'short_description_content'}).find('span').text
    DataSheet = htmlPage.find(attrs={'class':'table-data-sheet'})

    boxProductHtmls = htmlPage.find(attrs={'class':'product_attributes clearfix'}).find_all('fieldset')
    for boxProductHtml in boxProductHtmls :
            print('A')
            print(boxProductHtml.find('label').text)
            print(boxProductHtml.find(is_checked).find_next_sibling('span').text)
            print('B')
    
    print(boxProductHtml)

def get_html(url):
    contents = requests.get(url)
    respond = bs4.BeautifulSoup(contents.text, 'html.parser')
    return respond

# brands = call_brands()
# print(brands)
list_data = call_list()
detail_page = detail_url()
#https://redstarexhaustusa.com/porsche-992-911-turbo-headers
# https://redstarexhaustusa.com/aston-martin-db11-40-primary-downpipes
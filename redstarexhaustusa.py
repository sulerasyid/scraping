import requests
import bs4
import  pandas as pd 

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

def call_list(url):
    # url='https://redstarexhaustusa.com/aston-martin'
    contents = requests.get(url)
    respond = bs4.BeautifulSoup(contents.text, 'html.parser')
    grids = respond.find_all('ul', {'class': 'product_list grid row'})
    urls =[]
    for grid in grids :
        for litag in grid.find_all('li'):
            url = litag.find('a')['href']
            urlItem = {
                'url':url
            }
            urls.append(urlItem)
    return urls
def is_checked(tag):
    return tag.has_attr('checked')

def detail_url(url):
    htmlPage = get_html(url=url)
    referenceHtml = htmlPage.find(attrs={'id':'product_reference'})
    ProductReference= referenceHtml.find(attrs={'class':'editable'})['content']
    productNameHtml = htmlPage.find(attrs={'class':'pb-center-column'})
    productName = productNameHtml.find('h1').string
    brand  = productNameHtml.find(attrs={'id':'product_manufacturer'}).find('a')['title']
    ShortDescription = htmlPage.find(attrs={'id':'short_description_content'}).text
    DataSheet = htmlPage.find(attrs={'class':'table-data-sheet'})
    specificOne =""
    specificOneValue =""
    specificTwo =""
    specificTwoValue =""
    specificThree =""
    specificThreeValue =""
    boxProductHtmls = htmlPage.find(attrs={'class':'product_attributes clearfix'}).find_all('fieldset')
    i = 0
    for boxProductHtml in boxProductHtmls :
            i = i+1
            if(i==1):
                specificOne=boxProductHtml.find('label').text
                specificOneValue=boxProductHtml.find(is_checked).find_next_sibling('span').text
            if(i==2) :
              specificTwo=boxProductHtml.find('label').text
              specificTwoValue=boxProductHtml.find(is_checked).find_next_sibling('span').text
            if(i==3) :
              specificThree=boxProductHtml.find('label').text
              specificThreeValue=boxProductHtml.find(is_checked).find_next_sibling('span').text
    item = {
        'url':url,
        'ProductReference':ProductReference,
        'Name':productName,
        'Brand':brand,
        'ShortDescription':ShortDescription,
        'specificOne':specificOne,
        'specificOneValue':specificOneValue,
        'specificTwo':specificTwo,
        'specificTwoValue':specificTwoValue,
        'specificThree':specificThree,
        'specificThreeValue':specificThreeValue,
        'DataSheet':DataSheet
    }
    return item

def get_html(url):
    contents = requests.get(url)
    respond = bs4.BeautifulSoup(contents.text, 'html.parser')
    return respond

dataCollect = []
brands = call_brands()
for brand in brands :
    brandUrl = brand['url']
    list_data_details = call_list(brandUrl)
    for list_data_detail in list_data_details :
        detail_page = detail_url(list_data_detail['url'])
        print("detail-->",detail_page)
        dataCollect.append(detail_page)

root = 'csv'
df = pd.DataFrame(dataCollect)
df.to_csv(root + '/redExhaust-full.csv', index=False)
print("finish")
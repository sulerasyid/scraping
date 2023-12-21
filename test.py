import requests
import json
import  pandas as pd 
import io, base64
from PIL import Image


def call_univ(page):
  url = 'https://api-frontend.kemdikbud.go.id/v2/search_pt'
  dataCollect = []
  errorCollect = []
  josnobj = {
    "keyword": "",
    "provinsi": "",
    "akreditas": "",
    "jenis": "",
    "status": "",
    "koordinasi": "",
    "tipe": "",
    "page": page
  }
  contents = requests.post(url,json=josnobj)
  response_dict = json.loads(contents.text)
  pts = response_dict["pt"]
  print("url--->",url)
  print("josnobj--->",josnobj)
  for pt in pts:
      print("pt",pt)
      img_data = pt["logo"]
      namapt =pt["nama"]
      file_name =""
      file_nameDB =""
      if img_data:
          try:
            remove_Slash = namapt.replace('/', '_')
            file_name =remove_Slash.replace(" ", "_")+".png"
            print("file_name===",file_name)
            img = Image.open(io.BytesIO(base64.decodebytes(bytes(img_data, "utf-8"))))
            img.save("colleges/"+file_name)
            file_nameDB ="colleges/"+file_name
          except:
            file_nameDB=""
            
            itemError = {
            'id_pt': pt["id"]
            }
            errorCollect.append(itemError)
            print("error uuid",pt["id"])

      item = {
          'id': pt["id"],
          'nama': pt["nama"],
          'akreditas': pt["akreditas"],
          'provinsi': pt["provinsi"],
          'lintang': pt["lintang"],
          'bujur': pt["bujur"],
          'jln': pt["jln"],
          'logo': file_nameDB,
          'npsn': pt["npsn"],
          'website': pt["website"],
          'no_tel': pt["no_tel"],
          'jumlah_prodi': pt["jumlah_prodi"],
          'rasio': pt["rasio"],
          'page':page
      }
      dataCollect.append(item)
  return dataCollect

root = 'csv'

full = []
for x in range(1):
  page = x+1
  print("page collect===",page)
  a = call_univ(page)
  full = a + full
 
df = pd.DataFrame(full)
df.to_csv(root + '/result-collect-full-31.csv', index=False)
print("finish collect data")
   
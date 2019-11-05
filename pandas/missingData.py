import  pandas as pd

url = "https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv"

data = pd.read_csv(url)

#print(data.columns) # sütunları döndürür.

#print(data[["City","Colors Reported","Shape Reported","State","Time"]].head()) # sütunları yazdırmak için kullanıldı.

#print(data.isnull().head(100)) # ilk 100 eleman arasında boş ise true döner dolu ise false döner
#print(data.notnull().head(100)) # ilk 100 eleman arasında boş ise false döner dolu ise true döner
#print(data.isnull().sum()) # burada ise sütunlarda toplam boş alanlarını döndürür.
#print(data[data.City.isnull()])# burada ise city sütunundaki boş alanları götürür.


print(data.shape) # boyutu döndürür.
#data = data.dropna(how = "all") # eğer tüm satır boş ise silinir
# data = data.dropna( how = "any")
#print(data) # satırda herhangi bir sütun boş ise satırı direk  siler.

# data = data.dropna(subset=['City',"Colors Reported"],how="all") # eğer ikisi boş ise silinecek
#data = data.dropna(subset=['City',"Colors Reported"],how="any") # eğer ikisinden biri  boş ise silinecek

data['Shape Reported'].fillna(value='Belirsiz',inplace=True) # shape reported boş olanları belirsiz diye değiştir.
print(data['Shape Reported'].value_counts(dropna=False)) # Eğer dropna true olursa  Boş olanları siler
# eğer dropna false olursa belirsiz alanları silmez

print(data.shape)


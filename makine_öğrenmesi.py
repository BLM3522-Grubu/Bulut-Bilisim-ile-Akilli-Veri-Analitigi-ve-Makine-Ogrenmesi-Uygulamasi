# -*- coding: utf-8 -*-
"""bulut_proje.jpynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cdnXzVhd-jfZ2WTZ3W8RLG1Nwm1LhEGz
"""

import pandas as pd
from sklearn.datasets import load_iris

# Veri setini yükle
iris = load_iris()

# Sütun adlarını düzelt
column_names = ['sepal_length_cm', 'sepal_width_cm', 'petal_length_cm', 'petal_width_cm']
df = pd.DataFrame(iris.data, columns=column_names)

# Hedef sütunu ekle
df['target'] = iris.target

# Yeni csv olarak kaydet
df.to_csv('iris.csv', index=False)
#iris data setti “iris” adlı bir çiçek türünün 3 farklı alt türünü ayırt etmek için kullanılır

#Gerekli Kütüphanelerin Kurulması
!pip install google-cloud-bigquery pandas

from google.colab import auth
auth.authenticate_user()

#Bu kod ile Google hesabı doğrulandı. Colab, BigQuery’ye güvenli bağlantı kurdu.

#BigQuery’ye erişip erişemediğini test edelim
from google.cloud import bigquery


project_id = "bulutmlprojesi"

# BigQuery istemcisini proje ID ile oluştur
client = bigquery.Client(project=project_id)

# Test sorgusu çalıştır
query = "SELECT 'Colab bağlantısı başarılı!' AS durum"
result = client.query(query).to_dataframe()
print(result)

# Bu işlemimiz Google Cloud’daki iris verisini Colab’e getirir.
from google.cloud import bigquery


project_id = "bulutmlprojesi"

# BigQuery istemcisi başlattık
client = bigquery.Client(project=project_id)

# SQL sorgusu ile iris verilerini aldık
query = """
SELECT * FROM `bulutmlprojesi.iris_dataset.iris_table`
"""

# Sonuçları DataFrame'e aktardık
df = client.query(query).to_dataframe()
#Veri doğrudan BigQuery üzerinden pandas veri çerçevesine aktarıldı
# İlk 5 satırı gösteriyoruz
print(df.head())

#Şimdi elimizde veri var, modeli eğitelim
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Özellikler ve hedef ayırdık
X = df.drop('target', axis=1)
y = df['target']

# Eğitim ve test verilerine ayırdık
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model oluşturdukk
model = DecisionTreeClassifier()

# Modeli eğittik
model.fit(X_train, y_train)

# Test verisiyle tahmin yaptık
y_pred = model.predict(X_test)

# Doğruluk oranını yazdırdıkk
print("Model Doğruluğu:", accuracy_score(y_test, y_pred))
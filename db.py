from datetime import datetime

import psycopg2

# PostgreSQL veritabanına bağlan
conn = psycopg2.connect(
    dbname="tests_db",
    user="postgres",
    password="",
    host="127.0.0.1",
    port="5433"
)

# Veritabanı bağlantısı üzerinde bir imleç oluştur
cur = conn.cursor()

# Test sonucunu ve tarih bilgisini al
test_result = "Test Passed"  # Varsayılan olarak test başarılı kabul edilir
timestamp = datetime.now()

# Çıktı sonucunu eklemek için SQL sorgusu
sql = "INSERT INTO test_results (result, timestamp) VALUES (%s, %s)"
data = (test_result, timestamp)

# SQL sorgusunu çalıştır
cur.execute(sql, data)

# Değişiklikleri kaydet
conn.commit()

# Bağlantıyı kapat
cur.close()
conn.close()

print("Test sonucu ve tarih başarıyla PostgreSQL veritabanına eklendi.")

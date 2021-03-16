import pandas as pd
import psycopg2
import os 
from dotenv import load_dotenv

load_dotenv()

df = pd.read_csv('saglik.csv', encoding='ISO-8859-9')


# Boş verileri doldurmak için işlemler

df = df[df['ILCE_ADI'].notna()]

df = df.fillna({'TELEFON': 'BILGI YOK', 'WEBSITESI': 'BILGI YOK', 'ADRES': 'BILGI YOK', 'ACIL_SERVIS': 'BILGI YOK', 'YATAK': 'null', 'AMBULANS': 'BILGI YOK', 'MAHALLE': 'BILGI YOK'})

# Veri tabanına bağlanmak için
connection = psycopg2.connect(f"host={os.getenv('HOST')} dbname={os.getenv('DB_NAME')} user={os.getenv('DB_USER')} password={os.getenv('DB_PASS')}")

# Veri tabanı üzerinde işlemler gerçekleştirebilmek için imleç
cursor = connection.cursor()

# Veri tabanı üzerine postgis eklentisini kurmak için
cursor.execute("""
    CREATE EXTENSION postgis;        
""")


# Verileri eklemek için
for index, row in df.iterrows():
    cursor.execute(f"""
        INSERT INTO "geoApp_saglik"
        VALUES ({int(index)+1},
                '{row['ILCE_ADI']}',
                '{row['ADI'].replace("'", "")}',
                '{row['ALT_KATEGORI']}',
                '{row['ADRES']}',
                '{row['TELEFON']}',
                '{row['WEBSITESI']}',
                '{row['ACIL_SERVIS']}',
                {row['YATAK']},
                '{row['AMBULANS']}',
                '{row['MAHALLE']}',
                ST_Point({row['BOYLAM']}, {row['ENLEM']}));
                """)

# İşlemleri commitlemek için
connection.commit()
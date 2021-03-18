# Blog yazısı linkleri
- [Django, LeafletJS ve Postgres ile Web Haritası Yapımı - 1. Kısım](https://volkandagdelen.medium.com/django-lafletjs-ve-postgres-ile-web-haritas%C4%B1-yap%C4%B1m%C4%B1-1-k%C4%B1s%C4%B1m-5be5a7d6f071)
- [Django, LeafletJS ve Postgres ile Web Haritası Yapımı - 2. Kısım](https://volkandagdelen.medium.com/django-lafletjs-ve-postgres-ile-web-haritas%C4%B1-yap%C4%B1m%C4%B1-2-k%C4%B1s%C4%B1m-79ade6e8811b)

# Repo'nun Amacı
- Bu repo blog yazısı için hazırlanmıştır.
- Blogtaki yazıdaki kodu takip etmekte zorlanan için kodların genel halini içeren bir yapı oluşturmak amacıyla oluşturulmuştur.

# Kullanılan veriler
- Eğitimde kullanılan veriler [IBB Açık Portal](https://data.ibb.gov.tr/) üzerinden temin edilmiştir ve [IBB Açık Veri Lisansı](https://data.ibb.gov.tr/license)'na sahiptir.
4.0 Uluslararası (CC BY 4.0) kapsamında lisanslanan kamu sektörü bilgilerini içerir

# Reponun içeriği
- Repo verileri ve bazı özelleştirmeleri doğrudan içermediği için indirilip kullanılmaya hazır değildir.
- Repo kodların bütünlüğünün takip edilmesi amacını taşımaktadır.
- requirements.txt içerisinde projede kullanılan python kütüphaneleri ve versiyon numaraları yer almaktadır. Eğer sizde bu gereksinimleri kurmak istiyorsanız.
``` pip install -r requirements.txt ``` komutunu dosyaları indirdikten sonra terminal üzerinden çağırabilirsiniz.
- csv2db.py dosyası csv dosyasının veritabanımıza python scripti aracılığı ile hızlıca aktarılması için yazılmış script kodlarını içerir.
- geoProject klasörü altında Django framework'u ile geliştirilmiş yapıyı içerir.
- src dosyası Leaflet.js aracılığı ile oluşturulmuş web haritası kodlarını içerir.

# Destek
- Kodlarda tespit edeceğiniz herhangi bir hata durumunda pull requests açmaktan veya benimle iletişime geçmekten çekinmeyin.

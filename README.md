# levenshtein_distance
Bu kod, iki kelimenin Levenshtein mesafesini hesaplayan ve bu mesafeden yola çıkarak benzerlik oranını bulan bir fonksiyon içermektedir. Aşağıda, kodun nasıl kullanılacağına dair bir örnek ve açıklama yer almaktadır.
## Nasıl Kullanılır
İlk adımda, `numpy` kütüphanesini içe aktarıyoruz:
``python
import numpy ``
Ardından, `minimum` ve `max` adında iki fonksiyon tanımlanmıştır. `minimum`, üç sayı arasındaki en küçüğü bulmak için kullanılırken, `max`, iki sayı arasındaki maksimumu bulmak için kullanılmaktadır.

`normalize` fonksiyonu, bir metni belirli bir boyuta normalleştirmek için kullanılır. Eğer verilen metnin uzunluğu belirtilen boyuttan küçükse, eksik karakterleri boşluk karakteriyle doldurur.

`levenshteinMesafesi` fonksiyonu, iki kelimenin Levenshtein mesafesini hesaplar. Bu mesafe, iki kelimenin birbirine dönüştürülmesi için gereken minimum düzenleme işlemi sayısını temsil eder. Fonksiyon, verilen kelimelerin uzunluklarını dikkate alarak bir matris oluşturur ve Levenshtein mesafesini hesaplamak için bu matrisi kullanır.

Kullanıcıdan iki kelime istenir ve `normalize` fonksiyonu kullanılarak bu kelimeler normalleştirilir.

`levenshteinMesafesi` fonksiyonu, normalleştirilmiş kelimeleri kullanarak Levenshtein mesafesini hesaplar.

`Kodu çalıştırdığınızda, sırasıyla iki kelimeyi girmeniz istenecek ve sonuçlar ekrana yazdırılacaktır.`

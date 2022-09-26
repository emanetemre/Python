# Python Soket Programlama

```python
import socket

soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname()
port = 444

soket.bind((host, port))
soket.listen(3)

while True:
    clientsocket, address = soket.accept()
    
    print("bağlantı gönderildi " % str(address))

    mesaj = 'merhaba, sunucuya bağlantı attığın için sağol' + "\r\n"
    clientsocket.send(mesaj)

    clientsocket.close()
```
##### Address Family
* `AF_INET` - Internet Protocol version 4 (IPv4): 
* İnternet adresleri kullanılarak farklı makinalardaki yazılımların haberleşmesi için kullanılır.Fakat istenirse aynı makinadaki yazılımlar da biri biriyle bu soket türünü kullanarak haberleşebilirler.
* `AF_UNIX` - Unix File System
* Haberleşme aynı makinada çalışan iki yazılım arasında yerel olarak dosya sistemi üzerinden gerçekleşir. buyüzden veri kaybı ve paketlerin yeniden sıralanması gibi durumlar oluşmaz. Bu nedenle haberleşme başarımı yüksektir.
* `AF_IPX` - Novell IPX/SPX
* `AF_APPLETALK` - AppleTalk DDP
* `AF_NETBIOS` - NetBIOS
* `AF_INET6` - Internet Protocol version 6 (IPv6)
* `AF_IRDA` - Infrared Data Association (IrDA)
* `AF_BTH` - Bluetooth
* `AF_X25` - Reserved for X.25 Project

##### Socket Type
* `SOCK_STREAM` --> TCP
* Stream soketler TCP protokolune uygun olarak paket gönderiminde bulunurlar yani güvenilir iki yönlü iletişim kanallarıdır.Bir paket gönderdiklerinde gidip gitmediği ile ilgili bilgi döndürene kadar kendilerini kapatmazlar paketler eksik veya farklı sırada gönderilmez.
* `SOCK_DGRAM` --> UDP
* Datagram soketler IP protokolüne göre çalısır ve TCP yerine UDP. kullanırlar burada iletimdaha hızlı olur fakat Stream soketlere nazaran hata payı artar paketler sırasız yada eksik gönderilebilir ve Datagram soketler bunu kontrol etmez paket gonderildigi anda kapanırlar.
* `SOCK_RAW` --> Raw Socket

### Örnek Kod


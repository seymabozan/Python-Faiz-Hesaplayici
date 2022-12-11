
print(".*.*.*.*.*.*Welcome to the Interest Calculator*.*.*.*.*.*.")

İsim = input("Adınızı giriniz: ")
Kredi_tutari = float(input("Kredi tutarını giriniz: "))
Yillik_faiz_orani = float(input("Yıllık faiz oranını giriniz: "))
Maksimum_yil = int(input("Kredi vadesini yıl olarak giriniz: "))
Maksimum_ay = int(input("Kredi vadesini ay olarak giriniz: "))
Yineleme_araligi = int(input("Yineleme aralığını giriniz: "))


Toplamfaiz = (Kredi_tutari/100)*(Yillik_faiz_orani/12)*(Maksimum_yil*12+Maksimum_ay)

Toplam_odeme = Toplamfaiz/((Maksimum_yil*12+Maksimum_ay) / Yineleme_araligi)

def print_duration(ay):
    yil = ay / 12
    ay = ay % 12
    print("Yıl: %d , ay: %d" % (yil, ay)) # Yazdığımız rakamı ekrana yıl ve ay olarak yazdıracak #

def print_money(para):
    sayı = para  # Yazılan sayıyı para birimi olarak kabul edicek #
    sayı = int(sayı*10)
    sayı = sayı / 10
    print("{}0$".format(sayı))

def print_entry(Kredi_tutari, Yillik_faiz_orani, ay): # Süre ve para türlerinin yazılması icin 1. ve 2. işlev çağrılıyor #
    print("----------------------------")
    print_duration(ay)
    print("Total payment:")
    print_money(Kredi_tutari)
    print("Monthly payment:")
    print_money(Yillik_faiz_orani)
    print("----------------------------")


def print_full_report(Kredi_tutari, Yillik_faiz_orani, Yineleme_araligi, Maksimum_yil, Maksimum_ay, Toplam_odeme, İsim):
    print("Report for %s")
    a = Yineleme_araligi
    while a<= (Maksimum_yil*12+Maksimum_ay):
        Kredi_tutari = Kredi_tutari + Toplam_odeme
        Aylik_odeme = Kredi_tutari / a # Aylık ödemenin ne kadar ödenmisinin hesaplanması için formül yazılıyor #
        print_entry(Kredi_tutari, Aylik_odeme, a)
        a = a + Yineleme_araligi

print_full_report(Kredi_tutari, Yillik_faiz_orani, Yineleme_araligi, Maksimum_yil, Maksimum_ay, Toplam_odeme, İsim)

c=print()












import play 
from random import randint  

w = play.screen.width
h = play.screen.height

# Programın arayüzü
box1 = play.new_box(color="light green", x=-200, y=0, width=100, height=200, border_width=5, border_color="pink")
box2 = play.new_box(color="light green", x=0, y=0, width=100, height=200, border_width=5, border_color="pink")
box3 = play.new_box(color="light green", x=200, y=0, width=100, height=200, border_width=5, border_color="pink")

hello = play.new_text(words="Selam, tuşa basarak şansını dene!", x=0, y=250, font_size=40, color="blue")
win = play.new_text(words="KAZANDIN!", x=0, y=-250, font_size=50, color="green")
lose = play.new_text(words="Kaybettin, tekrar dene!", x=0, y=-200, font_size=50, color="red")
result = play.new_box(color="yellow", x=0, y=170, width=200, height=50)
result_text = play.new_text(words="Hadi, başla!", x=0, y=170, font_size=40)

# Rastgele sayıların gösterileceği alanlar
num1_text = play.new_text(words='', x=-200, y=0, font_size=100)
num2_text = play.new_text(words='', x=0, y=0, font_size=100)
num3_text = play.new_text(words='', x=200, y=0, font_size=100)

# Deneme sayacı
attempts_text = play.new_text(words="Deneme: 0", x=0, y=-250, font_size=30, color="black")
attempts = 0

@play.when_program_starts # program başladığında 1 kere çalışır başlangıç ayarları yapılır 
def start():
    num1_text.hide() # 1. sayı gizlendi
    num2_text.hide() 
    num3_text.hide()
    win.hide() # kazanma yzısı gizlendi
    lose.hide() # kaybetme yazısı gizlendi

@result.when_clicked # hadi başla butonuna tıklandığında yapılacak eylemler 
async def clicked():
    global attempts
    attempts += 1
    attempts_text.words = f"Deneme: {attempts}"  # Sayaç güncelleniyor

    # Rastgele sayılar oluşturuluyor
    num1, num2, num3 = randint(0, 9), randint(0, 9), randint(0, 9)

    num1_text.words, num2_text.words, num3_text.words = str(num1), str(num2), str(num3)

    # Sayılar yavaşça belirsin
    num1_text.show()
    await play.timer(seconds=0.5)
    num2_text.show()
    await play.timer(seconds=0.5)
    num3_text.show()
    
    # Kazanma kontrolü
    if num1 == num2 == num3: # 3 sayıda birbirine eşitse kazanacağız
        win.show()
        result.color = "light green"
        result_text.words = "Kazandın!"
    else:
        lose.show()
        result.color = "red"
        result_text.words = "Tekrar dene!"
    
    await play.timer(seconds=2.0)
    
    # Ekranı temizle
    num1_text.hide()
    num2_text.hide()
    num3_text.hide()
    win.hide()
    lose.hide()
    result.color = "yellow"
    result_text.words = "Hadi, başla!"

play.start_program()

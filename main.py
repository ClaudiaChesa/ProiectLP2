"""
Proiect LP2
Echipa: 12-E3
Studenti: Burduşel Giovanna-Andreea, Cheșa Claudia-Mihaela
Tema proiect: D9-T1 | Testarea unei aplicații web
Cerinta: Dezvoltati un script pentru platforma Facebook ce testează: login, funcția de afișare detaliată și funcția de apreciere a unei postări.
Surse folosite:
  -https://selenium-python.readthedocs.io/
  -geeksforgeeks.org/move_by_offset-action-chains-in-selenium-python/?fbclid=IwAR0cECCrFUgX5oaV-8hHvTkteHhP6h6LUUiLPxaCsZahrh5QKiFLpyuXz3Q
  -https://python-forum.io/thread-20543.html?fbclid=IwAR0r_4ZBlR8_dI5bSDb5ukOHNKUxrpiwpyU2ry0mRGJl3mK0pw2t28WqbVY
  -https://www.youtube.com/watch?v=kpxfcaIh9ZY
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains

#Vom utiliza Options() pentru a bloca orice notificare tip pop-up ce poate aparea dupa logare
option = Options()
login = True

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")


option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})

# Initializarea browserului Chrome prin intermiediul chromedriver
browser = webdriver.Chrome(options=option, executable_path="D:\AN II ETC\SEM II\LP2\PROIECT\chromedriver.exe")

# Navigarea catre pagina de login Facebook
browser.get("https://ro-ro.facebook.com/login/web/")

# Gasirea butonului care accepta cookies-urile si apasarea lui

browser.find_element_by_xpath('//*[@title="Acceptă tot"]').click()

#Gasirea elementelor ce constituie login-ul propriu-zis : Campul pentru email/username, campul pentru parola
# si respectiv butonul de logare propriu zis precum si transmiterea cheilor catre aceste campuri si apasarea butonului
time.sleep(3)
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit = browser.find_element_by_id("loginbutton")
username.send_keys("testLP2Timisoara@gmail.com")
password.send_keys("Vrem10lalp")
submit.click()
time.sleep(5)

#Daca dupa o perioada de 5 secunde este inca prezent butonul de login inseamna ca logarea nu a reusit
try:
  browser.find_element_by_id("loginbutton").is_displayed()
  login = False
  time.sleep(3)
  print("Logarea NU a reusit, valoarea variabilei login este: ", login)     #si inchiderea browserului daca login-ul a esuat
  browser.quit()
except:
  print("Logarea a reusit, valoarea variabilei login este: ", login)


#Gasirea si apasarea butonului "Home"
browser.find_element_by_xpath('//*[@aria-label="Home"]').click()
time.sleep(5)

#Gasirea campului de postare si apasarea acestuia
browser.find_element_by_xpath('//*[@class="m9osqain a5q79mjw jm1wdb64 k4urcfbm"]').click()
time.sleep(3)

#Trimiterea descrierii postarii
browser.switch_to_active_element().send_keys("Proiect LP2")
time.sleep(5)

#Gasirea elementului prin care poate fi incarcata o poza
path = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div[1]/input")
time.sleep(2)

#Trimiterea pozei dorite catre postare
path.send_keys("D:\AN II ETC\SEM II\LP2\PROIECT\Poza.jpg")
time.sleep(2)

#Postarea propriu-zisa a continutului trimis prin cheile anterioare
browser.find_element_by_xpath('//*[@aria-label="Post"]').click()
time.sleep(5)

#Navigarea catre pagina personala de facebook
browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/ul/li/div/a/div[1]/div[2]/div/div/div/div/span/span").click()
time.sleep(3)

#Utilizare metodei scrollBy pentru a vedea continutul postat anterior
browser.execute_script("window.scrollBy(0,1000)","")
time.sleep(3)

try:
    #Mutarea cursorului in pozitia mentionata prin cei doi parametrii ai functiei move_by_offset si apasarea elementului
    #care se afla in acea pozitie, respectiv ultima postare pentru afisarea ei detaliata

    action = ActionChains(browser)
    action.move_by_offset(929, 451).click().perform()
    print("Afisarea detaliata a imaginii a reusit")
    time.sleep(5)

    try:
        #Adaugarea numelor persoanelor care au dat initial like la postare intr-o lista
        nr_like_initial_text = []
        for elem in browser.find_elements_by_xpath('.//span[@class = "pcp91wgn"]'):
            if (elem.text != ""):
                nr_like_initial_text.append(elem.text)

        print("Numele persoanelor care au dat like initial este:" + str(nr_like_initial_text))

        #Gasirea butonului care acorda like-ul si apasarea acestuia
        browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[2]/div/div/div/div[1]/div[1]").click()
        time.sleep(3)

        # Adaugarea numelor persoanelor care au dat like la postare dupa executarea programului intr-o lista
        nr_like_final_text = []
        for elem in browser.find_elements_by_xpath('.//span[@class = "pcp91wgn"]'):
            if (elem.text != ""):
                nr_like_final_text.append(elem.text)

        print("Numele persoanelor care au dat like dupa rularea programului este:" + str(nr_like_final_text))

        #Compararea numarului elementelor dintre cele doua liste pentru a vedea daca acordarea like-ului a decurs cu succes
        if(len(nr_like_final_text) > len(nr_like_initial_text)):
            print("Numarul de like-uri a fost incrementat cu succes -> REUSIT")
        else:
            print("Numarul de like-uri nu a fost incrementat ->NEREUSIT")
        time.sleep(3)
        browser.quit()
    except:
        print("Acordarea like-ului nu a reusit")
        time.sleep(3)
        browser.quit()
except:
    print("Afisarea detaliata a imaginii nu a reusit")
    time.sleep(3)
    browser.quit()
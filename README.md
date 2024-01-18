Projektu veidoja Jānis Lauris Vilmanis 1.kurss 2.grupa (231RDB303), Daniels Draška 1.kurss 3.grupa (231RDB239) 

 

Projekta uzdevums: 

 

Veidojot automobīļu pārdošanas uzņēmumu 'IK Perekupi' ir svarīgi pētīt automobīļu tirgu un tirgus cenas sludinājumu portālos, lai varētu analizēt, kāda ir vidēja tirgus cena
automobīlim un ar kādu cenu, būtu izdevīgāk nopirkt vai pārdot automobīli.
Lai varētu automatizēt šo procesu, tika izveidots projekts, kas ļauj ievadīt automobīļa marku un modeli un caur sludinājuma portālu 'SS.COM' 
nolasīt informāciju par automobīļiem, piemēram, cena, motora tilpums, izlaišanas gads un modelis. Izveidotais projekts nolasa automobīļu cenas, 
saglabā tos excel failā, aprēķina vidējo automobīļu cenu un rāda automobīļus, kas ir zem vidējas cenas, kuru būtu izdevīgi pārpārdot. Izmantojot šo projektu, 
uzņēmuma darbiniekiem tiek atvieglots meklēšanas process.  

Izmantotās bibliotēkas: 
Selenium: Lai varētu strādāt ar mājaslapu pārlūk programmam, piemēram, datu iegūšanas nolūkos. 

Importēšana: 

Import selenium 

Papildus importi: 

from selenium import webdriver: Pārlūka saraksta vadītāja importēšana. 

from selenium.webdriver.chrome.service import Service: Chrome pārlūka servisa importēšana. 

from selenium.webdriver.common.by import By: Elementa atrašanās veida importēšana. 

from selenium.webdriver.common.keys import Keys: Klaviatūras darbību veida importēšana. 

 

OpenPyXL: 

Mērķis: Darbības ar Excel failiem (lasīšana, rakstīšana, rediģēšana). 

Importēšana: import openpyxl 

Papildus importi: 

from openpyxl import Workbook, load_workbook: Darba grāmatas un tās ielādes importēšana. 

Time: 

Mērķis: Nodrošina funkcionalitāti saistībā ar laiku. 

Importēšana : import time 
 

Programmatūras izmantošanas metodes: 
 
 
driver.get("https://www.ss.com/lv/transport/cars/") - Atver norādītā pārlūka URL. 

find = driver.find_element(By.LINK_TEXT, auto) - Atrod elementu lapā, kas atbilst norādītajam selektoram (by) un vērtībai (value). 

find.click()  - Veicina pogas uzspiešanu uz atrastā elementa. 

find.clear() -  Notīra teksta lauku (input elementu). 

find.send_keys(modelis) - Ievada tekstu teksta laukā. 

x = driver.find_elements(By.CLASS_NAME, 'amopt') - Atrod visus elementus lapā, kas atbilst norādītajam by un value vērtībām. 

Piemērs: x = driver.find_elements(By.CLASS_NAME, 'amopt') 

ws.append([nobr_list[i], mod_list[i], gad_list[i], tilp_list[i], cena_list[i]])  - Pievieno rindu excel lapā ar norādītajiem datiem. 

wb_test.save("cars.xlsx") - Saglabā izmaiņas excel lapā ar norādīto faila nosaukumu. 

wb_test.close() - Aizver excel. 

driver.quit() - Aizver pārlūka sesiju. 

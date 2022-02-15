from pickle import TRUE
import re


dict_start = {'satzart' : 0, 'kdnr' : 1 , 'artbez' : 49 , 'lime' : 82 , 'vkp' : 89 , 'ekp' :  99 , 'ean' : 191 }
dict_end   = {'satzart' : 1, 'kdnr' : 8 , 'artbez' : 80 , 'lime' : 89 , 'vkp' : 99 , 'ekp' : 109 , 'ean' : 204 }

source = "Hama.inv"



pattern = re.compile(r'\A0*')

# [\A0*\"*;]
# r"\b0*([1-9][0-9]*|0)\b"
# '\A0*'

data_list = []

with open(source, "r") as datei:
    #znr = 0
    for zeile in datei:
        if zeile[0] == 'B':
            # In der Zeile die benötigten Daten auslesen
            for key in dict_start:
                s = dict_start[key]
                e = dict_end[key]
                cdata = zeile[s:e]
                # Führende Nullen entfernen
                if key == 'vkp' or key == 'ekp':
                    redata = re.sub(pattern,'',cdata)
                    # Dezimalstelle 
                    redata = int(redata) /100
                else:
                    # führende Nullen weg und ggf. Sonderzeichen entfernen
                    redata = re.sub(pattern, '', cdata) 
                
                # wenn was gefunden wurde, dann drucken wir das
                if redata:
                    print(key+": ", redata)
                    data_list.append(redata)
                    # for debug
                    #print(data_list)

            # hier muss ein /n an das Listenende geschrieben werden    
            #data_list.append(temp)
            #data_list.append(str('\n'))  
            #with open('abc.txt', 'w') as temp_file:
             #   for item in data_list:
              #      temp_file.write(item)
#file = open('abc.txt', 'r')
#print(file.read())       
#for i in data_list:
#print(data_list,  end='\n') 
#print(data_list, sep=',', end='\n', file=sys.stdout, flush=False)

#print(data_list)

# with open('test.csv', 'w', newline=' ') as file:
#     writer = csv.writer(file, quoting=csv.QUOTE_NONE ,delimiter=';')
#     writer.writerows(data_list)

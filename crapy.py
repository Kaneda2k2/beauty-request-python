

#Call request.get() to dowload file
#Call open() with "wb" to create a n ew file in write binary mode.
#Loop over the Response object iter_content()  method ##iter_content()
#write() on each iteration to write the content to the file
#call close() to close the file .

##import requests
##res=requests.get("https://automatetheboringstuff.com/files/rj.txt")
##type(res)
##print(res.status_code==requests.codes.ok)  ##revisa si esta todo ok
#####True
##print(len(res.text)) ##comprueba el peso del documento
#####178961  #lo que pesa el texto
##print(res.text[:250])###Texto desde el 0 hasta el 250
##########################################

##import requests
##res=requests.get("https://automatetheboringstuff.com/files/No exists.txt")
##res.raise_for_status()   ## Se añade esta linea para comprobar el status del servicio y si existe o no

#########################################

##import requests
##
##res=requests.get("https://automatetheboringstuff.com/files/No exists.txt")
##
##try:
##    res.raise_for_status()
##except Exception as exc:
##    print("there was a problem: %s"%(exc))
##

#  IMPRIMIR EL PROBLEMA CON UN TRY

###########SAVING DOWNLOAD FILES TO THE HARD DRIVE

##import requests
##res=requests.get('https://automatetheboringstuff.com/files/rj.txt')
##res.raise_for_status()
##playFile=open("romeoyjulieta.txt","wb") ##creamos el archivo  "wb" binari mode
##for chunk in res.iter_content(100000):  #iter_content()method retunrs "Chunks" cara itineracion con el lop
##    playFile.write(chunk)
##
##playFile.close()

# Dont USE REGULAR EXPRESSION TO PARSE HTML

#Parsing html ocn bs4 modulo

#Beautiful Soup is a ,pdiñe fpr extractomg omfpr,atopm frp, am html

######################################


import requests , bs4
res=requests.get('https://nostarch.com')  #descargamos la pagina
res.raise_for_status()
noStartchSoup=bs4.BeautifulSoup(res.text, 'html.parser')  #retornamos el beautifulsouo objec y lo retornamos en una variable llamada nostarchsoup
print(type(noStartchSoup))   ##

######################################
##por si quieres parsear el dato de tu hard drive

##exampleFile = open('example.html')
##exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')  #lxml
##type(exampleSoup)

#########################################
##Selector passed to the select() method Will match . . .
##soup.select('div') All elements named <div>
##soup.select('#author') The element with an id attribute of author
##soup.select('.notice') All elements that use a CSS class attribute
##named notice
##soup.select('div span') All elements named <span> that are within
##an element named <div>
##soup.select('div > span') All elements named <span> that are
##directly within an element named <div>,
##with no other element in between
##soup.select('input[name]') All elements named <input> that have a
##name attribute with any value
##soup.select('input[type="button"]') All elements named <input> that have an
##attribute named type with value button

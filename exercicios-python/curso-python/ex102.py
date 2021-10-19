from os import read
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.cruzeiro.com.br')
except urllib.error.URLError:
    print('O site Cruzeiro não está acessível no momento.')
else:
    print('O site Cruzeiro está acessível!')
    print(site.read())
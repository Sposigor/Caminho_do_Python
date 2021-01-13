import urllib.request, urllib.error

try:
    urllib.request.urlopen('https://www.cursoemvideo.com/')
except urllib.error.URLError:
    print('O site não está no ar')
else:
    print('Acessou com sucesso')

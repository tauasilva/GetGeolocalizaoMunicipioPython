import requests

print('Informe o nome do municipio seguindo o modelo : Novo_Hamburgo / Campo_Bom / Porto_Alegre / São_Paulo')
municipio = input('Municipio:')

url = 'https://pt.wikipedia.org/wiki/'+municipio

r = requests.get(url)
r.text

posicao_ini = r.text.index('http://tools.wmflabs.org/geohack/geohack.php?pagename=')

NewURL = (r.text[posicao_ini:r.text.index('<span title="Mapas')-2])
if NewURL.index('amp;') > 0:
    NewURL = NewURL[0:NewURL.index('amp;')] + NewURL[NewURL.index('amp;')+4:5000]

r = requests.get(NewURL)
r.text

posicao_ini = r.text.index('<span class="latitude" title="Latitude">')
posicao_ini = posicao_ini+40
stringAux = r.text[posicao_ini:50000]
posicaoFim = stringAux.index('</span>')
latitude = stringAux[0:posicaoFim]
stringAux = stringAux[posicaoFim+52:50000]
posicaoFim = stringAux.index('</span>')
longitude = stringAux[0:posicaoFim]

print('latitude: ' + latitude)
print('longitude: ' + longitude)
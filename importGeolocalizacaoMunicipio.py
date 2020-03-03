import requests

municipio = 'ALTO_ALEGRE_DOS_PARECIS'

url = 'https://tools.wmflabs.org/geohack/geohack.php?pagename='+municipio+'&params=29_40_40_S_51_07_51_W_type:city_region:BR'
r = requests.get(url)
r.text
posicao_ini = r.text.index('<span class="latitude" title="Latitude">')
posicao_ini = posicao_ini+40
stringAux = r.text[posicao_ini:50000]

posicaoFim = stringAux.index('</span>')

latitude = stringAux[0:posicaoFim]
stringAux = stringAux[posicaoFim+52:50000]

posicaoFim = stringAux.index('</span>')

longitude = stringAux[0:posicaoFim]

print(latitude)
print(longitude)
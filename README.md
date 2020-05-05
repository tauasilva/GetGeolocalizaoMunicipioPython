# Overview
- Script desenvolvido para buscar a Geolocalização de um município utilizando a https://www.wikipedia.org/

## Sumary

- [How to Setup](#how-to-setup)
- [Scripts](#scripts)
- [Developers](#developers)

## How to Setup

first clone or download the repository

```
git clone https://github.com/tauasilva/GetGeolocalizaoMunicipioPython.git
```

After that you can install the dependencies by executing the following command in the root folder of the project

```
pip install -q requests
```

**Development Mode**

Run the following script to start the aplicattion on development mode with a watcher for file changes

```
python3 importGeolocalizacaoMunicipio.py 
```

## Scripts

```
Script monta uma URL dinamicamente com o nome do município  e faz um get na pagina da wikipedia.com.org, com a resposta do request o script faz um varredura de alguns dados para fazer um novo request para o wmflabs.org, através dessa página web podemos obter a posição de latitude e longitude no meio do HTML
```


## developers
```
Tauã Fagundes da Silva
```



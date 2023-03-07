from pytube import YouTube

def downloadyt(url):
  objetoyt = YouTube(url)
  objetoyt = objetoyt.transmissoes_maior_resolucao()
  try:
    objetoyt.download()
    print("Título:", objetoyt.title)
    print("Download completo com sucesso.")
  except:
    print("Não foi possível completar o download:")

url = input("Digite a URL do vídeo do YouTube: ")
downloadyt(url)
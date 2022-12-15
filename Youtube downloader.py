
from pytube import YouTube

# URL colocada pelo usuario
url = input("Coloque o link do audio que deseja baixar: ")

# Nome do Arquivo
_filename = input("Digite o nome do arquivo: ")

# Para selecionar o formato
audio = ".mp3"
video = ".mp4"

escolha = input("Escolha o formato: \n 1- Audio \n 2- Video \n R: ")

if escolha == "1":
    formato = f"'%s' {audio}" % _filename
elif escolha == "2":
    formato = f"'%s' {video}" % _filename
else:
    print("O formato escolhido é invalido, escolha entre 1 e 2")

# Para escolher o destino

dict = {"1": "C:\\Users\\alexa\\Downloads",
        "2": "C:\\Users\\alexa\\Music", "3": "C:\\Users\\alexa\\Videos"}

destination = input(
    "Selecione uma das opções para pasta de destino: \n 1-Downloads \n 2-Music \n 3-Videos \n R: ")

if destination == "1":
    output_path = dict["1"]
elif destination == "2":
    output_path = dict["2"]
else:
    output_path = dict["3"]


print("Aguarde....")
YouTube(url).streams.first().download(
    output_path=output_path, filename=formato)

print("Download realizado :)")


""" # importing packages
from pytube import YouTube
import os
  
# url input from user
yt = YouTube(
    str(input("Enter the URL of the video you want to download: \n>> ")))
  
# extract only audio
video = yt.streams.filter(only_audio=True).first()
  
# check for destination to save file
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'
  
# download the file
out_file = video.download(output_path=destination)
  
# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
  
# result of success
print(yt.title + " has been successfully downloaded.") """

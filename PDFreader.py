#Transformar PDF em Imagens
#Ler essas imagens e extrair textos delas
#Renomerar os PDFs 

import os
from pikepdf import Pdf
from pikepdf import PdfImage
import shutil

file = os.listdir("Documentos")
index = 0


while index < len(file):
   
    os.makedirs("PastaCaminho", exist_ok=True)

    arquivo = Pdf.open(f"Documentos/{file[index]}")
    pagina_1 = arquivo.pages[0]

    for nome, imagem in pagina_1.images.items():
        imagem_salvar = PdfImage(imagem)
        
        imagem_salvar.extract_to(fileprefix=f"PastaCaminho/{index + 1}")
        lista_imagens = os.listdir("PastaCaminho")

        shutil.move(f"PastaCaminho/{lista_imagens[0]}", "Imagens")
        print(f"Arquivo {file[index]} lido com sucesso!")

    index += 1
    if index == len(file):
        shutil.rmtree("PastaCaminho")

from PIL import Image
import pytesseract
caminho = "C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho + "\\tesseract.exe"
# Carregar a imagem
img = Image.open('2.jpg')

# Converter a imagem para texto usando pytesseract
texto = pytesseract.image_to_string(img)

# Imprimir o texto extraído
print(texto)

os.rename("Documentos/RG.pdf", "Documentos/RGB.pdf")


import pytesseract
import cv2

#Passo 1 - Ler a imagem
imagem = cv2.imread("test.png")

caminho = r"C:\Program Files\Tesseract-OCR"

#Passo 2 - Pedir para o tesseract extrair o texto da imagem
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
texto = pytesseract.image_to_string(imagem, lang="por")

print(texto)
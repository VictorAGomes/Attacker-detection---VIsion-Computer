import cv2
from ultralytics import YOLO
import pygame
import threading

# Inicializar o pygame mixer
pygame.mixer.init()

alarmeCtl = False

def alarme():
    global alarmeCtl
    sound = pygame.mixer.Sound('unplug.oga')
    for _ in range(7):
        sound.play()
        pygame.time.wait(500)  # Espera 500 milissegundos entre os toques do alarme

    alarmeCtl = False

video = cv2.VideoCapture('ex01.mp4')
modelo = YOLO('yolov8n.pt')

area = [510, 230, 910, 700]

# Verifica se o vídeo foi aberto corretamente
if not video.isOpened():
    print("Erro ao abrir o arquivo de vídeo")
    exit()

# Obter informações do vídeo original
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(video.get(cv2.CAP_PROP_FPS))

# Define o codec e cria o objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, fps, (1270, 720))

while True:
    check, img = video.read()
    if not check:
        break
    img = cv2.resize(img, (1270, 720))
    img2 = img.copy()
    cv2.rectangle(img2, (area[0], area[1]), (area[2], area[3]), (0, 255, 0), -1)
    resultado = modelo(img)

    for objects in resultado:
        obj = objects.boxes
        for data in obj:
            x, y, w, h = data.xyxy[0]
            x, y, w, h = int(x), int(y), int(w), int(h)
            cls = int(data.cls[0])
            cx, cy = (x + w) // 2, (y + h) // 2
            cv2.circle(img, (cx, cy), 5, (0, 0, 0), 5)
            if cls == 0:
                cv2.rectangle(img, (x, y), (w, h), (255, 0, 0), 2)

                if cx >= area[0] and cx <= area[2] and cy >= area[1] and cy <= area[3]:
                    cv2.rectangle(img2, (area[0], area[1]), (area[2], area[3]), (0, 0, 255), -1)
                    cv2.rectangle(img2, (100, 30), (470, 80), (0, 0, 255), -1)
                    cv2.putText(img2, "INVASOR DETECTADO", (105, 65), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
                    if not alarmeCtl:
                        alarmeCtl = True
                        threading.Thread(target=alarme).start()

    imgFinal = cv2.addWeighted(img2, 0.5, img, 0.5, 0)

    # Grava o frame no arquivo de saída
    out.write(imgFinal)

    cv2.imshow('img', imgFinal)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera os objetos VideoCapture e VideoWriter
video.release()
out.release()
cv2.destroyAllWindows()
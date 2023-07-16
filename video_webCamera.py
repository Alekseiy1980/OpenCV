import cv2

cap = cv2.VideoCapture(0) # Подключаем вебку(0 - это первая вебка 1 - это вторая вебка) если вебки нет вместо 0 пишим адресс видео как в с img

while True:
    success, frame = cap.read() # получаем картинку
    cv2.imshow('Camera', frame )

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

import cv2

face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") # подключаем нейросеть работающая с лицами
'''
Нейросеть работает с картинкой 
'''

# img = cv2.imread("faces.jpg")
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Меняем цветную картинку на черно-белую
# faces = face_cascades.detectMultiScale(img_gray)
#
# for ( x, y, w, h) in faces:     # перебираем координаты для нахождения лиц и и отрисовки рамок
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#
# cv2.imshow('Result', img) # # Выводим саму картинку( 'Result' -это названия открывающегося окна,img - это наша картинка
# cv2.waitKey(0)

'''
Нейросеть работает с вебкамерой ( можно подключить видео вместо камеры) 
'''

cap = cv2.VideoCapture(0) # Подключаем вебку(0 - это первая вебка 1 - это вторая вебка) если вебки нет вместо 0 пишим адресс видео как в с img

while True:
    success, frame = cap.read() # получаем картинку
    # cv2.imshow('Camera', frame )

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Меняем цветную картинку на черно-белую
    faces = face_cascades.detectMultiScale(img_gray)

    for ( x, y, w, h) in faces:     # перебираем координаты для нахождения лиц и и отрисовки рамок
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('Result', frame)  # # Выводим саму картинку( 'Result' -это названия открывающегося окна,img - это наша картинка
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

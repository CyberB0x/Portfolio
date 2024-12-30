import cv2
import numpy as np

# Функция для нахождения контура с максимальной площадью
def get_largest_contour(contours):
    max_contour = None
    max_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            max_contour = contour
    return max_contour

# Инициализация видеопотока с веб-камеры
cap = cv2.VideoCapture(0)

# Используем метод вычитания фона для отслеживания движения
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Преобразование кадра в черно-белый для упрощения обработки
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Применение метода вычитания фона
    fgmask = fgbg.apply(gray)

    # Уменьшение шума с помощью морфологических операций
    kernel = np.ones((5, 5), np.uint8)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)

    # Поиск контуров
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Выделяем наибольший контур
    largest_contour = get_largest_contour(contours)
    if largest_contour is not None:
        x, y, w, h = cv2.boundingRect(largest_contour)
        # Рисуем квадрат вокруг объекта
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Отображаем фокус в центре квадрата
        cv2.circle(frame, (x + w // 2, y + h // 2), 5, (0, 0, 255), -1)

    # Отображение оригинального видео с наложением
    cv2.imshow("Motion Tracking", frame)

    # Нажмите "q" для выхода
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение ресурсов
cap.release()
cv2.destroyAllWindows()

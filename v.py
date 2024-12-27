import cv2
import numpy as np

# Відкриваємо відео файл
video = cv2.VideoCapture('Gen-3 Alpha Turbo 4152625597, The video begins wit, Cropped - dog-186887, M 5.mp4')

# Отримуємо властивості відео (ширина, висота, FPS)
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = video.get(cv2.CAP_PROP_FPS)

# Визначаємо розмір відео
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter('output_video.mp4', fourcc, fps, (frame_width, frame_height))

# Створюємо маску кола
mask = np.zeros((frame_height, frame_width), dtype=np.uint8)
center = (frame_width // 2, frame_height // 2)
radius = min(frame_width, frame_height) // 2
cv2.circle(mask, center, radius, 255, -1)

while True:
    ret, frame = video.read()

    if not ret:
        break

    # Перетворюємо кадр в маску
    frame_masked = cv2.bitwise_and(frame, frame, mask=mask)

    # Записуємо оброблений кадр у новий відеофайл
    output.write(frame_masked)

# Закриваємо відео файли
video.release()
output.release()

# Закриваємо всі вікна
cv2.destroyAllWindows()


import cv2
import face_recognition
import os
import numpy as np

# المسار إلى مجلد الصور
image_folder = r"E:\matrial\CV\New folder\images_folder"
known_encodings = []
known_names = []

# تحميل الصور وحساب الـ encodings
for file_name in os.listdir(image_folder):
    if file_name.endswith((".jpg", ".png")):
        image_path = os.path.join(image_folder, file_name)
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)
        if encodings:
            known_encodings.append(encodings[0])
            name = os.path.splitext(file_name)[0].split("_")[0].lower()
            known_names.append(name)

# بدء الكاميرا
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # تصغير الصورة للتسريع
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # تحديد أماكن الوجوه واستخراج الـ encodings
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        # حساب المسافات لاختيار أقرب تطابق
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        if face_distances.size > 0:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index] and face_distances[best_match_index] < 0.5:
                name = known_names[best_match_index]

        # إعادة الحجم الطبيعي للموقع
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # رسم المستطيل واسم الشخص
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow('Face Recognition', frame)
    if cv2.waitKey(1) & 0xFF == 27:  # اضغط Esc للخروج
        break

cap.release()
cv2.destroyAllWindows()

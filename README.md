# 📸 Face Recognition using OpenCV and face_recognition

This project is a simple real-time face recognition system using a webcam.

It loads known face images from a folder, computes their face encodings, and then continuously captures frames from your webcam to detect and recognize faces in real time.

Built with Python, it uses the `face_recognition` library for facial detection and comparison, and `OpenCV` for video processing and display.

---

## 🧾 Requirements

- Python 3.7+
- Libraries:
  - `face_recognition`
  - `opencv-python`
  - `numpy`

Install the dependencies using:

```bash
pip install face_recognition opencv-python numpy
Note: face_recognition depends on dlib, which may require additional build tools depending on your OS (e.g., CMake and Visual C++ Build Tools on Windows).

📁 Folder Structure
css
Copy
Edit
face_recognition/
├── images_folder/
│   ├── ramez_1.jpg
│   ├── khaled_hamada.png
│   └── ...
├── main.py
└── README.md
images_folder/: contains known face images. Each image file should be named like name_1.jpg, name_2.png, etc.

The name shown in the recognition result is taken from the filename (before the underscore).

🚀 How to Run
Add clear face images of the people you want to recognize into the images_folder/ directory.

Run the main Python file:

bash
Copy
Edit
python main.py
The webcam will open and start detecting faces.

If a recognized face appears in front of the camera, their name will be displayed.

Press Esc to quit.

✅ Tips
Make sure each image in images_folder contains only one face.

Good lighting and frontal face images improve recognition accuracy.

Names are extracted automatically from the file name (e.g., ahmed_1.jpg will be shown as "ahmed").

📌 License
This project is for educational and personal use. No commercial use is allowed without permission.

yaml
Copy
Edit

---

لو عايز أضيف نسخة بالعربي أو لوجو أو صور توضيحية للنتيجة، قولّي وازودهم ليك. تحب أعملهولك ملف جاهز بامتداد `.md`؟






You said:
اهو 


# 📸 Face Recognition using OpenCV and face_recognition

This project is a simple real-time face recognition system using a webcam.

It loads known face images from a folder, computes their face encodings, and then continuously captures frames from your webcam to detect and recognize faces in real time.

Built with Python, it uses the face_recognition library for facial detection and comparison, and OpenCV for video processing and display.

---

## 🧾 Requirements

- Python 3.7+
- Libraries:
  - face_recognition
  - opencv-python
  - numpy

Install the dependencies using:

bash
pip install face_recognition opencv-python numpy
Note: face_recognition depends on dlib, which may require additional build tools depending on your OS (e.g., CMake and Visual C++ Build Tools on Windows).

📁 Folder Structure

face_recognition/
├── images_folder/
│   ├── ramez_1.jpg
│   ├── khaled_hamada.png
│   └── ...
├── main.py
└── README.md
images_folder/: contains known face images. Each image file should be named like name_1.jpg, name_2.png, etc.

The name shown in the recognition result is taken from the filename (before the underscore).

🚀 How to Run
Add clear face images of the people you want to recognize into the images_folder/ directory.

Run the main Python file:


python main.py
The webcam will open and start detecting faces.

If a recognized face appears in front of the camera, their name will be displayed.

Press Esc to quit.

✅ Tips
Make sure each image in images_folder contains only one face.

Good lighting and frontal face images improve recognition accuracy.

Names are extracted automatically from the file name (e.g., ahmed_1.jpg will be shown as "ahmed").

📌 License
This project is for educational and personal use. No commercial use is allowed without permission.


ظبطهولي بس يظهر بشكل حلو ومنظم وهاته كامل برضو


ChatGPT said:
أكيد، ظبطتهولك بتنسيق Markdown مظبوط علشان يظهر منظم وواضح على GitHub أو أي منصة تدعم Markdown:

markdown
Copy
Edit
# 📸 Face Recognition using OpenCV and face_recognition

This project is a simple real-time face recognition system using a webcam.

It loads known face images from a folder, computes their face encodings, and then continuously captures frames from your webcam to detect and recognize faces in real time.

Built with Python, it uses the `face_recognition` library for facial detection and comparison, and `OpenCV` for video processing and display.

---

## 🧾 Requirements

- Python 3.7+
- Libraries:
  - `face_recognition`
  - `opencv-python`
  - `numpy`

### Install Dependencies

```bash
pip install face_recognition opencv-python numpy
Note: face_recognition depends on dlib, which may require additional build tools depending on your OS
(e.g., CMake and Visual C++ Build Tools on Windows).

📁 Folder Structure
css
Copy
Edit
face_recognition/
├── images_folder/
│   ├── ramez_1.jpg
│   ├── khaled_hamada.png
│   └── ...
├── main.py
└── README.md
images_folder/: contains known face images.

Each image file should be named like name_1.jpg, name_2.png, etc.

The name shown in the recognition result is taken from the filename (before the underscore).

🚀 How to Run
Add clear face images of the people you want to recognize into the images_folder/ directory.

Run the main Python file:

bash
Copy
Edit
python main.py
The webcam will open and start detecting faces.

If a recognized face appears in front of the camera, their name will be displayed.

Press Esc to quit the program.

✅ Tips
Make sure each image in images_folder contains only one face.

Use good lighting and frontal face images for better accuracy.

Names are extracted automatically from the filename:

Example:
ahmed_1.jpg → will be shown as "ahmed"

📌 License
This project is for educational and personal use.
No commercial use is allowed without permission.

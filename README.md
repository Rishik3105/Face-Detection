# 😊 Face Detection with OpenCV & Haar Cascade

Welcome to my **Face Detection Project** using OpenCV! 🚀 This project makes face detection simple and fun using Python’s OpenCV library and a pre-trained **Haar Cascade Classifier**. Let’s explore how it works! 🎉

---

## 🌟 What This Project Can Do
✅ **Detect Faces** – Automatically finds and marks faces in an image.  
✅ **Grayscale Conversion** – Improves detection accuracy.  
✅ **Customizable Settings** – Adjust detection parameters for better results.  
✅ **Easy to Use** – Just provide an image, and let the magic happen!  

---

## 🛠️ Installation & Setup
To get started, you need a few things:
- **Python 3.x**
- **OpenCV Library**
- **NumPy**

Install OpenCV and NumPy with:
```bash
pip install opencv-python numpy
```

---

## 📜 How It Works
Let’s break it down step by step:

### 1️⃣ Load the Image
```python
img = cv.imread(path)
cv.imshow('Original Image', img)
```
The program loads your chosen image and displays it.

### 2️⃣ Convert to Grayscale
Grayscale images make detection faster and more efficient.
```python
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale Image', gray_img)
```

### 3️⃣ Load the Face Detector
```python
haar_cascade = cv.CascadeClassifier('D:\Python\opencv\haar_face.xml')
```
This pre-trained model recognizes facial features.

### 4️⃣ Detect Faces
```python
faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=1)
print(f'Faces detected: {len(faces_rect)}')
```
- **`scaleFactor`**: Defines how much the image is reduced at each scale.
- **`minNeighbors`**: Controls how strict the face detection is.

### 5️⃣ Draw Boxes Around Faces
```python
for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv.imshow('Detected Faces', img)
```
Marks detected faces with green rectangles.

### 6️⃣ Display the Final Result
Once the detection is complete, the processed image is displayed. 🎯

---

## 🎬 How to Run
1. Place your image in the same directory as the script.
2. Run the script in your IDE or terminal.
3. Input the image path when prompted.
4. Adjust `scaleFactor` & `minNeighbors` for better accuracy.

---

## 🔍 Things to Keep in Mind
🟢 **haar_face.xml** – A publicly available pre-trained model.  
🟢 **Parameter Tuning** – Modify settings based on image quality and lighting conditions.  

---

## 🎨 Sample Output
- **Original Image**:
  ![Original Image](https://via.placeholder.com/300x200.png?text=Original+Image)
- **Grayscale Image**:
  ![Grayscale Image](https://via.placeholder.com/300x200.png?text=Gray+Image)
- **Detected Face**:
  ![Detected Face](https://via.placeholder.com/300x200.png?text=Detected+Face)

---

## 👨‍💻 About Me
Hey there! I'm **Nimmani Rishik**, a tech enthusiast passionate about **Computer Vision, AI, and Deep Learning**. Let’s connect! 😊  

📧 [Email](mailto:nimmanirishik@gmail.com)  
🔗 [LinkedIn](https://linkedin.com/in/nimmani-rishik-66b632287)  
📷 [Instagram](https://instagram.com/rishik_3142)  

🚀 Have questions or ideas? Feel free to reach out!

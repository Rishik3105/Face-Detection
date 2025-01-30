# 😊 Face Detection with OpenCV & Haar Cascade

Welcome to my **Face Detection Project** using OpenCV! 🚀 This project enables you to detect faces in images effortlessly using a pre-trained **Haar Cascade Classifier** and Python’s OpenCV library. Let's dive in! 🎉

---

## 🌟 Features
✅ **Accurate Face Detection** – Detects faces with bounding rectangles.  
✅ **Grayscale Conversion** – Enhances detection performance.  
✅ **Customizable Parameters** – Adjust `scaleFactor` & `minNeighbors` for better accuracy.  
✅ **User-Friendly** – Just provide an image path, and you're good to go!  

---

## 🛠️ Installation & Setup
Make sure you have the following dependencies installed:
- **Python 3.x**
- **OpenCV Library**
- **NumPy**

Install OpenCV and NumPy using pip:
```bash
pip install opencv-python numpy
```

---

## 📜 Code Walkthrough
Here’s how the program works step by step:

### 1️⃣ Load the Image
```python
img = cv.imread(path)
cv.imshow('Original Image', img)
```
Loads the image from the provided path and displays it.

### 2️⃣ Convert Image to Grayscale
Grayscale images improve detection efficiency by focusing on patterns instead of colors.
```python
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale Image', gray_img)
```

### 3️⃣ Load the Haar Cascade Classifier
```python
haar_cascade = cv.CascadeClassifier('D:\Python\opencv\haar_face.xml')
```
Uses a pre-trained Haar Cascade model for face detection.

### 4️⃣ Detect Faces in the Image
```python
faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=1)
print(f'Faces detected: {len(faces_rect)}')
```
- **`scaleFactor`**: Defines how much the image size is reduced at each scale.
- **`minNeighbors`**: Determines how many neighbors each rectangle should have to be considered a valid face.
- **Tip**: Adjust these values to optimize accuracy! 🎯

### 5️⃣ Draw Rectangles Around Faces
```python
for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv.imshow('Detected Faces', img)
```
Marks detected faces with green rectangles.

### 6️⃣ Display the Final Output
Once processing is complete, the final image with detected faces is displayed. ✨

---

## 🎬 How to Run the Script
1. Place your image in the same directory as the script.
2. Run the script in your preferred IDE or terminal.
3. Input the image path when prompted.
4. Adjust `scaleFactor` & `minNeighbors` if needed for better results.

---

## 🔍 Important Notes
🟢 **haar_face.xml** – A publicly available XML file trained for face detection.  
🟢 **Parameter Tuning** – Modify `scaleFactor` and `minNeighbors` based on your image characteristics (resolution, lighting, etc.).  

---

## 🎨 Example Output
- **Original Image**:
  ![Original Image](https://via.placeholder.com/300x200.png?text=Original+Image)
- **Grayscale Image**:
  ![Grayscale Image](https://via.placeholder.com/300x200.png?text=Gray+Image)
- **Detected Face**:
  ![Detected Face](https://via.placeholder.com/300x200.png?text=Detected+Face)

---

## 👨‍💻 About Me
Hey there! I'm **Nimmani Rishik**, a tech enthusiast passionate about **Computer Vision, AI, and Deep Learning**. Let's connect! 😊  

📧 [Email](mailto:nimmanirishik@gmail.com)  
🔗 [LinkedIn](https://linkedin.com/in/nimmani-rishik-66b632287)  
📷 [Instagram](https://instagram.com/rishik_3142)  

🚀 Feel free to reach out if you have any questions or suggestions!

---

## 🎯 Contribution
Want to improve this project? Fork the repository, make changes, and submit a pull request! All contributions are welcome. 🚀

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

✨ **Happy Coding!** 💻🚀


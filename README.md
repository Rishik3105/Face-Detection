# 😊 Face Detection with OpenCV and Haar Cascade

Welcome to my **Face Detection Project** using OpenCV! 🎉 This project allows you to detect faces in any image using a pre-trained Haar Cascade Classifier and Python's OpenCV library.

---

#

---

## 🛠️ Installation
Ensure you have the following installed:
- Python 3.x
- OpenCV Library
- Numpy

You can install OpenCV and Numpy using pip:
```bash
pip install opencv-python
pip install numpy
```

---

## 📄 Code Walkthrough
Here’s how the magic happens step by step:

1. **Load the Image**:
   ```python
   img = cv.imread(path)
   cv.imshow('Original Image', img)
   ```
   The program asks for your image path and loads the image.

2. **Convert to Grayscale**:
   Grayscale images improve performance when detecting faces because the model focuses on patterns instead of color.
   ```python
   gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
   cv.imshow('Gray Scale Image', gray_img)
   ```

3. **Load the Haar Cascade Classifier**:
   ```python
   haar_cascade = cv.CascadeClassifier('D:\Python\opeancv\haar_face.xml')
   ```
   - The `haar_face.xml` file is a pre-trained Haar Cascade model.
   - Haar cascades are used to detect objects (like faces) based on features learned from thousands of positive and negative images.

4. **Detect Faces**:
   ```python
   faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=1)
   print(f'Number of faces found in the given image = {len(faces_rect)}')
   ```
   - `scaleFactor`: Adjusts how much the image size is reduced at each scale. Smaller values (e.g., 1.1) improve accuracy but increase computation time.
   - `minNeighbors`: Specifies how many neighbors each candidate rectangle should have to retain it as a face. Increase it to reduce false positives.
   - **TIP**: Tweak these values based on your image for the best results! 😎

5. **Draw Rectangles Around Detected Faces**:
   ```python
   for (x, y, w, h) in faces_rect:
       cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
   cv.imshow('Detected Face', img)
   ```
   Bounding rectangles are drawn around the detected faces with a green border.

6. **Display the Results**:
   Finally, the image with detected faces is displayed. 🎯

---

## 🎥 How to Run
1. Place your image in the desired directory.
2. Run the script in your IDE or terminal.
3. Input the full path to your image when prompted.
4. Adjust `scaleFactor` and `minNeighbors` values if required for better accuracy.

---

## 📝 Notes
- **haar_face.xml**: This is an XML file containing a pre-trained Haar cascade model for face detection. It is publicly available and trained on large datasets for object detection.
- **Parameter Tuning**: Experiment with `scaleFactor` and `minNeighbors` for different image resolutions and lighting conditions.

---

## 🎨 Example Output
- **Original Image**:
  ![Original Image Placeholder](https://via.placeholder.com/300x200.png?text=Original+Image)
- **Grayscale Image**:
  ![Grayscale Placeholder](https://via.placeholder.com/300x200.png?text=Gray+Image)
- **Detected Face**:
  ![Detected Face Placeholder](https://via.placeholder.com/300x200.png?text=Detected+Face)

---

## 🧑‍💻 About Me
👋 I'm **Nimmani Rishik**, a passionate programmer and problem-solver working on projects related to **Computer Vision, AI, and Deep Learning**. Connect with me:

📧 [Email](mailto:nimmanirishik@gmail.com)  
🔗 [LinkedIn](https://linkedin.com/in/nimmani-rishik-66b632287)  
📷 [Instagram](https://instagram.com/rishik_3142)  

Feel free to reach out if you have any questions or suggestions! 💬

---

## ⭐ Contribution
If you find this project useful or have improvements to suggest, feel free to fork the repository and submit a pull request. All contributions are welcome! 😊

---

## 📜 License
This project is open-source and available under the MIT License.

---
**Enjoy Coding! 💻✨**

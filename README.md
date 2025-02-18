# Helmet_Detection_YOLOv8
# 🚀 Helmet Detection using YOLOv8 🎯

[![YOLOv8](https://img.shields.io/badge/YOLOv8-ObjectDetection-blue)](https://github.com/ultralytics/ultralytics)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/OpenCV-4.5-blue)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-brightgreen)](LICENSE)

🔥 **Real-time Helmet Detection** using **YOLOv8** to ensure safety compliance. This project detects helmets in **live webcam footage** or from video streams using a **custom-trained YOLOv8 model**.

<p align="center">
  <img src="https://https://github.com/AnilPise7/Helmet_Detection_YOLOv8/raw/main/assets/demo.gif" width="70%" alt="Helmet Detection GIF">
</p>

---

## 📌 **Project Overview**
In many industries such as **construction, manufacturing, and transportation**, safety helmets are essential. This project automates **helmet detection** using **YOLOv8** for **real-time monitoring**.

### 🎯 **Features**
✅ Real-time Helmet Detection using YOLOv8  
✅ Detects Helmets in Webcam and Video Feeds  
✅ Uses a Custom Trained Model for Accuracy  
✅ Supports Multiple Object Detection  

---

## 📂 **Project Directory Structure**


---

## 🚀 **Installation Guide**
1️⃣ **Clone the Repository**
```bash
git clone https://https://github.com/AnilPise7/Helmet_Detection_YOLOv8.git
cd Helmet_Detection_YOLOv8

2️⃣ Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt

🎯 How to Use
🔹 Run the Helmet Detection Script

python src/helmet_detection.py

model = YOLO("models/helmet_detection.pt")  # Load custom trained model
🖼️ Demo Output
<p align="center"> <img src="https://github.com/AnilPise7/Helmet_Detection_YOLOv8/raw/main/assets/result1.jpg" width="60%" alt="Detection Result"> </p>

🔬 Training a Custom YOLOv8 Model
1️⃣ Find a Helmet Detection Dataset

Use Kaggle or Roboflow to download datasets.
Example: Helmet Detection Dataset
2️⃣ Train the Model using YOLOv8

yolo train model=yolov8n.pt data=dataset.yaml epochs=50 imgsz=640

3️⃣ Save and Use the Trained Model
model = YOLO("models/helmet_detection.pt")

🛠️ Future Enhancements
✅ Train with larger datasets for better accuracy.
✅ Integrate with CCTV camera feeds for real-world deployment.
✅ Deploy as a web application for remote monitoring.

💡 Contributing
Contributions are welcome! Feel free to submit pull requests or open an issue.

📝 License
This project is licensed under the MIT License. See the LICENSE file for details.

📬 Contact
💬 Author: Dr Anil Pise
📩 Email: anilapise7@gmail.com

🚀 If you found this project useful, don't forget to ⭐ star the repo!


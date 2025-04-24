# ♻️ GarbiAI - Smart Waste Detection & Real-Time Cleanup System

GarbiAI is an AI-powered smart waste management solution that detects, classifies, and routes garbage pickup tasks using computer vision, public reporting, and real-time notifications — helping cities become cleaner, smarter, and more responsive.

![GarbiAI Demo]() <!-- Add demo GIF or screenshot link here -->

---

## 🚀 Features

- 📸 Real-time object detection via webcam (plastic bottle, paper, etc.)
- 🔍 Classifies items as ♻️ Recyclable or ❌ Not Recyclable using **MobileNetV2**
- 🧠 Uses **TensorFlow + Keras** for deep learning
- 📍 Future-ready for geo-tagging and municipal alerts
- 💡 Built to scale into a full public reporting app with AI integration

---

## 🎯 Problem It Solves

- Overflowing garbage bins and unattended waste in public spaces
- Manual waste segregation is inefficient and labor-intensive
- Citizens don’t have a fast and easy way to report garbage
- Informal waste pickers are disconnected from the system

---

## 🧪 Technologies Used

| Tech          | Purpose                          |
|---------------|----------------------------------|
| Python        | Core programming                 |
| OpenCV        | Webcam integration & frame processing |
| TensorFlow    | Deep learning framework          |
| Keras         | High-level API for model loading |
| MobileNetV2   | Lightweight pretrained image classifier |
| Streamlit (future) | Web app deployment (optional) |

---

## 👁️ How It Works

1. User shows an object (bottle, paper, etc.) to the webcam
2. The image is processed by MobileNetV2
3. The top predicted label is matched with common recyclable keywords
4. Output is shown in real-time on screen:
   - `♻️ Recyclable (plastic_bottle, 93.2%)`
   - `❌ Not Recyclable (banana, 87.1%)`

---

## 🖥️ Live Demo (Local Run)

### 🔧 Requirements

- Python 3.8+
- Install dependencies:
```bash
pip install tensorflow opencv-python numpy

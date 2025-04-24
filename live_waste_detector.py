import cv2
import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions

model = MobileNetV2(weights='imagenet')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img = cv2.resize(frame, (224, 224))
    x = np.expand_dims(img, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    decoded = decode_predictions(preds, top=3)[0]
    print(decoded)

    label_text = "❌ Not Recyclable"
    for label in decoded:
        print(label)
        if 'bottle' in label[1] or 'can' in label[1] or 'paper' in label[1]:
            label_text = f"♻️ Recyclable ({label[1]}, {round(label[2] * 100, 2)}%)"
            break

    cv2.putText(frame, label_text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0) if "Recyclable" in label_text else (0, 0, 255), 2)
    cv2.imshow('GarbiAI - Live Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
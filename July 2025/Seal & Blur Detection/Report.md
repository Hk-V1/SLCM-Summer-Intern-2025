# Seal & Blur Detection Model

This project is a **dual-task image classification system** that:
1. Detects whether an image is **blurry or usable**.
2. Detects whether a **seal** (e.g., an industrial or object seal) is present in the image.

The workflow includes:
- Interactive image labeling (blur + seal categories simultaneously)
- Automatic dataset creation
- Model training using TensorFlow/Keras with **MobileNetV2** transfer learning (or custom CNN)
- Predictions on new images
- Export to **TensorFlow Lite (.tflite)** for deployment on edge/mobile devices

---

## Features

- **Interactive Labeling**  
  Uses Jupyter/Colab widgets to label both blur and seal status at the same time.
  
- **Automatic Dataset Organization**  
  Saves labeled images into separate folders for training.

- **Dual Model Training**  
  - **Blur detection model** (`blur_detector.h5`)
  - **Seal detection model** (`seal_detector.h5`)
  
- **Data Augmentation**  
  Improves generalization using random flips, rotations, zoom, and contrast adjustments.

- **Prediction Pipeline**  
  Runs inference on any uploaded image and outputs:
  - Blur/Usable classification
  - Seal/No Seal classification

- **TFLite Conversion**  
  Models exported to `.tflite` for mobile/embedded applications.

---

## 🛠 Requirements

This project is designed to run on **Google Colab**.

Python packages:
```bash
tensorflow
numpy
Pillow
ipywidgets
matplotlib
```

---

## Usage

### Upload Dataset ZIP
- Place all images (any folder structure) into a `.zip` file.
- Upload it in the first cell.
- The notebook will extract files into `all_images/`.

### Label Images
- The script displays each image with **4 buttons**:
  - Blurry + Seal Present
  - Blurry + No Seal
  - Clear + Seal Present
  - Clear + No Seal
- Click the correct label for each image.
- Images are copied into `blur_dataset/` and `seal_dataset/` accordingly.

### Train Models
- Models are trained with:
  - 80% training data, 20% validation data
  - Early stopping to avoid overfitting
- Two `.h5` models are saved in `models/`.

### Run Predictions
- Upload a new image.
- The notebook predicts blur status & seal presence.
- Displays the image with labels and confidence scores.

### Export to TFLite
- Automatically converts both models to `.tflite` format for deployment.

---

## Deployment

The `.tflite` models can be loaded in:
- Android (TensorFlow Lite)
- Raspberry Pi / Edge devices
- Microcontrollers with TinyML support

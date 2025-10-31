# Wheat Disease Recognition & Treatment Advisor  

An AI-powered web app for detecting wheat leaf diseases and recommending treatments using deep learning.  

---

## Overview  
The system analyzes uploaded leaf images, classifies diseases, and provides treatment suggestions to assist farmers and agricultural experts.  

---

## Features  
- Detects 6 diseases: Healthy, Wheat Rust, Leaf Blight, Powdery Mildew, Septoria Leaf Spot, Fusarium Head Blight  
- Image upload and preprocessing  
- Confidence score display  
- Expert-based treatment recommendations  
- History tracking and mobile-responsive design  

---

## Tech Stack  
**Language:** Python 3.13+  
**Frameworks:** Streamlit, PyTorch/TensorFlow  
**Libraries:** Pillow, NumPy  
**Model Format:** .pth / .h5  

---

## Disease & Treatment  

| Disease | Treatment |
|----------|------------|
| Healthy | Monitor regularly |
| Wheat Rust | Triazole or strobilurin fungicides |
| Leaf Blight | Mancozeb 75 WP, reduce irrigation |
| Powdery Mildew | Sulfur dust or Hexaconazole |
| Septoria Leaf Spot | Propiconazole, improve drainage |
| Fusarium Head Blight | Tebuconazole, seed quality control |

---

## Future Scope  
- Real-time camera input  
- Batch processing  
- PDF report generation  
- Multi-language support  
- Mobile app (TensorFlow Lite)  
- API integration (FastAPI)  

---

## Note  
Currently uses simulated predictions. Requires a trained model for production.  

# 🧠 Suicidal Post Detection System

A machine learning–based web application designed to detect suicidal content in user-generated posts and assess mental health severity using **BDI-II (Beck Depression Inventory-II)** scores.

Developed by **B.Tech Final Year Students, Haldia Institute of Technology**  
Department of Computer Science & Engineering  
Project Name: `Suicidal post detection system`

---

## 👥 Project Members

- **SUMIT KUNDU** – *10300121175*
- **SUBHRA BARAN SAHOO** – *10300121167*
- **SUBHRAJYOTI MAITY** – *10300121168*
- **SUMAN DHAR** – *10300121172*


---

## 🎓 Institutional Guide

- **Mr. Umesh Pal**  
  *(Project Mentor, Assistant Professor, Dept. of CSE)*

- **Dr. Subhankar Joardar**  
  *(Head of Department, CSE)*

---

## 🚀 Features

- 🧪 **Suicidal Text Detection**  
  Classifies text as either:
  - **Suicidal**
  - **Non-Suicidal**

- 📊 **BDI-II Score & Severity Level**  
  Calculates a Beck Depression Inventory-II score and provides:
  - **Score Range**:
    - 0–13: Minimal Depression
    - 14–19: Mild Depression
    - 20–28: Moderate Depression
    - 29–63: Severe Depression

- 🌐 **Streamlit Deployment**  
  Real-time, web-based interface for predictions.

- 🔄 **Tokenizer & Model Integration**
  - Uses `tokenizer.json` for consistent preprocessing
  - Loads `model.keras` for inference

---

## 🧰 Tech Stack

- **Python 3.9+**
- **TensorFlow 2.19.0**
- **Keras 3.10.0**
- **Streamlit**
- **scikit-learn**
- **neattext**
- **Pandas / NumPy**

---

## 📦 Installation

```bash
git clone https://github.com/SumitKundu102022/Final_year_project_suicidal_post_detection_system_Final.git
cd Final_year_project_suicidal_post_detection_system_Final

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# 🐾 Projet MistralAI: Chat Gourmand

Welcome to **Chat Gourmand** – a backend application for a chatbot that gives fun, cat-like food advice based on your meal photos! 🍽️😺

A lot of people snap pics of their meals before eating. This project is a proof of concept that uses those photos to analyze caloric intake and provide personalized food recommendations. 📸🥗

Image analysis is using **Ultralytics YOLO11** (custom-trained) and **MistralAI** models to estimate calories for each dish. The backend is built with **FastAPI** and **Ultralytics**. 🚀

**NOTE:** This is a **proof of concept** and was done quickly. The Yolo11 model is not entirely accurate and can sometimemiss items or misclassify them. This is because the training was done quickly on google colab and was not optimized to get the best results since it takes a **lot of time** to train and optimize. To see all the YOLO11 model classes check: src/backend/app.py

https://github.com/user-attachments/assets/391f307d-5afa-4447-99d9-161aed183c29

> **Frontend available:**  
> 👉 [project_mistralai_client](https://github.com/mana-byte/project_mistralai_client)

---

## ✨ Features

- 📷 Upload meal photos
- 🤖 Analyze meals with YOLOv11
- 🔥 Get caloric intake info
- 🍱 Personalized food recommendations (MistralAI)
- 🐱 Cat-like chatbot personality

---

## ⚡ Requirements

- 🐍 Python 3.8+
- 🚀 FastAPI
- 🦾 Ultralytics
- 🧠 MistralAI models
- 📦 Other dependencies in `requirements.txt`
- 💻 CUDA (for GPU acceleration)

---

## 🛠️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/mana-byte/project_mistralai.git
cd project_mistralai
```

> ⚠️ **Note:** THERE ARE **TWO DIFFERENT** INSTALLATION METHODS. Choose **ONE** of them.

### 2️⃣ Install with Nix/NixOS (Flake)

- Install Nix: https://nixos.org/
- Enter shell with dependencies:

```bash
sudo nix develop 
```

> ⚠️ **Note:** Cachix cache is for Linux x86_64 only. Other architectures may require source builds (can be slow).

### 3️⃣ Install with pip

- Install dependencies:

```bash
pip install -r requirements.txt
```

- Make sure you have **CUDA** and **SQLite** for GPU and database support.

---

## 🚀 Usage

⚠️ **Note:** You will need to have a **MistralAI API key** to use the chatbot features. Set it as an environment variable:

```bash
export MISTRAL_API_KEY="your_api_key_here"
```
Go to https://chat.mistral.ai/chat to get an API key. You will need to create an account.

- Start the FastAPI server:

```bash
fastapi run src/backend/api.py
```

- You can also test with pytest:

```bash
pytest
```

---

## 📚 API Endpoints

See the interactive docs:  
`http://localhost:8000/docs`

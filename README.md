# DaveAI 🤖🎙️  
**AI-powered desktop assistant with voice/text control**

[![GitHub license](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-yellow)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/Gemini-1.0_Pro-FF5F15)](https://ai.google.dev/)

![image](https://github.com/user-attachments/assets/9ed40c56-0ac8-454a-92e9-0d846ef831fb)
![image](https://github.com/user-attachments/assets/d101a775-3f8c-40f3-b2fb-adc1ae5eb58c)
![image](https://github.com/user-attachments/assets/a5280b9a-bf59-4fe3-8e05-707eb5525b8b)
*Sample interaction with DaveAI*

## Features ✨
- **Voice & text input/output** with speech recognition and TTS
- **System control** for apps, files, folders, and websites
- **Gemini Pro integration** for intelligent query responses
- **Customizable prompts** for domain-specific knowledge
- **Lightweight GUI** with ttkbootstrap/Tkinter
- **College-focused** with web-scraped data for personalized answers

## Tech Stack 🛠️
| Component       | Technologies |
|-----------------|-------------|
| **Core AI**     | Gemini 1.0 Pro API |
| **GUI**         | tkinter, ttkbootstrap |
| **Voice I/O**   | SpeechRecognition, pyttsx3 |
| **System Control** | os, subprocess, webbrowser |
| **Utilities**   | threading, queue |

## Installation ⚙️
```bash
# Clone repository
git clone https://github.com/yourusername/daveai.git

# Install dependencies
cd daveai
pip install -r requirements.txt

# Configure API key
# Edit UI.py and add your Gemini API key:
genai.configure(api_key="YOUR_API_KEY")  # Line ~25

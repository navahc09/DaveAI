# DaveAI
An AI-powered voice/text assistant that can open apps/websites/files/folders on your PC, and also intelligently answer your queries about anything really. 

Structure of the project:
Mainly divided into two parts, the UI, and the backend. The backend makes API requests to Gemini, has hardcoded scripts to open files/folders/apps/websites. Backend also contains additional prompt data for Gemini AI.
UI consists of a basic GUI built with ttkbootstrap and tkinter, speech recognition and text to speech libraries to perform tasks in collaboration with the backend. Contains functions to display input and output in text format, as the application accepts both voice/text input and returns voice/text output.
How to run:
1) Enter your Gemini API key in genai.configure(), keep note that the model used is Gemini AI 1.0 Pro.
2) Modify the temperature etc, and prompts according to your liking.
3) Run UI.py

Keep note that the program does lag a little when the audio button is clicked (in GUI) due to advancements in aforementioned libraries and the LLM itself. Try to converse on text as much as possible.

Edit: Some sample images for reference:
![image](https://github.com/user-attachments/assets/9ed40c56-0ac8-454a-92e9-0d846ef831fb)
![image](https://github.com/user-attachments/assets/d101a775-3f8c-40f3-b2fb-adc1ae5eb58c)
![image](https://github.com/user-attachments/assets/a5280b9a-bf59-4fe3-8e05-707eb5525b8b)


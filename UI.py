import ttkbootstrap as tk
import backendnew as bk
from tkinter import scrolledtext
from ttkbootstrap.style import Style
import pyttsx3
import speech_recognition as sr

recogniser = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)


class Assistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Assistant")
        self.root.geometry("650x476")

        self.style = Style(theme="darkly")

        self.chat_display = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, width=50, height=16, state=tk.DISABLED
        )

        self.chat_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.chat_display.vbar.configure(troughcolor='red', bg='blue')

        customfont = ("Helvetica",16)
        self.chat_display.config(font=customfont)

        self.user_input_entry = tk.Entry(root, width=70)
        self.user_input_entry.grid(row=1, column=0, padx=10, pady=10)

        self.display_message("Assistant: Hi there! I'm your Dave, your personal digital assistant "
                             "powered by Gemini 1.0 pro. I can open applications on your PC (ex: open chrome), "
                             "open websites on your browser (ex: open youtube.com), open files and folders on "
                             "your system (ex: open item saved pictures) And answer your general queries about "
                             "various topics. How may I assist you?", "green", "left")

        self.send_button = tk.Button(
            root, text="Send", command=self.send_message, style="Primary.TButton"
        )
        self.send_button.grid(row=1, column=1, padx=10, pady=10)
        self.audio_button = tk.Button(
            root, text="Audio", style="Primary.TButton", command=self.toggle_audio_button)
        self.audio_button.grid(row=1,column=2,padx=1,pady=10)

        self.root.bind('<Return>', lambda event: self.send_message())

    def toggle_audio_button(self):
        # if self.audio_button["state"] == "disabled":
        #     self.audio_button["state"] = "normal"
        #     print("button now clicked")
            self.audio_button_click()


    def audio_button_click(self):
        with sr.Microphone() as mic:
            recogniser.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recogniser.listen(mic)

            text_data = recogniser.recognize_google(audio)
            text_data = text_data.lower()
            print(text_data)
            self.display_message("You: " + text_data, "blue","right")
            assistant_response = bk.text_input(text_data)

            self.display_message("Assistant: " + str(assistant_response), "green", "left")
            self.user_input_entry.delete(0, tk.END)
            self.chat_display.yview(tk.END)
            self.speak()


    def speak(assistant_response):
        engine.say(assistant_response)
        engine.runAndWait()

    def send_message(self):

        user_message = self.user_input_entry.get()
        self.display_message("You: " + user_message, "blue","right")

        assistant_response = bk.text_input(user_message)

        self.display_message("Assistant: " + str(assistant_response), "green","left")
        self.user_input_entry.delete(0, tk.END)
        self.chat_display.yview(tk.END)
        Assistant.speak(assistant_response)

    def display_message(self, message, color, align):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.tag_configure(align, justify=align)
        self.chat_display.insert(tk.END, message + "\n", (color, "blue"))
        self.chat_display.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Window()
    app = Assistant(root)
    root.mainloop()

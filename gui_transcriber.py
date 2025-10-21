import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import speech_recognition as sr
from recorder import record_to_file


class GUITranscriber(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Speech-to-Text Transcriber')
        self.geometry('600x400')

        self.recognizer = sr.Recognizer()
        self.is_listening = False
        self.worker_thread = None

        self.text = tk.Text(self, wrap='word')
        self.text.pack(expand=True, fill='both')

        btn_frame = tk.Frame(self)
        btn_frame.pack(fill='x')
        self.start_btn = tk.Button(btn_frame, text='Start Listening', command=self.start_listening)
        self.start_btn.pack(side='left')
        self.stop_btn = tk.Button(btn_frame, text='Stop', state='disabled', command=self.stop_listening)
        self.stop_btn.pack(side='left')
        save_btn = tk.Button(btn_frame, text='Save Transcript', command=self.save_transcript)
        save_btn.pack(side='right')

    def start_listening(self):
        if self.is_listening:
            return
        self.is_listening = True
        self.start_btn.config(state='disabled')
        self.stop_btn.config(state='normal')
        self.worker_thread = threading.Thread(target=self._listen_loop, daemon=True)
        self.worker_thread.start()

    def _listen_loop(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            while self.is_listening:
                try:
                    audio = self.recognizer.listen(source, timeout=5)
                    try:
                        text = self.recognizer.recognize_google(audio)
                        self.text.insert('end', text + '\n')
                        self.text.see('end')
                    except sr.UnknownValueError:
                        self.text.insert('end', '[unintelligible]\n')
                    except sr.RequestError as e:
                        self.text.insert('end', f'[error: {e}]\n')
                except Exception as e:
                    self.text.insert('end', f'[listen error: {e}]\n')

    def stop_listening(self):
        self.is_listening = False
        self.start_btn.config(state='normal')
        self.stop_btn.config(state='disabled')

    def save_transcript(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files','*.txt')])
        if not file_path:
            return
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(self.text.get('1.0', 'end'))
        messagebox.showinfo('Saved', f'Saved transcript to {file_path}')


if __name__ == '__main__':
    app = GUITranscriber()
    app.mainloop()

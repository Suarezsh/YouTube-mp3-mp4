#Suarez sh
#GitHub:https://github.com/Suarezsh/
#
import os
import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import YouTube

class DescargasYouTuveShApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Descargador de YouTube mp3-mp4 Suarez sh")
        self.master.geometry("600x400+400+200")
        self.master.resizable(False, False)
        self.master.config(bg="#001a00")
        self.create_widgets()
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Enlace de YouTube:", font=("Arial", 14, "bold"), fg="#00ff00", bg="#001a00")
        self.label.pack(pady=10)
        self.link_entry = tk.Entry(self.master, width=50, font=("Arial", 12), bg="#003300", fg="#ffff00", bd=3, relief="solid")
        self.link_entry.pack(pady=10)
        self.format_var = tk.StringVar()
        self.format_var.set("mp3")  
        self.mp3_radio = tk.Radiobutton(self.master, text="MP3", variable=self.format_var, value="mp3", font=("Arial", 16, "bold"), fg="#00ff00", activebackground="#008000", bg="#001a00", selectcolor="#003300")
        self.mp3_radio.pack(pady=10)
        self.mp4_radio = tk.Radiobutton(self.master, text="MP4", variable=self.format_var, value="mp4", font=("Arial", 16, "bold"), fg="#ff0000", activebackground="#800000", bg="#001a00", selectcolor="#003300")
        self.mp4_radio.pack(pady=10)
        self.start_button = tk.Button(self.master, text="Iniciar Descarga", command=self.start_download, font=("Arial", 18, "bold"), bg="#008000", fg="#ffffff", activebackground="#004d00", bd=3, relief="solid")
        self.start_button.pack(pady=20)

    def start_download(self):
        video_url = self.link_entry.get()
        download_format = self.format_var.get()

        try:
            yt = YouTube(video_url)
            stream = None
            if download_format == "mp3":
                stream = yt.streams.filter(only_audio=True).first()
            elif download_format == "mp4":
                stream = yt.streams.get_highest_resolution()

            
            downloads_folder = os.path.join(os.path.expanduser("~"), "Descargas")

            folder_selected = filedialog.askdirectory(initialdir=downloads_folder)

            if folder_selected:
                download_path = f"{folder_selected}/{yt.title}.{download_format}"
                stream.download(output_path=folder_selected, filename=f"{yt.title}.{download_format}")
                messagebox.showinfo("Descarga Completa", f"La descarga se ha completado. Archivo guardado en:\n{download_path}")
            else:
                messagebox.showinfo("Descarga Cancelada", "Operación cancelada.")

        except KeyboardInterrupt:
            messagebox.showinfo("Descarga Cancelada", "Operación cancelada por el usuario.")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

    def on_closing(self):
        if messagebox.askokcancel("Cerrar", "¿Estás seguro de que quieres cerrar la aplicación?"):
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DescargasYouTuveShApp(root)
    root.mainloop()

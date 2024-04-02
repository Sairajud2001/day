def add(a,b):
    return a+b+0
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b
print("enter  the number")
print("enter anothe numbr")
print(mul(45845,3632))
import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
from ultralytics import YOLO

class ObjectDetectionGUI:
    def _init_(self, master):
        self.master = master
        self.master.title('bird_feeder')

        self.model = YOLO('best.pt')
        self.master.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 12))

        self.label = tk.Label(self.master, text='Select an image to detect objects:', font=('Helvetica', 14))
        self.label.pack()

        self.file_entry = tk.Entry(self.master, font=('Helvetica', 12))
        self.file_entry.pack(side=tk.TOP, pady=5)

        self.browse_button = ttk.Button(self.master, text='Browse', command=self.browse_file,)
        self.browse_button.pack(side=tk.TOP, pady=5)

        self.detect_button = ttk.Button(self.master, text='Detect image', command=self.detect_objects)
        self.detect_button.pack(side=tk.TOP, pady=5)

        self.use_cam_button = ttk.Button(self.master, text='Use Camera', command=self.use_camera)
        self.use_cam_button.pack(side=tk.TOP, pady=5)

        self.exit_button = ttk.Button(self.master, text='Exit', command=self.master.quit)
        self.exit_button.pack(side=tk.TOP, pady=5)

        self.image_label = tk.Label(self.master)
        self.image_label.pack()

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)

    def detect_objects(self):
        image_path = self.file_entry.get()
        results = self.model(source=image_path, show=True, conf=0.4, save=True,
                             project="runs/detect", name="inference", exist_ok=True)
    
        if results:
            image = Image.fromarray(results[0].render()[0])
            self.display_image(image)
        else:
            print("No results found.")

    def display_image(self, image):
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def use_camera(self):
        results = self.model(source=0, show=True, conf=0.4, save=False)

if _name_ == '_main_':
    root = tk.Tk()
    app = ObjectDetectionGUI(root)
    root.mainloop()

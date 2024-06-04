import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageEnhance, ImageFilter
import pytesseract

# Specify the path to the Tesseract executable if needed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class ImageToTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to Text Converter")

        # Instructions label
        self.label = tk.Label(root, text="Upload an image to extract text (supports Sinhala and English)")
        self.label.pack(pady=10)

        # Upload button
        self.upload_btn = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(pady=10)

        # Image display label
        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        # Extract Text button
        self.extract_btn = tk.Button(root, text="Extract Text", command=self.extract_text)
        self.extract_btn.pack(pady=10)

        # Text box to display extracted text
        self.text_box = tk.Text(root, wrap='word', height=10, width=50)
        self.text_box.pack(pady=10)

        # Store the image for extraction
        self.image = None

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            try:
                # Open and display the image
                image = Image.open(file_path)
                image.thumbnail((400, 400))
                img = ImageTk.PhotoImage(image)

                self.image_label.config(image=img)
                self.image_label.image = img

                # Store the image for later use
                self.image = image

                # Clear the text box
                self.text_box.delete(1.0, tk.END)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def extract_text(self):
        if self.image:
            try:
                # Preprocess the image for better OCR results
                processed_image = self.preprocess_image(self.image)

                # Extract text from the image using pytesseract with Sinhala language
                extracted_text = pytesseract.image_to_string(processed_image, lang='sin+eng')

                # Display extracted text in the text box
                self.text_box.delete(1.0, tk.END)
                self.text_box.insert(tk.END, extracted_text)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred during text extraction: {str(e)}")
        else:
            messagebox.showwarning("Warning", "Please upload an image first.")

    def preprocess_image(self, image):
        # Convert to grayscale
        image = image.convert('L')

        # Increase contrast
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(2)

        # Apply a slight blur to reduce noise
        image = image.filter(ImageFilter.MedianFilter())

        return image

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToTextApp(root)
    root.mainloop()

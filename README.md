# Image to Text Converter

This is a simple GUI application to extract text from images. It supports both Sinhala and English languages. The application is built using Python and uses Tesseract OCR for text extraction.

## Features

- Upload images in JPG, JPEG, and PNG formats.
- Display the uploaded image.
- Extract and display text from the uploaded image.
- Supports text extraction in Sinhala and English languages.

## Requirements

- Python 3.x
- tkinter
- Pillow
- pytesseract

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/image-to-text-converter.git
    cd image-to-text-converter
    ```

2. Install the required Python packages:
    ```bash
    pip install tkinter pillow pytesseract
    ```

3. Install Tesseract OCR:

    - **Windows:** Download the Tesseract installer from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki) and follow the installation instructions.
    - **macOS:** You can install Tesseract using Homebrew:
        ```bash
        brew install tesseract
        ```
    - **Linux:** You can install Tesseract using your package manager. For example, on Ubuntu:
        ```bash
        sudo apt-get install tesseract-ocr
        ```

4. Specify the path to the Tesseract executable in your script if needed:
    ```python
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    ```

## Usage

1. Run the application:
    ```bash
    python app.py
    ```

2. Use the "Upload Image" button to select an image file from your computer.
3. Click the "Extract Text" button to extract and display the text from the uploaded image.

## Preprocessing

The image is preprocessed before text extraction to improve the OCR results:
- Converted to grayscale
- Increased contrast
- Applied a slight blur to reduce noise

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

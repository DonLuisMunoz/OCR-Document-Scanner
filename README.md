# 🐍 OCR Document Scanner

<div align="center">

[![Python Version](https://img.shields.io/badge/Python-3.10.13-blue?style=for-the-badge&logo=python)](https://www.python.org/downloads/release/python-31013/)
[![Poetry](https://img.shields.io/badge/Poetry-Enabled-5D3480?style=for-the-badge&logo=poetry)](https://python-poetry.org/)
[![GitHub stars](https://img.shields.io/github/stars/DonLuisMunoz/OCR-Document-Scanner?style=for-the-badge)](https://github.com/DonLuisMunoz/OCR-Document-Scanner/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/DonLuisMunoz/OCR-Document-Scanner?style=for-the-badge)](https://github.com/DonLuisMunoz/OCR-Document-Scanner/network)
[![GitHub issues](https://img.shields.io/github/issues/DonLuisMunoz/OCR-Document-Scanner?style=for-the-badge)](https://github.com/DonLuisMunoz/OCR-Document-Scanner/issues)
[![GitHub license](https://img.shields.io/github/license/DonLuisMunoz/OCR-Document-Scanner?style=for-the-badge)](LICENSE) <!-- TODO: Add actual license file (e.g., MIT, Apache-2.0) -->

**A Python-based toolkit for automated document scanning, perspective transformation, and Optical Character Recognition (OCR).**

</div>

## 📖 Overview

This repository provides a Python library and example script for processing images of documents. It leverages computer vision techniques to detect and correct perspective distortions in scanned documents, and then applies Optical Character Recognition (OCR) to extract text content. Ideal for digitizing physical documents and making their text searchable.

## ✨ Features

-   🎯 **Automated Document Contour Detection**: Intelligently identifies the boundaries of a document within an image.
-   📐 **Perspective Transformation**: Corrects skewed images to provide a top-down, "scanned" view of the document.
-   ✨ **Image Enhancement**: Applies grayscale, blurring, edge detection, and adaptive thresholding for optimal OCR results.
-   📝 **Optical Character Recognition (OCR)**: Integrates with Tesseract OCR to extract text from the processed document images.

## 🛠️ Tech Stack

**Core Technologies:**

-   ![Python](https://img.shields.io/badge/Python-3.10.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
-   ![OpenCV](https://img.shields.io/badge/OpenCV-Python-blue?style=for-the-badge&logo=opencv)
-   ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
-   ![Scikit-image](https://img.shields.io/badge/scikit--image-black?style=for-the-badge&logo=scikit-learn&logoColor=white)
-   ![Pillow](https://img.shields.io/badge/Pillow-40914E?style=for-the-badge&logo=python&logoColor=white)
-   ![Tesseract OCR Engine](https://img.shields.io/badge/Tesseract_OCR-4A90E2?style=for-the-badge&logo=tesseract&logoColor=white)

**Dependency Management:**

-   ![Poetry](https://img.shields.io/badge/Poetry-5D3480?style=for-the-badge&logo=poetry&logoColor=white)

## 🚀 Quick Start

This section guides you through setting up the project and running the example script.

### Prerequisites

Before you begin, ensure you have the following installed:

-   **Python 3.10.13**: The project is configured for this specific version.
-   **Tesseract OCR Engine**: This is an external command-line tool. You need to install it separately.
    -   **Windows**: Download from [UB Mannheim](https://digi.bib.uni-mannheim.de/tesseract/).
    -   **macOS**: `brew install tesseract`
    -   **Linux**: `sudo apt install tesseract-ocr`

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/DonLuisMunoz/OCR-Document-Scanner.git
    cd OCR-Document-Scanner
    ```

2.  **Install dependencies using Poetry**
    ```bash
    # Ensure Poetry is installed: pip install poetry
    poetry install
    ```

3.  **Activate the Poetry shell**
    ```bash
    poetry shell
    ```

4.  **Configure Tesseract path (if necessary)**
    If Tesseract is not in your system's PATH, you might need to specify its path within `transform.py` or as an environment variable (see "Configuration" section below).

### Usage Example

The `transform_example.py` script demonstrates how to use the core `transform.py` module to scan and OCR an image.

1.  **Run the example script**
    From within the activated Poetry shell:
    ```bash
    python transform_example.py --image path/to/your/image.jpg
    ```
    Replace `path/to/your/image.jpg` with the actual path to an image file you want to process. The example expects an `images/` directory with a `page.jpg` file for testing.

    Example with a provided image:
    ```bash
    python transform_example.py --image images/page.jpg
    ```

## 📁 Project Structure

```
OCR-Document-Scanner/
├── .gitignore          # Specifies intentionally untracked files to ignore
├── .python-version     # Defines the specific Python version (3.10.13)
├── main.py             # Main entry point (currently a placeholder)
├── pyproject.toml      # Poetry configuration file for project dependencies and metadata
├── scan.py             # Document scanning helper module (currently a placeholder)
├── transform.py        # Core module containing image processing and OCR logic
├── transform_example.py # Example script demonstrating the usage of transform.py
└── README.md           # This README file
```

## ⚙️ Configuration

### Tesseract OCR Path

The `transform.py` module relies on the Tesseract OCR engine. By default, it expects Tesseract to be in your system's PATH. If it's not, you can specify the `tesseract_cmd` path directly in `transform.py` or ensure it's accessible via your environment.

In `transform.py`, look for the line:
```python
# Path to tesseract executable if not in PATH
# pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract' # Example for macOS/Linux
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # Example for Windows
```
Uncomment and adjust the path according to your Tesseract installation.

## 📚 API Reference

The core functionality resides in `transform.py`, which provides functions for image perspective correction and OCR.

### `transform.py`

#### `four_point_transform(image, pts)`

Applies a four-point perspective transform to an image.

**Parameters:**

-   `image` (numpy.ndarray): The input image.
-   `pts` (numpy.ndarray): A 4-element array or list of `(x, y)` points representing the corners of the object to transform (top-left, top-right, bottom-right, bottom-left).

**Returns:**

-   `warped` (numpy.ndarray): The transformed (warped) image.

**Example Usage (within `transform.py` or similar):**
```python
# Assuming 'image' is loaded and 'pts' (the 4 corners) are detected
# from imutils.perspective import four_point_transform
# warped_image = four_point_transform(image, pts)
```

#### `scan_image_and_ocr(image_path)`

Detects document contours, applies perspective transformation, enhances the image, and performs OCR.

**Parameters:**

-   `image_path` (str): The file path to the input image.

**Returns:**

-   `output_text` (str): The extracted text from the document.
-   `warped_image` (numpy.ndarray): The processed (warped and enhanced) image.

**Example:**
```python
from transform import scan_image_and_ocr

image_file = "images/page.jpg"
extracted_text, processed_image = scan_image_and_ocr(image_file)

print("--- Extracted Text ---")
print(extracted_text)

# You can save or display the processed_image if needed
# import cv2
# cv2.imwrite("processed_page.jpg", processed_image)
# cv2.imshow("Processed Document", processed_image)
# cv2.waitKey(0)
```

## 🔧 Development

### Available Scripts

Currently, the primary scripts are for running the example:

-   `python transform_example.py --image [image_path]` : Runs the document scanning and OCR process on a specified image.

### Development Workflow

1.  **Activate Poetry shell**: `poetry shell`
2.  **Make changes**: Edit `.py` files.
3.  **Test changes**: Run `transform_example.py` or write new test scripts.

## 🤝 Contributing

We welcome contributions! If you'd like to improve this project, please consider:

-   Forking the repository.
-   Creating a new branch (`git checkout -b feature/your-feature-name`).
-   Making your changes.
-   Submitting a pull request.

Please ensure your code adheres to Python best practices and includes appropriate comments.

## 📄 License

This project is licensed under the [LICENSE_NAME](LICENSE) - see the LICENSE file for details. <!-- TODO: Add an actual LICENSE file with a chosen license (e.g., MIT, Apache-2.0). -->

## 🙏 Acknowledgments

-   **OpenCV**: For robust image processing capabilities.
-   **NumPy**: For fundamental numerical operations.
-   **imutils**: For convenient OpenCV helper functions.
-   **Scikit-image**: For additional image filtering and processing utilities.
-   **Pillow**: For image manipulation.
-   **Tesseract OCR**: The powerful open-source OCR engine.
-   Inspired by various computer vision tutorials on document scanning and OCR.

## 📞 Support & Contact

-   🐛 Issues: [GitHub Issues](https://github.com/DonLuisMunoz/OCR-Document-Scanner/issues)

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ by [DonLuisMunoz](https://github.com/DonLuisMunoz)

</div>

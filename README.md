# Curriculum PDF Generator

Creating a PDF with "infinite scrolling" and a dark theme is an interesting challenge, as the PDF format was designed to mimic physical A4 paper (with page breaks). However, we can get around this by setting an extremely long page height or dynamically adjusting the PDF size to the content.

To create this PDF, we will use the **`fpdf2`** library (which is in requirements.txt), which is the modern successor to `fpdf` and handles custom colors and sizes much better.

A simple and automatic PDF generator in **dark mode**.

Choose the file name and press enter, paste your text into the terminal, press enter and then Ctrl+D and watch the magic happen ✨
Then check the file in the folder where the script was executed; it will be there.

---

## 💡 Highlights of this solution:

* **Single Page:** The script calculates the `len(lines)` and sets the PDF height proportionally. If the text is very long, the PDF will be a long "strip".

* **Visual Comfort:** I used a `#1E1E1E` background to avoid eye strain, similar to modern code editors (VS Code).

* **No Breaks:** Since `set_auto_page_break` is disabled and the format is customized, you won't see that annoying white line dividing the text.

**Important Note:** Some PDF viewers limit the maximum page height (the PDF standard has a theoretical limit of about 5 meters or 200 inches). If you are writing an entire book on a single page, the PDF reader may cut off the end, but for texts of common to long length, it works perfectly.

To make it more professional, an option was added to choose the filename directly from the terminal right at the beginning when running the script.

---

## 🚀 How to use

1. Clone the repository:
   ```bash
   git clone git@github.com:josemarpoubel/curriculum-pdf-generator.git
   cd curriculum-pdf-generator
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the script:
   ```bash
   python src/pdf_creator.py
   ```

5. Type or paste your text in the terminal.  
   - Press **Enter + Ctrl+D** (Linux/Mac) or **Enter + Ctrl+Z** (Windows) to finish.  
   - The PDF will be generated automatically in dark mode.

---

## 📂 Project structure

```
curriculum-pdf-generator/
├── LICENSE
├── README.md
├── requirements.txt
├── examples/
│   └── resume_example.txt
└── src/
    └── criador_de_pdf.py
```

---

## 📝 License
This project is licensed under the MIT License.

---

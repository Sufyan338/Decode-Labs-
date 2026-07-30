"""
Project 4: Image/Text Recognition Pipeline (OCR)
Path 1 - pytesseract + OpenCV, Gradio frontend.

Gatekeeper Rule (must pass all 4):
 1. Library Integration        -> pytesseract, error-free
 2. Pre-Processing Integrity   -> Grayscale + Adaptive Thresholding
 3. Accuracy Benchmarking      -> min 80% confidence
 4. Visual Confirmation        -> clean OCR text output

Run locally:
    pip install -r requirements.txt
    # system dep (Debian/Ubuntu): sudo apt-get install tesseract-ocr
    python app.py
"""

import cv2
import numpy as np
import pytesseract
import gradio as gr


def preprocess_image(image):
    """PIL/np image -> (grayscale, adaptive-thresholded) np arrays."""
    img = np.array(image)
    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    else:
        gray = img

    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    thresh = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31, 11
    )
    return gray, thresh


def extract_text_with_confidence(processed_img):
    data = pytesseract.image_to_data(processed_img, output_type=pytesseract.Output.DICT)

    words, confs = [], []
    for i in range(len(data['text'])):
        word = data['text'][i].strip()
        conf = int(data['conf'][i])
        if word and conf > 0:
            words.append(word)
            confs.append(conf)

    full_text = " ".join(words)
    avg_conf = round(sum(confs) / len(confs), 2) if confs else 0.0
    return full_text, avg_conf, list(zip(words, confs))


def gatekeeper_report(full_text, avg_conf, thresh_img):
    checks = {
        "1. Library Integration (pytesseract)": True,
        "2. Pre-Processing Integrity (Grayscale+AdaptiveThreshold)": thresh_img is not None,
        "3. Accuracy Benchmarking (>=80% confidence)": avg_conf >= 80,
        "4. Visual Confirmation (non-empty text output)": len(full_text.strip()) > 0,
    }
    lines = [f"[{'PASS' if passed else 'FAIL'}] {name}" for name, passed in checks.items()]
    overall = "ALL CHECKS PASSED" if all(checks.values()) else "MILESTONE NOT MET"
    lines.append("")
    lines.append(overall)
    return "\n".join(lines)


def run_pipeline(image):
    if image is None:
        return None, "No image provided.", 0.0, "No image provided."

    gray, thresh = preprocess_image(image)
    full_text, avg_conf, word_confs = extract_text_with_confidence(thresh)
    report = gatekeeper_report(full_text, avg_conf, thresh)

    thresh_display = cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)

    return thresh_display, full_text if full_text else "(no text detected)", avg_conf, report


demo = gr.Interface(
    fn=run_pipeline,
    inputs=gr.Image(type="pil", label="Upload Image (with text)"),
    outputs=[
        gr.Image(label="Pre-Processed Output (Grayscale + Adaptive Threshold)"),
        gr.Textbox(label="Extracted Text (OCR)"),
        gr.Number(label="Average Confidence (%)"),
        gr.Textbox(label="Gatekeeper Validation Report", lines=6),
    ],
    title="Project 4: Image/Text Recognition Pipeline (OCR)",
    description=(
        "Upload an image containing text. Pipeline: Grayscale -> Adaptive Threshold -> "
        "Tesseract OCR -> Confidence Scoring -> Gatekeeper Validation (min 80% confidence)."
    ),
    allow_flagging="never",
)

if __name__ == "__main__":
    demo.launch()

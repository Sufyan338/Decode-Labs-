# Project 4 — Image/Text Recognition Pipeline (OCR)

Image/text recognition pipeline built with **pytesseract** + **OpenCV**, wrapped in a **Gradio** frontend. Built to satisfy DecodeLabs Project 4's "Gatekeeper Rule" milestone validation.

## Pipeline (v3)
```
Upload Image
   -> Grayscale + 2x Upscale + CLAHE contrast boost
   -> 8 pre-process variants generated in parallel:
        - Adaptive Threshold (normal + inverted)
        - Otsu Threshold (normal + inverted)
        - Non-local-means Denoise + Otsu (normal + inverted)
        - Bilateral Filter + Otsu (normal + inverted)
   -> Tesseract OCR run on every variant x PSM 6 + PSM 11
   -> Best result auto-selected by average word confidence
   -> Low-confidence tokens (<35) dropped as noise
   -> Gatekeeper Validation Report
```

The multi-variant approach exists because a single threshold method doesn't generalize:
- **Adaptive/Otsu (basic)** → works well on clean, high-contrast screenshots (app UI text, bank transaction screenshots).
- **Denoise/Bilateral variants** → needed for structured documents with busy backgrounds (ID cards, security-pattern watermarks) that confuse basic thresholding into gibberish.

## Gatekeeper Rule (4 checks, all must pass)
| # | Check | How it's satisfied |
|---|-------|---------------------|
| 1 | Library Integration | `pytesseract` called error-free |
| 2 | Pre-Processing Integrity | Grayscale conversion + adaptive/Otsu/denoise thresholding variants |
| 3 | Accuracy Benchmarking | Average word confidence must be ≥ 80% (auto-picks best variant/PSM combo) |
| 4 | Visual Confirmation | Clean, non-empty OCR text output returned to UI |

## Results observed during testing
| Input type | Result |
|---|---|
| Stylized YouTube thumbnail (colored text over photo) | Fixed by upscale + CLAHE + multi-PSM (v2) |
| Structured ID card (security-pattern background) | Fixed by denoise/bilateral variants (v3) |
| Clean app screenshot (bank transaction) | High accuracy, text matches source exactly |

## Files
- `app.py` — standalone Gradio app (base v1 pipeline; run locally or deploy)
- `AI_Project4_OCR_Pipeline.ipynb` — current pipeline (v3), structured for Google Colab
- `requirements.txt` — pip deps
- `packages.txt` — system dep (needed for Hugging Face Spaces deployment)

## Run in Google Colab
1. Upload `AI_Project4_OCR_Pipeline.ipynb` to Colab (or open from GitHub once pushed).
2. Runtime → Run all.
3. Last cell prints a public Gradio share link (valid ~1 week).

## Run locally
```bash
sudo apt-get install tesseract-ocr     # system dependency
pip install -r requirements.txt
python app.py
```

## Privacy note
`share=True` generates a **public** Gradio tunnel link — anyone with the link can open the app and any image processed passes through Gradio's servers during that session. Don't run real personal documents (CNIC, passports, bank statements with real account numbers) through it during testing. Use redacted/sample images, or set `share=False` and access locally only.

## Push to GitHub
```bash
git init
git add .
git commit -m "Project 4: OCR recognition pipeline (v3 - multi-variant preprocessing) with Gradio frontend"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```
If pushing from Colab, authenticate with a GitHub **Personal Access Token** (used as password when prompted).

# Paper Image Downloader - Setup Guide

This set of scripts automates downloading first-page images from your research papers and updating the publications carousel on your website.

## Scripts

1. **download_paper_images.py** - Downloads PDFs and extracts first pages as JPG images
2. **update_carousel.py** - Helps update the research.html carousel with the new images

## Prerequisites

You'll need to install Python packages:

```bash
pip install requests pdf2image Pillow
```

### Additional System Requirements

Since `pdf2image` requires poppler-utils, install it for your OS:

**Windows:**
```bash
choco install poppler
```

Or download from: https://github.com/oschwartz10612/poppler-windows/releases/

**macOS:**
```bash
brew install poppler
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install poppler-utils
```

## Usage

### Step 1: Download Paper Cover Images

Run the downloader script from the workspace root:

```bash
python download_paper_images.py
```

This will:
- Download all 18 papers from your publications
- Extract the first page from each PDF
- Convert to JPG images (150 DPI)
- Save to `/images` folder with pattern: `{paper_name}_cover.jpg`
- Show a summary of success/failures

### Step 2: Review Generated Images

Check the `/images` folder to review the generated cover images. You should see:

```
images/
  ├── backbones_cover.jpg
  ├── breakhis_cover.jpg
  ├── chatty_cover.jpg
  ├── cxv_cover.jpg
  ├── edsnet_cover.jpg
  ├── emnlp_cover.jpg
  ├── federated_cover.jpg
  ├── fld_cover.jpg
  ├── fld_plus_cover.jpg
  ├── graphs_cover.jpg
  ├── inpainting_cover.jpg
  ├── rl2_cover.jpg
  ├── samsung_cover.jpg
  ├── vixwacv22_cover.jpg
  ├── wavemix_cover.jpg
  ├── wavemixsr_cover.jpg
  ├── wavemixsrv2_cover.jpg
  └── wavepaint_cover.jpg
```

### Step 3: Update Carousel HTML

Run the carousel updater to assist with HTML updates:

```bash
python update_carousel.py
```

Then manually update `_pages/research.html` carousel section:

**Replace this pattern:**
```html
<div class="w-full h-48 bg-gradient-to-br from-purple-400 to-indigo-600 flex items-center justify-center">
  <span class="text-white text-center px-4"><strong>Paper Name</strong><br/>Subtitle</span>
</div>
```

**With:**
```html
<img src="/images/{paper_name}_cover.jpg" alt="Paper Cover" class="w-full h-48 object-cover">
```

## Paper Name Mappings

| Image File | Publication |
|---|---|
| backbones_cover.jpg | Which Backbone to Use |
| breakhis_cover.jpg | Magnification Invariant Medical Image Analysis |
| chatty_cover.jpg | Adversarial Transport Terms (ATT) |
| cxv_cover.jpg | Convolutional Xformers for Vision |
| edsnet_cover.jpg | EDSNet: Efficient-DSNet for Video Summarization |
| emnlp_cover.jpg | So You Think You're Funny? |
| federated_cover.jpg | FLeNS: Federated Learning |
| fld_cover.jpg | FLD: Normalizing Flow Based Metric |
| fld_plus_cover.jpg | FLD+: Data-efficient Evaluation Metric |
| graphs_cover.jpg | Heterogeneous Graphs for Breast Cancer |
| inpainting_cover.jpg | Resource-efficient Image Inpainting |
| rl2_cover.jpg | RL2: Histopathology Metric |
| samsung_cover.jpg | PawFACS: Pet Facial Action Recognition |
| vixwacv22_cover.jpg | ViX: Resource-Efficient Hybrid X-Formers |
| wavemix_cover.jpg | WaveMix: Token Mixer |
| wavemixsr_cover.jpg | WaveMixSR: Super-resolution |
| wavemixsrv2_cover.jpg | WaveMixSR-V2: Enhanced Super-resolution |
| wavepaint_cover.jpg | WavePaint: Self-Supervised Inpainting |

## Troubleshooting

### Downloads fail for certain papers

Some journals may:
- Block automated downloads
- Have CAPTCHAs
- Require subscriptions

**Solution:** Manually download PDFs and place in `.temp_papers` folder, then run the script again (it skips existing files).

### PDF to image conversion fails

Ensure poppler is installed correctly:

```bash
# Test poppler (if installed via chocolatey/brew)
pdftoppm --version
```

### Missing first page

Some PDFs may have blank first pages. Review the generated images and manually crop better pages if needed.

### Script crashes on specific papers

Check the error message. Common issues:
- PDF is encrypted or corrupted
- Network timeout (try again)
- Unsupported PDF format

You can manually download and convert those PDFs separately.

## Manual Alternative

If automated downloading fails, you can:

1. Visit each paper link manually
2. Download the PDF
3. Extract first page using any PDF reader
4. Save as JPG to `/images/{paper_name}_cover.jpg`
5. Update the HTML manually

## Clean Up

After successful conversion, the script auto-deletes temporary PDFs. To manually clean:

```bash
rm -rf .temp_papers  # Linux/macOS
rmdir /s .temp_papers  # Windows
```

## Need Help?

If you encounter issues:

1. Check that all required packages are installed: `pip list`
2. Verify poppler is in system PATH: `pdftoppm --version`
3. Try downloading a single paper manually to test the PDF
4. Check file permissions in `/images` folder

---

**Created:** March 2026  
**For:** Pranav's Research Portfolio Website

#!/usr/bin/env python3
"""
Script to download first page images of research papers for the publications carousel.
This script:
1. Downloads PDFs from paper links
2. Extracts the first page
3. Converts to JPG images
4. Saves to the images folder
"""

import os
import requests
import subprocess
import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse

# Paper links mapping (paper_name -> url)
PAPERS = {
    'backbones': 'https://arxiv.org/abs/2406.05612',
    'breakhis': 'https://www.scitepress.org/PublicationsDetail.aspx?ID=SZAO62y/tp4=&t=1',
    'chatty': 'https://link.springer.com/chapter/10.1007/978-3-031-78166-7_1',
    'cxv': 'https://arxiv.org/abs/2201.10271',
    'edsnet': 'https://arxiv.org/abs/2409.14724',
    'emnlp': 'https://aclanthology.org/2021.emnlp-main.789',
    'federated': 'https://ieeexplore.ieee.org/abstract/document/10825820',
    'fld': 'https://arxiv.org/abs/2410.02004',
    'fld_plus': 'https://openaccess.thecvf.com/content/ICCV2025W/CV4DC/html/Jeevan_FLD_Data-efficient_Evaluation_Metric_for_Generative_Models_ICCVW_2025_paper.html',
    'graphs': 'https://link.springer.com/chapter/10.1007/978-3-031-55088-1_9',
    'inpainting': 'https://dblp.org/rec/conf/iclr/KumarJS23.html',
    'rl2': 'https://ieeexplore.ieee.org/document/10981064',
    'samsung': 'https://bmvc2024.org/proceedings/288/',
    'vixwacv22': 'https://openaccess.thecvf.com/content/WACV2022/papers/Jeevan_Resource-Efficient_Hybrid_X-Formers_for_Vision_WACV_2022_paper.pdf',
    'wavemix': 'https://arxiv.org/abs/2205.14375',
    'wavemixsr': 'https://openaccess.thecvf.com/content/WACV2024/html/Jeevan_WaveMixSR_Resource-Efficient_Neural_Network_for_Image_Super-Resolution_WACV_2024_paper.html',
    'wavemixsrv2': 'https://ojs.aaai.org/index.php/AAAI/article/view/35262',
    'wavepaint': 'https://openaccess.thecvf.com/content/ICCV2025W/CV4DC/html/Jeevan_WavePaint_Resource-efficient_Token-mixer_for_Self-supervised_Inpainting_ICCVW_2025_paper.html',
}

# PDF direct links (for sites that don't serve PDFs directly)
PDF_DIRECT_LINKS = {
    'backbones': 'https://arxiv.org/pdf/2406.05612.pdf',
    'cxv': 'https://arxiv.org/pdf/2201.10271.pdf',
    'edsnet': 'https://arxiv.org/pdf/2409.14724.pdf',
    'fld': 'https://arxiv.org/pdf/2410.02004.pdf',
    'wavemix': 'https://arxiv.org/pdf/2205.14375.pdf',
    'vixwacv22': 'https://openaccess.thecvf.com/content/WACV2022/papers/Jeevan_Resource-Efficient_Hybrid_X-Formers_for_Vision_WACV_2022_paper.pdf',
}

class PaperImageDownloader:
    def __init__(self, workspace_path=None):
        """Initialize the downloader."""
        if workspace_path is None:
            # Assume script is in workspace root
            self.workspace_path = Path(__file__).parent
        else:
            self.workspace_path = Path(workspace_path)
        
        self.images_path = self.workspace_path / 'images'
        self.temp_path = self.workspace_path / '.temp_papers'
        
        # Create directories if needed
        self.images_path.mkdir(exist_ok=True)
        self.temp_path.mkdir(exist_ok=True)
        
        print(f"Workspace: {self.workspace_path}")
        print(f"Images folder: {self.images_path}")
    
    def download_pdf(self, paper_name, url):
        """Download PDF from URL."""
        print(f"\n{'='*60}")
        print(f"Processing: {paper_name}")
        print(f"URL: {url}")
        print(f"{'='*60}")
        
        try:
            # Check if we have a direct PDF link
            if paper_name in PDF_DIRECT_LINKS:
                pdf_url = PDF_DIRECT_LINKS[paper_name]
                print(f"Using direct PDF link: {pdf_url}")
            else:
                pdf_url = url
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(pdf_url, headers=headers, timeout=30)
            response.raise_for_status()
            
            pdf_path = self.temp_path / f"{paper_name}.pdf"
            with open(pdf_path, 'wb') as f:
                f.write(response.content)
            
            print(f"✓ Downloaded: {pdf_path}")
            return pdf_path
            
        except Exception as e:
            print(f"✗ Failed to download {paper_name}: {e}")
            return None
    
    def extract_first_page(self, pdf_path, paper_name):
        """Extract first page from PDF and convert to JPG."""
        try:
            output_path = self.images_path / f"{paper_name}_cover.jpg"
            
            # Try using pdf2image (more reliable for complex PDFs)
            try:
                from pdf2image import convert_from_path
                
                print(f"Converting PDF to image using pdf2image...")
                images = convert_from_path(str(pdf_path), first_page=1, last_page=1, dpi=150)
                
                if images:
                    images[0].save(output_path, 'JPEG', quality=85)
                    print(f"✓ Created: {output_path}")
                    return output_path
            except ImportError:
                print("pdf2image not available, trying pypdf2...")
                raise
            
        except Exception as e:
            print(f"✗ Failed to extract page from {paper_name}: {e}")
            print(f"  Install required: pip install pdf2image pillow")
            return None
    
    def process_all_papers(self):
        """Process all papers."""
        print("\n" + "="*60)
        print("PAPER IMAGE DOWNLOADER")
        print("="*60)
        
        results = {
            'success': [],
            'failed': [],
            'skipped': []
        }
        
        for paper_name, url in PAPERS.items():
            try:
                # Download PDF
                pdf_path = self.download_pdf(paper_name, url)
                if not pdf_path or not pdf_path.exists():
                    results['failed'].append(paper_name)
                    continue
                
                # Extract first page
                image_path = self.extract_first_page(pdf_path, paper_name)
                if image_path and image_path.exists():
                    results['success'].append(paper_name)
                    # Clean up PDF
                    pdf_path.unlink()
                else:
                    results['failed'].append(paper_name)
                    
            except Exception as e:
                print(f"✗ Error processing {paper_name}: {e}")
                results['failed'].append(paper_name)
        
        # Summary
        print("\n" + "="*60)
        print("SUMMARY")
        print("="*60)
        print(f"✓ Success: {len(results['success'])} papers")
        for paper in results['success']:
            print(f"  - {paper}")
        
        if results['failed']:
            print(f"\n✗ Failed: {len(results['failed'])} papers")
            for paper in results['failed']:
                print(f"  - {paper}")
        
        print(f"\nImages saved to: {self.images_path}")
        print("\nNext steps:")
        print("1. Review the generated cover images in the images folder")
        print("2. Run: python update_carousel.py")
        print("   to update the HTML carousel with new images")

def main():
    """Main entry point."""
    print("Paper Image Downloader for Research Publications\n")
    
    # Check for required libraries
    required_packages = {
        'requests': 'requests',
        'pdf2image': 'pdf2image',
        'PIL': 'Pillow',
    }
    
    missing_packages = []
    for module_name, package_name in required_packages.items():
        try:
            __import__(module_name)
        except ImportError:
            missing_packages.append(package_name)
    
    if missing_packages:
        print("Missing required packages:")
        for pkg in missing_packages:
            print(f"  - {pkg}")
        print("\nInstall them with:")
        print(f"  pip install {' '.join(missing_packages)}")
        print("\nNote: pdf2image also requires poppler-utils:")
        print("  - Windows: choco install poppler")
        print("  - macOS: brew install poppler")
        print("  - Linux: sudo apt-get install poppler-utils")
        sys.exit(1)
    
    # Run the downloader
    downloader = PaperImageDownloader()
    downloader.process_all_papers()

if __name__ == '__main__':
    main()

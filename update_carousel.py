#!/usr/bin/env python3
"""
Script to update the publications carousel in research.html to use cover images.
This script matches downloaded paper cover images with carousel entries and updates the HTML.
"""

import re
from pathlib import Path

# Mapping of carousel paper names to filename prefixes
CAROUSEL_MAPPING = {
    'fld': 'fld_plus',  # FLD+ paper
    'rl2': 'rl2',
    'wavemixsrv2': 'wavemixsrv2',
    'wavepaint': 'wavepaint',
    'backbones': 'backbones',
    'samsung': 'samsung',
    'breakhis': 'breakhis',
    'chatty': 'chatty',
    'federated': 'federated',
    'edsnet': 'edsnet',
    'graphs': 'graphs',
    'wavemixsr': 'wavemixsr',
    'fld': 'fld',
    'inpainting': 'inpainting',
    'vixwacv22': 'vixwacv22',
    'wavemix': 'wavemix',
    'cxv': 'cxv',
    'emnlp': 'emnlp',
}

PAPER_TITLES = {
    'fld': ('FLD+', 'Image Quality Metric', 'FLD+: Data-efficient Evaluation Metric for Generative Models'),
    'rl2': ('RL2', 'Histopathology Metric', 'Evaluation Metric for Quality Control and Generative Models in Histopathology Images'),
    'wavemixsrv2': ('WaveMixSR-V2', 'Super Resolution', 'WaveMixSR-V2: Enhancing Super-Resolution with Higher Efficiency'),
    'wavepaint': ('WavePaint', 'Image Inpainting', 'WavePaint: A Resource-Efficient Token-Mixer for Self-Supervised Inpainting'),
    'backbones': ('Backbones', 'Model Selection', 'Which Backbone to Use: A Resource-efficient Domain Specific Comparison for Computer Vision'),
    'samsung': ('PawFACS', 'Facial Recognition', 'PawFACS: Leveraging Semi-Supervised Learning for Pet Facial Action Recognition'),
    'breakhis': ('BreakHis', 'Medical Imaging', 'Magnification Invariant Medical Image Analysis: A Comparison of Convolutional Networks, Vision Transformers, and Token Mixers'),
    'chatty': ('ATT', 'Domain Adaptation', 'Adversarial Transport Terms for Unsupervised Domain Adaptation'),
    'federated': ('FLeNS', 'Federated Learning', 'FLeNS: Federated Learning with Enhanced Nesterov-Newton Sketch'),
    'edsnet': ('EDSNet', 'Video Summarization', 'EDSNet: Efficient-DSNet for Video Summarization'),
    'graphs': ('Graphs', 'GNN Architecture', 'Heterogeneous Graphs Model Spatial Relationships Between Biological Entities for Breast Cancer Diagnosis'),
    'wavemixsr': ('WaveMixSR', 'Super Resolution', 'WaveMixSR: A Resource-efficient Neural Network for Image Super-resolution'),
    'fld_orig': ('FLD', 'Normalizing Flow Metric', 'Normalizing Flow Based Metric for Image Generation'),
    'inpainting': ('Inpainting', 'WaveMix-based', 'Resource-efficient Image Inpainting'),
    'vixwacv22': ('ViX', 'Hybrid Transformers', 'Resource-Efficient Hybrid X-Formers for Vision'),
    'wavemix': ('WaveMix', 'Token Mixer', 'WaveMix: A Resource-efficient Neural Network for Image Analysis'),
    'cxv': ('CXV', 'CNN-Transformer Hybrid', 'Convolutional Xformers for Vision'),
    'emnlp': ('Open Mic', 'Humor Detection', '"So You Think You\'re Funny?": Rating the Humour Quotient in Standup Comedy'),
}

class CarouselUpdater:
    def __init__(self, workspace_path=None):
        """Initialize the updater."""
        if workspace_path is None:
            self.workspace_path = Path(__file__).parent
        else:
            self.workspace_path = Path(workspace_path)
        
        self.images_path = self.workspace_path / 'images'
        self.research_file = self.workspace_path / '_pages' / 'research.html'
        
        print(f"Workspace: {self.workspace_path}")
        print(f"Images folder: {self.images_path}")
        print(f"Research file: {self.research_file}")
    
    def find_cover_images(self):
        """Find all generated cover images."""
        cover_images = {}
        for img_file in self.images_path.glob('*_cover.jpg'):
            paper_name = img_file.stem.replace('_cover', '')
            cover_images[paper_name] = img_file.name
        
        print(f"\nFound {len(cover_images)} cover images:")
        for paper, filename in sorted(cover_images.items()):
            print(f"  - {paper}: {filename}")
        
        return cover_images
    
    def create_carousel_item(self, paper_key, cover_image, years_data):
        """Create updated carousel item HTML with cover image."""
        # Default mapping
        title, subtitle, full_title = PAPER_TITLES.get(paper_key, ('', '', ''))
        year = years_data.get(paper_key, '')
        venue = '2025'  # Default
        
        html = f'''            <!-- Paper - {paper_key} -->
            <a href="/publication/{paper_key}" class="paper-card bg-white rounded-xl overflow-hidden shadow-md hover:shadow-lg transition-all no-underline">
              <img src="/images/{cover_image}" alt="{title} Paper Cover" class="w-full h-48 object-cover">
              <div class="p-4">
                <h5 class="font-bold text-gray-900 text-sm mb-2 line-clamp-2">{full_title}</h5>
                <p class="text-xs text-gray-500 mb-3">{venue}</p>
                <div class="flex flex-wrap gap-1">
                  <span class="tag bg-purple-100 text-purple-800">{subtitle}</span>
                </div>
              </div>
            </a>'''
        return html
    
    def update_research_html(self, cover_images):
        """Update research.html with new carousel items."""
        if not self.research_file.exists():
            print(f"✗ Research file not found: {self.research_file}")
            return False
        
        with open(self.research_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find carousel section
        carousel_pattern = r'(<div class="paper-carousel w-max">)(.*?)(<\/div>\s*<\/div>)'
        match = re.search(carousel_pattern, content, re.DOTALL)
        
        if not match:
            print("✗ Could not find carousel section in research.html")
            return False
        
        print(f"\n✓ Found carousel section")
        
        # For now, just print what would be updated
        print("\nTo complete the update:")
        print("1. Manually replace gradient background divs with:")
        print("   <img src=\"/images/{image_name}\" alt=\"Paper Cover\" class=\"w-full h-48 object-cover\">")
        print("\n2. Update paper titles and venues as needed")
        print("\nOr run a more advanced version of this script with full HTML replacement")
        
        return True

def main():
    """Main entry point."""
    print("Research Carousel Updater\n")
    
    updater = CarouselUpdater()
    
    # Find cover images
    cover_images = updater.find_cover_images()
    
    if not cover_images:
        print("\n✗ No cover images found!")
        print("Please run download_paper_images.py first")
        return
    
    # Update carousel
    updater.update_research_html(cover_images)
    
    print("\n" + "="*60)
    print("NEXT STEPS")
    print("="*60)
    print(f"Cover images are ready at: {updater.images_path}")
    print("\nYou can now manually update the carousel in research.html:")
    print("Replace gradient background divs with:")
    print('  <img src="/images/{paper_name}_cover.jpg" alt="Paper Cover" class="w-full h-48 object-cover">')
    print("\nOR create issue/commit with generated images for full automation")

if __name__ == '__main__':
    main()

---
permalink: /
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<!-- Tailwind and FontAwesome CDN links -->
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">

<!-- Custom styles -->
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
body { font-family: 'Inter', sans-serif; }
.gradient-text {
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.card-hover { transition: all 0.3s ease; }
.card-hover:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
}
.timeline-item {
    position: relative;
    padding-left: 2rem;
    margin-bottom: 1.5rem;
}
.timeline-item:before {
    content: '';
    position: absolute;
    left: 0;
    top: 0.5rem;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #667eea;
}
.timeline-item:after {
    content: '';
    position: absolute;
    left: 4px;
    top: 15px;
    bottom: -1rem;
    width: 2px;
    background: #e2e8f0;
}
.timeline-item:last-child:after { display: none; }
.publication-item {
    opacity: 0;
    transform: translateY(20px);
}
.animated-gradient {
    background-size: 200% 200%;
    animation: gradient 3s ease infinite;
}
@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.typing-effect {
    border-right: 2px solid #667eea;
    animation: typing 3.5s steps(40) 1s 1 normal both,
               blink 0.7s infinite;
}
@keyframes typing {
    from { width: 0; }
    to { width: 100%; }
}
@keyframes blink {
    0%, 100% { border-color: transparent; }
    50% { border-color: #667eea; }
}
</style>

<div class="container mx-auto px-4 py-12 max-w-4xl">
    <!-- About Section -->
    <section class="bg-white rounded-2xl shadow-lg p-8 mb-10 card-hover">
        <h2 class="text-2xl font-bold mb-6 gradient-text">About Me</h2>
        <div class="space-y-4 text-gray-700 leading-relaxed">
            <p>I am <strong class="text-gray-900">Pranav Jeevan P</strong>, a Research Scientist at <a href="https://sync.so/" class="text-blue-600 hover:text-blue-800 font-medium transition-colors">sync</a>, where I develop advanced AI-driven video editing tools. My work focuses on designing and implementing generative architectures—spanning diffusion models, GANs, and transformer-based networks—to enable precise, controllable modification of human appearance, motion, and expression in video sequences.</p>
            <p>I earned my Ph.D. in Artificial Intelligence from the <a href="https://www.ee.iitb.ac.in" class="text-blue-600 hover:text-blue-800 font-medium transition-colors">Department of Electrical Engineering</a> at the <a href="https://www.iitb.ac.in/" class="text-blue-600 hover:text-blue-800 font-medium transition-colors">Indian Institute of Technology Bombay</a>, where I developed resource-efficient neural architectures for various computer vision tasks such as classification, segmentation, inpainting and super-resolution. During my doctoral studies, I was associated with the <em class="text-gray-800">MeDAL (Medical Imaging, Deep Learning, and Artificial Intelligence Lab)</em> under the supervision of <a href="https://www.ee.iitb.ac.in/~asethi/" class="text-blue-600 hover:text-blue-800 font-medium transition-colors">Prof. Amit Sethi</a>.</p>
            <p>Prior to my Ph.D., I completed a Master's in Robotics at the <a href="https://www.iitk.ac.in/" class="text-blue-600 hover:text-blue-800 font-medium transition-colors">Department of Mechanical Engineering</a>, Indian Institute of Technology Kanpur, where I was part of the <a href="http://www.iitk.ac.in/robotics/" class="text-blue-600 hover:text-blue-800 font-medium transition-colors">Center for Mechatronics</a>. Under the guidance of <a href="https://home.iitk.ac.in/~adutta/" class="text-blue-600 hover:text-blue-800 font-medium transition-colors">Prof. Ashish Dutta</a>, I designed and prototyped a lower-extremity exoskeleton for rehabilitation applications.</p>
            <p>I began my professional career as a Post-Graduate Engineering Trainee at the Engineering Research Centre of <a href="https://www.tatamotors.com/" class="text-blue-600 hover:text-blue-800 font-medium transition-colors">Tata Motors Limited</a>, where I conducted vehicle performance and thermal analysis for braking systems. Subsequently, I returned to academia at the <a href="https://physics.iitm.ac.in/" class="text-blue-600 hover:text-blue-800 font-medium transition-colors">Department of Physics</a>, IIT Madras, focusing on theoretical physics, quantum computing, and quantum information under <a href="https://sites.google.com/view/madhok" class="text-blue-600 hover:text-blue-800 font-medium transition-colors">Prof. Vaibhav Madhok</a>.</p>
            <p>I also completed a six-month internship (July 2023–January 2024) with the AI Camera Team of Visual Intelligence Division at <a href="https://research.samsung.com/sri-b" class="text-blue-600 hover:text-blue-800 font-medium transition-colors">Samsung R&D Institute India, Bangalore (SRI-B)</a>, where I developed and optimized deep learning models for image classification, object detection, and generative tasks. These models have been integrated into Samsung's flagship <a href="https://en.wikipedia.org/wiki/Samsung_Galaxy_S24" class="text-blue-600 hover:text-blue-800 font-medium transition-colors">Galaxy S24 series</a>.</p>
            <p>I regularly serve as a reviewer for premier conferences in computer vision and machine learning, including CVPR, ICCV, ECCV, ICLR, AAAI, and WACV.</p>
        </div>
        <div class="mt-8 flex justify-center">
            <a href="https://drive.google.com/file/d/1-BkKK9OD12Yq5J6TGXAQr53f1jmGQXwN/view?usp=sharing" target="_blank" class="bg-gradient-to-r from-blue-500 to-purple-600 text-white px-8 py-3 rounded-lg font-medium hover:from-blue-600 hover:to-purple-700 transition-all duration-300 shadow-lg hover:shadow-xl transform hover:-translate-y-1 inline-flex items-center">
                <i class="fas fa-file-pdf mr-2"></i>
                My Resume
            </a>
        </div>
    </section>

    <!-- Timeline Section -->
    <section class="bg-white rounded-2xl shadow-lg p-8 mb-10 card-hover">
        <h2 class="text-2xl font-bold mb-6 gradient-text">Professional Journey</h2>
        <div class="relative pl-8 border-l-2 border-gray-200">
            <div class="timeline-item">
                <h3 class="text-lg font-semibold text-gray-900">Research Scientist</h3>
                <p class="text-blue-600 font-medium">sync • 2023 – Present</p>
                <p class="text-gray-600 mt-1">Developing AI-driven video editing tools with generative architectures for precise human appearance and motion modification.</p>
            </div>
            <div class="timeline-item">
                <h3 class="text-lg font-semibold text-gray-900">AI Camera Team Intern</h3>
                <p class="text-blue-600 font-medium">Samsung R&D Institute • Jul 2023 – Jan 2024</p>
                <p class="text-gray-600 mt-1">Developed deep learning models for image classification, object detection, and generative tasks integrated into Galaxy S24 series.</p>
            </div>
            <div class="timeline-item">
                <h3 class="text-lg font-semibold text-gray-900">Ph.D. in Artificial Intelligence</h3>
                <p class="text-blue-600 font-medium">IIT Bombay • 2018 – 2023</p>
                <p class="text-gray-600 mt-1">Developed resource-efficient neural architectures for computer vision tasks at MeDAL lab under Prof. Amit Sethi.</p>
            </div>
            <div class="timeline-item">
                <h3 class="text-lg font-semibold text-gray-900">M.Tech in Robotics</h3>
                <p class="text-blue-600 font-medium">IIT Kanpur • 2016 – 2018</p>
                <p class="text-gray-600 mt-1">Designed and prototyped a lower-extremity exoskeleton for rehabilitation applications at Center for Mechatronics.</p>
            </div>
            <div class="timeline-item">
                <h3 class="text-lg font-semibold text-gray-900">Post-Graduate Engineering Trainee</h3>
                <p class="text-blue-600 font-medium">Tata Motors Limited • 2015 – 2016</p>
                <p class="text-gray-600 mt-1">Conducted vehicle performance and thermal analysis for braking systems at Engineering Research Centre.</p>
            </div>
            <div class="timeline-item">
                <h3 class="text-lg font-semibold text-gray-900">Research Associate</h3>
                <p class="text-blue-600 font-medium">IIT Madras • 2014 – 2015</p>
                <p class="text-gray-600 mt-1">Focused on theoretical physics, quantum computing, and quantum information under Prof. Vaibhav Madhok.</p>
            </div>
        </div>
    </section>

    <!-- Publications Section -->
    <section class="bg-white rounded-2xl shadow-lg p-8 mb-10 card-hover">
        <h2 class="text-2xl font-bold mb-6 gradient-text">Recent Publications & Awards</h2>
        <div id="publications-container" class="space-y-3">
            <!-- Publications will be dynamically inserted here -->
        </div>
        <div class="mt-6 text-center">
            <button id="load-more-btn" class="bg-gray-100 hover:bg-gray-200 text-gray-700 px-6 py-2 rounded-lg font-medium transition-colors duration-300">
                Load More
            </button>
        </div>
    </section>

    <!-- Skills Section -->
    <section class="bg-white rounded-2xl shadow-lg p-8 mb-10 card-hover">
        <h2 class="text-2xl font-bold mb-6 gradient-text">Expertise</h2>
        <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
            <div class="bg-blue-50 p-4 rounded-lg text-center">
                <i class="fas fa-brain text-2xl text-blue-600 mb-2"></i>
                <h3 class="font-semibold text-gray-900">Deep Learning</h3>
            </div>
            <div class="bg-purple-50 p-4 rounded-lg text-center">
                <i class="fas fa-image text-2xl text-purple-600 mb-2"></i>
                <h3 class="font-semibold text-gray-900">Computer Vision</h3>
            </div>
            <div class="bg-green-50 p-4 rounded-lg text-center">
                <i class="fas fa-project-diagram text-2xl text-green-600 mb-2"></i>
                <h3 class="font-semibold text-gray-900">Generative Models</h3>
            </div>
            <div class="bg-yellow-50 p-4 rounded-lg text-center">
                <i class="fas fa-microchip text-2xl text-yellow-600 mb-2"></i>
                <h3 class="font-semibold text-gray-900">Neural Architecture</h3>
            </div>
            <div class="bg-red-50 p-4 rounded-lg text-center">
                <i class="fas fa-medkit text-2xl text-red-600 mb-2"></i>
                <h3 class="font-semibold text-gray-900">Medical Imaging</h3>
            </div>
            <div class="bg-indigo-50 p-4 rounded-lg text-center">
                <i class="fas fa-robot text-2xl text-indigo-600 mb-2"></i>
                <h3 class="font-semibold text-gray-900">Robotics</h3>
            </div>
        </div>
        <div class="mt-6 pt-6 border-t border-gray-200">
            <h3 class="font-semibold text-gray-900 mb-3">Programming & Tools</h3>
            <div class="flex flex-wrap gap-2">
                <span class="bg-gray-100 text-gray-800 px-3 py-1 rounded-full text-sm">Python</span>
                <span class="bg-gray-100 text-gray-800 px-3 py-1 rounded-full text-sm">PyTorch</span>
                <span class="bg-gray-100 text-gray-800 px-3 py-1 rounded-full text-sm">TensorFlow</span>
                <span class="bg-gray-100 text-gray-800 px-3 py-1 rounded-full text-sm">CUDA</span>
                <span class="bg-gray-100 text-gray-800 px-3 py-1 rounded-full text-sm">OpenCV</span>
                <span class="bg-gray-100 text-gray-800 px-3 py-1 rounded-full text-sm">MATLAB</span>
                <span class="bg-gray-100 text-gray-800 px-3 py-1 rounded-full text-sm">ROS</span>
                <span class="bg-gray-100 text-gray-800 px-3 py-1 rounded-full text-sm">Git</span>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="text-center text-gray-500 text-sm py-8">
        <p>© 2025 Pranav Jeevan P. All rights reserved.</p>
        <p class="mt-2">Built with HTML, CSS, and JavaScript</p>
    </footer>
</div>

<!-- Custom scripts -->
<script>
// Publications data
const publications = [
    { id: 1, title: "FLD+: Data-efficient Evaluation Metric for Generative Models", venue: "Workshop on Computer Vision for Developing Countries (CV4DC) at ICCV 2025", color: "red" },
    { id: 2, title: "WavePaint: Resource-efficient Token-mixer for Self-supervised Inpainting", venue: "Workshop on Computer Vision for Developing Countries (CV4DC) at ICCV 2025", color: "red" },
    { id: 3, title: "Which Backbone to Use: A Resource-efficient Domain Specific Comparison for Computer Vision", venue: "TMLR Journal", color: "red" },
    { id: 4, title: "Evaluation Metric for Quality Control and Generative Models in Histopathology Images", venue: "ISBI 2025", color: "red" },
    { id: 5, title: "WaveMixSR-V2: Enhancing Super-resolution with Higher Efficiency", venue: "AAAI 2025 Student Abstract and Poster Program (oral presentation)", color: "red" },
    { id: 6, title: "FLeNS: Federated Learning with Enhanced Nesterov-Newton Sketch", venue: "Special Session on Federated Learning at IEEE BigData 2024", color: "red" },
    { id: 7, title: "Adversarial Transport Terms for Unsupervised Domain Adaptation", venue: "ICPR 2024", color: "red" },
    { id: 8, title: "PawFACS: Leveraging Semi-Supervised Learning for Pet Facial Action Recognition", venue: "BMVC 2024 (Patent filed)", color: "red" },
    { id: 9, title: "A Comparative Study of Deep Neural Network Architectures in Magnification Invariant Breast Cancer Histopathology Image Analysis", venue: "CCIS", color: "red" },
    { id: 10, title: "Magnification Invariant Medical Image Analysis: A Comparison of Convolutional Networks, Vision Transformers, and Token Mixers", venue: "Bioimaging 2024 [Best Student Paper Award]", color: "red", award: true },
    { id: 11, title: "WaveMixSR: Resource-efficient Neural Network for Image Super-resolution", venue: "WACV 2024", color: "red" },
    { id: 12, title: "Heterogeneous Graphs Model Spatial Relationships Between Biological Entities for Breast Cancer Diagnosis", venue: "5th MICCAI Workshop on GRaphs in biomedicAl Image anaLysis (GRAIL) 2023", color: "red" },
    { id: 13, title: "Resource-efficient Image Inpainting", venue: "ICLR 2023", color: "red" },
    { id: 14, title: "Resource-efficient Hybrid X-Formers for Vision", venue: "WACV 2022", color: "red" },
    { id: 15, title: "So You Think You're Funny?\": Rating the Humour Quotient in Standup Comedy", venue: "EMNLP 2021", color: "red" }
];

// Display publications
const publicationsContainer = document.getElementById('publications-container');
const loadMoreBtn = document.getElementById('load-more-btn');
const publicationsPerPage = 5;
let currentPage = 1;

function displayPublications(page) {
    const startIndex = (page - 1) * publicationsPerPage;
    const endIndex = startIndex + publicationsPerPage;
    const paginatedPublications = publications.slice(startIndex, endIndex);

    // Clear container
    publicationsContainer.innerHTML = '';

    // Add publications with animation
    paginatedPublications.forEach((pub, index) => {
        setTimeout(() => {
            const pubElement = document.createElement('div');
            pubElement.className = 'publication-item bg-gray-50 p-4 rounded-lg border-l-4 border-red-500';
            pubElement.style.opacity = '0';
            pubElement.style.transform = 'translateY(20px)';

            const awardIcon = pub.award ? '<i class="fas fa-trophy text-yellow-500 ml-2"></i>' : '';

            pubElement.innerHTML = `
                <div class="flex items-start">
                    <span class="bg-red-100 text-red-800 text-xs font-semibold mr-2 px-2.5 py-0.5 rounded">${page * publicationsPerPage - publicationsPerPage + index + 1}</span>
                    <div class="ml-3 flex-1">
                        <h3 class="font-medium text-gray-900">${pub.title}</h3>
                        <p class="text-${pub.color}-600 text-sm mt-1">${pub.venue}${awardIcon}</p>
                    </div>
                </div>
            `;

            publicationsContainer.appendChild(pubElement);

            // Trigger animation
            setTimeout(() => {
                pubElement.style.transition = 'all 0.5s ease';
                pubElement.style.opacity = '1';
                pubElement.style.transform = 'translateY(0)';
            }, 50 * index);
        }, 100 * index);
    });
}

// Initial display
displayPublications(currentPage);

// Load more button click
loadMoreBtn.addEventListener('click', () => {
    const nextPage = currentPage + 1;
    const startIndex = (nextPage - 1) * publicationsPerPage;

    if (startIndex < publications.length) {
        currentPage = nextPage;
        displayPublications(currentPage);

        if (startIndex + publicationsPerPage >= publications.length) {
            loadMoreBtn.style.display = 'none';
        }
    } else {
        loadMoreBtn.innerHTML = 'All publications loaded';
        loadMoreBtn.disabled = true;
        loadMoreBtn.style.opacity = '0.6';
        setTimeout(() => {
            loadMoreBtn.style.display = 'none';
        }, 2000);
    }
});

// Add smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Add scroll animations
const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate-fade-in');
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe sections
document.querySelectorAll('section').forEach(section => {
    section.style.opacity = '0';
    section.style.transform = 'translateY(20px)';
    section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(section);
});

// Add typing effect to header
const headerText = document.querySelector('h1');
if (headerText) {
    headerText.classList.add('typing-effect');
}
</script>



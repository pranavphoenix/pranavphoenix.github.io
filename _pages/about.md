---
permalink: /
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pranav Jeevan P - Research Scientist</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        body {
            font-family: 'Inter', sans-serif;
        }
        .gradient-text {
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .card-hover {
            transition: all 0.3s ease;
        }
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
        .timeline-item:last-child:after {
            display: none;
        }
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
    /* <!-- </style>
    <style> --> */
      body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        line-height: 1.6;
        color: #333;
        max-width: 1800px;
        margin: 0 auto;
        padding: 20px;
      }
      .container {
        margin: 0 auto;
        padding: 0;
      }
      .row {
        display: flex;
        align-items: flex-start;
        margin: 20px 0;
      }
      #dhead {
        margin-bottom: 30px;
      }
      #dpic {
        margin-right: 20px;
        flex-shrink: 0;
      }
      .ppic {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        object-fit: cover;
      }
      h1 {
        margin: 0 0 5px 0;
        font-size: 32px;
      }
      h2 {
        margin: 0 0 15px 0;
        font-size: 18px;
        font-weight: normal;
        color: #555;
      }
      #dico {
        margin: 10px 0;
      }
      .iico {
        width: 24px;
        height: 24px;
        margin-right: 15px;
        opacity: 0.7;
        transition: opacity 0.2s;
      }
      .iico:hover {
        opacity: 1;
      }
      hr {
        border: none;
        border-top: 1px solid #eee;
        margin: 30px 0;
      }
      .entry {
        display: flex;
        margin-bottom: 30px;
      }
      .timespan {
        width: 50px;
        font-weight: bold;
        color: #555;
        margin-right: 10px;
        flex-shrink: 0;
        text-align: right;
        font-size: 14px;
      }
      .ico {
        position: relative;
        width: 60px;
        flex-shrink: 0;
      }
      .entry-dot {
        position: absolute;
        top: 10px;
        left: 15px;
        width: 12px;
        height: 12px;
        background-color: #ddd;
        border-radius: 50%;
        z-index: 1;
      }
      .ico img {
        position: absolute;
        top: 0;
        left: 0;
        width: 40px;
        height: 40px;
        border-radius: 5px;
      }
      .desc {
        flex: 1;
        padding-left: 0;
        text-align: justify;
      }
      .htxt {
        margin-bottom: 15px;
      }
      .hassets {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
      }
      .hasset {
        position: relative;
      }
      .video {
        border-radius: 8px;
      }
      .ctitle {
        font-size: 24px;
        font-weight: bold;
        margin: 40px 0 20px 0;
        padding-bottom: 10px;
        border-bottom: 1px solid #eee;
      }
      .card {
        width: calc(33.333% - 10px);
        margin: 0 5px 20px 5px;
        display: inline-block;
        vertical-align: top;
      }
      @media (max-width: 768px) {
        .card {
          width: calc(50% - 10px);
        }
      }
      @media (max-width: 480px) {
        .card {
          width: 100%;
        }
      }
      .ccimg img {
        width: 100%;
        border-radius: 8px;
      }
      .cdesc {
        margin-top: 8px;
        font-size: 14px;
      }
      .project {
        display: flex;
        margin-bottom: 20px;
        align-items: flex-start;
      }
      .pico {
        width: 60px;
        margin-right: 15px;
        flex-shrink: 0;
      }
      .pico img {
        width: 60px;
        height: 60px;
        border-radius: 8px;
      }
      .pdesc {
        flex: 1;
      }
      .pend {
        width: 60px;
        flex-shrink: 0;
      }
      .pub {
        margin-bottom: 15px;
      }
      .pub-title {
        font-weight: bold;
      }
      .pub-venue {
        font-size: 14px;
        color: #555;
        margin: 3px 0;
      }
      .pub-authors {
        font-size: 14px;
        color: #666;
      }
      .tul {
        list-style: none;
        padding-left: 0;
      }
      .til {
        margin: 5px 0;
      }
      .tilb {
        font-weight: bold;
      }
      .nodot {
        list-style: none;
        padding-left: 0;
      }
      .nodot li {
        margin: 8px 0;
      }
      /* News Section Styles */
      .news-section {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 8px;
        margin: 30px 0;
        overflow: hidden;
      }
      .news-title {
        font-size: 24px;
        font-weight: bold;
        margin: 0 0 15px 0;
        color: #333;
        border-bottom: 1px solid #eee;
        padding-bottom: 10px;
      }
      .news-container {
        overflow: hidden;
        position: relative;
        height: 500px;
      }
      .news-list {
        list-style: none;
        padding: 0;
        margin: 0;
        position: absolute;
        width: 100%;
        animation: scrollNews 40s linear infinite;
      }
      .news-item {
        border-top: 1px solid #eee;
        padding: 15px 0;
        opacity: 0.7;
        transition: opacity 0.3s;
      }
      .news-item:hover {
        opacity: 1;
      }
      .news-item:first-child {
        border-top: none;
      }
      .news-date {
        display: inline-block;
        background-color: #e3f2fd;
        color: #1565c0;
        font-weight: bold;
        font-size: 12px;
        padding: 4px 8px;
        border-radius: 4px;
        margin-right: 10px;
      }
      .news-content {
        font-size: 16px;
        color: #333;
      }
      .news-content a {
        color: #1976d2;
        text-decoration: none;
      }
      .news-content a:hover {
        text-decoration: underline;
      }
      @keyframes scrollNews {
        0% {
          transform: translateY(0);
        }
        100% {
          transform: translateY(-100%);
        }
      }
      /* Add a gradient fade at the bottom to enhance the looping effect */
      .news-section::after {
        content: '';
        position: absolute;
        bottom: 20px;
        left: 20px;
        right: 20px;
        height: 20px;
        background: linear-gradient(to bottom, rgba(248, 249, 250, 0), rgba(248, 249, 250, 1));
        pointer-events: none;
        z-index: 1;
      }
    </style>
</head>


<h2 class="text-2xl font-bold mb-6" style="color: #111;">About Me</h2>

<div id="history" class="container">
      <div class="entry row">
        <div class="timespan">
          2025 -
        </div>
        <div class="ico">
          <img src="https://sync.so/favicon.ico" />
        </div>
        <div class="desc">
           I am working as a <strong>Research Scientist</strong> at <a href="https://sync.so/" style="text-decoration: none; color: #2563eb;">sync</a>, where I develop advanced AI-driven video editing tools. My work focuses on designing and implementing generative architectures—spanning diffusion models, GANs, and transformer-based networks—to enable precise, controllable modification of human appearance, motion, and expression in video sequences.
        </div>
      </div>
      <div class="entry row">
        <div class="timespan">
          2020 - 2025
        </div>
        <div class="ico">
          <img src="https://pranavphoenix.github.io/images/IITB.png" />
        </div>
        <div class="desc">
          I earned my <strong>Ph.D. in Artificial Intelligence</strong> from the <a href="https://www.ee.iitb.ac.in" style="text-decoration: none; color: #2563eb;">Department of Electrical Engineering</a> at the <a href="https://www.iitb.ac.in/" style="text-decoration: none; color: #2563eb;">Indian Institute of Technology Bombay</a>, where I developed resource-efficient neural architectures for various computer vision tasks such as classification, segmentation, inpainitng and super-resolution. During my doctoral studies, I was associated with the <em>MeDAL (Medical Imaging, Deep Learning, and Artificial Intelligence Lab)</em> under the supervision of <a href="https://www.ee.iitb.ac.in/~asethi/" style="text-decoration: none; color: #2563eb;">Prof. Amit Sethi</a>.
        </div>
      </div>
      <div class="entry row">
        <div class="timespan">
          2023 - 2024
        </div>
        <div class="ico">
          <img src="https://upload.wikimedia.org/wikipedia/commons/2/24/Samsung_Logo.svg" />
        </div>
        <div class="desc">
           I also completed a six-month <strong>internship</strong> (July 2023–January 2024) with the AI Camera Team of Visual Intelligence Division at <a href="https://research.samsung.com/sri-b" style="text-decoration: none; color: #2563eb;">Samsung R&D Institute India, Bangalore (SRI-B)</a>, where I developed and optimized deep learning models for image classification, object detection, and generative tasks. These models have been integrated into Samsung’s flagship <a href="https://en.wikipedia.org/wiki/Samsung_Galaxy_S24" style="text-decoration: none; color: #2563eb;">Galaxy S24 series</a>.
        </div>
      </div>
      <div class="entry row">
        <div class="timespan">
          2017 - 2019
        </div>
        <div class="ico">
          <img src="https://pranavphoenix.github.io/images/IITM.png" />
        </div>
        <div class="desc">
          I returned to <strong>Academic Research</strong> at the <a href="https://physics.iitm.ac.in/" style="text-decoration: none; color: #2563eb;">Department of Physics</a>, IIT Madras, focusing on theoretical physics, quantum computing, and quantum information under <a href="https://sites.google.com/view/madhok" style="text-decoration: none; color: #2563eb;">Prof. Vaibhav Madhok</a>.
        </div>
      </div>
      <div class="entry row">
        <div class="timespan">
          2015 - 2016
        </div>
        <div class="ico">
          <img src="https://pranavphoenix.github.io/images/tata.png" />
        </div>
        <div class="desc">
          <strong>Post-Graduate Engineering Trainee</strong> at the Engineering Research Centre of <a href="https://www.tatamotors.com/" style="text-decoration: none; color: #2563eb;">Tata Motors Limited</a>, where I conducted vehicle performance and thermal analysis for braking systems.
        </div>
      </div>
      <div class="entry row">
        <div class="timespan">
          2013 - 2015
        </div>
        <div class="ico">
          <img src="https://pranavphoenix.github.io/images/IITK.png" />
        </div>
        <div class="desc">
          <strong>M.Tech in Robotics</strong> at the <a href="https://www.iitk.ac.in/" style="text-decoration: none; color: #2563eb;">Department of Mechanical Engineering</a>, Indian Institute of Technology Kanpur, where I was part of the <a href="http://www.iitk.ac.in/robotics/" style="text-decoration: none; color: #2563eb;">Center for Mechatronics</a>. Under the guidance of <a href="https://home.iitk.ac.in/~adutta/" style="text-decoration: none; color: #2563eb;">Prof. Ashish Dutta</a>, I designed and prototyped a lower-extremity exoskeleton for rehabilitation applications.
        </div>
      </div>
      <div class="entry row">
        <div class="timespan">
          2009 - 2013
        </div>
        <div class="ico">
          <img src="/images/calicut.png" />
        </div>
        <div class="desc">
          <strong>B.Tech in Mechanical Engineering</strong> from <a href="https://www.nssce.ac.in/" style="text-decoration: none; color: #2563eb;">NSS College of Engineering</a>, <a href="https://uoc.ac.in/" style="text-decoration: none; color: #2563eb;">University of Calicut</a>. 
        </div>
      </div>
</div>


<div style="text-align: justify; margin-top: 1em;">
  I regularly serve as a reviewer for premier conferences in computer vision and machine learning, including CVPR, ICCV, ECCV, ICLR, AAAI, and WACV.
</div>




<div class="mt-8 flex justify-center">
  <a href="https://drive.google.com/file/d/1-BkKK9OD12Yq5J6TGXAQr53f1jmGQXwN/view?usp=sharing" target="_blank" class="bg-gradient-to-r from-blue-500 to-purple-600 text-white px-8 py-3 rounded-lg font-medium hover:from-blue-600 hover:to-purple-700 transition-all duration-300 shadow-lg hover:shadow-xl transform hover:-translate-y-1 inline-flex items-center" style="text-decoration: none;">
    <i class="fas fa-file-pdf mr-2"></i>
    My Resume
  </a>
</div>

<!-- News Section -->
<div class="container news-section">
    <div class="news-title">News</div>
    <div class="news-container">
    <ul class="news-list">
        <!-- First set of news items -->
        <li class="news-item">
        <span class="news-date">JUL'25</span>
        <div class="news-content">Our paper "<strong>FLD+</strong>: a data-efficient evaluation metric for generative models" has been accepted for publication at <strong>ICCV 2025</strong>.</div>
        </li>
        <li class="news-item">
        <span class="news-date">JUL'25</span>
        <div class="news-content">Our paper "<strong>WavePaint</strong>: a resource-efficient token-mixer for self-supervised inpainting" has been accepted for publication at <strong>ICCV 2025</strong>.</div>
        </li>
        <li class="news-item">
        <span class="news-date">DEC'24</span>
        <div class="news-content">Our Paper "<strong>WaveMixSR-V2</strong>, enhancing super-resolution with higher efficiency" accepted at <strong>AAAI 2025</strong>.</div>
        </li>
        <li class="news-item">
        <span class="news-date">JAN'24</span>
        <div class="news-content">Successfully completed a six-month internship with the AI Camera Team at Samsung R&D Institute, Bangalore.</div>
        </li>
        <!-- <li class="news-item">
        <span class="news-date">OCT'24</span>
        <div class="news-content">Defended Ph.D. thesis on resource-efficient neural architectures for computer vision tasks at IIT Bombay.</div>
        </li> -->
        <li class="news-item">
        <span class="news-date">MAY'24</span>
        <div class="news-content">Paper on <strong>FLeNS</strong>, Federated Learning with Enhanced Nesterov-Newton Sketch, has been accepted at <strong>IEEE BigData 2024</strong>.</div>
        </li>
        <li class="news-item">
        <span class="news-date">APR'24</span>
        <div class="news-content">Paper on <strong>Adversarial Transport Terms for Unsupervised Domain Adaptation</strong> accepted at <strong>ICPR 2024</strong>.</div>
        </li>
        <li class="news-item">
        <span class="news-date">MAR'24</span>
        <div class="news-content">Paper on <strong>PawFACS</strong> for pet facial action recognition accepted at <strong>BMVC 2024</strong>.</div>
        </li>
        <li class="news-item">
        <span class="news-date">FEB'24</span>
        <div class="news-content">Our work on Magnification Invariant Medical Image Analysis received the <strong>Best Student Paper Award</strong> at Bioimaging 2024.</div>
        </li>
        <!-- <li class="news-item">
        <span class="news-date">JAN'24</span>
        <div class="news-content">Paper on a comparative study of deep neural networks in breast cancer analysis has been published in <strong>CCIS</strong>.</div>
        </li> -->
        <li class="news-item">
        <span class="news-date">OCT'23</span>
        <div class="news-content">Our paper on <strong>WaveMixSR</strong>, a resource-efficient neural network for image super-resolution, accepted at <strong>WACV 2024</strong>.</div>
        </li>
        <li class="news-item">
        <span class="news-date">NOV'23</span>
        <div class="news-content">Paper on Heterogeneous Graphs Model Spatial Relationships for Breast Cancer Diagnosis accepted at <strong>MICCAI 2023</strong>.</div>
        </li>
        <!-- Duplicate the news items to create a seamless loop -->
        <li class="news-item">
        <span class="news-date">JUL'25</span>
        <div class="news-content">Our paper "<strong>FLD+</strong>: a data-efficient evaluation metric for generative models" has been accepted for publication at <strong>ICCV 2025</strong>.</div>
        </li>
        <li class="news-item">
        <span class="news-date">JUL'25</span>
        <div class="news-content">Our paper "<strong>WavePaint</strong>: a resource-efficient token-mixer for self-supervised inpainting" has been accepted for publication at <strong>ICCV 2025</strong>.</div>
        </li>
        <li class="news-item">
        <span class="news-date">DEC'24</span>
        <div class="news-content">Our Paper "<strong>WaveMixSR-V2</strong>, enhancing super-resolution with higher efficiency" accepted at <strong>AAAI 2025</strong>.</div>
        </li>
        <li class="news-item">
        <span class="news-date">JAN'24</span>
        <div class="news-content">Successfully completed a six-month internship with the AI Camera Team at Samsung R&D Institute, Bangalore.</div>
        </li>
        <!-- <li class="news-item">
        <span class="news-date">OCT'24</span>
        <div class="news-content">Defended Ph.D. thesis on resource-efficient neural architectures for computer vision tasks at IIT Bombay.</div>
        </li> -->
        <li class="news-item">
        <span class="news-date">MAY'24</span>
        <div class="news-content">Paper on <strong>FLeNS</strong>, Federated Learning with Enhanced Nesterov-Newton Sketch, has been accepted at <strong>IEEE BigData 2024</strong>.</div>
        </li>
        <li class="news-item">
        <span class="news-date">APR'24</span>
        <div class="news-content">Paper on <strong>Adversarial Transport Terms for Unsupervised Domain Adaptation</strong> accepted at <strong>ICPR 2024</strong>.</div>
        </li>
        <li class="news-item">
        <span class="news-date">MAR'24</span>
        <div class="news-content">Paper on <strong>PawFACS</strong> for pet facial action recognition accepted at <strong>BMVC 2024</strong>.</div>
        </li>
        <li class="news-item">
        <span class="news-date">FEB'24</span>
        <div class="news-content">Our work on Magnification Invariant Medical Image Analysis received the <strong>Best Student Paper Award</strong> at Bioimaging 2024.</div>
        </li>
        <!-- <li class="news-item">
        <span class="news-date">JAN'24</span>
        <div class="news-content">Paper on a comparative study of deep neural networks in breast cancer analysis has been published in <strong>CCIS</strong>.</div>
        </li> -->
        <li class="news-item">
        <span class="news-date">OCT'23</span>
        <div class="news-content">Our paper on <strong>WaveMixSR</strong>, a resource-efficient neural network for image super-resolution, accepted at <strong>WACV 2024</strong>.</div>
        </li>
        <li class="news-item">
        <span class="news-date">NOV'23</span>
        <div class="news-content">Paper on Heterogeneous Graphs Model Spatial Relationships for Breast Cancer Diagnosis accepted at <strong>MICCAI 2023</strong>.</div>
        </li>
    </ul>
    </div>
</div>


 <section class="bg-white rounded-2xl shadow-lg p-8 mb-10 card-hover">
            <h2 class="text-2xl font-bold mb-6" style="color: #111;">Expertise</h2>
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
                <div class="bg-pink-50 p-4 rounded-lg text-center">
                    <i class="fas fa-atom text-2xl text-pink-600 mb-2"></i>
                    <h3 class="font-semibold text-gray-900">Theoretical Physics</h3>
                </div>
                <div class="bg-teal-50 p-4 rounded-lg text-center">
                    <i class="fas fa-language text-2xl text-teal-600 mb-2"></i>
                    <h3 class="font-semibold text-gray-900">NLP</h3>
                </div>
                <div class="bg-orange-50 p-4 rounded-lg text-center">
                    <i class="fas fa-cogs text-2xl text-orange-600 mb-2"></i>
                    <h3 class="font-semibold text-gray-900">Mechanical Engg</h3>
                </div>
            </div>
            <div class="mt-6 pt-6 border-t border-gray-200" style="color: #111;">
                <h3 class="font-semibold text-gray-900 mb-3">Programming & Tools</h3>
                <div class="flex flex-wrap gap-2">
                    <span class="bg-gray-100 text-gray-800 px-3 py-1 rounded-full text-sm">Python</span>
                    <span class="bg-gray-100 text-gray-800 px-3 py-1 rounded-full text-sm">PyTorch</span>
                    <span class="bg-gray-100 text-gray-800 px-3 py-1 rounded-full text-sm">TensorFlow</span>
                    <span class="bg-gray-100 text-gray-800 px-3 py-1 rounded-full text-sm">CUDA</span>
                    <span class="bg-gray-100 text-gray-800 px-3 py-1 rounded-full text-sm">OpenCV</span>
                    <span class="bg-gray-100 text-gray-800 px-3 py-1 rounded-full text-sm">MATLAB</span>
                    <span class="bg-gray-100 text-gray-800 px-3 py-1 rounded-full text-sm">C++</span>
                    <span class="bg-gray-100 text-gray-800 px-3 py-1 rounded-full text-sm">Git</span>
                </div>
            </div>
</section>




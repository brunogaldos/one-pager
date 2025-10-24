# Project Technical Reference: Polisense.AI One-Pager Generator

This document contains a full-fidelity dump of all project components, as requested.

## 1. File Structure and Naming Conventions

The project utilizes the following directory and file structure:

```
.
├── assets/                 # Directory for all static image assets.
│   ├── demo.jpg
│   ├── logo_new.png
│   └── supported-by/
│       ├── a-logo.jpg
│       ├── b-logo.png
│       └── c-logo.png
├── one-pager/              # Output directory for final PDF documents.
│   ├── ES-polisense-one-pager.pdf
│   └── polisense-one-pager.pdf
├── generate_pdf.py         # Main Python script for PDF generation.
├── labels.json             # Data file for English language content.
├── labels_es.json          # Data file for Spanish language content.
├── polisense-A4.html       # Master HTML template for the one-pager.
├── README.md               # Project documentation.
└── requirements.txt        # Python dependency list.
```

**Naming Conventions:**
-   Language-specific content files are named `labels_{lang_code}.json` (e.g., `labels_es.json`). The base `labels.json` is treated as English (`en`).
-   Output PDFs are named `{LANG_CODE}-polisense-one-pager.pdf` for non-English versions.

## 2. Full Code, Scripts, and Configuration Files

### 2.1. `generate_pdf.py`

This script orchestrates the PDF generation process.

```python
#!/usr/bin/env python3
"""
PDF Generator for Polisense One-Pager
Uses Playwright to convert HTML to PDF with proper styling and colors
"""

import asyncio
import sys
import subprocess
from pathlib import Path
from playwright.async_api import async_playwright
import http.server
import socketserver
import threading
import socket
import json

def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

class QuietHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass # Suppress logging

def run_server(port, server_started):
    handler = QuietHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        server_started.set()
        httpd.serve_forever()

async def generate_pdf(language='en'):
    """Generate PDF from HTML file using Playwright"""
    
    # File paths
    html_file = Path("polisense-A4.html")
    output_dir = Path("one-pager")
    output_dir.mkdir(exist_ok=True)
    
    if language == 'en':
        pdf_file = output_dir / "polisense-one-pager.pdf"
        labels_file = "labels.json"
    else:
        pdf_file = output_dir / f"{language.upper()}-polisense-one-pager.pdf"
        labels_file = f"labels_{language}.json"

    if not html_file.exists():
        print(f"❌ Error: {html_file} not found")
        return False

    port = find_free_port()
    server_started = threading.Event()
    server_thread = threading.Thread(target=run_server, args=(port, server_started))
    server_thread.daemon = True
    server_thread.start()
    server_started.wait() # Wait for server to be ready
    
    try:
        print(f"🚀 Starting PDF generation for language: {language.upper()}...")
        
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()

            page.on("console", lambda msg: print(f"📄 PAGE LOG: {msg.text}"))
            
            # Pass the labels file name to the page via query parameter
            url = f"http://localhost:{port}/{html_file}?lang={language}"
            print(f"📄 Loading HTML file from {url}...")
            await page.goto(url, wait_until="networkidle")
            
            await page.wait_for_selector('body.content-loaded', timeout=5000)

            print("🎨 Generating PDF...")
            pdf_bytes = await page.pdf(
                format='A4',
                print_background=True,
                margin={'top': '0mm', 'right': '0mm', 'bottom': '0mm', 'left': '0mm'}
            )
            await browser.close()
            
        with open(pdf_file, "wb") as f:
            f.write(pdf_bytes)
            
        if pdf_file.exists():
            file_size = pdf_file.stat().st_size / 1024
            # The verify_pdf_page_count function was removed for brevity in this context
            print(f"📄 PDF generated: {pdf_file} ({file_size:.1f} KB)")
            return True
        else:
            print("❌ Error: PDF file was not created")
            return False
            
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        # The server thread is a daemon, so it will exit when the main thread exits.
        pass

if __name__ == "__main__":
    # Generate English version
    en_success = asyncio.run(generate_pdf(language='en'))
    
    # Generate Spanish version
    es_success = asyncio.run(generate_pdf(language='es'))

    sys.exit(0 if en_success and es_success else 1)
```

### 2.2. `polisense-A4.html`

This file is the complete HTML and CSS template for the document.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Polisense.AI - A4 One Pager</title>
    <style>
        :root {
            --bg-primary: #293a4f;
            --color-primary: #50e7ff;
            --color-accent: #02ffb9;
            --color-text: #ffffff;
            --color-text-secondary: rgba(255, 255, 255, 0.8);
            --color-text-muted: rgba(255, 255, 255, 0.6);
            --gradient-primary: linear-gradient(135deg, #50e7ff 0%, #02ffb9 100%);
            --gradient-card: linear-gradient(145deg, rgba(80, 231, 255, 0.1) 0%, rgba(2, 255, 185, 0.05) 100%);
        }

        /* These styles are ONLY for printing */
        * {
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            border: none !important; /* Globally remove all borders */
            box-shadow: none !important; /* Globally remove all shadows */
        }

        html, body {
            background: var(--bg-primary) !important;
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            line-height: 1.2;
            color: var(--color-text) !important;
        }

        @page {
            size: A4;
            margin: 0;
        }

        .page-wrapper {
            display: flex;
            flex-direction: column;
            width: 100%;
            height: 100vh;
            padding: 10mm;
            gap: 10px;
            border-top: 1px solid transparent !important; /* Fix for potential rendering artifact line */
        }

        .header, .problem {
            flex-shrink: 0;
        }
        
        .card {
            background: var(--gradient-card) !important;
            border-radius: 8px;
            padding: 10px;
            display: flex;
            flex-direction: column;
        }

        h2, h3 {
            border-bottom: none !important; /* Force remove bottom border */
        }

        /* Header */
        .header {
            display: flex;
            align-items: center;
            gap: 20px;
            padding-bottom: 8px !important;
            border-bottom: none !important; /* Force remove bottom border */
        }
        .header .logo { width: 100px; height: auto; }
        .header .header-text {
            text-align: left;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .header h1 { font-size: 3rem; font-weight: 800; background: var(--gradient-primary); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
        .header p { font-size: 1.5rem; color: var(--color-text-secondary) !important; }

        /* Problem */
        .problem-container {
            display: flex;
            gap: 20px;
            align-items: stretch;
        }
        .crisis-summary {
            flex: 1; /* 25% */
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }
        .crisis-summary-content {
            flex-grow: 1;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .problem-details {
            flex: 3; /* 75% */
            margin-top: 0;
        }
        .problem h2 { font-size: 1.05rem; text-align: center; color: var(--color-primary) !important; margin-bottom: 11px; }
        .problem .crisis-summary p { text-align: center; color: var(--color-text-secondary) !important; font-size: 0.9rem; margin-bottom: 11px !important; }

        .problem-details h3 {
            font-size: 1.05rem;
            color: var(--color-accent) !important;
            text-align: center;
            margin-bottom: 6px !important;
        }
        .problem-details p {
            font-size: 0.9rem;
            margin-bottom: 6px !important;
        }
        .pain-points-container {
            display: flex;
            justify-content: space-around;
            gap: 7px;
            margin-top: 7px;
        }
        .pain-point-card {
            flex: 1;
            text-align: center;
        }
        .pain-point-card {
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }
        .pain-point-card p {
             font-size: 0.75rem;
        }
        .pain-point-card i {
            font-size: 1.5rem;
            color: var(--color-accent);
            margin-bottom: 6px;
        }
        .problem-details ul {
            list-style-position: inside;
            padding-left: 0;
        }
        .problem-details li {
            font-size: 0.95rem;
            margin-bottom: 4px !important;
        }
        .problem p { text-align: center; color: var(--color-text-secondary) !important; font-size: 0.9rem; margin-bottom: 15px !important; }

        /* Main Content Area */
        .main-content {
            flex-grow: 1;
            min-height: 0;
            display: flex;
            flex-direction: column; /* Stack sections vertically */
            gap: 10px;
        }

        .opportunity-pillars, .dashboard-features {
            flex: 1;
        }
        
        /* Opportunity & Pillars */
        .opportunity-pillars h3 { font-size: 1.05rem; color: var(--color-accent) !important; text-align: center; margin-bottom: 8px !important; border-bottom: none; }
        .opportunity-pillars > p { font-size: 0.9rem; margin-bottom: 10px !important; }
        .pillars-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 8px;
            flex-grow: 1;
            align-items: center;
        }
        .pillar-card {
            justify-content: center;
            text-align: center;
            padding-top: 5px;
        }
        .pillar-card i {
            font-size: 1.7rem;
            color: var(--color-primary);
            margin-bottom: 8px;
        }
        .pillar-card .pillar-title { font-size: 0.9rem; color: var(--color-primary) !important; font-weight: 600; margin-bottom: 4px; }
        .pillar-card .pillar-description { font-size: 0.75rem; color: var(--color-text-muted) !important; }

        /* Dashboard & Features */
        .dashboard-features {
            height: 100%;
        }
        .dashboard-features h3 {
            font-size: 1.05rem;
            color: var(--color-accent) !important;
            margin-bottom: 8px !important;
            border-bottom: none;
            text-align: center;
        }
        .dashboard-content {
            display: grid;
            grid-template-columns: 2.25fr 1fr;
            gap: 10px;
            align-items: center;
            flex-grow: 1;
        }
        .dashboard-image {
            width: 80%;
            border-radius: 6px;
            display: block;
            margin: 0 auto;
        }
        .features-list ul { list-style: none; padding: 0; }
        .features-list li { background: var(--gradient-card) !important; border-radius: 4px; padding: 6px; margin-bottom: 5px !important; font-weight: 500; font-size: 0.77rem; }
        .features-list i { color: var(--color-primary) !important; margin-right: 6px; }

        /* Footer */
        .footer {
            margin-top: auto;
            flex-shrink: 0;
            text-align: center;
        }
        .results-summary p { font-size: 1.5rem; font-weight: 600; color: var(--color-accent) !important; margin-bottom: 8px !important; }
        
        .supported-by {
            margin: 10px 0;
        }
        .supported-by h4 {
            font-size: 1rem;
            color: var(--color-text-secondary) !important;
            margin-bottom: 8px !important;
        }
        .supporter-logos {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 25px;
        }
        .supporter-logos img {
            height: 40px;
            width: auto;
            filter: grayscale(100%) brightness(3);
        }

        .contact-info { display: flex; justify-content: center; gap: 25px; margin-top: 10px; }
        .contact-info span { font-size: 1rem; }
        .contact-info i { color: var(--color-primary) !important; margin-right: 5px; }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div class="page-wrapper">
        
        <!-- Header -->
        <header class="header">
            <img src="assets/logo_new.png" alt="Polisense.AI Logo" class="logo">
            <div class="header-text">
                <h1 id="header-title"></h1>
                <p id="header-subtitle"></p>
            </div>
        </header>

        <!-- Problem -->
        <section class="problem">
            <div class="problem-container">
                <div class="crisis-summary card">
                    <h2 id="problem-crisis-title"></h2>
                    <div class="crisis-summary-content">
                        <p id="problem-crisis-text"></p>
                    </div>
                </div>
                <div class="problem-details card">
                    <h3 id="problem-local_gov-title"></h3>
                    <p id="problem-local_gov-text"></p>
                    <div id="problem-local_gov-pain_points" class="pain-points-container">
                        <!-- Pain points will be inserted here by JS -->
                    </div>
                </div>
            </div>
        </section>

        <!-- Main Content Area -->
        <main class="main-content">
            <div class="opportunity-pillars card">
                <h3 id="main_content-opportunity-title"></h3>
                <p id="main_content-opportunity-text"></p>
                <div id="main_content-opportunity-pillars" class="pillars-container">
                    <!-- Pillars will be inserted here by JS -->
                </div>
            </div>
            <div class="dashboard-features card">
                <h3 id="main_content-features-title"></h3>
                <div class="dashboard-content">
                    <img src="assets/demo.jpg" alt="Polisense.AI Dashboard" class="dashboard-image">
                    <div class="features-list">
                        <ul id="main_content-features-list">
                            <!-- Features will be inserted here by JS -->
                        </ul>
                    </div>
                </div>
            </div>
        </main>

        <!-- Footer -->
        <footer class="footer">
            <div class="results-summary">
                <p id="footer-results"></p>
            </div>
            <div class="supported-by">
                <h4 id="footer-supported_by"></h4>
                <div class="supporter-logos">
                    <img src="assets/supported-by/a-logo.jpg" alt="Supporter A Logo">
                    <img src="assets/supported-by/b-logo.png" alt="Supporter B Logo">
                    <img src="assets/supported-by/c-logo.png" alt="Supporter C Logo">
                </div>
            </div>
            <div id="footer-contact" class="contact-info">
                <!-- Contact info will be inserted here by JS -->
            </div>
        </footer>

    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Function to get query parameters
            const getQueryParam = (param) => {
                const urlParams = new URLSearchParams(window.location.search);
                return urlParams.get(param);
            };

            // Determine which labels file to load
            const lang = getQueryParam('lang') || 'en';
            const labelsFile = lang === 'en' ? 'labels.json' : `labels_${lang}.json`;
            console.log(`Loading labels from: ${labelsFile}`);

            fetch(labelsFile)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`Network response was not ok: ${response.statusText} for file ${labelsFile}`);
                    }
                    return response.json();
                })
                .then(data => {
                    // Header
                    document.getElementById('header-title').innerHTML = data.header.title;
                    document.getElementById('header-subtitle').innerHTML = data.header.subtitle;

                    // Problem Section
                    document.getElementById('problem-crisis-title').innerHTML = data.problem.crisis.title;
                    document.getElementById('problem-crisis-text').innerHTML = data.problem.crisis.text;
                    document.getElementById('problem-local_gov-title').innerHTML = data.problem.local_gov.title;
                    document.getElementById('problem-local_gov-text').innerHTML = data.problem.local_gov.text;
                    
                    const painPointsContainer = document.getElementById('problem-local_gov-pain_points');
                    painPointsContainer.innerHTML = ''; // Clear existing
                    data.problem.local_gov.pain_points.forEach(point => {
                        const pointDiv = document.createElement('div');
                        pointDiv.className = 'pain-point-card';
                        pointDiv.innerHTML = `<i class="${point.icon}"></i><p>${point.text}</p>`;
                        painPointsContainer.appendChild(pointDiv);
                    });

                    // Main Content
                    document.getElementById('main_content-opportunity-title').innerHTML = data.main_content.opportunity.title;
                    document.getElementById('main_content-opportunity-text').innerHTML = data.main_content.opportunity.text;

                    const pillarsContainer = document.getElementById('main_content-opportunity-pillars');
                    pillarsContainer.innerHTML = ''; // Clear existing
                    data.main_content.opportunity.pillars.forEach(pillar => {
                        const pillarDiv = document.createElement('div');
                        pillarDiv.className = 'pillar-card';
                        pillarDiv.innerHTML = `<i class="${pillar.icon}"></i><h4 class="pillar-title">${pillar.title}</h4><p class="pillar-description">${pillar.description}</p>`;
                        pillarsContainer.appendChild(pillarDiv);
                    });

                    document.getElementById('main_content-features-title').innerHTML = data.main_content.features.title;
                    const featuresList = document.getElementById('main_content-features-list');
                    featuresList.innerHTML = ''; // Clear existing
                    data.main_content.features.list.forEach(feature => {
                        const featureLi = document.createElement('li');
                        featureLi.innerHTML = `<i class="${feature.icon}"></i> ${feature.text}`;
                        featuresList.appendChild(featureLi);
                    });

                    // Footer
                    document.getElementById('footer-results').innerHTML = data.footer.results;
                    document.getElementById('footer-supported_by').innerHTML = data.footer.supported_by;

                    const contactContainer = document.getElementById('footer-contact');
                    contactContainer.innerHTML = ''; // Clear existing
                    data.footer.contact.forEach(item => {
                        const contactSpan = document.createElement('span');
                        contactSpan.innerHTML = `<i class="${item.icon}"></i> ${item.text}`;
                        contactContainer.appendChild(contactSpan);
                    });

                    // Signal that content is loaded
                    document.body.classList.add('content-loaded');
                    console.log('Content loaded successfully.');
                })
                .catch(error => {
                    console.error('Error loading or parsing labels:', error);
                    const errorDiv = document.createElement('div');
                    errorDiv.textContent = `Failed to load content: ${error.message}. Please check the console.`;
                    errorDiv.style.color = 'red';
                    errorDiv.style.padding = '20px';
                    errorDiv.style.fontFamily = 'sans-serif';
                    document.body.prepend(errorDiv);
                });
        });
    </script>
</body>
</html>
```

### 2.3. Data Schemas

#### `labels.json` (English)

This file defines the data schema for the text content. All other language files must follow this exact structure.

```json
{
    "header": {
        "title": "Polisense.AI",
        "subtitle": "AI Co-Pilot for Energy Access"
    },
    "problem": {
        "crisis": {
            "title": "The Global Energy Access Crisis",
            "text": "<strong>760 million people</strong> lack reliable electricity, while <strong>49% of energy projects</strong> fail due to poor planning."
        },
        "local_gov": {
            "title": "The Problem for Local Governments",
            "text": "Local governments are facing planning gridlock due to fragmented data, which causes high project risk and failure to reach those in need.",
            "pain_points": [
                {
                    "icon": "fas fa-sitemap",
                    "text": "<strong>Data Fragmentation:</strong> Information is siloed and scattered, blocking a unified view."
                },
                {
                    "icon": "fas fa-balance-scale-left",
                    "text": "<strong>Subjective Prioritization:</strong> Project selection is biased, lacking objective metrics."
                },
                {
                    "icon": "fas fa-exclamation-triangle",
                    "text": "<strong>High Risk (49% Failure):</strong> Inefficiency drives major project delays and risk."
                },
                {
                    "icon": "fas fa-bullseye",
                    "text": "<strong>Inadequate Targeting:</strong> Inability to precisely locate the vulnerable, wasting resources."
                }
            ]
        }
    },
    "main_content": {
        "opportunity": {
            "title": "Polisense AI: A Global Impact Opportunity & Solution Pillars",
            "text": "By targeting high-density communities with low energy access, Polisense.AI helps bridge the energy gap for millions, ensuring investments are directed where they are most needed.",
            "pillars": [
                {
                    "icon": "fas fa-database",
                    "title": "1. Integrated Data",
                    "description": "Unifies geospatial, government, and web data into a single source of truth."
                },
                {
                    "icon": "fas fa-lightbulb",
                    "title": "2. AI Prioritization",
                    "description": "Ranks projects on Need, Feasibility, and Impact for objective decisions."
                },
                {
                    "icon": "fas fa-tasks",
                    "title": "3. Decision Support",
                    "description": "Interactive dashboards and collaboration tools to accelerate deployment."
                }
            ]
        },
        "features": {
            "title": "Platform & Features",
            "list": [
                { "icon": "fas fa-map-marked-alt", "text": "Geospatial Intelligence & Analysis" },
                { "icon": "fas fa-brain", "text": "AI-Powered Scoring & Analytics" },
                { "icon": "fas fa-chart-line", "text": "Interactive Dashboard & Reporting" },
                { "icon": "fas fa-users", "text": "Stakeholder Collaboration Tools" }
            ]
        }
    },
    "footer": {
        "results": "Proven Results: Up to 80% reduction in project delays and 2.8x better budget targeting accuracy.",
        "supported_by": "Supported by:",
        "contact": [
            { "icon": "fas fa-envelope", "text": "contact@polisense.ai" },
            { "icon": "fas fa-globe", "text": "www.polisense.ai" },
            { "icon": "fab fa-linkedin", "text": "/company/polisense" }
        ]
    }
}
```

#### `labels_es.json` (Spanish)

```json
{
    "header": {
        "title": "Polisense.AI",
        "subtitle": "Copiloto de IA para el acceso a la energía"
    },
    "problem": {
        "crisis": {
            "title": "La crisis mundial del acceso a la energía",
            "text": "<strong>760 millones de personas</strong> carecen de electricidad fiable, mientras que el <strong>49% de los proyectos energéticos</strong> fracasan por una mala planificación."
        },
        "local_gov": {
            "title": "El problema para los gobiernos locales",
            "text": "Los gobiernos locales se enfrentan a un bloqueo de la planificación debido a la fragmentación de los datos, lo que provoca un alto riesgo en los proyectos y la imposibilidad de llegar a los necesitados.",
            "pain_points": [
                {
                    "icon": "fas fa-sitemap",
                    "text": "<strong>Fragmentación de datos:</strong> La información está aislada y dispersa, lo que impide una visión unificada."
                },
                {
                    "icon": "fas fa-balance-scale-left",
                    "text": "<strong>Priorización subjetiva:</strong> La selección de proyectos es sesgada y carece de métricas objetivas."
                },
                {
                    "icon": "fas fa-exclamation-triangle",
                    "text": "<strong>Alto riesgo (49% de fracaso):</strong> La ineficiencia provoca grandes retrasos y riesgos en los proyectos."
                },
                {
                    "icon": "fas fa-bullseye",
                    "text": "<strong>Focalización inadecuada:</strong> Incapacidad para localizar con precisión a los vulnerables, malgastando recursos."
                }
            ]
        }
    },
    "main_content": {
        "opportunity": {
            "title": "Oportunidad de impacto global y pilares de la solución",
            "text": "Al dirigirse a comunidades de alta densidad con bajo acceso a la energía, Polisense.AI ayuda a cerrar la brecha energética para millones de personas, garantizando que las inversiones se dirijan a donde más se necesitan.",
            "pillars": [
                {
                    "icon": "fas fa-database",
                    "title": "1. Datos Integrados",
                    "description": "Unifica datos geoespaciales, gubernamentales y web en una única fuente de verdad."
                },
                {
                    "icon": "fas fa-lightbulb",
                    "title": "2. Priorización con IA",
                    "description": "Clasifica proyectos por Necesidad, Viabilidad e Impacto para decisiones objetivas."
                },
                {
                    "icon": "fas fa-tasks",
                    "title": "3. Soporte a Decisiones",
                    "description": "Paneles interactivos y herramientas de colaboración para acelerar la implementación."
                }
            ]
        },
        "features": {
            "title": "Plataforma y Características",
            "list": [
                { "icon": "fas fa-map-marked-alt", "text": "Inteligencia y Análisis Geoespacial" },
                { "icon": "fas fa-brain", "text": "Puntuación y Análisis Impulsados por IA" },
                { "icon": "fas fa-chart-line", "text": "Panel Interactivo y Reportes" },
                { "icon": "fas fa-users", "text": "Herramientas de Colaboración para Interesados" }
            ]
        }
    },
    "footer": {
        "results": "Resultados Comprobados: Hasta un 80% de reducción en retrasos de proyectos y 2.8x mejor precisión en la asignación de presupuestos.",
        "supported_by": "Con el apoyo de:",
        "contact": [
            { "icon": "fas fa-envelope", "text": "contact@polisense.ai" },
            { "icon": "fas fa-globe", "text": "www.polisense.ai" },
            { "icon": "fab fa-linkedin", "text": "/company/polisense" }
        ]
    }
}
```

### 2.4. `requirements.txt`

This file specifies the Python dependencies.

```
playwright
googletrans==4.0.0-rc1
```

## 3. Module Relationships and Data Flow

The project follows a clear data flow orchestrated by the main Python script.

1.  **Initiation**: The process starts when `generate_pdf.py` is executed.
2.  **Server Creation**: The script immediately launches a temporary local web server. This is a critical step to overcome browser security restrictions (`CORS`) that prevent local `file://` access for JavaScript's `fetch` API.
3.  **Browser Automation**: Playwright is invoked to launch a headless Chromium browser.
4.  **Navigation with Parameters**: The script directs the browser to `polisense-A4.html`, appending a language parameter to the URL (e.g., `?lang=es`).
5.  **Client-Side Logic**: The JavaScript within `polisense-A4.html` executes.
    *   It reads the `lang` parameter from the URL.
    *   Based on the language, it determines which JSON file to load (`labels.json` for `en` or `labels_es.json` for `es`).
    *   It sends a `fetch` request to the local server for the appropriate JSON file.
6.  **DOM Population**: Upon receiving the JSON data, the script iterates through the data and injects the content into the corresponding HTML elements by matching JSON keys to element `id` attributes.
7.  **Completion Signal**: Once the DOM is fully populated, the script adds a `content-loaded` class to the `<body>` tag.
8.  **Synchronization**: The `generate_pdf.py` script, which has been waiting, detects the `body.content-loaded` selector. It also waits for network activity to cease (`wait_until="networkidle"`) to ensure all external resources like fonts and icons are loaded.
9.  **PDF Rendering**: Playwright is instructed to save the fully rendered page as a PDF, preserving all styles, fonts, and images.
10. **Output**: The final PDF is saved to the `one-pager/` directory.

This architecture creates a robust separation of concerns:
-   **Data Layer**: `labels_*.json` files.
-   **Presentation Layer**: `polisense-A4.html` (HTML structure and CSS).
-   **Control/Orchestration Layer**: `generate_pdf.py` and the embedded JavaScript.

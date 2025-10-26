#!/usr/bin/env python3
"""
PDF Generator for Policy AIX User Guide - NEW VERSION
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

async def generate_user_guide_pdf():
    """Generate PDF from Policy AIX User Guide HTML file using Playwright"""
    
    # File paths
    html_file = Path("policy-aix-user-guide-new.html")
    output_dir = Path("one-pager")
    output_dir.mkdir(exist_ok=True)
    pdf_file = output_dir / "policy-aix-user-guide.pdf"

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
        print(f"🚀 Starting PDF generation for Policy AIX User Guide (NEW VERSION)...")
        
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()

            page.on("console", lambda msg: print(f"📄 PAGE LOG: {msg.text}"))
            
            # Load the HTML file
            url = f"http://localhost:{port}/{html_file}"
            print(f"📄 Loading HTML file from {url}...")
            await page.goto(url, wait_until="networkidle")
            
            # Wait for content to load
            await page.wait_for_selector('body', timeout=5000)

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
    # Generate Policy AIX User Guide PDF
    success = asyncio.run(generate_user_guide_pdf())
    sys.exit(0 if success else 1)

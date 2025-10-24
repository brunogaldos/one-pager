# Polisense.AI One-Pager Generator

## 1. Project Overview

This project automatically generates a polished, single-page A4 PDF document, known as a "one-pager," from an HTML template. The key feature of this system is its separation of content from presentation, allowing for easy updates and localization. All text is stored in external JSON files, and the system can generate PDFs in multiple languages.

The generation process is handled by a Python script that uses the Playwright library to control a headless browser, ensuring that the final PDF looks exactly like it would in a modern web browser.

## 2. File Structure

Here is a breakdown of the important files and directories and their roles in the project:

-   `generate_pdf.py`
    -   **Role**: The main executable script and the heart of the project.
    -   **Function**: It starts a local web server, launches a headless browser with Playwright, navigates to the HTML file, and saves the rendered page as a PDF. It is designed to handle different languages.

-   `polisense-A4.html`
    -   **Role**: The master template for the one-pager.
    -   **Function**: This file contains the HTML structure and all the CSS styling for the document. It does **not** contain any hardcoded text. Instead, it has elements with unique IDs that act as placeholders (e.g., `<h1 id="header-title"></h1>`). An embedded JavaScript fetches the content from a JSON file and populates these placeholders.

-   `labels.json`
    -   **Role**: The content database for the **English** version.
    -   **Function**: This JSON file holds all the text content for the one-pager, organized in a structured way. The keys in this file (e.g., `"header-title"`) correspond to the element IDs in `polisense-A4.html`.

-   `labels_es.json`
    -   **Role**: The content database for the **Spanish** version.
    -   **Function**: A direct translation of `labels.json`. The structure is identical, but the values are in Spanish.

-   `requirements.txt`
    -   **Role**: Python dependency list.
    -   **Function**: Specifies the Python libraries needed to run the project (`playwright`).

-   `assets/`
    -   **Role**: Asset storage.
    -   **Function**: This directory contains all static images, such as the logo and the demo picture, used in the document.

-   `one-pager/`
    -   **Role**: Output directory.
    -   **Function**: This is where the final, generated PDF files are saved (e.g., `polisense-one-pager.pdf` and `ES-polisense-one-pager.pdf`).

## 3. How It Works: The Generation Process

The system cleverly works around browser security limitations to create a reliable generation pipeline.

1.  **Execution**: A developer or an automated process runs the command `python3 generate_pdf.py`.
2.  **Web Server**: The script immediately starts a temporary, lightweight web server on a random, free port. This is a critical step. Modern browsers block JavaScript's `fetch` API from accessing local files (for security reasons). By serving the files over `http://localhost`, we treat them as a real website, allowing `fetch` to work as intended.
3.  **Headless Browser**: Playwright launches a headless instance of the Chromium browser in the background.
4.  **Navigation**: The script instructs the browser to navigate to a specific URL, like `http://localhost:12345/polisense-A4.html?lang=es`. The `lang` query parameter tells the page which language to load.
5.  **Content Fetching**: The JavaScript inside `polisense-A4.html` wakes up, reads the `lang` parameter from the URL, and constructs the name of the JSON file to fetch (e.g., `labels_es.json`).
6.  **Dynamic Population**: The script fetches the JSON file, parses it, and iterates through all the keys. For each key, it finds the HTML element with the matching `id` and injects the corresponding text value into it.
7.  **Completion Signal**: After all the content has been loaded, the JavaScript adds a special class, `content-loaded`, to the `<body>` tag of the page.
8.  **Waiting for Signal**: Meanwhile, the `generate_pdf.py` script has been patiently waiting for the selector `body.content-loaded` to appear in the DOM. It also waits for the network to be idle, ensuring external resources like fonts and icons from the Font Awesome CDN are fully loaded.
9.  **PDF Generation**: Once the signal is received, the Python script commands Playwright to print the page to a PDF. This captures the fully rendered page, complete with dynamic content, styling, and external resources.
10. **File Saved**: The final PDF is saved into the `one-pager/` directory with a language-specific filename.

## 4. How to Use and Customize

### Running the Project

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Install Playwright Browsers**:
    ```bash
    playwright install
    ```
3.  **Generate the PDFs**:
    ```bash
    python3 generate_pdf.py
    ```

### Changing Text Content

**Do not edit `polisense-A4.html` to change text.**

-   To change **English** text, open `labels.json`. Find the key corresponding to the text you want to change and edit its value.
-   To change **Spanish** text, open `labels_es.json` and do the same.

For example, to change the main title, you would edit the `title` value within the `header` object in `labels.json`.

### Adding a New Language (e.g., French)

1.  **Create the JSON File**: Duplicate `labels.json` and rename it to `labels_fr.json`.
2.  **Translate the Content**: Open `labels_fr.json` and translate all the string values into French. Keep the keys exactly the same.
3.  **Update the Generation Script**: Open `generate_pdf.py`. At the bottom of the file, add a new line to call the generation function for French:
    ```python
    # ... existing calls for 'en' and 'es'
    fr_success = asyncio.run(generate_pdf(language='fr'))
    ```

### Changing Styles or Layout

All visual aspects of the document are controlled by the CSS inside the `<style>` block in `polisense-A4.html`. You can edit these CSS rules to change fonts, colors, spacing, layout, etc. The HTML structure itself can also be modified in this file, but be sure to keep the `id` attributes on elements that are populated by the script.

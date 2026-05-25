from playwright.sync_api import sync_playwright
import os, sys

HTML_FILE = os.path.abspath('/home/user/etsy-agent-final/vorwort-editorial.html')
PDF_FILE  = '/home/user/etsy-agent-final/vorwort-editorial.pdf'

# Override body wrapper so the .page fills the printed A4 cleanly
PRINT_OVERRIDES = """
  html, body {
    background: #F5F1EC !important;
    display: block !important;
    padding: 0 !important;
    margin: 0 !important;
    width: 210mm !important;
  }
  .page {
    box-shadow: none !important;
    width: 210mm !important;
    min-height: 297mm !important;
    margin: 0 auto !important;
    padding: 54px 96px 104px !important;
  }
"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(
        viewport={'width': 794, 'height': 1123},
        extra_http_headers={'Cache-Control': 'no-cache'}
    )
    page = context.new_page()
    page.goto(f'file://{HTML_FILE}', wait_until='networkidle', timeout=20000)
    # Extra wait to ensure Google Fonts fully render
    try:
        page.wait_for_timeout(4500)
    except Exception:
        pass
    page.add_style_tag(content=PRINT_OVERRIDES)
    pdf_bytes = page.pdf(
        format='A4',
        print_background=True,
        margin={'top': '0', 'right': '0', 'bottom': '0', 'left': '0'},
        prefer_css_page_size=False
    )
    with open(PDF_FILE, 'wb') as f:
        f.write(pdf_bytes)
    browser.close()

print(f'PDF generated: {PDF_FILE}')
print(f'Size: {os.path.getsize(PDF_FILE):,} bytes')

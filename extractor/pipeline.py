from extractor.dom import create_dom
from extractor.cleaner import remove_unwanted_tags
from extractor.extractor import extract_main_content


def extract(html):
    """
    Extract the main content block from raw HTML.
    """
    
    dom = create_dom(html)
    remove_unwanted_tags(dom)
    best = extract_main_content(dom)
    
    return best
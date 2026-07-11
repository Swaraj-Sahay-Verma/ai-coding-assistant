from bs4 import BeautifulSoup


def create_dom(html: str) -> BeautifulSoup:
    """
    Create a BeautifulSoup DOM object from HTML.

    Args:
        html (str): Raw HTML content.

    Returns:
        BeautifulSoup: Parsed DOM tree.
    """
    return BeautifulSoup(html, "html.parser")


def get_all_nodes(soup):
    """
    Return all HTML tag nodes from the DOM.
    
    Args:
        soup (BeautifulSoup): Parsed DOM tree.
        
    Returns:
        ResultSet: Collection of all HTML tags.
    """
    return soup.find_all(True)


def get_text(tag) -> str:
    """
    Extract all text from an HTML tag.
    
    Args:
        tag (Tag): HTML tag.
        
    Returns:
        str: Clean extracted text.
    """
    return tag.get_text(separator=" ", strip=True)


def get_children(tag) -> list:
    """
    Return all direct child tags of an HTML tag.
    
    Args:
        tag (Tag): HTML tag.
        
    Returns:
        list: List of direct child nodes.
    """
    return list(tag.children)


def get_parent(tag):
    """
    Return the parent tag of an HTML tag.
    
    Args:
        tag (Tag): HTML tag.
        
    Returns:
        Tag: Parent node.
    """
    return tag.parent

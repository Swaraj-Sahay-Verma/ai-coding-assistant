from extractor.dom import get_text


def get_word_count(tag) -> int:
    """
    Count the number of words in a given HTML tag.
    
    Args:
        tag (Tag): HTML tag.
        
    Returns:
        int: Total number of words.
    """
    
    text = get_text(tag)
    words = text.split()
    return len(words)

def get_link_density(tag) -> float:
    """
    Calculate the link density of a given HTML tag.
    
    Args:
        tag (Tag): HTML tag.
        
    Returns:
        float: Ratio of link to total words.
    """
    
    total_words = get_word_count(tag)
    
    if total_words == 0:
        return 0.0
    
    link_words = sum(get_word_count(link) for link in tag.find_all("a"))
    
    return link_words / total_words

def get_paragraph_count(tag) -> int:
    """
    Count the number of paragraph tags inside an HTML tag.
    
    Args:
        tag (Tag): HTML tag.
        
    Returns:
        int: Total number of paragraph tags.
    """
    
    return len(tag.find_all("p"))
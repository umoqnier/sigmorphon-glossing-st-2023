import os
from typing import Text, Dict, List


def sentence_to_dict(raw_sentence: Text) -> Dict:
    """Convert a raw sentences to dict
    
    Raw sentences has the structure as follow: 
    
    \\t <text>\n\\g <gloss>\n\t <traslation>
    """
    data = raw_sentence.split("\n")
    original_lang = data[0].lstrip("\\t ")
    gloss = data[1].lstrip("\\g ")
    translation = data[2].lstrip("\\l ")
    return {"text": original_lang, "gloss": gloss, "translation": translation}


def load_corpus(path: Text) -> List[Dict]:
    """Loads a corpus of given path as list of dicts
    """
    with open(path, 'r') as f:
        data_raw = f.read()
    data_raw = data_raw.split("\n\n")
    return [sentence_to_dict(line) for line in data_raw]
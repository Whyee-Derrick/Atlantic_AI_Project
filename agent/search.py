import fitz
from pathlib import Path
def search_for_info (user_input):
    
    file = Path("data")/"python textbook.pdf"
    doc = fitz.open(file)   

    user_words = user_input.lower().split()
    knowledge_text = ""
    for page in doc:
         knowledge_text+=page.get_text() 
        
         knowledge_text_lower = knowledge_text.lower()
        
         for word in user_words:
            if word in knowledge_text_lower:
                return knowledge_text_lower
            else:
                return "Not Available "
                   
        
    
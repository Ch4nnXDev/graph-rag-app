import fitz
import os
class PDFLoader:
    def __init__(self, data_path):
        self.data_path = data_path
        
    def load(self):
        for doc in os.listdir(self.data_path):
            data_path = os.path.join(self.data_path, doc)
            document = fitz.open(data_path)
            text = ""
            for num in range(document.page_count):
                page = document.load_page(num)
                text += page.get_text()
            
        return text
    
    
            
            
            
            
            
            
        
        
        
import os
from crewai_tools import (
    PDFSearchTool,
    TXTSearchTool,
    JSONSearchTool,
    MDXSearchTool,
    FileReadTool,
    WebsiteSearchTool
)

os.environ["PDF_API_KEY"] = "Your Key" 
os.environ["OPENAI_API_KEY"] = "Your Key"
pdf_tool = PDFSearchTool()
txt_tool = TXTSearchTool()
json_tool = JSONSearchTool()
mdx_tool = MDXSearchTool()
file_read_tool = FileReadTool()
web_search_tool = WebsiteSearchTool() 

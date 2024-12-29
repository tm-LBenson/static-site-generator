from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = "normal"
    BOLD_TEXT = "Bold"
    ITALIC_TEXT = "Italic"
    CODE_TEXT = "Code"
    LINKS = "Links"
    IMAGES = "Images"

class TextNode:
  def __init__(self, text, text_type, url):
    self.text = text
    self.text_type = text_type
    self.url = url
  def __eq__(self, Node1, Node2):
    check1 = Node1.text == Node2.text
    check2 = Node1.text_type == Node2.text_type
    check3 = Node1.url == Node1.url
    return check1 == check2 == check3
  def __repr__(self):
     return f"TextNode({self.text}, {self.text_type}, {self.url})"
   
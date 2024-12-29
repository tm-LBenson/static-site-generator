from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "Bold"
    ITALIC = "Italic"
    CODE = "Code"
    LINKS = "Links"
    IMAGES = "Images"

class TextNode:
  def __init__(self, text, text_type, url=None):
    self.text = text
    self.text_type = text_type
    self.url = url
  def __eq__(self, Node2):
    print("TESTING")
    check1 = self.text == Node2.text
    check2 = self.text_type == Node2.text_type
    check3 = self.url == Node2.url
    return check1 == check2 == check3
  def __repr__(self):
     return f"TextNode({self.text}, {self.text_type}, {self.url})"

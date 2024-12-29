import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "url")
        node2 = TextNode("This is a text node", TextType.BOLD, "url")
        node3 = TextNode("This is a text node", TextType.BOLD, "url2")
        self.assertEqual(node, node2)
        self.assertNotEqual(node,node3)

    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.example.com")
        self.assertTrue(node.url is None)
        self.assertTrue(isinstance(node2.url, str))

    def test_text_type(self):
        node1 = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)
        
if __name__ == "__main__":
    unittest.main()
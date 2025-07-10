
import unittest
from services.nlp_service import process_text

class TestNLPService(unittest.TestCase):
    def test_entities_extraction(self):
        text = "List all employees in the Marketing department."
        structured = process_text(text)
        self.assertIn("original_text", structured)
        self.assertIsInstance(structured["entities"], list)

if __name__ == '__main__':
    unittest.main()

import unittest
import app

class SupportDeskTests(unittest.TestCase):
    def test_priorities_are_defined(self):
        self.assertIn("critical", app.PRIORITIES)
        self.assertIn("open", app.STATUSES)

    def test_module_exposes_http_handler(self):
        self.assertTrue(issubclass(app.handler, app.BaseHTTPRequestHandler))

if __name__=="__main__":
    unittest.main()

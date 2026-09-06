import unittest
from el_mehasin.rhetoric import RhetoricDetector

class TestRhetoricDetector(unittest.TestCase):
    def test_detection(self):
        text = "Söz gümüş ise sükût altındır; iki kutup arasında vakar parıldar."
        devices = RhetoricDetector.identify_potential_devices(text)
        self.assertIn("Icaz", devices)
        self.assertIn("Mukabele", devices)

if __name__ == "__main__":
    unittest.main()

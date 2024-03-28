import unittest
import numpy as np
from heart_model import model

class TestHeartPrediction(unittest.TestCase):
    def test_heart_prediction(self):
        input_data = np.array([53,0,63,1,63,1,60,0,368000,0.8,135,1,0,22])
        input_data = input_data.reshape(1,-1)
        result_1 = model.predict(input_data)
        print(f"Test case 1 result is {result_1}")
        self.assertEqual(result_1, 0)


        input_data2 = np.array([80,0,148,1,38,0,149000,1.9,144,1,1,23,1])
        input_data2 = input_data2 
        result_2 = model.predict(input_data)
        print(f"Test case 2 result is {result_2}")
        self.assertEqual(result_2, 1)

if __name__ == ' __main__ ':
    unittest.main()

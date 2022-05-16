import unittest

import pandas as pd
import pathlib as pl
from sklearn.linear_model import LogisticRegression

from dataframe.model import save_model


class TestModel(unittest.TestCase):

    def test_model(self):
        # Given
        filename = "test_model_saved.sav"
        path = pl.Path(filename)
        model = LogisticRegression()

        # When
        save_model(model, filename)

        # Then
        self.assertEqual((str(path), path.is_file()), (str(path), True))


if __name__ == '__main__':
    unittest.main()

import pytest

import pandas as pd
import pathlib as pl
from sklearn.linear_model import LogisticRegression

from dataframe.model import save_model

def test_model():
    # Given
    filename = "test_model_saved.sav"
    path = pl.Path(filename)
    model = LogisticRegression()

    # When
    save_model(model, filename)

    # Then
    assert (str(path), path.is_file()) == (str(path), True)


if __name__ == '__main__':
    pytest.main()

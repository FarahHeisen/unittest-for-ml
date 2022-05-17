import pytest
from unittest.mock import patch

import pandas as pd
from pandas.testing import assert_frame_equal
import numpy as np

from dataframe.dataframe import delete_columns, fill_empty_values, one_hot, process, fill_empty_numerical_values, \
    fill_empty_categorical_values


def test_delete_columns_return_df_without_deleted_columns():
    # Given
    input_df = pd.DataFrame({"a": [0, 0], "b": [0, 0]})
    expected_df = pd.DataFrame({"a": [0, 0]})

    # When
    result_df = delete_columns(input_df, ["b"])
    # Then
    assert_frame_equal(expected_df, result_df)


def test_fill_empty_numerical_values_return_df_filled_with_mean_for_numerical_values():
    # Given
    input_df = pd.DataFrame({"age": [16.0, None, 0.0, None], "taille": [120, None, 140, None]})
    expected_df = pd.DataFrame({"age": [16, 8, 0, 8], "taille": [120, 130, 140, 130]})
    # When
    result_df = fill_empty_numerical_values(input_df)
    # Then
    assert_frame_equal(expected_df, result_df)


def test_fill_empty_categorical_values_return_df_filled_with_most_occurence_for_categorical_values():
    # Given
    input_df = pd.DataFrame({"couleur": ["bleu", "bleu", "red", None]})
    expected_df = pd.DataFrame({"couleur": ["bleu", "bleu", "red", "bleu"]})
    # When
    result_df = fill_empty_categorical_values(input_df)
    # Then
    assert_frame_equal(expected_df, result_df)


def test_fill_empty_value_for_categorical_and_numeric_return_df_filled():
    # Given
    input_df = pd.DataFrame({"age": [16.0, None, 0.0, None], "taille": [120, None, 140, None],
                             "couleur": ["bleu", "bleu", "red", None]})
    expected_df = pd.DataFrame(
        {"age": [16, 8, 0, 8], "taille": [120, 130, 140, 130], "couleur": ["bleu", "bleu", "red", "bleu"]})
    # When
    result_df = fill_empty_values(input_df)
    # Then
    assert_frame_equal(expected_df, result_df)


def test_one_hot_encode_correctly_dummifies_a_one_column_category_df():
    # Given
    input_df = pd.DataFrame({"couleur": ["bleu", "bleu", "red", "bleu"]})
    expected_df = pd.DataFrame({"couleur_bleu": [1, 1, 0, 1], "couleur_red": [0, 0, 1, 0]}).astype("uint8")
    # When
    result_df = one_hot(input_df)
    # Then
    assert_frame_equal(expected_df, result_df)


def test_process_return_processed_dataframe():
    # Given

    input_df = pd.DataFrame({"age": [18.0, 20.0, 22.0, np.nan],
                             "couleur": ["rouge", "bleu", None, "bleu"],
                             "taille": [180, 180, 170, 180],
                             "a_supprimer": [None, None, None, None]})

    output_df = pd.DataFrame({"age": [18, 20, 22, 20],
                              "couleur_bleu": [0, 1, 1, 1],
                              "couleur_rouge": [1, 0, 0, 0],
                              "taille": [180, 180, 170, 180]})
    expected_df = output_df
    # When
    result_df = process(input_df)
    # Then
    assert_frame_equal(expected_df, result_df, check_dtype=False)


@patch("dataframe.dataframe.delete_columns", return_value="delete_columns_called")
@patch("dataframe.dataframe.fill_empty_values", return_value="fill_empty_values_called")
@patch("dataframe.dataframe.one_hot", return_value=pd.DataFrame())
def test_process_call_functions_in_the_right_order(one_hot_mock, fill_empty_values_mock,
                                                   delete_columns_mock
                                                   ):
    # Given

    input_df = pd.DataFrame({"age": [18.0, 20.0, 22.0, np.nan],
                             "couleur": ["rouge", "bleu", None, "bleu"],
                             "taille": [180, 180, 170, 180],
                             "a_supprimer": [None, None, None, None]})
    # When
    process(input_df)

    # Then
    delete_columns_mock.assert_called()
    fill_empty_values_mock.assert_called_with("delete_columns_called")
    one_hot_mock.assert_called_with("fill_empty_values_called")


if __name__ == '__main__':
    pytest.main()

import unittest
import pandas as pd
from dataframe import process, delete_columns, fill_missing_values, fill_numerical_columns, fill_categorical_columns, \
    process_categories
from pandas.testing import assert_frame_equal


class TestDataFrame(unittest.TestCase):
    def test_process_should_correctly_process_df(self):
        # given
        df = pd.DataFrame({'age': [18, 20, 22, None],
                           'couleur': ['rouge', 'bleu', None, 'bleu'],
                           'taille': [180, 180, 170, 180],
                           'a_supprimer': [None, None, None, None]})

        expected_df = pd.DataFrame({'age': [18, 20, 22, 20],
                                    'couleur_bleu': [0, 1, 1, 1],
                                    'couleur_rouge': [1, 0, 0, 0],
                                    'taille': [180, 180, 170, 180]})
        # when
        processed_df = process(df)

        # then
        assert_frame_equal(processed_df, expected_df)

    def test_delete_columns_should_return_a_dataframe_without_the_given_column(self):
        # given
        df = pd.DataFrame({'age': [18, 20, 22, None],
                           'couleur': ['rouge', 'bleu', None, 'bleu'],
                           'taille': [180, 180, 170, 180],
                           'a_supprimer': [None, None, None, None]})

        expected_df = pd.DataFrame({'age': [18, 20, 22, None],
                                    'couleur': ['rouge', 'bleu', None, 'bleu'],
                                    'taille': [180, 180, 170, 180]})
        # when
        processed_df = delete_columns(df, ['a_supprimer'])

        # then
        assert_frame_equal(processed_df, expected_df)

    def test_fill_missing_values_should_return_a_dataframe_without_missing_values(self):
        # given
        df = pd.DataFrame({'age': [18, 20, 22, None],
                           'couleur': ['rouge', 'bleu', None, 'bleu'],
                           'taille': [180, 180, 170, 180]})

        expected_df = pd.DataFrame({'age': [18, 20, 22, 20],
                                    'couleur': ['rouge', 'bleu', 'bleu', 'bleu'],
                                    'taille': [180, 180, 170, 180]})
        # when
        processed_df = fill_missing_values(df)

        # then
        assert_frame_equal(processed_df, expected_df)
        self.assertEqual(processed_df.isnull().sum().sum(), 0)

    def test_fill_numerical_columns_should_fill_with_means(self):
        # given
        df = pd.DataFrame({'age': [18, 20, 22, None],
                           'taille': [180, 180, 170, 180]})

        expected_df = pd.DataFrame({'age': [18, 20, 22, 20],
                                    'taille': [180, 180, 170, 180]})
        # when
        processed_df = fill_numerical_columns(df)

        # then
        assert_frame_equal(processed_df, expected_df)
        self.assertEqual(processed_df.isnull().sum().sum(), 0)

    def test_fill_categorical_columns_should_fill_with_most_frequent_value(self):
        # given
        df = pd.DataFrame({'couleur': ['rouge', 'bleu', None, 'bleu'],
                           'taille': [180, 180, 170, 180]})

        expected_df = pd.DataFrame({'couleur': ['rouge', 'bleu', 'bleu', 'bleu'],
                                    'taille': [180, 180, 170, 180]})
        # when
        processed_df = fill_categorical_columns(df)

        # then
        assert_frame_equal(processed_df, expected_df)

    def test_process_categories_should_return_one_hot_encoded_column_given_categorical_column(self):
        # given
        df = pd.DataFrame({'couleur': ['rouge', 'bleu', 'bleu', 'bleu']})

        expected_df = pd.DataFrame({'couleur_bleu': [0, 1, 1, 1],
                                    'couleur_rouge': [1, 0, 0, 0]
                                    })
        # when
        processed_df = process_categories(df)

        # then
        assert_frame_equal(processed_df, expected_df)


if __name__ == '__main__':
    unittest.main()

from typing import List

import pandas as pd


def process(df: pd.DataFrame) -> pd.DataFrame:
    df_without_a_supprimer = delete_columns(df, ['a_supprimer'])
    df_filled = fill_missing_values(df_without_a_supprimer)
    df_processed = process_categories(df_filled)
    return df_processed


def delete_columns(df: pd.DataFrame, column_name: List[str]) -> pd.DataFrame:
    return df.drop(column_name, axis=1)


def process_categories(df: pd.DataFrame) -> pd.DataFrame:
    categorical_df = df.select_dtypes(include=object)
    dummies_df = pd.get_dummies(categorical_df, dtype='int64')
    df_processed_categories = pd.concat([df.drop(categorical_df, axis=1), dummies_df], axis=1)
    return df_processed_categories.sort_index(axis=1)


def fill_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    numerical_df = fill_numerical_columns(df.select_dtypes(include='number'))
    categorical_df = fill_categorical_columns(df.select_dtypes(include=object))
    filled_df = pd.concat([numerical_df, categorical_df], axis=1)

    return filled_df[df.columns]


def fill_numerical_columns(numerical_df: pd.DataFrame) -> pd.DataFrame:
    return numerical_df.fillna(numerical_df.mean()).astype(int)


def fill_categorical_columns(categorical_df: pd.DataFrame) -> pd.DataFrame:
    return categorical_df.apply(lambda x: x.fillna(x.value_counts().index[0]))

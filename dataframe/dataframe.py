from typing import List

import pandas as pd


def delete_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    return df.drop(columns=columns)


def fill_empty_values(df: pd.DataFrame) -> pd.DataFrame:
    df_numerical = fill_empty_numerical_values(df.select_dtypes(exclude=['object']))
    df_categorical = fill_empty_categorical_values(df.select_dtypes(include=['object']))
    return pd.concat([df_numerical, df_categorical], axis=1)


def fill_empty_numerical_values(df: pd.DataFrame) -> pd.DataFrame:
    return df.fillna(value=df.mean()).astype("int64")


def fill_empty_categorical_values(df: pd.DataFrame) -> pd.DataFrame:
    return df.fillna(value=df.mode().iloc[0])


def one_hot(df: pd.DataFrame) -> pd.DataFrame:
    return pd.get_dummies(df)


def process(df: pd.DataFrame) -> pd.DataFrame:
    filtered_df = delete_columns(df, columns=["a_supprimer"])
    filtered_df = fill_empty_values(filtered_df)
    filtered_df = one_hot(filtered_df)
    filtered_df = filtered_df.reindex(sorted(filtered_df.columns), axis=1)
    return filtered_df

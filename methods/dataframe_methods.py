import pandas as pd


def clean_columns(df):
    processed_df = df.copy()
    processed_df.columns = processed_df.columns.str.lower()
    processed_df.columns = processed_df.columns.str.replace(" ", "_")
    return processed_df

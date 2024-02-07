def clean_columns(df):
    """
    Function called to format the columns of a dataframe to lowercase and replace spaces with underscores.
    Args:
        df (pandas.Dataframe): A pandas dataframe with columns that need to be cleaned.
    Returns:
        Prints the processed dataframe.
    """
    processed_df = df.copy()
    processed_df.columns = processed_df.columns.str.lower()
    processed_df.columns = processed_df.columns.str.replace(" ", "_")
    return processed_df

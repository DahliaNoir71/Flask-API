def dictionnairy_factory(cursor, row):
    """
    :param cursor: Database cursor that provides metadata about the result set.
    :param row: A single row of data from the result set.
    :return: A dictionary mapping column names to their corresponding row values.
    """
    dictionnary = {}
    for index, column in enumerate(cursor.description):
        dictionnary[column[0]] = row[index]
    return dictionnary
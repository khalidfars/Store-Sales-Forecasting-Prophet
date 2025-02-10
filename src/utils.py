def check_nulls(data):
    return data.isnull().sum()

def check_duplicates(data):
    return data.duplicated().sum()

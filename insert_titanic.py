

def build_insert_query(df):
    query = """
    INSERT INTO titianc (
        survived,
        pclass,
        name,
        sex,
        age,
        sibs_spouses,
        parents_children,
        fare
    ) VALUES
    """
    for index, row in df.iterrows():
        row_tuple = (
            row['Survived'],
            row['Pclass'],
            row['Name'],
            row['Sex'],
            row['Age'],
            row['Siblings/Spouses Aboard'],
            row['Parents/Children Aboard'],
            row['Fare']
        )
        print(row_tuple)
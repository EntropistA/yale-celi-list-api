import pandas as pd

YALE_CELI_LIST = "https://som.yale.edu/story/2022/over-1000-companies-have-curtailed-operations-russia-some-remain"

tables = pd.read_html(YALE_CELI_LIST)

grade_F, grade_D, grade_C, grade_B, grade_A = tables


class Companies:
    grades = "FDCBA"

    def __init__(self, grades_dataframes: list[pd.DataFrame]):
        self.grades_dataframes = grades_dataframes

    def __iter__(self):
        self.iterator = zip(Companies.grades, self.grades_dataframes)
        return self

    def __next__(self):
        return self.iterator.__next__()

    @property

    @property
    def company_names(self):
        return

    def no_lowercase_duplicates(self, debugging=False):
        names = []
        for grade, df in self:
            names.extend(df["Name"])
        names = [name.lower() for name in names]

        if debugging:
            duplicates = set()
            for name in names:
                if names.count(name) > 1:
                    duplicates.add(name)
            print("duplicates found: ", duplicates)

        unique_names = set(names)
        return len(names) == len(unique_names)


no_lowercase_duplicates(tables, debugging=True)

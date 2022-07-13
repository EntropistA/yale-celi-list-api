from datetime import date
from pathlib import Path

import pandas as pd

GRADES = "FDCBA"
YALE_CELI_LIST = "https://som.yale.edu/story/2022/over-1000-companies-have-curtailed-operations-russia-some-remain"


def lowercase_search(list_, target):
    return target.lower() in (elem.lower() for elem in list_)


class Companies:
    def __init__(self):
        self.companies_df = self.fetch_data()

    @staticmethod
    def fetch_data() -> pd.DataFrame:
        file_name = f"./yale_companies_{date.today()}.json"
        if Path(file_name).exists():
            return pd.read_json(file_name)
        else:
            companies_by_grade = pd.read_html(YALE_CELI_LIST)

            result = pd.DataFrame()
            for grade, df in zip(GRADES, companies_by_grade):
                df["Grade"] = grade
                result = pd.concat([result, df])
            result.reset_index(inplace=True)
            result.to_json(file_name)
            return result

    def find(self, company_name: str) -> pd.Series:
        for search_function in (
                self.by_exact_company_name,
                self.by_company_name_fragment_lowercase,
        ):
            result = search_function(company_name)
            if not result.empty:
                return result[0]

    def by_exact_company_name(self, company_name):
        return self.companies_df[company_name == self.companies_df["Name"]]

    def by_company_name_fragment_lowercase(self, company_name):
        return self.companies_df[company_name.lower() in self.companies_df["Name"].lower()]

    @staticmethod
    def _valid_grade(grade: str):
        return len(grade) == 1 and grade.lower() in GRADES.lower()

    def by_grade(self, letter):
        if not self._valid_grade(letter):
            raise ValueError(f"Invalid grade: {letter}. Valid grades: {GRADES}")

        return self.companies_df[self.companies_df["Grade"] == letter.upper()]

    def _valid_country(self, country_name):
        return country_name.title() in self.companies_df["Country"]

    def by_country(self, country_name):
        if not self._valid_country:
            raise ValueError(f"Invalid country_name: {country_name}")

        return self.companies_df[self.companies_df["Country"] == country_name.title()]


class CompanyInformation:
    def __init__(self, company_data: pd.Series):
        self.name = company_data["Name"]
        self.action = company_data["Action"]
        self.industry = company_data["Industry"]
        self.country = company_data["Country"]
        self.grade = company_data["Grade"]

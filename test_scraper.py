import os
import unittest
from datetime import date
from pathlib import Path

from scraper import Companies


class TestCompanies(unittest.TestCase):
    def fetch(self, fetch_method="f"):
        proper_methods = {
            "f": "file fetch",
            "w": "web fetch",
        }
        if fetch_method not in proper_methods:
            raise ValueError(f"Invalid fetch_method: {fetch_method} Valid methods: {proper_methods}")

        file_name = Path(f"./yale_companies_{date.today()}.json")
        if file_name.exists() and fetch_method == "w":
            os.remove(file_name)
        self.companies = Companies()
        self.assertTrue(file_name.exists())

    def setUp(self) -> None:
        pass

    def test_fetch_data(self) -> None:
        for fetch_method in "wf":
            self.fetch(fetch_method)

            df_column_names = list(self.companies.companies_df.columns[1:])
            self.assertEqual(df_column_names, ["Name", "Action", "Industry", "Country", "Grade"])

            df_country_column = self.companies.companies_df["Country"]
            self.assertTrue(all(country == country.title() for country in df_country_column))

            self.assertEqual(set(self.companies.companies_df["Grade"]), set("FDCBA"))

    def test_find(self):
        self.fetch()

        self.assertIsNotNone(self.companies.find("alphabet"))


if __name__ == '__main__':
    unittest.main()

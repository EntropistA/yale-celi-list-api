import json

from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse

from fetch_companies import Companies

app = FastAPI()

companies = Companies()


@app.get("/", response_class=PlainTextResponse)
async def root():
    return """Usage:
/find-company-by-name/{company_name}
"""


@app.get("/find-company-by-name/{company_name}")
async def find_company_by_name(company_name: str):
    try:
        json_string_result = companies.find(company_name).drop("index").to_json(orient="index")
        return json.loads(json_string_result)
    except (ValueError, KeyError) as err:
        print(err)
        raise HTTPException(status_code=404, detail="Item not found")

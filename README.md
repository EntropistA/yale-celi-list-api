# Yale CELI List API

## Backstory

This API serves to find information about companies' responses to Russian invasion on Ukraine.

The information is fully based on a free to use list published by the Yale University:
https://som.yale.edu/story/2022/over-1000-companies-have-curtailed-operations-russia-some-remain

The list offers an easy-to-use A-F grade system.

### Article links:
- https://www.washingtonpost.com/business/2022/03/08/russia-company-boycott-yale-list/
- https://fortune.com/2022/06/14/ukraine-zelensky-addresses-us-ceos-yale-summit/

## Usage

JSON with "Name", "Action", "Industry", "Country" as an attribute.

`{server}/find-company-by-name/{company_name}`

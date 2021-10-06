import json
from math import ceil
from pathlib import Path

import requests
from tqdm import trange

# ##### Seattle ######

# get_url = lambda n=0: f"https://www.amazon.jobs/en/search.json?normalized_location%5B%5D=Seattle%2C+Washington%2C+USA&business_category%5B%5D=amazon-web-services&radius=24km&facets%5B%5D=normalized_country_code%2Cnormalized_state_name%2Cnormalized_city_name%2Clocation%2Cbusiness_category%2Ccategory%2Cschedule_type_id%2Cemployee_class%2Cnormalized_location%2Cjob_function_id&offset={n * 10}&result_limit=10&sort=relevant&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&="

# output_path = Path("data/job-data-seattle.json")
# all_data = []

# res = requests.get(get_url(0)).json()
# all_data.extend(res["jobs"])

# n_hits = res["hits"]
# n = ceil(n_hits / 10)

# for i in trange(n):
#     try:
#         res = requests.get(get_url(0)).json()
#         assert not res["error"], f'Error returned: {res["error"]}'
#         all_data.extend(res["jobs"])
#     except Exception as e:
#         print("Stopping early, after", i, "iterations because of error:", e)
#         break

# print("Writing output")
# output_path.write_text(json.dumps(all_data, indent=2))


# ##### New York ######

# get_url = lambda n=0: f"https://www.amazon.jobs/en/search.json?normalized_location%5B%5D=New+York%2C+New+York%2C+USA&business_category%5B%5D=amazon-web-services&radius=24km&facets%5B%5D=normalized_country_code%2Cnormalized_state_name%2Cnormalized_city_name%2Clocation%2Cbusiness_category%2Ccategory%2Cschedule_type_id%2Cemployee_class%2Cnormalized_location%2Cjob_function_id&offset={n * 10}&result_limit=10&sort=relevant&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&="


# output_path = Path("data/job-data-newyork.json")
# all_data = []

# res = requests.get(get_url(0)).json()
# all_data.extend(res["jobs"])

# n_hits = res["hits"]
# n = ceil(n_hits / 10)

# for i in trange(n):
#     try:
#         res = requests.get(get_url(0)).json()
#         assert not res["error"], f'Error returned: {res["error"]}'
#         all_data.extend(res["jobs"])
#     except Exception as e:
#         print("Stopping early, after", i, "iterations because of error:", e)
#         break

# print("Writing output")
# output_path.write_text(json.dumps(all_data, indent=2))


# ##### San Francisco ######

# get_url = lambda n=0: f"https://www.amazon.jobs/en/search.json?normalized_location%5B%5D=San+Francisco%2C+California%2C+USA&business_category%5B%5D=amazon-web-services&radius=24km&facets%5B%5D=normalized_country_code%2Cnormalized_state_name%2Cnormalized_city_name%2Clocation%2Cbusiness_category%2Ccategory%2Cschedule_type_id%2Cemployee_class%2Cnormalized_location%2Cjob_function_id&offset={n * 10}&result_limit=10&sort=relevant&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&="


# output_path = Path("data/job-data-newyork.json")
# all_data = []

# res = requests.get(get_url(0)).json()
# all_data.extend(res["jobs"])

# n_hits = res["hits"]
# n = ceil(n_hits / 10)

# for i in trange(n):
#     try:
#         res = requests.get(get_url(0)).json()
#         assert not res["error"], f'Error returned: {res["error"]}'
#         all_data.extend(res["jobs"])
#     except Exception as e:
#         print("Stopping early, after", i, "iterations because of error:", e)
#         break

# print("Writing output")
# output_path.write_text(json.dumps(all_data, indent=2))


##### LA ######

get_url = lambda n=0: f"https://www.amazon.jobs/en/search.json?normalized_location%5B%5D=Los+Angeles%2C+California%2C+USA&business_category%5B%5D=amazon-web-services&radius=24km&facets%5B%5D=normalized_country_code%2Cnormalized_state_name%2Cnormalized_city_name%2Clocation%2Cbusiness_category%2Ccategory%2Cschedule_type_id%2Cemployee_class%2Cnormalized_location%2Cjob_function_id&offset={n * 10}&result_limit=10&sort=relevant&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&="


output_path = Path("data/job-data-newyork.json")
all_data = []

res = requests.get(get_url(0)).json()
all_data.extend(res["jobs"])

n_hits = res["hits"]
n = ceil(n_hits / 10)

for i in trange(n):
    try:
        res = requests.get(get_url(0)).json()
        assert not res["error"], f'Error returned: {res["error"]}'
        all_data.extend(res["jobs"])
    except Exception as e:
        print("Stopping early, after", i, "iterations because of error:", e)
        break

print("Writing output")
output_path.write_text(json.dumps(all_data, indent=2))



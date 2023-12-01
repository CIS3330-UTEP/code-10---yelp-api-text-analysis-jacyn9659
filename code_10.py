from yelpapi import YelpAPI
import pandas as pd

api_key = "nxYMwJ5oMK7di01GrItPb8Sn53Z0XxAc4JYwoKzEfnR-rmoOEFT57rECChraQIpMU4bLU0weDATCKNIpdAS0I5APPkeFB8pC2sfGcm7M0DG8vGIYVw3nPGiaTIhMZXYx"
yelp_api = YelpAPI(api_key) 

search_term = "tacos"
search_location = "el paso"
search_sort_by = "rating" 
search_limit = 10

search_results = yelp_api.search_query(term=search_term, location=search_location,
                                        sort_by=search_sort_by, limit=search_limit)

Restaurant_under_review = "birria-culiacan-el-paso"

result_df = pd.DataFrame.from_dict(search_results['businesses'])
print(result_df['alias'])

reviews_result = yelp_api.reviews_query(id = Restaurant_under_review)
print(reviews_result)

for review in reviews_result['reviews']:
    print(review['text'])

reviews_df = pd.DataFrame([review for review in reviews_result['reviews']])
print(reviews_df)
result_df.to_csv(f"{Restaurant_under_review}_request_reviews_results.csv")

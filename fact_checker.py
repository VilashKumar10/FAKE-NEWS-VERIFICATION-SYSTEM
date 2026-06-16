import requests

API_KEY = "AIzaSyBtaWdV0nvzBcBrc4Cm83UTwDYzrwwhFq4"

def fact_check(claim):

    url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"

    params = {
        "query": claim,
        "key": API_KEY
    }

    response = requests.get(url, params=params)

    print("STATUS:", response.status_code)

    data = response.json()

    print("DATA:", data)

    results = []

    if "claims" in data:
        for item in data["claims"]:

            if "claimReview" in item:

                review = item["claimReview"][0]

                results.append({
                    "claim": item.get("text", ""),
                    "publisher": review.get("publisher", {}).get("name", ""),
                    "rating": review.get("textualRating", ""),
                    "url": review.get("url", "")
                })

    print("RESULTS:", results)

    return results
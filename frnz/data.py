import pandas as pd

cities = pd.DataFrame(
    data={
        "city": [
            "Berlin",
            "Vienna",
            "Montreal",
            "Mumbai",
            "cape-town",
            "Cape Town",
            "Sydney",
        ],
        "country": ["DE", "AT", "CA", "IN", pd.NA, "ZA", "AUS"],
        "population": [3750000, 1900000, 1780000, 184100000, 430000, 440000, pd.NA],
    }
)

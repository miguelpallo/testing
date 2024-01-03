Standard Test Cases:
Happy Path:

Test retrieving the exchange rate for a valid source and target currency pair with a known exchange rate on a specific date.

Missing Exchange Rate:
Test the API's response when the exchange rate for the given date is missing, and the API should find the closest previous date with an available rate.

Triangular Conversion:
Test the API's ability to perform a triangular conversion when there is no direct exchange rate available between the source and target currency.

Invalid Currency Codes:
Test the API's response to requests with invalid source or target currency codes.

Future Date:
Test the API's response when the requested date is in the future (beyond the last known exchange rate).

Boundary Dates:
Test the API with the earliest and latest dates available in the exchange rate data to ensure it handles boundary conditions properly.

Data Format:
Push different format whatever

# Additional Interesting Test Cases:
Subscription Service Down:
Simulate the condition where the subscription service for live data feed is down and verify that the API falls back to the most recent data available.

Concurrent Requests:
Test the API's performance and accuracy under a high load by sending multiple concurrent requests.

Caching Mechanism:
Test the effectiveness of any caching mechanisms by requesting the same exchange rate multiple times and noting response times.

Rate Limiting:
Test the API's handling of rate limiting, ensuring that clients are appropriately throttled.

Cross-Year and Leap Year:
Test the API's logic in handling dates across different years and during leap years.

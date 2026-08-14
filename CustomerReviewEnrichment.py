# pip install pandas nltk pyodbc sqlalchemy

import pandas as pd
import pyodbc
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# Download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')


# Define a function to fetch data from SQL Server
def fetch_data_from_sql():

    # SQL Server connection details
    conn_str = (
        "Driver={ODBC Driver 18 for SQL Server};"
        "Server=SAGARPAUL07;"
        "Database=PortfolioProject_MarketingAnalytics;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

    # Establish connection
    conn = pyodbc.connect(conn_str)

    # SQL query
    query = """
    SELECT
        ReviewID,
        CustomerID,
        ProductID,
        ReviewDate,
        Rating,
        ReviewText
    FROM dbo.customer_reviews;
    """

    # Load SQL data into pandas DataFrame
    df = pd.read_sql(query, conn)

    # Close connection
    conn.close()

    return df


# Fetch customer reviews from SQL Server
customer_reviews_df = fetch_data_from_sql()

print("Successfully loaded customer reviews from SQL Server!")
print(customer_reviews_df.head())


# Initialize VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()


# Calculate sentiment score
def calculate_sentiment(review):

    # Handle missing reviews
    if pd.isna(review):
        return 0

    sentiment = sia.polarity_scores(str(review))

    return sentiment['compound']


# Categorize sentiment using sentiment score + rating
def categorize_sentiment(score, rating):

    if score > 0.05:

        if rating >= 4:
            return 'Positive'

        elif rating == 3:
            return 'Mixed Positive'

        else:
            return 'Mixed Negative'

    elif score < -0.05:

        if rating <= 2:
            return 'Negative'

        elif rating == 3:
            return 'Mixed Negative'

        else:
            return 'Mixed Positive'

    else:

        if rating >= 4:
            return 'Positive'

        elif rating <= 2:
            return 'Negative'

        else:
            return 'Neutral'


# Create sentiment buckets
def sentiment_bucket(score):

    if score >= 0.5:
        return '0.5 to 1.0'

    elif 0.0 <= score < 0.5:
        return '0.0 to 0.49'

    elif -0.5 <= score < 0.0:
        return '-0.49 to 0.0'

    else:
        return '-1.0 to -0.5'


# Calculate sentiment score
customer_reviews_df['SentimentScore'] = (
    customer_reviews_df['ReviewText']
    .apply(calculate_sentiment)
)


# Calculate sentiment category
customer_reviews_df['SentimentCategory'] = customer_reviews_df.apply(
    lambda row: categorize_sentiment(
        row['SentimentScore'],
        row['Rating']
    ),
    axis=1
)


# Calculate sentiment bucket
customer_reviews_df['SentimentBucket'] = (
    customer_reviews_df['SentimentScore']
    .apply(sentiment_bucket)
)


# Display results
print("\nCustomer Reviews with Sentiment Analysis:")
print(customer_reviews_df.head())


# Save results to CSV
customer_reviews_df.to_csv(
    'customer_reviews_with_sentiment.csv',
    index=False
)

print("\nSentiment analysis completed successfully!")
print("CSV file saved as: customer_reviews_with_sentiment.csv")
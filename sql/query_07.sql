-- Extracted from the project notebook
SELECT
  release_year,
  consumer_sentiment_change,
  movie_revenue_yoy_change
FROM `cs-145-project-fall-25.uploaded_movie_data.sentiment_vs_movie_revenue`
WHERE release_year IS NOT NULL
ORDER BY release_year

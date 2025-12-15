-- Extracted from the project notebook
SELECT
  genre_name,
  year_bucket,
  mean_revenue,
  median_revenue
FROM
  `cs-145-project-fall-25.uploaded_movie_data.genre_stats_over_time`
WHERE
  -- Filter out older data to make the chart cleaner
  year_bucket >= 1970
ORDER BY
  genre_name, year_bucket

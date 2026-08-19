UPDATE dbo.customer_reviews
SET ReviewText = REPLACE(ReviewText, '  ', ' ')
WHERE ReviewText LIKE '%  %';
GO

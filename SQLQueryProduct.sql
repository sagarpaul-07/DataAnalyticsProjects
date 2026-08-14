USE PortfolioProject_MarketingAnalytics;
GO

ALTER TABLE dbo.products
ADD PriceCategory VARCHAR(20);
GO

UPDATE dbo.products
SET PriceCategory =
    CASE
        WHEN Price < 50 THEN 'Low'
        WHEN Price BETWEEN 50 AND 200 THEN 'Medium'
        ELSE 'High'
    END;
GO

SELECT *
FROM dbo.products;
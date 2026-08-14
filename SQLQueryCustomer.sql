USE PortfolioProject_MarketingAnalytics;
GO

IF COL_LENGTH('dbo.customers', 'AgeGroup') IS NULL
BEGIN
    ALTER TABLE dbo.customers
    ADD AgeGroup VARCHAR(20);
END;
GO

UPDATE dbo.customers
SET AgeGroup =
    CASE
        WHEN Age > 50 THEN 'Old'
        WHEN Age BETWEEN 20 AND 50 THEN 'Adult'
        ELSE 'Young'
    END;
GO

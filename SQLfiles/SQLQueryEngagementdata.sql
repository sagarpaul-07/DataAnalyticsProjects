USE PortfolioProject_MarketingAnalytics;
GO

IF COL_LENGTH('dbo.engagement_data', 'Views') IS NULL
    ALTER TABLE dbo.engagement_data ADD Views INT;

IF COL_LENGTH('dbo.engagement_data', 'Clicks') IS NULL
    ALTER TABLE dbo.engagement_data ADD Clicks INT;
GO
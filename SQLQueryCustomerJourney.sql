USE PortfolioProject_MarketingAnalytics;
GO

UPDATE dbo.customer_journey
SET Stage = UPPER(Stage);
GO

UPDATE cj
SET Duration = avg_data.avg_duration
FROM dbo.customer_journey AS cj
INNER JOIN
(
    SELECT
        VisitDate,
        AVG(Duration) AS avg_duration
    FROM dbo.customer_journey
    WHERE Duration IS NOT NULL
    GROUP BY VisitDate
) AS avg_data
    ON cj.VisitDate = avg_data.VisitDate
WHERE cj.Duration IS NULL;
GO

WITH DuplicateRecords AS
(
    SELECT
        JourneyID,
        ROW_NUMBER() OVER
        (
            PARTITION BY
                CustomerID,
                ProductID,
                VisitDate,
                Stage,
                Action
            ORDER BY JourneyID
        ) AS row_num
    FROM dbo.customer_journey
)
DELETE FROM DuplicateRecords
WHERE row_num > 1;
GO

SELECT
    JourneyID,
    CustomerID,
    ProductID,
    VisitDate,
    Stage,
    Action,
    Duration
FROM dbo.customer_journey
ORDER BY JourneyID;
GO

SELECT *
FROM dbo.customer_journey
SELECT
	c.CustomerID,
	c.CustomerName,
	c.Email,
	c.Gender,
	c.Age,
	g.Country,
	g.City,

	CASE
		WHEN c.Age>50 THEN 'Old'
		WHEN c.Age BETWEEN 20 AND 50 THEN 'Adult'
		ELSE 'Young'
	END AS AgeGroup

FROM 
    dbo.customers as c
	LEFT JOIN
	dbo.geography as g
ON 
    c.GeographyID = g.GeographyID; 
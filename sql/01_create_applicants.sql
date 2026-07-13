DROP TABLE IF EXISTS applicants;
CREATE TABLE applicants (
    applicant_id TEXT PRIMARY KEY,
    income INTEGER,
    debt INTEGER,
    credit_score INTEGER,
    defaulted INTEGER
);

INSERT INTO applicants VALUES
('A003', 72000, 15000, 750, 0),
('A005', 60000, 10000, 710, 0),
('A001', 48000, 12000, 690, 0),
('A006', 52000, 26000, 640, 1),
('A002', 35000, 18000, 610, 1),
('A004', 41000, 22000, 580, 1);

SELECT *
FROM applicants;

-- Show selected columns only
SELECT applicant_id, income, credit_score
FROM applicants;

-- Find applicants with credit score below 650
SELECT *
FROM applicants
WHERE credit_score < 650;

-- Sort applicants by credit score from high to low
SELECT *
FROM applicants
order by credit_score desc;

-- Calculate debt-to-income ratio
SELECT
    applicant_id,
    income,
    debt,
    ROUND(1.0 * debt / income, 3) AS debt_to_income
FROM applicants;

-- Create risk flag using CASE
SELECT
    applicant_id,
    credit_score,
    CASE
        WHEN credit_score < 650 THEN 'High'
        ELSE 'Low'
    END AS risk_flag
FROM applicants;

-- Calculate portfolio-level KPIs
SELECT
    COUNT(*) AS applicant_count,
    ROUND(AVG(income), 2) AS average_income,
    ROUND(AVG(defaulted), 3) AS default_rate
FROM applicants;

-- Compare average credit score by default status
SELECT
    defaulted,
    COUNT(*) AS applicant_count,
    ROUND(AVG(credit_score), 2) AS average_credit_score
FROM applicants
GROUP BY defaulted;
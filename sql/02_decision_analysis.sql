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

SELECT
    applicant_id,
    credit_score,
    ROUND(1.0 * debt / income, 3) AS debt_to_income,
    CASE
        WHEN credit_score < 600 THEN 'Decline'
        WHEN 1.0 * debt / income >= 0.50 THEN 'Review'
        ELSE 'Approve'
    END AS decision
FROM applicants;

-- Count applicants by lending decision
SELECT
    CASE
        WHEN credit_score < 600 THEN 'Decline'
        WHEN 1.0 * debt / income >= 0.50 THEN 'Review'
        ELSE 'Approve'
    END AS decision,
    COUNT(*) AS applicant_count
FROM applicants
GROUP BY decision
ORDER BY applicant_count DESC;

-- Keep only decision groups with more than one applicant
SELECT
    CASE
        WHEN credit_score < 600 THEN 'Decline'
        WHEN 1.0 * debt / income >= 0.50 THEN 'Review'
        ELSE 'Approve'
    END AS decision,
    COUNT(*) AS applicant_count
FROM applicants
GROUP BY decision
HAVING COUNT(*) > 1
ORDER BY applicant_count DESC;

-- Use a subquery to summarize decisions
SELECT
    decision,
    COUNT(*) AS applicant_count,
    ROUND(AVG(debt_to_income), 3) AS average_dti
FROM (
    SELECT
        applicant_id,
        ROUND(1.0 * debt / income, 3) AS debt_to_income,
        CASE
            WHEN credit_score < 600 THEN 'Decline'
            WHEN 1.0 * debt / income >= 0.50 THEN 'Review'
            ELSE 'Approve'
        END AS decision
    FROM applicants
) AS decision_table
GROUP BY decision
ORDER BY applicant_count DESC;
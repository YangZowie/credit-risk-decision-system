DROP TABLE IF EXISTS applicants;
DROP TABLE IF EXISTS loans;

CREATE TABLE applicants (
    applicant_id TEXT PRIMARY KEY,
    income INTEGER,
    debt INTEGER,
    credit_score INTEGER,
    defaulted INTEGER
);

CREATE TABLE loans (
    loan_id TEXT PRIMARY KEY,
    applicant_id TEXT,
    loan_amount INTEGER,
    product_type TEXT
);

INSERT INTO applicants VALUES
('A003', 72000, 15000, 750, 0),
('A005', 60000, 10000, 710, 0),
('A001', 48000, 12000, 690, 0),
('A006', 52000, 26000, 640, 1),
('A002', 35000, 18000, 610, 1),
('A004', 41000, 22000, 580, 1);

INSERT INTO loans VALUES
('L001', 'A003', 12000, 'Auto Loan'),
('L002', 'A005', 8000, 'Credit Card'),
('L003', 'A001', 10000, 'Personal Loan'),
('L004', 'A006', 15000, 'Auto Loan'),
('L005', 'A002', 9000, 'Credit Card'),
('L006', 'A004', 11000, 'Personal Loan'),
('L007', 'A999', 7000, 'Credit Card');

-- Join applicants with loan information
SELECT
    a.applicant_id,
    a.income,
    a.credit_score,
    l.loan_amount,
    l.product_type
FROM applicants AS a
INNER JOIN loans AS l
    ON a.applicant_id = l.applicant_id;

-- Keep all loans, even when applicant information is missing
SELECT
    l.loan_id,
    l.applicant_id,
    a.income,
    a.credit_score,
    l.loan_amount,
    l.product_type
FROM loans AS l
LEFT JOIN applicants AS a
    ON l.applicant_id = a.applicant_id;

-- Find loans without matching applicant records
SELECT
    l.loan_id,
    l.applicant_id,
    l.loan_amount,
    l.product_type
FROM loans AS l
LEFT JOIN applicants AS a
    ON l.applicant_id = a.applicant_id
WHERE a.applicant_id IS NULL;

-- Analyze default rate by loan product type
SELECT
    l.product_type,
    COUNT(*) AS loan_count,
    ROUND(AVG(a.defaulted), 3) AS default_rate,
    ROUND(AVG(l.loan_amount), 2) AS average_loan_amount
FROM loans AS l
INNER JOIN applicants AS a
    ON l.applicant_id = a.applicant_id
GROUP BY l.product_type
ORDER BY default_rate DESC;
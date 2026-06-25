-- 1
SELECT scheme_name,aum_crore
FROM clean_scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

--2
SELECT
strftime('%Y-%m',date) AS month,
AVG(nav) AS average_nav
FROM clean_nav_history
GROUP BY month;

--3
SELECT *
FROM 04_monthly_sip_inflows;

--4
SELECT
state,
COUNT(*) AS transactions
FROM clean_investor_transactions
GROUP BY state
ORDER BY transactions DESC;

--5
SELECT
scheme_name,
expense_ratio_pct
FROM clean_scheme_performance
WHERE expense_ratio_pct<1;

--6
SELECT
scheme_name,
return_5yr_pct
FROM clean_scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

--7
SELECT
fund_house,
AVG(expense_ratio_pct)
FROM clean_scheme_performance
GROUP BY fund_house;

--8
SELECT
transaction_type,
SUM(amount_inr)
FROM clean_investor_transactions
GROUP BY transaction_type;

--9
SELECT
risk_category,
COUNT(*)
FROM 01_fund_master
GROUP BY risk_category;

--10
SELECT
category,
COUNT(*)
FROM 01_fund_master
GROUP BY category;
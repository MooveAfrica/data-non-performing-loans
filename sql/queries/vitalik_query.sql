WITH colombia AS (
    SELECT 
        'Colombia' AS country,
        week,
        AVG(net_earnings) AS avg_net_earnings,
        AVG(driver_remit_per_plan) AS avg_daily_remittance,
        COUNT(distinct drn) AS total_drivers_count,
        COUNT(CASE WHEN net_earnings > driver_remit_per_plan THEN 1 END) AS driver_count_earning_exceeds_remittance
    FROM dbt.recon__colombia
    WHERE driver_remit_per_plan > 0 AND days_off = 0
    GROUP BY week
),
india AS (
    
    SELECT 
        'India' AS country,
        week,
        AVG(net_earning) AS avg_net_earnings,
        AVG(remittance) AS avg_daily_remittance,
        COUNT(DISTINCT drn) AS total_drivers_count,
                COUNT(DISTINCT CASE WHEN net_earning > remittance THEN drn END) AS driver_count_earning_exceeds_remittance
    FROM dbt.recon__india
    WHERE remittance > 0 AND days_off = 0
    GROUP BY week
),
/*mexico AS (
    SELECT 
        'Mexico' AS country,
        week,
        AVG(net_earnings) AS avg_net_earnings,
        AVG(driver_remit_per_plan) AS avg_daily_remittance,
        COUNT(distinct drn) AS total_drivers_count,
        COUNT(CASE WHEN net_earnings > driver_remit_per_plan THEN 1 END) AS driver_count_earning_exceeds_remittance
    FROM dbt.recon__mexico
    WHERE driver_remit_per_plan > 0 AND days_off = 0
    GROUP BY week
),*/
nigeria AS (
    SELECT 
        'Nigeria' AS country,
        week,
        AVG(net_earnings) AS avg_net_earnings,
        AVG(daily_remittance) AS avg_daily_remittance,
        COUNT(DISTINCT drn) AS total_drivers_count,
                COUNT(DISTINCT CASE WHEN net_earnings > daily_remittance THEN drn END) AS driver_count_earning_exceeds_remittance
    FROM dbt.recon__nigeria
    WHERE daily_remittance > 0 AND days_off = 0
    GROUP BY week
),
southafrica AS (
    SELECT 
        'South Africa' AS country,
        week,
        AVG(net_earnings) AS avg_net_earnings,
        AVG(amount_due) AS avg_daily_remittance,
        COUNT(DISTINCT drn) AS total_drivers_count,
                COUNT(DISTINCT CASE WHEN net_earnings > total_refund THEN drn END) AS driver_count_earning_exceeds_remittance
    FROM dbt.recon__southafrica
    WHERE effective_days != 0
    GROUP BY week    
),
ghana AS (
    SELECT 
        'Ghana' AS country,
        week,
        AVG(net_earnings) AS avg_net_earnings,
        AVG(daily_remittance) AS avg_daily_remittance,
        COUNT(DISTINCT drn) AS total_drivers_count,
                COUNT(DISTINCT CASE WHEN net_earnings > daily_remittance THEN drn END) AS driver_count_earning_exceeds_remittance
    FROM dbt.recon__ghana
    WHERE daily_remittance > 0 AND days_off = 0
    GROUP BY week
),
unified_recon AS (
    SELECT * FROM india
    UNION ALL
    SELECT * FROM nigeria
    UNION ALL
    SELECT * FROM southafrica
    UNION ALL
    SELECT * FROM ghana
)
SELECT
    country,
    week,
    avg_net_earnings,
    avg_daily_remittance,
    avg_net_earnings / NULLIF(avg_daily_remittance, 0) AS earnings_to_remit_ratio,  
    total_drivers_count,
    driver_count_earning_exceeds_remittance,
    (1.0 * driver_count_earning_exceeds_remittance / NULLIF(total_drivers_count, 0))::decimal(9,2) AS pct_drivers_earning_more_than_remittance  
FROM
    unified_recon
ORDER BY
    country, week ASC;
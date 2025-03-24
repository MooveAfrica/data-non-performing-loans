-- Raw records from all reconciliation tables
-- 1) India currently. 
SELECT
    INITCAP(LOWER(city)) as city,
    week,
    NULL as day,
    drn,
    uber_id,
    vehicle_type,
    effective_days,
    net_earning,
    cash_collected,
    uber_balance,
    weekly_remittance as remittance,
    amount_due,
    outstanding,
    cumm_outstanding,
    'recon_india' as schema_name,
    'reconciliation' as table_name
FROM recon_india.reconciliation

UNION ALL 
SELECT
    INITCAP(LOWER(city)) as city,
    week,
    day,
    drn,
    uber_id,
    vehicle_type,
    effective_days,
    net_earning,
    cash_collected,
    uber_balance,
    remittance,
    amount_due,
    outstanding,
    cum_outstanding as cumm_outstanding,
    'recon_india' as schema_name,
    'daily_reconciliation' as table_name
FROM recon_india.daily_reconciliation

-- History Schema Tables
UNION ALL 
SELECT
    'Bangalore' as city,
    week,
    NULL as day,
    drn,
    uber_id,
    vehicle_type,
    effective_days,
    net_earnings AS net_earning,
    cash_collected,
    uber_balance,
    weekly_remittance AS remittance,
    amount_due,
    outstanding,
    cumm_outstanding,
    'reconciliation_history' as schema_name,
    'drivers_data_reconciliation_blr_india' as table_name
FROM reconciliation_history.drivers_data_reconciliation_blr_india

UNION ALL 
SELECT
    'Hyderabad' as city,
    week,
    NULL as day,
    drn,
    uber_id,
    vehicle_type,
    effective_days,
    net_earnings AS net_earning,
    cash_collected,
    uber_balance,
    weekly_remittance AS remittance,
    amount_due,
    outstanding,
    cumm_outstanding,
    'reconciliation_history' as schema_name,
    'drivers_data_reconciliation_hyd_india' as table_name
FROM reconciliation_history.drivers_data_reconciliation_hyd_india

UNION ALL 
SELECT
    'Mumbai' as city,
    week,
    NULL as day,
    drn,
    uber_id,
    vehicle_type,
    effective_days,
    net_earnings AS net_earning,
    cash_collected,
    uber_balance,
    weekly_remittance AS remittance,
    amount_due,
    outstanding,
    cumm_outstanding,
    'reconciliation_history' as schema_name,
    'drivers_data_reconciliation_bom_india' as table_name
FROM reconciliation_history.drivers_data_reconciliation_bom_india


-- 2) Ghana - Accra - MUltiple models
UNION ALL
SELECT
    city,
    week,
    day,
    drn,
    uber_id,
    vehicle_type,
    effective_days,
    net_earning,
    cash_collected,
    uber_balance,
    remittance,
    amount_due,
    outstanding,
    cum_outstanding AS cumm_outstanding,
    'recon_ghana' as schema_name,
    'reconciliation' as table_name
FROM recon_ghana.reconciliation

-- History Schema Tables
UNION ALL
SELECT
    'Accra' as city,
    week,
    day,
    drn,
    uber_id,
    vehicle_type,
    case when days_off=TRUE then 0 else 1 end as effective_days,
    net_earnings as net_earning,
    cash_collected,
    uber_balance,
    daily_remittance as remittance,
    amount_due,
    outstanding,
    cumm_outstanding,
    'reconciliation_history' as schema_name,
    'drivers_data_reconciliation_accra' as table_name
FROM reconciliation_history.drivers_data_reconciliation_accra

UNION ALL
SELECT
    'Accra' as city,
    week,
    day,
    drn,
    uber_id,
    vehicle_type,
    case when days_off=TRUE then 0 else 1 end as effective_days,
    net_earnings as net_earning,
    cash_collected,
    uber_balance,
    amount_due as remittance,
    amount_due,
    outstanding,
    cumm_outstanding,
    'reconciliation_history' as schema_name,
    'drivers_data_reconciliation_accra_03_21_03_22' as table_name
FROM reconciliation_history.drivers_data_reconciliation_accra_03_21_03_22

-- 3) Ghana - Accra - Glovo
UNION ALL
SELECT
    'Accra' as city,
    week,
    NULL as day,
    drn,
    cast(glovo_id as CHAR) as uber_id,
    'Glovo' as vehicle_type,
    effective_days,
    total_earnings as net_earning,
    total_cashout_adjustments as cash_collected,
    glovo_balance as uber_balance,
    amount_due as remittance,
    amount_due,
    outstanding,
    cumm_outstanding,
    'reconciliation_proxy_current' as schema_name,
    'payments_recontiliation_glovo_accra' as table_name
FROM reconciliation_proxy_current.payments_recontiliation_glovo_accra

-- 4) Cape Town and Johannesburg - Multiple models
UNION ALL
SELECT
    city,
    week,
    day,
    drn,
    uber_id,
    vehicle_type,
    effective_days,
    net_earning,
    cash_collected,
    uber_balance,
    remittance, 
    amount_due,
    outstanding,
    cum_outstanding as cumm_outstanding,
    'recon_south_africa' as schema_name,
    'reconciliation' as table_name
FROM recon_south_africa.reconciliation
WHERE city in ('Cape Town', 'Johannesburg')

-- History Schema Tables
UNION ALL
SELECT
    'Cape Town' as city,
    week,
    NULL as day,
    drn,
    NULL as uber_id,
    vehicle_type,
    net_earnings as net_earning,
    effective_days,
    cash_collection as cash_collected,
    uber_balance,
    amount_due as remittance,
    amount_due,
    week_outstanding as outstanding,
    cumm_outstanding,
    'reconciliation_history' as schema_name,
    'drivers_data_reconciliation_cape_town' as table_name
FROM reconciliation_history.drivers_data_reconciliation_cape_town

UNION ALL
SELECT
    'Johannesburg' as city,
    week,
    NULL as day,
    drn,
    NULL as uber_id,
    vehicle_type,
    effective_days,
    net_earnings as net_earning,
    cash_collection as cash_collected,
    uber_balance,
    amount_due as remittance,
    amount_due,
    week_outstanding as outstanding,
    cumm_outstanding,
    'reconciliation_history' as schema_name,
    'drivers_data_reconciliation_johannesburg' as table_name
FROM reconciliation_history.drivers_data_reconciliation_johannesburg

-- 5) Nigeria - Lagos - Suzuki Alto
UNION ALL
SELECT
    city,
    week,
    day,
    drn,
    uber_id,
    vehicle_type,
    effective_days,
    net_earning,
    cash_collected,
    uber_balance,
    remittance,
    amount_due,
    outstanding,
    cum_outstanding as cumm_outstanding,
    'recon_nigeria' as schema_name,
    'reconciliation_alto' as table_name
FROM recon_nigeria.reconciliation_alto
-- WHERE vehicle_type = 'Suzuki Alto'

-- History Schema Tables
UNION ALL
SELECT
    'Lagos' as city,
    week,
    day,
    drn,
    driveruuid as uber_id,
    'Suzuki Alto' as vehicle_type,
    case when day_off=TRUE then 0 else 1 end as effective_days,
    total_earnings as net_earning,
    total_cash_collected as cash_collected,
    total_uber_balance as uber_balance,
    amount_due as remittance,
    amount_due,
    net_outstanding as outstanding,
    cumm_outstanding,
    'reconciliation_history' as schema_name,
    'drivers_data_reconciliation_ubergo_lagos_dto48_altos' as table_name
FROM reconciliation_history.drivers_data_reconciliation_ubergo_lagos_dto48_altos

-- 6) Nigeria - Lagos - Spresso
UNION ALL
SELECT
    city,
    week,
    day,
    drn,
    uber_id,
    vehicle_type,
    effective_days,
    net_earning,
    cash_collected,
    uber_balance,
    remittance,
    amount_due,
    outstanding,
    cum_outstanding as cumm_outstanding,
    'recon_nigeria' as schema_name,
    'reconciliation_spresso' as table_name
FROM recon_nigeria.reconciliation_spresso
-- WHERE vehicle_type = 'Suzuki S-Presso'

-- History Schema Tables
UNION ALL
SELECT
    'Lagos' as city,
    week,
    day,
    drn,
    uber_id,
    vehicle_type,
    case when days_off=TRUE then 0 else 1 end as effective_days,
    net_earnings as net_earning,
    cash_collected,
    uber_balance,
    daily_remittance as remittance,
    amount_due,
    outstanding,
    cumm_outstanding,
    'reconciliation_history' as schema_name,
    'drivers_data_reconciliation_ubergo_lagos_tryout' as table_name
FROM reconciliation_history.drivers_data_reconciliation_ubergo_lagos_tryout
-- WHERE vehicle_type = 'Suzuki S-Presso'

-- 7) Nigeria - Lagos - UberGo DTO 18
UNION ALL
SELECT
    'Lagos' as city,
    week,
    day,
    drn,
    driveruuid as uber_id,
    'UberGo DTO 18' as vehicle_type,
    NULL as effective_days,
    total_earnings as net_earning,
    total_cash_collected as cash_collected,
    total_uber_balance as uber_balance,
    amount_due as remittance,
    amount_due,
    net_outstanding as outstanding,
    cumm_outstanding,
    'reconciliation_proxy_current' as schema_name,
    'drivers_data_reconciliation_ubergo_lagos' as table_name
FROM reconciliation_proxy_current.drivers_data_reconciliation_ubergo_lagos

-- History Schema Tables
UNION ALL
SELECT
    'Lagos' as city,
    week,
    day,
    drn,
    driveruuid as uber_id,
    'UberGo DTO 18' as vehicle_type,
    NULL as effective_days,
    total_earnings as net_earning,
    total_cash_collected as cash_collected,
    total_uber_balance as uber_balance,
    amount_due as remittance,
    amount_due,
    net_outstanding as outstanding,
    cumm_outstanding,
    'reconciliation_history' as schema_name,
    'drivers_data_reconciliation_ubergo_lagos' as table_name
FROM reconciliation_history.drivers_data_reconciliation_ubergo_lagos

-- 7) Nigeria - Lagos - UberX
UNION ALL
SELECT
    'Lagos' as city,
    week_date as week,
    NULL as day,
    drns as drn,
    NULL as uber_id,
    'UberX' as vehicle_type,
    NULL as effective_days,
    earnings as net_earning,
    cash_collected,
    uber_balance,
    amount_due as remittance,
    net_outstanding as amount_due,
    outstanding,
    cumm_outstanding,
    'reconciliation_proxy_current' as schema_name,
    'drivers_outstanding_report_uberx_lagos' as table_name
FROM reconciliation_proxy_current.drivers_outstanding_report_uberx_lagos

-- History Schema Tables
UNION ALL
SELECT
    'Lagos' as city,
    week_date as week,
    NULL as day,
    drns as drn,
    NULL as uber_id,
    'UberX' as vehicle_type,
    NULL as effective_days,
    earnings as net_earning,
    cash_collected,
    uber_balance,
    amount_due as remittance,
    net_outstanding as amount_due,
    outstanding,
    cumm_outstanding,
    'reconciliation_history' as schema_name,
    'drivers_outstanding_report_uberx_lagos' as table_name
FROM reconciliation_history.drivers_outstanding_report_uberx_lagos

-- 8) Nigeria - Lagos - UberConnect
UNION ALL
SELECT
    'Lagos' as city,
    week,
    day,
    drn,
    driveruuid as uber_id,
    'UberConnect TVS' as vehicle_type,
    case when day_off=TRUE then 0 else 1 end as effective_days,
    total_earnings as net_earning,
    total_cash_collected as cash_collected,
    total_uber_balance as uber_balance,
    amount_due as remittance,
    amount_due,
    net_outstanding as outstanding,
    cumm_outstanding,
    'reconciliation_proxy_current' as schema_name,
    'riders_data_reconciliation_uberconnect_lagos' as table_name
FROM reconciliation_proxy_current.riders_data_reconciliation_uberconnect_lagos

UNION ALL
SELECT
    'Lagos' as city,
    week,
    day,
    drn,
    driveruuid as uber_id,
    'UberConnect TVS' as vehicle_type,
    case when day_off=TRUE then 0 else 1 end as effective_days,
    total_earnings as net_earning,
    total_cash_collected as cash_collected,
    total_uber_balance as uber_balance,
    amount_due as remittance,
    amount_due,
    net_outstanding as outstanding,
    cumm_outstanding,
    'reconciliation_history' as schema_name,
    'riders_data_reconciliation_uberconnect_lagos' as table_name
FROM reconciliation_history.riders_data_reconciliation_uberconnect_lagos

-- 9) Nigeria - Ibadan - UberMoto
UNION ALL
SELECT
    'Ibadan' as city,
    week,
    NULL as day,
    drn,
    driveruuid as uber_id,
    'UberMoto TVS' as vehicle_type,
    effective_days,
    total_earnings as net_earning,
    total_cash_collected as cash_collected,
    total_uber_balance as uber_balance,
    amount_due as remittance,
    amount_due,
    net_outstanding as outstanding,
    cumm_outstanding,
    'reconciliation_proxy_current' as schema_name,
    'riders_data_reconciliation_ubermoto_ibadan' as table_name
FROM reconciliation_proxy_current.riders_data_reconciliation_ubermoto_ibadan


-- 10) Kenya - Nairobi - TVS
UNION ALL
SELECT
    'Nairobi' as city,
    week,
    day,
    drn,
    driveruuid as uber_id,
    'TVS' as vehicle_type,
    case when day_off=TRUE then 0 else 1 end as effective_days,
    total_earnings as net_earning,
    total_cash_collected as cash_collected,
    total_uber_balance as uber_balance,
    amount_due as remittance,
    amount_due,
    net_outstanding as outstanding,
    cumm_outstanding,
    'reconciliation_proxy_current' as schema_name,
    'drivers_data_reconciliation_nairobi' as table_name
FROM reconciliation_proxy_current.drivers_data_reconciliation_nairobi

-- History Schema Tables
UNION ALL
SELECT
    'Nairobi' as city,
    week,
    day,
    drn,
    driveruuid as uber_id,
    'TVS' as vehicle_type,
    case when day_off=TRUE then 0 else 1 end as effective_days,
    total_earnings as net_earning,
    total_cash_collected as cash_collected,
    total_uber_balance as uber_balance,
    amount_due as remittance,
    amount_due,
    net_outstanding as outstanding,
    cumm_outstanding,
    'reconciliation_history' as schema_name,
    'drivers_data_reconciliation_nairobi' as table_name
FROM reconciliation_history.drivers_data_reconciliation_nairobi

ORDER BY city, week, day, drn;
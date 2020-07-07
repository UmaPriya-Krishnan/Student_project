create table if not exists placement_details(COMPANY_ID VARCHAR(9) NOT NULL PRIMARY KEY,
                        COMPANY_NAME    VARCHAR(15),
                        PLACEMENT_VENUE VARCHAR(50),
                        PLACEMENT_DATE  DATE,
                        PLACEMENT_START_DATE DATETIME,
                        PLACEMENT_END_DATE   DATETIME);
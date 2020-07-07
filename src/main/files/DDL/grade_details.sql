create table if not exists grade_details(GRADE_ID CHAR(2) NOT NULL PRIMARY KEY,
                        GRADE_DESCRIPTION    CHAR(20),
                        GRADE_START_DATE DATETIME,
                        GRADE_END_DATE   DATETIME);
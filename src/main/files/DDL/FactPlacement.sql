create table if not exists FactPlacement(STUDENT_ID BIGINT NOT NULL,
                     DEP_ID    VARCHAR(9),
                     COMPANY_ID VARCHAR(9),
                     HIRED  VARCHAR(5),
                     PLACEMENT_FACT_START_DATE DATETIME,
                     PLACEMENT_FACT_END_DATE   DATETIME,
					 FOREIGN KEY(STUDENT_ID) REFERENCES STUDENT_REFERENCE(STUDENT_ID),
					 FOREIGN KEY(DEP_ID) REFERENCES department_details(DEP_ID),
					 FOREIGN KEY(COMPANY_ID) REFERENCES placement_details(COMPANY_ID));
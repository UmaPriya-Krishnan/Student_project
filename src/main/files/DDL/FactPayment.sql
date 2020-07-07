create table if not exists FactPayment(STUDENT_ID BIGINT NOT NULL,
                     FEE_ID    VARCHAR(10)   NOT NULL,
                     PAYMENT_ID VARCHAR(9),
                     PAYMENT_FACT_START_DATE DATETIME,
                     PAYMENT_FACT_END_DATE   DATETIME,
					 FOREIGN KEY (STUDENT_ID) REFERENCES STUDENT_REFERENCE(STUDENT_ID),
					 FOREIGN KEY(FEE_ID) REFERENCES payment_details(FEE_ID));
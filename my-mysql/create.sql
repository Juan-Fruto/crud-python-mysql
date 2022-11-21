CREATE TABLE workers(
    id VARCHAR(10) PRIMARY KEY NOT NULL,
    nameWorker VARCHAR(90) NOT NULL,
    phone VARCHAR(10) UNIQUE,
    designation VARCHAR(20) NOT NULL,
    salary  DECIMAL(13, 2)
);
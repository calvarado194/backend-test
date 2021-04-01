CREATE TABLE users(
    id INT AUTO_INCREMENT primary key,
    email VARCHAR(255),
    password VARCHAR(255)
);

INSERT into users (email, password) 
values
    ("ema@oneninefour.cl", "$2b$12$OAgctCnoSaKGBIg3sfDXDulETFFDSn9Tpm48XXa.F6O1UWrBUBiGa");

CREATE TABLE businesses(
    id INT AUTO_INCREMENT primary key,
    name VARCHAR(255),
    address VARCHAR(255),
    rut VARCHAR(255),
    contact_email VARCHAR(255)
);
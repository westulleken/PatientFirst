CREATE TABLE salutation (
    salutation_id SERIAL PRIMARY KEY,
    salutation_label VARCHAR(50) NOT NULL
);

CREATE TABLE id_type (
    id_type_id SERIAL PRIMARY KEY,
    id_type_label VARCHAR(50) NOT NULL
);

CREATE TABLE sex (
    sex_id SERIAL PRIMARY KEY,
    sex_label VARCHAR(30) NOT NULL
);

CREATE TABLE gender_identity (
    gender_identity_id SERIAL PRIMARY KEY,
    gender_label VARCHAR(50) NOT NULL
);

CREATE TABLE nationality (
    nationality_id SERIAL PRIMARY KEY,
    nationality_label VARCHAR(100) NOT NULL
);

CREATE TABLE home_language (
    language_id SERIAL PRIMARY KEY,
    language_label VARCHAR(100) NOT NULL
);

CREATE TABLE medical_aid (
    medical_aid_id SERIAL PRIMARY KEY,
    medical_aid_label VARCHAR(150) NOT NULL
);

CREATE TABLE medical_aid_plan (
    plan_id SERIAL PRIMARY KEY,
    medical_aid_id INTEGER REFERENCES medical_aid(medical_aid_id),
    plan_label VARCHAR(150) NOT NULL
);

CREATE TABLE patient (
    patient_id UUID PRIMARY KEY,
    first_name VARCHAR(150) NOT NULL,
    surname VARCHAR(150) NOT NULL,
    salutation_id INTEGER REFERENCES salutation(salutation_id),
    id_type_id INTEGER REFERENCES id_type(id_type_id),
    id_number VARCHAR(50),
    date_of_birth DATE,
    sex_id INTEGER REFERENCES sex(sex_id),
    gender_identity_id INTEGER REFERENCES gender_identity(gender_identity_id),
    nationality_id INTEGER REFERENCES nationality(nationality_id),
    language_id INTEGER REFERENCES home_language(language_id),
    occupation VARCHAR(255),
    archived BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE patient_medical_aid (
    patient_medical_aid_id SERIAL PRIMARY KEY,
    patient_id UUID REFERENCES patient(patient_id),
    medical_aid_id INTEGER REFERENCES medical_aid(medical_aid_id),
    plan_id INTEGER REFERENCES medical_aid_plan(plan_id),
    membership_number VARCHAR(100),
    dependent_code VARCHAR(20),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE contact_type (
    contact_type_id SERIAL PRIMARY KEY,
    contact_type_label VARCHAR(50) NOT NULL
);

CREATE TABLE patient_contact (
    contact_id SERIAL PRIMARY KEY,
    patient_id UUID REFERENCES patient(patient_id),
    contact_type_id INTEGER REFERENCES contact_type(contact_type_id),
    contact_value VARCHAR(255),
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE address_type (
    address_type_id SERIAL PRIMARY KEY,
    address_type_label VARCHAR(50) NOT NULL
);

CREATE TABLE address (
    address_id SERIAL PRIMARY KEY,
    patient_id UUID REFERENCES patient(patient_id),
    address_type_id INTEGER REFERENCES address_type(address_type_id),
    line1 TEXT,
    line2 TEXT,
    city VARCHAR(150),
    province VARCHAR(150),
    postal_code VARCHAR(20)
);

CREATE TABLE relationship_type (
    relationship_id SERIAL PRIMARY KEY,
    relationship_label VARCHAR(50) NOT NULL
);

CREATE TABLE next_of_kin (
    nok_id SERIAL PRIMARY KEY,
    patient_id UUID REFERENCES patient(patient_id),
    nok_name VARCHAR(150),
    nok_surname VARCHAR(150),
    relationship_id INTEGER REFERENCES relationship_type(relationship_id),
    phone VARCHAR(50),
    email VARCHAR(150),
    address TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE researchers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    institution VARCHAR(255),
    start_year INT,
    citation_count INT,
    publications_count INT,
    h_index INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE publications (
    id SERIAL PRIMARY KEY,
    researcher_id INT REFERENCES researchers(id),
    title TEXT NOT NULL,
    publication_date DATE,
    citation_count INT,
    journal VARCHAR(255)
);

CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    researcher_id INT REFERENCES researchers(id),
    prediction_score FLOAT,
    confidence FLOAT,
    calculated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
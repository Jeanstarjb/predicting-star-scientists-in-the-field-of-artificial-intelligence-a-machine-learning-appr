CREATE TABLE researchers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    institution VARCHAR(255),
    start_year INT NOT NULL,
    citation_count INT DEFAULT 0,
    publications_count INT DEFAULT 0,
    h_index INT DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE publications (
    id SERIAL PRIMARY KEY,
    researcher_id INT NOT NULL REFERENCES researchers(id),
    title VARCHAR(255) NOT NULL,
    publication_date DATE NOT NULL,
    citation_count INT DEFAULT 0,
    journal VARCHAR(255) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    researcher_id INT NOT NULL REFERENCES researchers(id),
    prediction_score FLOAT NOT NULL,
    feature_set JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_researchers_institution ON researchers(institution);
CREATE INDEX idx_publications_researcher ON publications(researcher_id);
CREATE INDEX idx_predictions_researcher ON predictions(researcher_id);
CREATE INDEX idx_predictions_score ON predictions(prediction_score);
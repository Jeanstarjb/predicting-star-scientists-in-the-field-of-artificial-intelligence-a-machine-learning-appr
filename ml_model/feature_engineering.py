import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

def get_features(db_uri):
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = text("""
        SELECT 
            r.id as researcher_id,
            r.start_year,
            r.h_index,
            COUNT(p.id) as early_publications_count,
            COUNT(DISTINCT p.journal) as early_discipline_diversity,
            COALESCE(SUM(p.citation_count), 0) as early_citation_sum
        FROM researchers r
        LEFT JOIN publications p ON r.id = p.researcher_id
        WHERE EXTRACT(YEAR FROM p.publication_date) BETWEEN r.start_year AND r.start_year + 5
        GROUP BY r.id, r.start_year, r.h_index
    """)
    result = session.execute(query)
    features_df = pd.DataFrame(result.fetchall(), columns=result.keys())
    session.close()
    
    features_df['target'] = (features_df['h_index'] >= 20).astype(int)
    return features_df

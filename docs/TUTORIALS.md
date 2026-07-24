# Platform Tutorials

## Researcher Quickstart
1. **Profile Setup**
```python
# Example API call to update profile
import requests

response = requests.patch(
  '/api/researchers/me',
  json={'h_index': 12, 'grants': ['NIH-R01']},
  headers={'Authorization': 'Bearer <token>'}
)
```
2. **Interpreting Results**
- Star Score components breakdown
- Benchmark against peers

## Funding Agency Workshop
- Creating custom filters:
```json
{
  "min_prediction_confidence": 0.85,
  "research_areas": ["LLMs", "Robotics"],
  "max_career_age": 5
}
```
- Setting automated alerts for promising researchers

## Admin Training
- Model version management
- Anomaly detection configuration
- Data privacy controls
# Recommendation System for Job Suggestions

## Overview

This project implements a recommendation system designed to suggest job opportunities to users based on their skills and industry. The system takes into account user data and job information, including job title, industry, skills required, and more. It utilizes a variety of machine learning models, including pre-trained models for embedding generation, to recommend jobs with the highest relevance to the user's profile.

### Features:
- Recommends jobs based on user-provided skills and industry.
- Uses models like `SBERT`, `PhoBERT`, and `XLM-RoBERTa` to compute embeddings and determine job relevance.
- Provides job recommendations with calculated distances (similarities) between user profile and job requirements.
- Supports batch processing to generate job recommendations for multiple users at once.

## Technologies Used

- **Python**: Main programming language for backend development.
- **Pandas**: Data manipulation and analysis.
- **SQLAlchemy**: ORM for interacting with the database and querying job data.
- **Hugging Face Transformers**: For pre-trained models like `SBERT`, `PhoBERT`, and `XLM-RoBERTa` for embedding generation.
- **Asyncio**: To handle asynchronous operations and manage multiple concurrent tasks.
- **PostgreSQL**: Database used to store job information.
- **Flask/FastAPI (optional)**: For creating a web API to interact with the recommendation system.



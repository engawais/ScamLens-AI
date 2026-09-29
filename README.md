# ScamLens AI

**Multimodal Scam Detection, Evidence Analysis & Digital Safety Intelligence Platform**

ScamLens AI is a portfolio-grade AI/ML project designed to analyze suspicious messages, URLs, screenshots, phone-number reputation signals, and related scam patterns. The system combines machine learning, NLP, computer vision/OCR, semantic similarity, evidence fusion, explainability, and retrieval-augmented generation (RAG).

## Project status

Phase 1 — Project setup and architecture: **Complete**

## Planned technology stack

- Python
- FastAPI
- PostgreSQL
- scikit-learn / PyTorch
- NLP and transformer models
- OpenCV + OCR
- Sentence Transformers
- FAISS
- RAG + LLM
- SHAP
- Flutter
- Docker
- Git / GitHub

## Repository structure

```text
ScamLens-AI/
├── backend/          # FastAPI backend and application services
├── ml/               # datasets, training code, models, evaluation
├── rag/              # RAG documents and vector data
├── mobile/           # Flutter mobile application (later phase)
├── docs/             # architecture and project documentation
├── scripts/          # utility/development scripts
├── docker/           # Docker configuration (later phase)
└── .github/          # CI/CD configuration (later phase)
```

## Responsible-use principle

ScamLens reports evidence and risk signals. A user report is not automatically proof that a person committed a crime. The application should preserve source attribution and distinguish community reports, external intelligence matches, and officially verified information.

## Development roadmap

1. Project setup and architecture
2. Data collection and dataset design
3. Data preprocessing
4. NLP scam detection
5. URL risk engine
6. Screenshot/OCR engine
7. Phone reputation engine
8. Scam pattern memory
9. Evidence fusion
10. Explainable AI
11. RAG knowledge system
12. FastAPI backend
13. PostgreSQL integration
14. Flutter mobile app
15. Testing and security
16. Docker and deployment
17. Documentation and portfolio release

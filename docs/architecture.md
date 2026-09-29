# ScamLens AI — Architecture

## High-level flow

Flutter Mobile App
        |
        v
FastAPI Backend
        |
        +--> NLP Scam Engine
        +--> URL Risk Engine
        +--> OCR / Screenshot Engine
        +--> Phone Reputation Engine
        |
        v
Evidence Fusion Engine
        |
        +--> Risk Assessment
        +--> Scam Pattern Memory / Vector Search
        +--> Explainable AI
        +--> RAG / AI Explanation
        |
        v
Final Security Report

## Core design principle

The system should combine multiple pieces of evidence instead of relying on one binary classifier. Every risk result should retain its source and confidence.

## Data-source principle

ScamLens will not claim access to private police/NCCIA databases. Phone reputation data will come from ScamLens reports, legitimately accessible public information, and authorized external threat-intelligence sources where available.

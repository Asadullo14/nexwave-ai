nexwave-ai/
│
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── docker-compose.yml
│
├── docs/
│   ├── SRS.md
│   ├── architecture.md
│   ├── database-schema.md
│   ├── api-specification.md
│   └── roadmap.md
│
├── backend/
│   ├── requirements.txt
│   ├── app/
│   │   ├── main.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── api/
│   │   │   └── routes/
│   │   │       ├── rf.py
│   │   │       ├── ai.py
│   │   │       ├── telecom.py
│   │   │       ├── events.py
│   │   │       └── reports.py
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   │   ├── rf_processor.py
│   │   │   ├── anomaly_detector.py
│   │   │   └── telecom_analyzer.py
│   │   └── database/
│   │       ├── connection.py
│   │       └── repositories/
│   └── tests/
│
├── frontend/
│   ├── package.json
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── charts/
│   │   └── App.jsx
│   └── public/
│
├── ai/
│   ├── notebooks/
│   │   └── rf_anomaly_experiment.ipynb
│   ├── models/
│   ├── training/
│   └── evaluation/
│
├── data/
│   ├── sample/
│   └── README.md
│
└── scripts/
    ├── generate_sample_data.py
    └── run_demo.py

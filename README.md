# Python Coding Challenges – Rate Limiting & Data Refactoring

This repository contains two practical coding exercises designed to assess real-world Python engineering skills:

- **Rate Limiting Logic** using a mock API
- **DataFrame Refactoring** for data processing and transformation

Each module includes implementation code and accompanying `pytest`-based tests.

---

## 🧩 Contents

```

rate_limiting
├── api.py                       # Mock API with rate limiting logic
├── app.py                       # Candidate implementation (rate-limited requests)
└── tests
    └── test_api.py              # Tests for rate limiting behavior

refactor
├── data_processor.py            # DataFrame transformation logic
└── tests
    └── test_data_processor.py   # Tests for expected output

````

---

## 🧪 Setup Instructions

1. **Clone the repo**  
```bash
git clone <your-repo-url>
cd <repo-root>
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run tests**

```bash
pytest
```

---

## 🧠 Exercise 1: Rate Limiting

Located in `rate_limiting/`.

### Description:

Implements logic to call `MockAPI.call()` safely, avoiding a `RateLimitError` when more than 5 requests are made within 5 seconds.

### Test:

```bash
pytest rate_limiting/tests/test_api.py
```

---

## 🧠 Exercise 2: Data Refactoring

Located in `refactor/`.

### Description

Refactor the code provided in `refactor/data_processor.py`, ensure all tests pass.

### Test:

```bash
pytest refactor/tests/test_data_processor.py
```

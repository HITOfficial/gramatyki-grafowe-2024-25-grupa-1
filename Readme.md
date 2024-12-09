# GramatykiGrafowe Grupa 5 projekt 1

### Setup

```ps1
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

```ps1
python -m venv .venv
.venv\Scripts\activate
```

// on lesser os

```ps1
python -m venv .venv
source .venv/bin/activate
```

---

```ps1
pip install -r requirements.txt
pip install -e .
```

### Test

```ps1
pip install pytest
pip install PyQt5
python -m pytest
```

### Run

```ps1
python productions/p1.py
python productions/p2.py
```

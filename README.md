# Piyush Kumar Vedwal — Interactive Portfolio

A clean, editorial-style interactive portfolio served with Streamlit.

**Live:** https://portfolio-piyush-vedwal.streamlit.app/

**Features:** precision-reticle cursor that morphs over links and project cards, a quiet dot-grid background that responds to the cursor, word-by-word heading reveals, magnetic buttons, animated counters, a tech marquee, and live canvas visuals for each project (audio-fingerprint constellation, a differential-privacy data flow, and an attendance dashboard).

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Edit content
All content and animations live in `portfolio.html`; `app.py` just renders it full-screen.

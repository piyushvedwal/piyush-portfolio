"""Piyush Kumar Vedwal - interactive portfolio (Streamlit).

The whole site lives in portfolio.html and is rendered full-screen inside
Streamlit, so the custom cursor, canvas animations and JS all work.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Piyush Kumar Vedwal | Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide all Streamlit chrome and make the portfolio iframe fill the window.
st.markdown(
    """
    <style>
      #MainMenu, header, footer, [data-testid="stToolbar"],
      [data-testid="stDecoration"], [data-testid="stStatusWidget"],
      [data-testid="stSidebar"], [data-testid="collapsedControl"] { display: none !important; }
      html, body, .stApp { background: #05060a !important; overflow: hidden !important; }
      .block-container, [data-testid="stMainBlockContainer"] { padding: 0 !important; max-width: 100% !important; }
      [data-testid="stAppViewContainer"], [data-testid="stMain"] { overflow: hidden !important; }
      iframe {
        position: fixed !important; inset: 0 !important;
        width: 100vw !important; height: 100vh !important; height: 100dvh !important;
        border: 0 !important; z-index: 999 !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "portfolio.html").read_text(encoding="utf-8")
components.html(html, height=800, scrolling=True)

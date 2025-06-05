import streamlit as st

def load_tabs_style():  
    st.markdown(
        """
    <style>
    /* Tab list container */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #f0f2f6;
        padding: 5px;
        border-radius: 8px;
        margin-bottom: 20px;
    }

    /* Individual tab styling */
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        white-space: pre-wrap;
        background-color: #ffffff;
        border-radius: 8px;
        color: #47556b;
        font-size: 16px;
        font-weight: 500;
        padding: 12px 24px;
        margin: 0;
        border: 2px solid transparent;
        transition: all 0.3s ease;
    }

    /* Active tab styling */
    .stTabs [aria-selected="true"] {
        background-color: #1f77b4;
        color: white;
        border-color: #1f77b4;
        box-shadow: 0 4px 12px rgba(31, 119, 180, 0.3);
    }

    /* Hover effect for inactive tabs */
    .stTabs [data-baseweb="tab"]:hover:not([aria-selected="true"]) {
        background-color: #e6f3ff;
        border-color: #1f77b4;
        color: #1f77b4;
        transform: translateY(-2px);
    }

    /* Tab highlight (bottom border) */
    .stTabs [data-baseweb="tab-highlight"] {
        background-color: transparent;
    }

    /* Button styling within tabs */
    .stTabs [data-baseweb="tab"] button {
        font-size: 16px;
        font-weight: 500;
        border: none;
        background: transparent;
        color: inherit;
        width: 100%;
        height: 100%;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

def load_style():
    load_tabs_style()
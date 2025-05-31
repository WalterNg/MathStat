import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="Statistics Calculator")

# Initialize session state for data persistence
if "statistics_data" not in st.session_state:
    st.session_state.statistics_data = pd.DataFrame(
        {
            "Sample_ID": ["Sample_1", "Sample_2", "Sample_3"],
            "Value": [10.5, 15.2, 8.7],
            "Weight": [1, 1, 1],  # Default equal weights of 1
        }
    )

# Main title
st.title("📊 Interactive Statistics Calculator")
st.markdown("Add and edit data directly in the table below:")

# Create the interactive data editor
edited_df = st.data_editor(
    st.session_state.statistics_data,
    num_rows="dynamic",  # Allow adding/deleting rows
    use_container_width=True,
    key="main_data_editor",
)

# Ensure Weight column exists and has default values for new rows
if "Weight" not in edited_df.columns:
    edited_df["Weight"] = 1
else:
    # Fill any NaN weights with default value of 1
    edited_df["Weight"] = edited_df["Weight"].fillna(1)

n_rows = len(edited_df)

tab1, tab2 = st.tabs(["Cửa sổ trượt", "Linear Regression"])

with tab1:
    st.subheader("Cửa sổ trượt")
    start_window, end_window = st.select_slider(
        "Chọn độ dài cửa sổ trượt",
        options=list(range(1, n_rows + 1)),
        value=(1,3)
    )

    # Calculate next value prediction
    if len(edited_df) >= end_window:
        # Convert from 1-based sample numbers to 0-based indices
        start_idx = start_window - 1
        end_idx = end_window - 1
        
        # Get the window values and weights using the correct indices
        window_values = edited_df['Value'].iloc[start_idx:end_idx + 1]
        window_weights = edited_df['Weight'].iloc[start_idx:end_idx + 1]
        
        # Calculate relative weights (proportions)
        total_weight = window_weights.sum()
        relative_weights = window_weights / total_weight
        
        # Calculate weighted average
        next_value_prediction = sum(w * v for w, v in zip(relative_weights, window_values))
        
        # Display prediction in a mathematical format
        st.markdown("---")
        st.markdown("### Weighted Moving Average Calculation")
        
        # Show the formula and values with both raw weights and their proportions
        weight_info = []
        for w, v in zip(window_weights, window_values):
            prop = w / total_weight
            weight_info.append(f"({w} × {v:.2f}) = {prop:.2%} influence")
        
        values_str = " + ".join([f"({w:.2f} × {v:.2f})" for w, v in zip(relative_weights, window_values)])
        
        st.markdown(
            f"""
            <div style='background-color: #f8f9fa; padding: 20px; border-radius: 5px; border: 1px solid #dee2e6; font-family: "Courier New", monospace;'>
                <p style='margin: 0; color: #495057;'>WMA = Σ(wᵢ × xᵢ) / Σwᵢ</p>
                <p style='margin: 10px 0; color: #495057;'>Raw Weights: {', '.join([str(w) for w in window_weights])}</p>
                <p style='margin: 10px 0; color: #495057;'>Weight Proportions: {', '.join([f"{w/total_weight:.2%}" for w in window_weights])}</p>
                <p style='margin: 10px 0; color: #495057;'>WMA = {values_str}</p>
                <p style='margin: 10px 0; color: #495057;'>WMA = {next_value_prediction:.2f}</p>
            </div>  
            """,
            unsafe_allow_html=True
        )
        
        # Show the final result in a more prominent way
        st.markdown(
            f"""
            <div style='background-color: #e9ecef; padding: 15px; border-radius: 5px; margin-top: 10px; text-align: center;'>
                <p style='margin: 0; font-size: 1.2em; color: #212529;'>Next Value Prediction = <strong>{next_value_prediction:.2f}</strong></p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning(f"Need at least {end_window} data points to make a prediction")

with tab2:
    st.subheader("Linear Regression")

# Only update session state if the data actually changed
if not edited_df.equals(st.session_state.statistics_data):
    st.session_state.statistics_data = edited_df
    st.rerun()  # Rerun to update UI with new data

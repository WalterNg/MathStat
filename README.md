# MathStat - Interactive Statistics Calculator

A powerful web-based statistics calculator built with Streamlit that allows users to perform statistical calculations and data analysis through an intuitive interface.

## Features

- 📊 Interactive data editor with dynamic row management
- 🔢 Weighted Moving Average (WMA) calculations
- 📈 Linear Regression analysis (coming soon)
- ⚖️ Customizable weights for data points
- 🎯 Real-time calculations and predictions
- 📱 Responsive and user-friendly interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/MathStat.git
cd MathStat
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run main.py
```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Use the interactive data editor to:
   - Add new data points
   - Edit existing values
   - Adjust weights for each data point
   - Delete rows as needed

4. Navigate between different analysis tabs:
   - "Cửa sổ trượt" (Sliding Window) for weighted moving average calculations
   - "Linear Regression" for regression analysis

## Features in Detail

### Weighted Moving Average
- Select a window size using the slider
- View detailed calculations including:
  - Raw weights
  - Weight proportions
  - Step-by-step calculation process
  - Final prediction value

### Data Management
- Dynamic data table with the following columns:
  - Sample_ID: Identifier for each data point
  - Value: The numerical value to be analyzed
  - Weight: Customizable weight for each data point (defaults to 1)

## Requirements

- Python 3.7+
- Streamlit
- Pandas
- NumPy

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
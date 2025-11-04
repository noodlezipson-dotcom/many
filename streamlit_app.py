import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Hong Kong Stock Recommendation System",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stock-card {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        border-left: 5px solid #1f77b4;
    }
    .rank-badge {
        background-color: #ff6b6b;
        color: white;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .price {
        font-size: 1.8rem;
        font-weight: bold;
        color: #1f77b4;
        margin: 0.5rem 0;
    }
    .score {
        font-size: 1.5rem;
        font-weight: bold;
        color: #e74c3c;
        margin: 0.5rem 0;
    }
    .indicator {
        background-color: #e8f4fd;
        padding: 0.5rem;
        border-radius: 5px;
        margin: 0.3rem 0;
        font-size: 0.9rem;
    }
    .buy-signal {
        color: #e74c3c;
        font-weight: bold;
    }
    .positive {
        color: #2ecc71;
    }
    .negative {
        color: #e74c3c;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Application title
    st.markdown('<div class="main-title">📈 Hong Kong Stock Recommendation System</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Beginner-friendly stock analysis tool</div>', unsafe_allow_html=True)
    
    # Analysis settings area
    st.header("1. Analysis Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        overlap_index = st.slider("Recommendation Overlap Index", 1, 10, 5)
    
    with col2:
        min_trading_amount = st.number_input("Minimum Trading Amount (Million HKD)", min_value=10, max_value=1000, value=100, step=10)
    
    # Output settings
    st.header("2. Output Settings")
    if st.button("Run New Analysis", type="primary"):
        st.success("Analysis completed!")
    
    # Recommended stocks area
    st.header("3. Recommended Stocks TOP 5")
    st.markdown("**Higher scores indicate better buying opportunities**")
    
    # Display recommended stocks
    display_recommended_stocks()

def display_recommended_stocks():
    """Display recommended stocks"""
    
    # Mock stock data for Hong Kong stocks
    stocks_data = [
        {
            "rank": 1,
            "name": "TENCENT",
            "code": "0700.HK",
            "price": "HK$320.50",
            "score": 9.2,
            "indicators": [
                {"text": "Recent 5-day return: +12.3%", "type": "positive"},
                {"text": "Technical rebound potential: High", "type": "normal"},
                {"text": "Buy signal", "type": "buy"},
                {"text": "Uptrend reversal (Short-term crossing long-term)", "type": "normal"},
                {"text": "Strong upward momentum (+12.5%)", "type": "positive"},
                {"text": "Reasonable price level (Overheating: 58.7)", "type": "normal"}
            ]
        },
        {
            "rank": 2,
            "name": "HSBC HOLDINGS",
            "code": "0005.HK",
            "price": "HK$68.90",
            "score": 8.5,
            "indicators": [
                {"text": "Average trading volume: HK$1,235M", "type": "normal"},
                {"text": "Recent 5-day return: +8.2%", "type": "positive"},
                {"text": "Technical rebound potential: Medium", "type": "normal"},
                {"text": "Buy signal", "type": "buy"},
                {"text": "Uptrend reversal (Short-term crossing long-term)", "type": "normal"},
                {"text": "Strong upward momentum (+8.2%)", "type": "positive"},
                {"text": "Resistance zone, possible adjustment (Overheating: 76.4)", "type": "negative"}
            ]
        },
        {
            "rank": 3,
            "name": "ALIBABA GROUP",
            "code": "9988.HK",
            "price": "HK$85.60",
            "score": 8.0,
            "indicators": [
                {"text": "Average trading volume: HK$892M", "type": "normal"},
                {"text": "Recent 5-day return: +7.1%", "type": "positive"},
                {"text": "Technical rebound potential: High", "type": "normal"},
                {"text": "Buy signal", "type": "buy"},
                {"text": "Uptrend reversal (Short-term crossing long-term)", "type": "normal"},
                {"text": "Strong upward momentum (+7.1%)", "type": "positive"},
                {"text": "Reasonable price level (Overheating: 55.3)", "type": "normal"}
            ]
        },
        {
            "rank": 4,
            "name": "AIA GROUP",
            "code": "1299.HK",
            "price": "HK$72.40",
            "score": 7.8,
            "indicators": [
                {"text": "Average trading volume: HK$756M", "type": "normal"},
                {"text": "Recent 5-day return: +5.8%", "type": "positive"},
                {"text": "Technical rebound potential: Medium", "type": "normal"},
                {"text": "Buy signal", "type": "buy"},
                {"text": "Uptrend reversal (Short-term crossing long-term)", "type": "normal"},
                {"text": "Stable upward trend (+5.8%)", "type": "positive"},
                {"text": "Reasonable price level (Overheating: 52.9)", "type": "normal"}
            ]
        },
        {
            "rank": 5,
            "name": "MEITUAN",
            "code": "3690.HK",
            "price": "HK$125.80",
            "score": 7.5,
            "indicators": [
                {"text": "Average trading volume: HK$1,042M", "type": "normal"},
                {"text": "Recent 5-day return: +4.9%", "type": "positive"},
                {"text": "Technical rebound potential: Low", "type": "normal"},
                {"text": "Buy signal", "type": "buy"},
                {"text": "Uptrend reversal (Short-term crossing long-term)", "type": "normal"},
                {"text": "Stable upward trend (+4.9%)", "type": "positive"},
                {"text": "Approaching resistance zone (Overheating: 68.2)", "type": "negative"}
            ]
        }
    ]
    
    # Display stock cards
    for stock in stocks_data:
        display_stock_card(stock)

def display_stock_card(stock):
    """Display individual stock card"""
    st.markdown(f"""
    <div class="stock-card">
        <div style="display: flex; align-items: center; margin-bottom: 1rem;">
            <div class="rank-badge">{stock['rank']}</div>
            <div style="margin-left: 1rem;">
                <h3 style="margin: 0;">{stock['name']}</h3>
                <p style="margin: 0; color: #666; font-size: 0.9rem;">{stock['code']}</p>
            </div>
        </div>
        
        <div class="price">{stock['price']}</div>
        <div class="score">{stock['score']} points</div>
        
        <div style="margin-top: 1rem;">
    """, unsafe_allow_html=True)
    
    # Display indicators
    for indicator in stock['indicators']:
        if indicator['type'] == 'buy':
            st.markdown(f'<div class="indicator buy-signal">✓ {indicator["text"]}</div>', unsafe_allow_html=True)
        elif indicator['type'] == 'positive':
            st.markdown(f'<div class="indicator positive">↑ {indicator["text"]}</div>', unsafe_allow_html=True)
        elif indicator['type'] == 'negative':
            st.markdown(f'<div class="indicator negative">↓ {indicator["text"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="indicator">• {indicator["text"]}</div>', unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("© 2024 Hong Kong Stock Recommendation System | Investment losses are the responsibility of the investor")

if __name__ == "__main__":
    main()

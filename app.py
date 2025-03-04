import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Set page configuration as the first command
st.set_page_config(
    page_title="Project 9: Build a Python Website",
    page_icon="./static/favicon.ico",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
<style>
html, body, .stApp {
    background-color: #2d345b !important;
    color: #ffffff !important;
}

.stApp {
    background-color: #2d345b !important;
}

.metric-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 50px;
        margin-top: 50px;
    }
    .metric-box {
        text-align: center;
        background-color: #1c2042;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        color: white;  /* Ensures the text color contrasts well with the dark background */
    }
    .metric-label {
        font-size: 18px;
        color: #FFF;
    }
    .metric-value {
        font-size: 32px;
        font-weight: bold;
        color: #ffffff;
    }

[data-testid="stSidebar"] {
    background-color: #1c2042 !important;
}
            
.centered-image {
            display: block;
            margin-left: auto;
            margin-right: auto;
}         

.stMarkdown, .stDataFrame, .stMetric {
    color: #ffffff !important;
}

h1, h2, h3, h4, h5, h6 {
    color: #4ECDC4 !important;
}

.stButton>button {
    background-color: #4ECDC4 !important;
    color: #2d345b !important;
}

.stSelectbox>div>div>div {
    background-color: #1c2042 !important;
    color: #ffffff !important;
}

.stPlotlyChart {
    background-color: #1c2042 !important;
}
</style>
""", unsafe_allow_html=True)

# Sample data generation function
def generate_sample_data():
    np.random.seed(42)
    df = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D', 'E'],
        'Value': np.random.randint(50, 200, 5),
        'Performance': np.random.uniform(0.5, 1.5, 5)
    })
    return df

def create_visualization(data, chart_type):
    """Create different types of visualizations"""
    if chart_type == "Bar Chart":
        fig = px.bar(
            data, 
            x='Category', 
            y='Value', 
            color='Performance',
            title='Interactive Bar Chart',
            color_continuous_scale=px.colors.sequential.Viridis
        )
    elif chart_type == "Pie Chart":
        fig = px.pie(
            data, 
            values='Value', 
            names='Category', 
            title='Category Distribution',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
    else:
        fig = px.scatter(
            data, 
            x='Category', 
            y='Value', 
            size='Performance',
            color='Performance',
            title='Scatter Plot Analysis',
            color_continuous_scale=px.colors.sequential.Plasma
        )
    
    # Update layout for dark theme
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        title_font_color='white'
    )
    
    return fig

def main():    
    st.image("./static/logo.png", width=120)
    st.markdown("<div style='text-align: left; color: #fff; font-size: 2rem; font-weight: 900;'>Interactive Data Explorer 📊</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: left; color: #fff; margin-top:-1vmin;'>Project 9: Build a Python Website in 15 Minutes With Streamlit</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: left; color: #fff; margin-top:-1vmin;'>FOR GIAIC Q3 - ROLL # 00037391 BY MERCHANTSONS</div>", unsafe_allow_html=True)

    # Sidebar for user inputs
    st.sidebar.header("🛠 Control Panel")

    # Data generation
    data = generate_sample_data()
    
    # Sidebar widgets
    chart_type = st.sidebar.selectbox(
        "Select Visualization Type",
        ["Bar Chart", "Pie Chart", "Scatter Plot"]
    )
    
    # Dynamic visualization
    st.markdown("<h2 style='color: #4ECDC4;'>Data Visualization</h2>", unsafe_allow_html=True)
    
    # Create and display chart
    fig = create_visualization(data, chart_type)
    st.plotly_chart(fig, use_container_width=True)
    
    # Additional information section
    col1, col2 = st.columns(2)
    
    with col1:
     st.markdown('<div class="metric-box"><p class="metric-label">Total Value</p><p class="metric-value">{}</p></div>'.format(data['Value'].sum()), unsafe_allow_html=True)

    with col2:
     st.markdown('<div class="metric-box"><p class="metric-label">Average Performance</p><p class="metric-value">{:.2f}</p></div>'.format(data['Performance'].mean()), unsafe_allow_html=True)

def upload_section():
    """File upload functionality"""
    st.sidebar.header("📤 Data Upload")
    uploaded_file = st.sidebar.file_uploader(
        "Choose a CSV file", 
        type="csv"
    )
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.sidebar.success("File uploaded successfully!")
            
            # Display uploaded data
            st.markdown("### Uploaded Data")
            st.dataframe(df)
            
            # Optional: Additional data insights
            st.markdown("#### Data Summary")
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Total Rows", len(df))
            
            with col2:
                st.metric("Total Columns", len(df.columns))
        
        except Exception as e:
            st.sidebar.error(f"Error processing file: {e}")

def run_app():
    """Main app runner"""
    main()
    upload_section()

    # Footer
    st.markdown(
        "<div style='text-align: center; color: #fff; margin-top: 2rem;'>© Copyright 2025 Merchantsons. All rights reserved.</div>", 
        unsafe_allow_html=True
    )

# Execute the app
if __name__ == "__main__":
    run_app()
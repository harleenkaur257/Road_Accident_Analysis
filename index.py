import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px       #visualization
import pandas as pd
import requests
import base64
def get_base64(img_path):
    with open(img_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

df=pd.read_csv("indian_roads_dataset.csv")
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month_name()
df["day"] = df["date"].dt.day
year_col = "year"

df.info()
st.set_page_config(
    page_title="Road Accident Analysis",
    page_icon="images/logo.png",
    layout="wide"
)

with st.sidebar:
    opt = option_menu(
        "Navigation",
        [
            "Home",
            "Dataset",
            "Processing",
            "Visualization",
            "Accident Map",
            "Reports",
            "Query",
            "About",
        ],
        icons=[
            "house",
            "table",
            "gear",
            "bar-chart",
            "geo-alt",
            "file-earmark-text",
            "chat-dots",
            "info-circle",
        ],
        menu_icon="display",
        default_index=0,

        styles={
            "container": {
                "padding": "10px",
                "background-color": "#0B1F3A",   # Navy Blue
                "border-radius": "12px",
            },

            "icon": {
                "color": "#FFD700",              # Gold icons
                "font-size": "18px",
            },

            "nav-link": {
                "font-size": "17px",
                "font-weight": "600",
                "color": "white",
                "padding": "10px",
                "margin": "5px 0",
                "border-radius": "8px",
                "--hover-color": "#1E3A5F",      # Hover color
            },

            "nav-link-selected": {
                "background-color": "#2563EB",   # Blue selected
                "color": "white",
                "font-weight": "bold",
            },

            "menu-title": {
                "color": "white",
                "font-size": "22px",
                "font-weight": "bold",
            },
        },
    )
###################################################################################################################  .  
if opt == "Home":
    st.markdown("""
    <style>

    /* ===================== MAIN BACKGROUND ===================== */
    .stApp{
        background-color:#0B1F3A;
    }

    /* ===================== HEADINGS ===================== */
    h1,h2,h3,h4,h5,h6{
        color:#FFD700 !important;
        font-weight:bold;
    }

    /* ===================== NORMAL TEXT ===================== */
    p, div, span, label{
        color:white !important;
    }

    /* ===================== CAPTION ===================== */
    [data-testid="stCaptionContainer"]{
        color:#EAEAEA !important;
    }

    /* ===================== METRIC CARDS ===================== */
    div[data-testid="stMetric"]{
        background:#112B4A;
        border:2px solid #FFD700;
        border-radius:12px;
        padding:15px;
        transition:0.4s;
        box-shadow:0px 4px 10px rgba(0,0,0,.3);
    }

    div[data-testid="stMetric"]:hover{
        background:#1E3A5F;
        transform:translateY(-5px);
        box-shadow:0px 8px 18px rgba(255,215,0,.35);
    }

    /* Metric Label */
    div[data-testid="stMetricLabel"]{
        color:#FFD700 !important;
    }

    /* Metric Value */
    div[data-testid="stMetricValue"]{
        color:white !important;
    }

    /* ===================== CONTAINERS ===================== */
    div[data-testid="stVerticalBlockBorderWrapper"]{
        background:#112B4A;
        border:2px solid #FFD700;
        border-radius:15px;
        transition:0.4s;
    }

    div[data-testid="stVerticalBlockBorderWrapper"]:hover{
        background:#1E3A5F;
        transform:scale(1.02);
        box-shadow:0px 8px 20px rgba(255,215,0,.25);
    }

    /* ===================== IMAGES ===================== */
    img{
        border-radius:12px;
        transition:0.4s;
    }

    img:hover{
        transform:scale(1.05);
        box-shadow:0px 8px 20px rgba(255,215,0,.4);
        border:2px solid #FFD700;
    }

    /* ===================== VIDEO ===================== */
    video{
        border-radius:15px;
        border:2px solid #FFD700;
    }

    /* ===================== BUTTON ===================== */
    .stButton>button{
        background:#FFD700;
        color:#0B1F3A;
        border:none;
        border-radius:8px;
        font-weight:bold;
    }

    .stButton>button:hover{
        background:#FFC107;
        color:#0B1F3A;
    }

    /* ===================== HR ===================== */
    hr{
        border:1px solid #FFD700;
    }

    /* ===================== SCROLLBAR ===================== */
    ::-webkit-scrollbar{
        width:8px;
    }

    ::-webkit-scrollbar-thumb{
        background:#FFD700;
        border-radius:10px;
    }

    ::-webkit-scrollbar-track{
        background:#0B1F3A;
    }

    </style>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns([1, 6])
    
    with col1:
        st.image("images/logo.png", width=100)
    with col2:
        st.title("Road Accident Analysis")
        st.caption("Data Analysis & Visualization Dashboard")

    st.video("images/road.mp4")
    st.markdown("---")


    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("Total Records", len(df))
        
    with col2:
            st.metric("Total Columns", df.shape[1])
            
    with col3:
        if year_col:
            st.metric("Years Covered", df[year_col].nunique())
        else:
            st.metric("Years Covered", "N/A")

    with col4:
        if "state" in df.columns.str.lower():
            state_col = [c for c in df.columns if c.lower() == "state"][0]
            st.metric("States", df[state_col].nunique())
        else:
            st.metric("States", "N/A")

    with col5:
        if "city" in df.columns.str.lower():
            city_col = [c for c in df.columns if c.lower() == "city"][0]
            st.metric("Cities", df[city_col].nunique())
        else:
            st.metric("Cities", "N/A")
    st.markdown("---")
    st.title(" Features of Road Accident Analysis")
    img1 = get_base64("images/feature1.jpg")
    img2 = get_base64("images/feature2.jpg")
    img3 = get_base64("images/feature3.jpg")
    img4 = get_base64("images/feature4.jpg")
    col1, col2, col3, col4 = st.columns(4)

    # ---------------- Card 1 ----------------
    st.markdown("""
    <style>

    /* Feature Card */
    .feature-card{
        background:#112B4A;
        border:2px solid;
        border-color:"#FFD700";
        border-radius:15px;
        padding:15px;
        height:320px;
        box-shadow:0px 4px 12px rgba(0,0,0,0.30);
        transition:all 0.4s ease;
        cursor:pointer;
    }

    /* Hover Effect */
    .feature-card:hover{
        background:#1E3A5F;
        transform:translateY(-8px);
        box-shadow:0px 8px 20px rgba(255,215,0,0.35);
    }

    /* Title */
    .title{
        text-align:center;
        font-size:22px;
        font-weight:700;
        color:#FFD700;
        margin-bottom:15px;
    }

    /* Description */
    .desc{
        text-align:justify;
        font-size:15px;
        line-height:1.7;
        color:white;
    }

    /* Images inside feature cards */
    .feature-card img{
        width:100%;
        height:200px;
        object-fit:cover;
        border-radius:12px ;
        transition:0.4s;
    }

    .feature-card img:hover{
        transform:scale(1.05);
        border:2px solid #FFD700;
    }

    </style>
    """, unsafe_allow_html=True)
    with col1:
        # Image
        st.markdown(f"""
        <img src="data:image/jpg;base64,{img1}"
            style="width:100%; height:200px;
            object-fit:cover; border-radius:12px;">
        """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown(
                "<h4 style='text-align:center; color:#1f4e79;'>Accident Trend Analysis</h4>",
                unsafe_allow_html=True,
            )

            st.write(
                "This feature analyzes accident data over different years, "
                "months, and days to identify trends. It helps understand "
                "how accident rates change over time."
            )
    # ---------------- Card 2 ----------------

    with col2:

        st.markdown(f"""
        <img src="data:image/jpg;base64,{img2}"
        style="width:100%; height:200px; object-fit:cover; border-radius:12px;">
        """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown(
                "<h4 style='text-align:center; color:#1f4e79;'>Time-based Analysis</h4>",
                unsafe_allow_html=True,
            )

            st.write(
                "Time-based analysis shows when accidents occur most "
                "frequently during the day, week, or month, year. It helps "
                "identify peak accident hours."
            )
            # ---------------- Card 3 ----------------

    with col3:

        st.markdown(f"""
        <img src="data:image/jpg;base64,{img3}"
        style="width:100%; height:200px; object-fit:cover; border-radius:12px;">
        """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown(
                "<h4 style='text-align:center; color:#1f4e79;'>Weather Condition Analysis</h4>",
                unsafe_allow_html=True,
            )

            st.write(
                "This feature studies the impact of different weather "
                "conditions on road accidents such as rain, fog, and clear weather."
            )
        # ---------------- Card 4 ----------------

    with col4:

        st.markdown(f"""
        <img src="data:image/jpg;base64,{img4}"
        style="width:100%; height:200px; object-fit:cover; border-radius:12px;">
        """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown(
                "<h4 style='text-align:center; color:#1f4e79;'>Cause of Accident Analysis</h4>",
                unsafe_allow_html=True,
            )

            st.write(
                "This feature examines the major causes of road accidents "
                "including overspeeding, distracted driving, and poor road conditions."
            )
    st.markdown("---")

    st.header(" Road Accident Analysis Gallery")

   # Function to convert image to base64
    def get_base64(image_path):
        with open(image_path, "rb") as img:
            return base64.b64encode(img.read()).decode()


    # Image paths
    images = [
        "images/gallery1.PNG",
        "images/gallery2.PNG",
        "images/gallery3.PNG",
        "images/gallery4.PNG",
        "images/gallery5.PNG",
        "images/gallery6.PNG",
        "images/gallery7.PNG",
        "images/gallery8.PNG",
    ]           

    # Display 4 images per row
    for i in range(0, len(images), 4):

        cols = st.columns(4)

        for col, img in zip(cols, images[i:i+4]):
            with col:
                img64 = get_base64(img)

                st.markdown(
                    f"""
                    <div style="
                        border-radius:12px;
                        overflow:hidden;
                        box-shadow:0 4px 10px rgba(0,0,0,0.2);
                        margin-bottom:20px;
                    ">
                        <img src="data:image/jpeg;base64,{img64}"
                            style="
                                width:100%;
                                height:220px;
                                object-fit:cover;
                                display:block;
                            ">
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
    
    st.markdown("---")
    
    
################################################################################################################

elif opt == "Dataset":
    st.title(" Dataset Overview")
    st.markdown("""
    ### Description
    The Dataset section provides a comprehensive overview of the Road Accident Dataset.
    It enables users to explore the complete dataset, understand its structure,
    examine data quality, inspect missing and duplicate values, view statistical
    summaries, and analyze relationships among numerical variables. This section
    serves as the foundation for all further visualizations and analytical insights.
    """)

    # ---------------- Tabs ----------------
    t1, t2, t3, t4, t5, t6, t7, t8, t9 = st.tabs([
        "📄 Data",
        "📋 Columns",
        "📐 Shape",
        "🔠 Data Types",
        "❓ Missing Values",
        "🔁 Duplicates",
        "🔢 Unique Values",
        "📈 Summary",
        "📊 Correlation"
    ])
    st.markdown("""
<style>

/* ==================== MAIN APP ==================== */
.stApp{
    background-color:#0B1F3A;
}

/* ==================== HEADINGS ==================== */
h1,h2,h3,h4,h5,h6{
    color:#FFD700 !important;
    font-weight:bold;
}

/* ==================== TEXT ==================== */
p, label, span{
    color:white !important;
}

/* ==================== INFO BOX ==================== */
div[data-testid="stAlert"]{
    background:#112B4A;
    border-left:5px solid #FFD700;
    color:white;
    border-radius:10px;
}

/* ==================== METRICS ==================== */
div[data-testid="stMetric"]{
    background:#112B4A;
    border:2px solid #FFD700;
    border-radius:12px;
    padding:15px;
    transition:0.3s;
}

div[data-testid="stMetric"]:hover{
    background:#1E3A5F;
    transform:translateY(-5px);
    box-shadow:0px 8px 18px rgba(255,215,0,.35);
}

div[data-testid="stMetricLabel"]{
    color:#FFD700 !important;
}

div[data-testid="stMetricValue"]{
    color:white !important;
}

/* ==================== DATAFRAME ==================== */
div[data-testid="stDataFrame"]{
    border:2px solid #FFD700;
    border-radius:12px;
    overflow:hidden;
    transition:0.3s;
}

div[data-testid="stDataFrame"]:hover{
    box-shadow:0px 8px 18px rgba(255,215,0,.35);
}

/* ==================== TABS ==================== */
button[data-baseweb="tab"]{
    background:#112B4A !important;
    color:white !important;
    border-radius:8px 8px 0 0;
    margin-right:5px;
    transition:0.3s;
}

button[data-baseweb="tab"]:hover{
    background:#1E3A5F !important;
    color:#FFD700 !important;
}

button[aria-selected="true"]{
    background:#FFD700 !important;
    color:#0B1F3A !important;
    font-weight:bold;
}

/* ==================== PLOTLY ==================== */
.js-plotly-plot{
    border:2px solid #FFD700;
    border-radius:12px;
    transition:0.3s;
}

.js-plotly-plot:hover{
    box-shadow:0px 8px 18px rgba(255,215,0,.35);
}

/* ==================== HORIZONTAL LINE ==================== */
hr{
    border:1px solid #FFD700;
}

/* ==================== SCROLLBAR ==================== */
::-webkit-scrollbar{
    width:8px;
}

::-webkit-scrollbar-track{
    background:#0B1F3A;
}

::-webkit-scrollbar-thumb{
    background:#FFD700;
    border-radius:10px;
}

::-webkit-scrollbar-thumb:hover{
    background:#FFC107;
}

</style>
""", unsafe_allow_html=True)
    
    st.markdown("""
<style>

/* App Background */
.stApp{
    background:#0B1F3A;
}

/* DataFrame Container */
div[data-testid="stDataFrame"]{
    border:2px solid #FFD700;
    border-radius:12px;
    overflow:hidden;
}

/* Header */
div[data-testid="stDataFrame"] thead tr th{
    background:#112B4A !important;
    color:#FFD700 !important;
    font-weight:bold !important;
}

/* Cells */
div[data-testid="stDataFrame"] tbody tr td{
    background:#0B1F3A !important;
    color:white !important;
}

/* Alternate Rows */
div[data-testid="stDataFrame"] tbody tr:nth-child(even) td{
    background:#102847 !important;
}

/* Hover Row */
div[data-testid="stDataFrame"] tbody tr:hover td{
    background:#1E3A5F !important;
    color:#FFD700 !important;
}

/* Index Column */
div[data-testid="stDataFrame"] tbody th{
    background:#112B4A !important;
    color:#FFD700 !important;
}

</style>
""", unsafe_allow_html=True)
    
    # ==========================================================
    # DATA
    # ==========================================================
    with t1:
        st.subheader("📄 Complete Dataset")

        st.info("""
        Displays all accident records available in the dataset.
        Users can browse, search, and inspect individual records before analysis.
        """)

        st.dataframe(df, use_container_width=True)

    # ==========================================================
    # COLUMNS
    # ==========================================================
    with t2:
        st.subheader("📋 Dataset Columns")

        st.info("""
        Lists all columns (features) present in the dataset along with their names.
        These attributes are used throughout the accident analysis dashboard.
        """)

        columns_df = pd.DataFrame({
            "Column Name": df.columns
        })

        st.dataframe(columns_df, use_container_width=True)

    # ==========================================================
    # SHAPE
    # ==========================================================
    with t3:
        st.subheader("📐 Dataset Shape")

        st.info("""
        Shows the total number of records (rows) and attributes (columns)
        available in the dataset.
        """)

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Total Rows", df.shape[0])

        with col2:
            st.metric("Total Columns", df.shape[1])

    # ==========================================================
    # DATA TYPES
    # ==========================================================
    with t4:
        st.subheader("🔠 Data Types")

        st.info("""
        Displays the data type of each feature such as integer,
        float, string, or datetime.
        """)

        dtype_df = pd.DataFrame({
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str).values
        })

        st.dataframe(dtype_df, use_container_width=True)

    # ==========================================================
    # MISSING VALUES
    # ==========================================================
    with t5:
        st.subheader("❓ Missing Values")

        st.info("""
        Identifies missing or null values present in each column.
        This helps evaluate data quality before performing analysis.
        """)

        missing = df.isnull().sum()

        missing_df = pd.DataFrame({
            "Column": missing.index,
            "Missing Values": missing.values
        })

        st.dataframe(missing_df, use_container_width=True)

        st.bar_chart(missing)

    # ==========================================================
    # DUPLICATES
    # ==========================================================
    with t6:
        st.subheader("🔁 Duplicate Records")

        st.info("""
        Displays the number of duplicate records in the dataset.
        Duplicate records may affect analytical accuracy.
        """)

        duplicate_count = df.duplicated().sum()

        st.metric("Duplicate Rows", duplicate_count)

        if duplicate_count > 0:
            st.dataframe(df[df.duplicated()], use_container_width=True)
        else:
            st.success("✅ No duplicate records found.")

    # ==========================================================
    # UNIQUE VALUES
    # ==========================================================
    with t7:
        st.subheader("🔢 Unique Values")

        st.info("""
        Shows the number of unique values present in every column.
        This helps understand feature diversity and cardinality.
        """)

        unique_df = pd.DataFrame({
            "Column": df.columns,
            "Unique Values": df.nunique().values
        })

        st.dataframe(unique_df, use_container_width=True)

    # ==========================================================
    # SUMMARY
    # ==========================================================
    with t8:
        st.subheader("📈 Statistical Summary")

        st.info("""
        Provides descriptive statistics including count, mean,
        standard deviation, minimum, maximum, and quartile values
        for numerical columns.
        """)

        st.dataframe(df.describe(include="all"), use_container_width=True)

    # ==========================================================
    # CORRELATION
    # ==========================================================
    with t9:
        st.subheader("📊 Correlation Matrix")

        st.info("""
        Displays the correlation among numerical variables.
        Values close to +1 indicate strong positive correlation,
        values close to -1 indicate strong negative correlation,
        while values near 0 indicate little or no relationship.
        """)

        numeric_df = df.select_dtypes(include=["int64", "int32", "float64"])

        corr = numeric_df.corr()

        st.dataframe(corr.round(2), use_container_width=True)

        fig = px.imshow(
            corr,
            text_auto=True,
            color_continuous_scale="RdBu_r",
            aspect="auto",
            title="Correlation Heatmap"
        )

        st.plotly_chart(fig, use_container_width=True)

   
####################################################################################################################

elif opt == "Processing":

    st.title("⚙️ Data Processing")
    st.markdown("""
<style>

    /* Main Background */
    .stApp {
        background-color: #081b33;
        color: white;
    }


    /* Title */
    h1, h2, h3, h4 {
        color: #ffffff !important;
        font-family: 'Segoe UI', sans-serif;
    }


    /* Normal Text */
    p, div, span, label {
        color: #e6f0ff !important;
        font-size: 16px;
    }


    /* Tabs Container */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background-color: #0b2447;
        padding: 10px;
        border-radius: 12px;
    }


    /* Tab Buttons */
    .stTabs [data-baseweb="tab"] {
        background-color: #12355b;
        color: white !important;
        border-radius: 10px;
        padding: 10px 18px;
        font-size: 15px;
        font-weight: 600;
        transition: 0.3s;
    }


    /* Hover Effect */
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #1e90ff;
        color: white !important;
        transform: scale(1.05);
    }


    /* Active Tab */
    .stTabs [aria-selected="true"] {
        background-color: #0077ff !important;
        color: white !important;
        border-radius: 10px;
    }


    /* Description Box */
    .stMarkdown {
        background-color: #102a43;
        padding: 18px;
        border-radius: 12px;
        line-height: 1.6;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
    }


    /* Dataframe */
    .stDataFrame {
        border-radius: 10px;
        overflow: hidden;
    }


</style>
""", unsafe_allow_html=True)

    st.markdown("""
    ### Description
    The Data Processing section illustrates the preprocessing steps performed
    on the Road Accident Dataset before visualization and analysis. Data
    preprocessing improves data quality by handling missing values,
    removing unnecessary columns, resetting the index, and verifying
    the cleaned dataset. These steps ensure accurate and reliable results
    during analysis.
    """)

    t1, t2, t3, t4, t5 = st.tabs([
        "📌 Original Data",
        "❓ Missing Values",
        "🧹 Processing Steps",
        "✅ Cleaned Data",
        "📊 Summary"
    ])

    # ==========================================================
    # Original Dataset
    # ==========================================================
    with t1:

        st.subheader("📌 Original Dataset")

        st.info("""
        This tab displays the original Road Accident Dataset before applying any
        preprocessing operations. It shows the actual data received from the source,
        including missing values and unnecessary columns.
        """)

        # Original Dataset Metrics
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Total Rows",
                df.shape[0]
            )

        with col2:
            st.metric(
                "Total Columns",
                df.shape[1]
            )

        with col3:
            st.metric(
                "Missing Values",
                df.isnull().sum().sum()
            )


        st.write("### Dataset Preview")


        # Select rows to display
        n = st.slider(
            "Select number of rows to display",
            min_value=5,
            max_value=100,
            value=20000
        )


        st.dataframe(
            df.head(n),
            use_container_width=True
        )


        

    # ==========================================================
    # Missing Values
    # ==========================================================
    with t2:

        st.subheader("❓ Missing Values Before Processing")

        st.info("""
        This tab displays the missing values present in the original dataset before
        applying any preprocessing techniques. Identifying missing values is an
        important step because incomplete data can affect the accuracy of analysis
        and visualization results.
        """)

        # Original Dataset Information
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Rows Before Processing", df.shape[0])

        with col2:
            st.metric("Columns Before Processing", df.shape[1])

        with col3:
            st.metric("Total Missing Values", df.isnull().sum().sum())


        # Missing Value Table
        missing_before = df.isnull().sum()

        missing_df = pd.DataFrame({
            "Column Name": missing_before.index,
            "Missing Values": missing_before.values,
            "Percentage (%)": 
                ((missing_before.values / len(df)) * 100).round(2)
        })


        st.write("### Missing Value Details")

        st.dataframe(
            missing_df,
            use_container_width=True
        )


        # Only show columns having missing values
        missing_only = missing_df[missing_df["Missing Values"] > 0]


        if len(missing_only) > 0:

            st.write("### Missing Values Visualization")

            fig = px.bar(
                missing_only,
                x="Column Name",
                y="Missing Values",
                text="Missing Values",
                title="Missing Values Before Processing"
            )

            fig.update_layout(
                xaxis_title="Columns",
                yaxis_title="Number of Missing Values"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        else:
            st.success("✅ No missing values found in the dataset.")
    # ==========================================================
    # Processing Steps
    # ==========================================================
    with t3:

        st.subheader("🧹 Data Cleaning Steps")

        st.info("""
        The following preprocessing operations are performed:
        • Removed the 'festival' column because it contains many missing values.
        • Removed rows containing null values.
        • Reset the dataframe index.
        """)

        processed_df = df.copy()

        processed_df.drop(columns=["festival"], inplace=True)
        processed_df.dropna(inplace=True)
        processed_df.reset_index(drop=True, inplace=True)

        st.code("""
            1. Remove 'festival' column
            2. Drop rows containing missing values
            3. Reset dataframe index
        """)

    # ==========================================================
    # Cleaned Dataset
    # ==========================================================
    with t4:

        st.subheader("✅ Dataset After Processing")

        st.info("""
        This tab displays the cleaned Road Accident Dataset after applying
        preprocessing techniques. The unnecessary 'festival' column has been
        removed, missing records have been handled, and the index has been reset
        to prepare the dataset for further analysis and visualization.
        """)


        # Create Processed Dataset
        processed_df = df.copy()

        # Remove unnecessary column
        if "festival" in processed_df.columns:
            processed_df.drop(columns=["festival"], inplace=True)

        # Remove missing values
        processed_df.dropna(inplace=True)

        # Reset index
        processed_df.reset_index(drop=True, inplace=True)


        # Dataset Metrics
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Rows After Processing",
                processed_df.shape[0]
            )

        with col2:
            st.metric(
                "Columns After Processing",
                processed_df.shape[1]
            )

        with col3:
            st.metric(
                "Missing Values",
                processed_df.isnull().sum().sum()
            )


        st.write("### Cleaned Dataset Preview")

        rows = st.slider(
            "Select number of rows to display",
            min_value=5,
            max_value=100,
            value=20000,
            key="processed_rows"
        )


        st.dataframe(
            processed_df.head(rows),
            use_container_width=True
        )


        st.write("### Missing Values After Processing")

        missing_after = pd.DataFrame({
            "Column Name": processed_df.columns,
            "Missing Values": processed_df.isnull().sum().values
        })


        st.dataframe(
            missing_after,
            use_container_width=True
        )


        st.success("""
        ✅ Dataset cleaning completed successfully.

        The processed dataset is now ready for:
        - Exploratory Data Analysis (EDA)
        - Data Visualization
        - Accident Pattern Analysis
        - Statistical Analysis
        """)

    # ==========================================================
    # Summary
    # ==========================================================
    with t5:

        st.subheader("📊 Processing Summary")

        processed_df = df.copy()

        processed_df.drop(columns=["festival"], inplace=True)
        processed_df.dropna(inplace=True)
        processed_df.reset_index(drop=True, inplace=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Rows", processed_df.shape[0])

        with col2:
            st.metric("Columns", processed_df.shape[1])

        with col3:
            st.metric("Missing Values", processed_df.isnull().sum().sum())

        st.write("### Missing Values After Processing")

        st.dataframe(
            pd.DataFrame({
                "Column": processed_df.columns,
                "Missing Values": processed_df.isnull().sum().values
            }),
            use_container_width=True
        )
###############################################################################################################

elif opt == "Visualization":
    st.title("Visualization") 


    st.markdown(""" Visualization is the graphical representation of data using charts, graphs, and plots. 
                It helps to identify patterns, trends, and relationships in data. In this project, visualization is used to 
                analyze road accident patterns and understand factors like location, weather, severity, and traffic conditions.""")
    # Main Tabs
    tab_state, tab_city, tab_weather, tab_road, tab_severity, tab_month, tab_vehicle = st.tabs([
        "Accidents by State",
        "Accidents by City",
        "Accidents by Weather",
        "Accidents by Road Type",
        "Severity Distribution",
        "Monthly Trend",
        "Vehicle Type Analysis"
    ])
    
    # ---------------- STATE ANALYSIS TABS ----------------
    with tab_state:
        st.subheader(" state-wise Accident Analysis")

        st.info("""
        The State-wise Analysis provides a comprehensive overview of road accidents
        across different states. It examines accident counts, severity levels,
        casualties, average risk scores, weather impact, road types, traffic
        conditions, and time-based accident trends. This analysis helps identify
        high-risk regions and supports effective road safety strategies,
        resource allocation, and policy planning.
        """)

        state_tab1, state_tab2, state_tab3, state_tab4, state_tab5, state_tab6, state_tab7 = st.tabs([
            "Accident Count",
            "Risk Score",
            "Casualties",
            "Vehicles Involved",
            "Temperature",
            "Lanes",
            "Accident Hour"
        ])


        # ==========================================================
        # TAB 1 : STATE VS ACCIDENT COUNT
        # ==========================================================
        with state_tab1:

            st.subheader("📊 State-wise Accident Distribution")

            rows = st.slider(
                "Select number of states to display",
                min_value=5,
                max_value=len(df["state"].unique()),
                value=10,
                key="state_pie_slider"
            )

            state_acc = df.groupby("state").size().reset_index(
                name="Accidents"
            )

            state_acc = state_acc.sort_values(
                by="Accidents",
                ascending=False
            ).head(rows)


            st.dataframe(
                state_acc,
                use_container_width=True
            )


            fig = px.pie(
                state_acc,
                names="state",
                values="Accidents",
                hole=0.45,
                title=f"🚦 Top {rows} States - Accident Contribution",
                color_discrete_sequence=px.colors.sequential.RdBu
            )


            fig.update_traces(
                textinfo="percent+label",
                hovertemplate=
                "<b>State:</b> %{label}<br>" +
                "<b>Accidents:</b> %{value}<br>" +
                "<b>Percentage:</b> %{percent}"
            )


            fig.update_layout(
                title={
                    "text": f"🚦 Top {rows} States - Accident Contribution",
                    "x":0.5,
                    "font": {
                        "size":22,
                        "family":"Arial Black"
                    }
                },
                template="plotly_dark",
                height=600
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # ==========================================================
        # TAB 2 : STATE VS RISK SCORE
        # ==========================================================
        with state_tab2:

            st.subheader("📈 State vs Average Risk Score")

            rows = st.slider(
                "Select number of states to display",
                min_value=5,
                max_value=len(df["state"].unique()),
                value=len(df["state"].unique()),
                key="risk_slider"
            )

            risk = df.groupby("state")["risk_score"].mean().reset_index()

            risk = risk.sort_values(
                by="risk_score",
                ascending=False
            ).head(rows)


            st.dataframe(
                risk,
                use_container_width=True
            )


            fig = px.bar(
                risk,
                x="risk_score",
                y="state",
                orientation="h",
                color="risk_score",
                title=f"Top {rows} States by Average Risk Score",
                text="risk_score"
            )

            fig.update_traces(
                texttemplate="%{text:.2f}",
                textposition="outside"
            )

            fig.update_layout(
                xaxis_title="Average Risk Score",
                yaxis_title="State",
                height=600
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # ==========================================================
        # TAB 3 : STATE VS CASUALTIES
        # ==========================================================
        with state_tab3:

            st.subheader("🚑 State vs Total Casualties")


            rows = st.slider(
                "Select number of states to display",
                min_value=5,
                max_value=len(df["state"].unique()),
                value=len(df["state"].unique()),
                key="casualty_slider"
            )


            cas = df.groupby("state")["casualties"].sum().reset_index()


            cas = cas.sort_values(
                by="casualties",
                ascending=False
            ).head(rows)


            st.dataframe(
                cas,
                use_container_width=True
            )


            fig = px.bar(
                cas,
                x="state",
                y="casualties",
                color="casualties",
                title=f"Top {rows} States - Total Casualties"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # ==========================================================
        # TAB 4 : VEHICLES INVOLVED
        # ==========================================================
        with state_tab4:

            st.subheader("🚗 State vs Average Vehicles Involved")


            rows = st.slider(
                "Select number of states to display",
                min_value=5,
                max_value=len(df["state"].unique()),
                value=len(df["state"].unique()),
                key="vehicle_slider"
            )


            veh = df.groupby("state")["vehicles_involved"].mean().reset_index()


            veh = veh.sort_values(
                by="vehicles_involved",
                ascending=False
            ).head(rows)


            st.dataframe(
                veh,
                use_container_width=True
            )


            fig = px.bar(
                veh,
                x="state",
                y="vehicles_involved",
                color="vehicles_involved",
                title=f"Top {rows} States - Average Vehicles Involved"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # ==========================================================
        # TAB 5 : TEMPERATURE
        # ==========================================================
        with state_tab5:

            st.subheader("🌡️ State vs Average Temperature")


            rows = st.slider(
                "Select number of states to display",
                min_value=5,
                max_value=len(df["state"].unique()),
                value=len(df["state"].unique()),
                key="temperature_slider"
            )


            temp = df.groupby("state")["temperature"].mean().reset_index()


            temp = temp.head(rows)


            st.dataframe(
                temp,
                use_container_width=True
            )


            fig = px.line(
                temp,
                x="state",
                y="temperature",
                markers=True,
                title=f"Top {rows} States - Average Temperature"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # ==========================================================
        # TAB 6 : LANES
        # ==========================================================
        with state_tab6:

            st.subheader("🛣️ State vs Average Number of Lanes")


            rows = st.slider(
                "Select number of states to display",
                min_value=5,
                max_value=len(df["state"].unique()),
                value=len(df["state"].unique()),
                key="lane_slider"
            )


            lane = df.groupby("state")["lanes"].mean().reset_index()


            lane = lane.sort_values(
                by="lanes",
                ascending=False
            ).head(rows)


            st.dataframe(
                lane,
                use_container_width=True
            )


            fig = px.bar(
                lane,
                x="state",
                y="lanes",
                color="lanes",
                title=f"Top {rows} States - Average Number of Lanes"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # ==========================================================
        # TAB 7 : ACCIDENT HOUR
        # ==========================================================
        with state_tab7:

            st.subheader("⏰ State vs Average Accident Hour")


            rows = st.slider(
                "Select number of states to display",
                min_value=5,
                max_value=len(df["state"].unique()),
                value=len(df["state"].unique()),
                key="hour_slider"
            )


            hr = df.groupby("state")["hour"].mean().reset_index()


            hr = hr.sort_values(
                by="hour",
                ascending=False
            ).head(rows)


            st.dataframe(
                hr,
                use_container_width=True
            )


            fig = px.scatter(
                hr,
                x="state",
                y="hour",
                color="hour",
                size="hour",
                title=f"Top {rows} States - Average Accident Hour"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )
    # ================= CITY =================
        with tab_city:

            st.subheader("🏙️ City-wise Accident Analysis")

            st.info("""
            This section analyzes accident patterns across different cities.
            It provides insights into accident frequency, risk score, casualties,
            vehicle involvement, weather conditions, road infrastructure, and
            peak hour accident patterns.
            """)


            city_tab1, city_tab2, city_tab3, city_tab4, city_tab5, city_tab6, city_tab7 = st.tabs([
                "Accident Count",
                "Risk Score",
                "Casualties",
                "Vehicles",
                "Temperature",
                "Lanes",
                "Peak Hour"
            ])


            # =====================================================
            # TAB 1 - ACCIDENT COUNT
            # =====================================================
            with city_tab1:

                st.subheader("📊 City vs Accident Count")

                rows = st.slider(
                    "Select number of cities",
                    5,
                    df["city"].nunique(),
                    15,
                    key="city_accident_slider"
                )

                city = df.groupby("city").size().reset_index(name="Accidents")

                city = city.sort_values(
                    "Accidents",
                    ascending=False
                ).head(rows)


                st.dataframe(
                    city,
                    use_container_width=True
                )


                fig = px.treemap(
                    city,
                    path=["city"],
                    values="Accidents",
                    color="Accidents",
                    title=f"Top {rows} Cities by Accident Count"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )


            # =====================================================
            # TAB 2 - RISK SCORE
            # =====================================================
            with city_tab2:

                st.subheader("📈 City vs Average Risk Score")


                rows = st.slider(
                    "Select number of cities",
                    5,
                    df["city"].nunique(),
                    15,
                    key="city_risk_slider"
                )


                risk = df.groupby("city")["risk_score"].mean().reset_index()


                risk = risk.sort_values(
                    "risk_score",
                    ascending=False
                ).head(rows)


                st.dataframe(
                    risk,
                    use_container_width=True
                )


                fig = px.bar(
                    risk,
                    x="city",
                    y="risk_score",
                    color="risk_score",
                    title=f"Top {rows} Cities by Average Risk Score"
                )


                st.plotly_chart(
                    fig,
                    use_container_width=True
                )


            # =====================================================
            # TAB 3 - CASUALTIES
            # =====================================================
            with city_tab3:

                st.subheader("🚑 City vs Total Casualties")


                rows = st.slider(
                    "Select number of cities",
                    5,
                    df["city"].nunique(),
                    15,
                    key="city_casualty_slider"
                )


                cas = df.groupby("city")["casualties"].sum().reset_index()


                cas = cas.sort_values(
                    "casualties",
                    ascending=False
                ).head(rows)


                st.dataframe(
                    cas,
                    use_container_width=True
                )


                fig = px.scatter(
                    cas,
                    x="city",
                    y="casualties",
                    size="casualties",
                    color="casualties",
                    title=f"Top {rows} Cities by Casualties"
                )


                st.plotly_chart(
                    fig,
                    use_container_width=True
                )


            # =====================================================
            # TAB 4 - VEHICLES
            # =====================================================
            with city_tab4:

                st.subheader("🚗 City vs Average Vehicles Involved")


                rows = st.slider(
                    "Select number of cities",
                    5,
                    df["city"].nunique(),
                    15,
                    key="city_vehicle_slider"
                )


                veh = df.groupby("city")["vehicles_involved"].mean().reset_index()


                veh = veh.sort_values(
                    "vehicles_involved",
                    ascending=False
                ).head(rows)


                st.dataframe(
                    veh,
                    use_container_width=True
                )


                fig = px.bar(
                    veh,
                    x="city",
                    y="vehicles_involved",
                    color="vehicles_involved",
                    title=f"Top {rows} Cities - Average Vehicles Involved"
                )


                st.plotly_chart(
                    fig,
                    use_container_width=True
                )


            # =====================================================
            # TAB 5 - TEMPERATURE
            # =====================================================
            with city_tab5:

                st.subheader("🌡️ City vs Average Temperature")


                rows = st.slider(
                    "Select number of cities",
                    5,
                    df["city"].nunique(),
                    15,
                    key="city_temp_slider"
                )


                temp = df.groupby("city")["temperature"].mean().reset_index()


                temp = temp.head(rows)


                st.dataframe(
                    temp,
                    use_container_width=True
                )


                fig = px.line(
                    temp,
                    x="city",
                    y="temperature",
                    markers=True,
                    title=f"Top {rows} Cities - Average Temperature"
                )


                st.plotly_chart(
                    fig,
                    use_container_width=True
                )


            # =====================================================
            # TAB 6 - LANES
            # =====================================================
            with city_tab6:

                st.subheader("🛣️ City vs Lane Distribution")


                rows = st.slider(
                    "Select number of cities",
                    5,
                    df["city"].nunique(),
                    15,
                    key="city_lane_slider"
                )


                lane = df.groupby("city")["lanes"].mean().reset_index()


                lane = lane.sort_values(
                    "lanes",
                    ascending=False
                ).head(rows)


                st.dataframe(
                    lane,
                    use_container_width=True
                )


                fig = px.bar(
                    lane,
                    x="city",
                    y="lanes",
                    color="lanes",
                    title=f"Top {rows} Cities - Average Number of Lanes"
                )


                st.plotly_chart(
                    fig,
                    use_container_width=True
                )


            # =====================================================
            # TAB 7 - PEAK HOUR
            # =====================================================
            with city_tab7:

                st.subheader("⏰ City vs Peak Hour Accidents")


                rows = st.slider(
                    "Select number of cities",
                    5,
                    df["city"].nunique(),
                    15,
                    key="city_peak_slider"
                )


                peak = df.groupby(
                    ["city", "is_peak_hour"]
                ).size().reset_index(name="Count")


                top_city = (
                    df.groupby("city")
                    .size()
                    .reset_index(name="Total")
                    .sort_values("Total", ascending=False)
                    .head(rows)["city"]
                )


                peak = peak[
                    peak["city"].isin(top_city)
                ]


                fig = px.sunburst(
                    peak,
                    path=["city", "is_peak_hour"],
                    values="Count",
                    title=f"Top {rows} Cities - Peak Hour Accident Analysis"
                )


                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

    # ================= WEATHER =================
    with tab_weather:

        st.subheader("🌦️ Weather Analysis")

        st.markdown("""
        The Weather-wise Accident Analysis examines the relationship between different
        weather conditions and road accidents. It identifies how weather conditions
        influence accident frequency, severity, casualties, vehicle involvement,
        risk score, traffic density, and road type. These insights help in improving
        road safety strategies and preparing preventive measures during adverse
        weather conditions.
        """)


        weather_tab1, weather_tab2, weather_tab3, weather_tab4, weather_tab5, weather_tab6, weather_tab7 = st.tabs([
            "Accident Count",
            "Severity",
            "Risk Score",
            "Casualties",
            "Vehicles",
            "Traffic Density",
            "Road Type"
        ])



        # =====================================================
        # TAB 1 - ACCIDENT COUNT
        # =====================================================
        with weather_tab1:

            st.subheader("📊 Accidents by Weather Condition")


            rows = st.slider(
                "Select number of weather conditions",
                1,
                df["weather"].nunique(),
                df["weather"].nunique(),
                key="weather_count_slider"
            )


            weather = df["weather"].value_counts().reset_index()

            weather.columns = [
                "Weather",
                "Accidents"
            ]


            weather = weather.head(rows)


            st.dataframe(
                weather,
                use_container_width=True
            )


            fig = px.pie(
                weather,
                names="Weather",
                values="Accidents",
                hole=0.4,
                title=f"Top {rows} Weather Conditions - Accident Count"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 2 - SEVERITY
        # =====================================================
        with weather_tab2:

            st.subheader("⚠️ Weather vs Accident Severity")


            rows = st.slider(
                "Select number of weather conditions",
                1,
                df["weather"].nunique(),
                df["weather"].nunique(),
                key="weather_severity_slider"
            )


            severity = (
                df.groupby(
                    ["weather", "accident_severity"]
                )
                .size()
                .reset_index(name="Count")
            )


            top_weather = (
                df["weather"]
                .value_counts()
                .head(rows)
                .index
            )


            severity = severity[
                severity["weather"].isin(top_weather)
            ]


            fig = px.sunburst(
                severity,
                path=[
                    "weather",
                    "accident_severity"
                ],
                values="Count",
                title="Weather vs Accident Severity"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 3 - RISK SCORE
        # =====================================================
        with weather_tab3:

            st.subheader("📈 Average Risk Score by Weather")


            rows = st.slider(
                "Select number of weather conditions",
                1,
                df["weather"].nunique(),
                df["weather"].nunique(),
                key="weather_risk_slider"
            )


            risk = (
                df.groupby("weather")["risk_score"]
                .mean()
                .reset_index()
            )


            risk = (
                risk.sort_values(
                    "risk_score",
                    ascending=False
                )
                .head(rows)
            )


            st.dataframe(
                risk,
                use_container_width=True
            )


            fig = px.bar(
                risk,
                x="weather",
                y="risk_score",
                color="risk_score",
                title="Average Risk Score by Weather"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 4 - CASUALTIES
        # =====================================================
        with weather_tab4:

            st.subheader("🚑 Casualties by Weather")


            rows = st.slider(
                "Select number of weather conditions",
                1,
                df["weather"].nunique(),
                df["weather"].nunique(),
                key="weather_casualty_slider"
            )


            cas = (
                df.groupby("weather")["casualties"]
                .sum()
                .reset_index()
            )


            cas = (
                cas.sort_values(
                    "casualties",
                    ascending=False
                )
                .head(rows)
            )


            st.dataframe(
                cas,
                use_container_width=True
            )


            fig = px.bar(
                cas,
                x="weather",
                y="casualties",
                color="casualties",
                title="Total Casualties by Weather"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 5 - VEHICLES
        # =====================================================
        with weather_tab5:

            st.subheader("🚗 Vehicles Involved by Weather")


            rows = st.slider(
                "Select number of weather conditions",
                1,
                df["weather"].nunique(),
                df["weather"].nunique(),
                key="weather_vehicle_slider"
            )


            veh = (
                df.groupby("weather")["vehicles_involved"]
                .mean()
                .reset_index()
            )


            veh = (
                veh.sort_values(
                    "vehicles_involved",
                    ascending=False
                )
                .head(rows)
            )


            st.dataframe(
                veh,
                use_container_width=True
            )


            fig = px.bar(
                veh,
                x="weather",
                y="vehicles_involved",
                color="vehicles_involved",
                title="Average Vehicles Involved by Weather"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 6 - TRAFFIC DENSITY
        # =====================================================
        with weather_tab6:

            st.subheader("🚦 Traffic Density by Weather")


            rows = st.slider(
                "Select number of weather conditions",
                1,
                df["weather"].nunique(),
                df["weather"].nunique(),
                key="weather_traffic_slider"
            )


            traffic = (
                df.groupby(
                    ["weather", "traffic_density"]
                )
                .size()
                .reset_index(name="Count")
            )


            top_weather = (
                df["weather"]
                .value_counts()
                .head(rows)
                .index
            )


            traffic = traffic[
                traffic["weather"].isin(top_weather)
            ]


            fig = px.treemap(
                traffic,
                path=[
                    "weather",
                    "traffic_density"
                ],
                values="Count",
                color="Count",
                title="Traffic Density by Weather"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 7 - ROAD TYPE
        # =====================================================
        with weather_tab7:

            st.subheader("🛣️ Road Type Distribution Across Weather")


            rows = st.slider(
                "Select number of weather conditions",
                1,
                df["weather"].nunique(),
                df["weather"].nunique(),
                key="weather_road_slider"
            )


            road = (
                df.groupby(
                    ["road_type", "weather"]
                )
                .size()
                .reset_index(name="Count")
            )


            top_weather = (
                df["weather"]
                .value_counts()
                .head(rows)
                .index
            )


            road = road[
                road["weather"].isin(top_weather)
            ]


            fig = px.bar(
                road,
                x="road_type",
                y="Count",
                color="weather",
                barmode="group",
                title="Road Type Distribution Across Weather Conditions"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )
                    
    # ================= ROAD TYPE =================
    with tab_road:

        st.subheader("🛣️ Road Type Analysis")

        st.markdown("""
        The Road Type Analysis examines how different road infrastructures affect
        accident patterns. It analyzes accident count, severity, risk score,
        casualties, vehicle involvement, traffic density, and weather impact.
        These insights help understand which road types require better planning,
        safety improvements, and preventive measures.
        """)


        road_tab1, road_tab2, road_tab3, road_tab4, road_tab5, road_tab6, road_tab7 = st.tabs([
            "Accident Count",
            "Severity",
            "Risk Score",
            "Casualties",
            "Vehicles",
            "Traffic Density",
            "Weather Impact"
        ])



        # =====================================================
        # TAB 1 - ACCIDENT COUNT
        # =====================================================
        with road_tab1:

            st.subheader("📊 Accidents by Road Type")


            rows = st.slider(
                "Select number of road types",
                1,
                df["road_type"].nunique(),
                df["road_type"].nunique(),
                key="road_count_slider"
            )


            road = df["road_type"].value_counts().reset_index()

            road.columns = [
                "Road Type",
                "Accidents"
            ]


            road = road.head(rows)


            st.dataframe(
                road,
                use_container_width=True
            )


            fig = px.pie(
                road,
                names="Road Type",
                values="Accidents",
                hole=0.5,
                title=f"Top {rows} Road Types - Accident Count"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 2 - SEVERITY
        # =====================================================
        with road_tab2:

            st.subheader("⚠️ Road Type vs Accident Severity")


            rows = st.slider(
                "Select number of road types",
                1,
                df["road_type"].nunique(),
                df["road_type"].nunique(),
                key="road_severity_slider"
            )


            severity = (
                df.groupby(
                    ["road_type","accident_severity"]
                )
                .size()
                .reset_index(name="Count")
            )


            top_road = (
                df["road_type"]
                .value_counts()
                .head(rows)
                .index
            )


            severity = severity[
                severity["road_type"].isin(top_road)
            ]


            fig = px.sunburst(
                severity,
                path=[
                    "road_type",
                    "accident_severity"
                ],
                values="Count",
                title="Road Type vs Accident Severity"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 3 - RISK SCORE
        # =====================================================
        with road_tab3:

            st.subheader("📈 Average Risk Score by Road Type")


            rows = st.slider(
                "Select number of road types",
                1,
                df["road_type"].nunique(),
                df["road_type"].nunique(),
                key="road_risk_slider"
            )


            risk = (
                df.groupby("road_type")["risk_score"]
                .mean()
                .reset_index()
            )


            risk = (
                risk.sort_values(
                    "risk_score",
                    ascending=False
                )
                .head(rows)
            )


            st.dataframe(
                risk,
                use_container_width=True
            )


            fig = px.bar(
                risk,
                x="road_type",
                y="risk_score",
                color="risk_score",
                title="Average Risk Score by Road Type"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 4 - CASUALTIES
        # =====================================================
        with road_tab4:

            st.subheader("🚑 Casualties Distribution by Road Type")


            rows = st.slider(
                "Select number of road types",
                1,
                df["road_type"].nunique(),
                df["road_type"].nunique(),
                key="road_casualty_slider"
            )


            cas = (
                df.groupby("road_type")["casualties"]
                .sum()
                .reset_index()
            )


            cas = (
                cas.sort_values(
                    "casualties",
                    ascending=False
                )
                .head(rows)
            )


            st.dataframe(
                cas,
                use_container_width=True
            )


            fig = px.box(
                df[
                    df["road_type"].isin(
                        cas["road_type"]
                    )
                ],
                x="road_type",
                y="casualties",
                color="road_type",
                title="Casualties Distribution by Road Type"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 5 - VEHICLES
        # =====================================================
        with road_tab5:

            st.subheader("🚗 Vehicles Involved by Road Type")


            rows = st.slider(
                "Select number of road types",
                1,
                df["road_type"].nunique(),
                df["road_type"].nunique(),
                key="road_vehicle_slider"
            )


            veh = (
                df.groupby("road_type")["vehicles_involved"]
                .mean()
                .reset_index()
            )


            veh = (
                veh.sort_values(
                    "vehicles_involved",
                    ascending=False
                )
                .head(rows)
            )


            fig = px.violin(
                df[
                    df["road_type"].isin(
                        veh["road_type"]
                    )
                ],
                x="road_type",
                y="vehicles_involved",
                color="road_type",
                box=True,
                title="Vehicles Involved by Road Type"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 6 - TRAFFIC DENSITY
        # =====================================================
        with road_tab6:

            st.subheader("🚦 Traffic Density Across Road Types")


            rows = st.slider(
                "Select number of road types",
                1,
                df["road_type"].nunique(),
                df["road_type"].nunique(),
                key="road_traffic_slider"
            )


            traffic = (
                df.groupby(
                    [
                        "road_type",
                        "traffic_density"
                    ]
                )
                .size()
                .reset_index(name="Count")
            )


            top_road = (
                df["road_type"]
                .value_counts()
                .head(rows)
                .index
            )


            traffic = traffic[
                traffic["road_type"].isin(top_road)
            ]


            fig = px.treemap(
                traffic,
                path=[
                    "road_type",
                    "traffic_density"
                ],
                values="Count",
                color="Count",
                title="Traffic Density Across Road Types"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 7 - WEATHER IMPACT
        # =====================================================
        with road_tab7:

            st.subheader("🌦️ Weather Impact Across Road Types")


            rows = st.slider(
                "Select number of road types",
                1,
                df["road_type"].nunique(),
                df["road_type"].nunique(),
                key="road_weather_slider"
            )


            weather = (
                df.groupby(
                    [
                        "road_type",
                        "weather"
                    ]
                )
                .size()
                .reset_index(name="Count")
            )


            top_road = (
                df["road_type"]
                .value_counts()
                .head(rows)
                .index
            )


            weather = weather[
                weather["road_type"].isin(top_road)
            ]


            fig = px.bar(
                weather,
                x="road_type",
                y="Count",
                color="weather",
                barmode="group",
                title="Weather Impact Across Road Types"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )
    # ================= SEVERITY =================
    with tab_severity:

        st.subheader("⚠️ Accident Severity Distribution")

        st.markdown("""
        The Accident Severity Distribution analysis focuses on understanding the
        impact level of road accidents. It examines severity categories along with
        casualties, risk score, weather conditions, road types, and vehicle
        involvement. These insights help identify accident patterns and support
        effective road safety planning.
        """)


        severity_tab1, severity_tab2, severity_tab3, severity_tab4, severity_tab5, severity_tab6, severity_tab7 = st.tabs([
            "Severity Count",
            "Severity Percentage",
            "Risk Score",
            "Casualties",
            "Weather Impact",
            "Road Type Impact",
            "Vehicle Impact"
        ])



        # =====================================================
        # TAB 1 - SEVERITY COUNT
        # =====================================================
        with severity_tab1:

            st.subheader("📊 Accident Severity Distribution")


            rows = st.slider(
                "Select number of severity categories",
                1,
                df["accident_severity"].nunique(),
                df["accident_severity"].nunique(),
                key="severity_count_slider"
            )


            severity = (
                df["accident_severity"]
                .value_counts()
                .reset_index()
            )

            severity.columns = [
                "Severity",
                "Count"
            ]


            severity = severity.head(rows)


            st.dataframe(
                severity,
                use_container_width=True
            )


            fig = px.pie(
                severity,
                names="Severity",
                values="Count",
                hole=0.5,
                title="Accident Severity Distribution"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 2 - SEVERITY PERCENTAGE
        # =====================================================
        with severity_tab2:

            st.subheader("📈 Severity Level Comparison")


            rows = st.slider(
                "Select number of severity categories",
                1,
                df["accident_severity"].nunique(),
                df["accident_severity"].nunique(),
                key="severity_percentage_slider"
            )


            severity = (
                df["accident_severity"]
                .value_counts()
                .reset_index()
            )

            severity.columns = [
                "Severity",
                "Count"
            ]


            severity = severity.head(rows)


            severity["Percentage"] = (
                severity["Count"] /
                severity["Count"].sum()
                * 100
            ).round(2)


            st.dataframe(
                severity,
                use_container_width=True
            )


            fig = px.funnel(
                severity,
                x="Count",
                y="Severity",
                title="Severity Level Comparison"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 3 - RISK SCORE
        # =====================================================
        with severity_tab3:

            st.subheader("📈 Risk Score Distribution by Severity")


            rows = st.slider(
                "Select number of severity categories",
                1,
                df["accident_severity"].nunique(),
                df["accident_severity"].nunique(),
                key="severity_risk_slider"
            )


            top_severity = (
                df["accident_severity"]
                .value_counts()
                .head(rows)
                .index
            )


            data = df[
                df["accident_severity"]
                .isin(top_severity)
            ]


            fig = px.violin(
                data,
                x="accident_severity",
                y="risk_score",
                color="accident_severity",
                box=True,
                title="Risk Score Distribution by Severity"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 4 - CASUALTIES
        # =====================================================
        with severity_tab4:

            st.subheader("🚑 Casualties Based on Severity")


            rows = st.slider(
                "Select number of severity categories",
                1,
                df["accident_severity"].nunique(),
                df["accident_severity"].nunique(),
                key="severity_casualty_slider"
            )


            cas = (
                df.groupby(
                    "accident_severity"
                )["casualties"]
                .sum()
                .reset_index()
            )


            cas = cas.sort_values(
                "casualties",
                ascending=False
            ).head(rows)


            st.dataframe(
                cas,
                use_container_width=True
            )


            fig = px.box(
                df[
                    df["accident_severity"]
                    .isin(cas["accident_severity"])
                ],
                x="accident_severity",
                y="casualties",
                color="accident_severity",
                title="Casualties Based on Accident Severity"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 5 - WEATHER IMPACT
        # =====================================================
        with severity_tab5:

            st.subheader("🌦️ Weather Impact on Accident Severity")


            rows = st.slider(
                "Select number of weather conditions",
                1,
                df["weather"].nunique(),
                df["weather"].nunique(),
                key="severity_weather_slider"
            )


            weather = (
                df.groupby(
                    [
                        "accident_severity",
                        "weather"
                    ]
                )
                .size()
                .reset_index(name="Count")
            )


            top_weather = (
                df["weather"]
                .value_counts()
                .head(rows)
                .index
            )


            weather = weather[
                weather["weather"]
                .isin(top_weather)
            ]


            fig = px.sunburst(
                weather,
                path=[
                    "accident_severity",
                    "weather"
                ],
                values="Count",
                title="Weather Impact on Accident Severity"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 6 - ROAD TYPE IMPACT
        # =====================================================
        with severity_tab6:

            st.subheader("🛣️ Road Type Impact on Severity")


            rows = st.slider(
                "Select number of road types",
                1,
                df["road_type"].nunique(),
                df["road_type"].nunique(),
                key="severity_road_slider"
            )


            road = (
                df.groupby(
                    [
                        "accident_severity",
                        "road_type"
                    ]
                )
                .agg(
                    casualties=("casualties","sum"),
                    risk_score=("risk_score","mean")
                )
                .reset_index()
            )


            top_road = (
                df["road_type"]
                .value_counts()
                .head(rows)
                .index
            )


            road = road[
                road["road_type"]
                .isin(top_road)
            ]


            fig = px.treemap(
                road,
                path=[
                    "accident_severity",
                    "road_type"
                ],
                values="casualties",
                color="risk_score",
                title="Road Type Impact on Accident Severity"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 7 - VEHICLE IMPACT
        # =====================================================
        with severity_tab7:

            st.subheader("🚗 Vehicle Involvement vs Severity")


            rows = st.slider(
                "Select number of severity categories",
                1,
                df["accident_severity"].nunique(),
                df["accident_severity"].nunique(),
                key="severity_vehicle_slider"
            )


            top_severity = (
                df["accident_severity"]
                .value_counts()
                .head(rows)
                .index
            )


            data = df[
                df["accident_severity"]
                .isin(top_severity)
            ]


            fig = px.scatter(
                data,
                x="vehicles_involved",
                y="casualties",
                color="accident_severity",
                size="risk_score",
                hover_name="city",
                title="Vehicle Involvement vs Accident Severity"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )
    # ================= MONTH =================
    with tab_month:

        st.subheader("📅 Monthly Accident Trend Analysis")

        st.markdown("""
        The Monthly Trend Analysis shows how road accidents change across different
        months and years. It identifies seasonal patterns, accident peaks, severity
        trends, casualties, risk score variations, weather influence, and yearly
        comparisons to support better road safety planning.
        """)


        month_tab1, month_tab2, month_tab3, month_tab4, month_tab5, month_tab6, month_tab7 = st.tabs([
            "Accident Trend",
            "Severity Trend",
            "Monthly Distribution",
            "Casualties Trend",
            "Risk Score",
            "Weather Impact",
            "Year Comparison"
        ])


        # =====================================================
        # TAB 1 - ACCIDENT TREND
        # =====================================================
        with month_tab1:

            st.subheader("📈 Monthly Accident Trend")


            months = df["month"].unique()

            rows = st.slider(
                "Select number of months",
                1,
                len(months),
                len(months),
                key="month_trend_slider"
            )


            monthly = (
                df.groupby("month")
                .size()
                .reset_index(name="Accidents")
            )


            monthly = monthly.head(rows)


            st.dataframe(
                monthly,
                use_container_width=True
            )


            fig = px.line(
                monthly,
                x="month",
                y="Accidents",
                markers=True,
                title="Monthly Accident Trend"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 2 - SEVERITY TREND
        # =====================================================
        with month_tab2:

            st.subheader("⚠️ Monthly Accident Severity Trend")


            rows = st.slider(
                "Select number of months",
                1,
                df["month"].nunique(),
                df["month"].nunique(),
                key="severity_month_slider"
            )


            severity_month = (
                df.groupby(
                    [
                        "month",
                        "accident_severity"
                    ]
                )
                .size()
                .reset_index(name="Count")
            )


            top_month = (
                df["month"]
                .value_counts()
                .head(rows)
                .index
            )


            severity_month = severity_month[
                severity_month["month"]
                .isin(top_month)
            ]


            fig = px.area(
                severity_month,
                x="month",
                y="Count",
                color="accident_severity",
                title="Monthly Accident Severity Trend"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 3 - MONTHLY DISTRIBUTION
        # =====================================================
        with month_tab3:

            st.subheader("📊 Monthly Accident Distribution")


            rows = st.slider(
                "Select number of months",
                1,
                df["month"].nunique(),
                df["month"].nunique(),
                key="monthly_distribution_slider"
            )


            monthly = (
                df["month"]
                .value_counts()
                .reset_index()
            )

            monthly.columns = [
                "Month",
                "Accidents"
            ]


            monthly = monthly.head(rows)


            st.dataframe(
                monthly,
                use_container_width=True
            )


            fig = px.pie(
                monthly,
                names="Month",
                values="Accidents",
                hole=0.5,
                title="Monthly Accident Distribution"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 4 - CASUALTIES TREND
        # =====================================================
        with month_tab4:

            st.subheader("🚑 Monthly Casualties Distribution")


            rows = st.slider(
                "Select number of months",
                1,
                df["month"].nunique(),
                df["month"].nunique(),
                key="monthly_casualty_slider"
            )


            casualty_month = (
                df.groupby("month")["casualties"]
                .sum()
                .reset_index()
            )


            casualty_month = (
                casualty_month
                .sort_values(
                    "casualties",
                    ascending=False
                )
                .head(rows)
            )


            st.dataframe(
                casualty_month,
                use_container_width=True
            )


            fig = px.bar(
                casualty_month,
                x="month",
                y="casualties",
                color="casualties",
                title="Monthly Total Casualties"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 5 - RISK SCORE
        # =====================================================
        with month_tab5:

            st.subheader("📌 Average Risk Score by Month")


            rows = st.slider(
                "Select number of months",
                1,
                df["month"].nunique(),
                df["month"].nunique(),
                key="monthly_risk_slider"
            )


            risk = (
                df.groupby("month")["risk_score"]
                .mean()
                .reset_index()
            )


            risk = (
                risk.sort_values(
                    "risk_score",
                    ascending=False
                )
                .head(rows)
            )


            st.dataframe(
                risk,
                use_container_width=True
            )


            fig = px.scatter(
                risk,
                x="month",
                y="risk_score",
                size="risk_score",
                color="risk_score",
                title="Average Risk Score by Month"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 6 - WEATHER IMPACT
        # =====================================================
        with month_tab6:

            st.subheader("🌦️ Weather Impact by Month")


            rows = st.slider(
                "Select number of months",
                1,
                df["month"].nunique(),
                df["month"].nunique(),
                key="month_weather_slider"
            )


            weather = (
                df.groupby(
                    [
                        "month",
                        "weather"
                    ]
                )
                .size()
                .reset_index(name="Count")
            )


            top_month = (
                df["month"]
                .value_counts()
                .head(rows)
                .index
            )


            weather = weather[
                weather["month"]
                .isin(top_month)
            ]


            fig = px.sunburst(
                weather,
                path=[
                    "month",
                    "weather"
                ],
                values="Count",
                title="Weather Impact by Month"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 7 - YEAR COMPARISON
        # =====================================================
        with month_tab7:

            st.subheader("📆 Year-wise Accident Comparison")


            rows = st.slider(
                "Select number of years",
                1,
                df["year"].nunique(),
                df["year"].nunique(),
                key="year_slider"
            )


            year_data = (
                df.groupby("year")
                .size()
                .reset_index(name="Accidents")
            )


            year_data = year_data.head(rows)


            st.dataframe(
                year_data,
                use_container_width=True
            )


            fig = px.bar(
                year_data,
                x="year",
                y="Accidents",
                color="Accidents",
                title="Year-wise Accident Comparison"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )
    # ================= VEHICLE =================
    with tab_vehicle:

        st.subheader("🚗 Vehicle Involvement Analysis")

        st.markdown("""
        The Vehicle Involvement Analysis examines how the number of vehicles involved
        affects accident patterns. It analyzes accident frequency, severity,
        casualties, risk score, weather conditions, road types, and traffic density.
        These insights help understand multi-vehicle accident patterns and support
        better road safety planning.
        """)


        vehicle_tab1, vehicle_tab2, vehicle_tab3, vehicle_tab4, vehicle_tab5, vehicle_tab6, vehicle_tab7 = st.tabs([
            "Accident Count",
            "Severity",
            "Casualties",
            "Risk Score",
            "Weather Impact",
            "Road Type",
            "Traffic Density"
        ])



        # =====================================================
        # TAB 1 - ACCIDENT COUNT
        # =====================================================
        with vehicle_tab1:

            st.subheader("📊 Distribution of Vehicles Involved")


            max_vehicle = int(
                df["vehicles_involved"].max()
            )


            vehicle_limit = st.slider(
                "Select maximum number of vehicles involved",
                1,
                max_vehicle,
                max_vehicle,
                key="vehicle_count_slider"
            )


            data = df[
                df["vehicles_involved"] <= vehicle_limit
            ]


            vehicle_count = (
                data["vehicles_involved"]
                .value_counts()
                .reset_index()
            )

            vehicle_count.columns = [
                "Vehicles",
                "Accidents"
            ]


            st.dataframe(
                vehicle_count,
                use_container_width=True
            )


            fig = px.histogram(
                data,
                x="vehicles_involved",
                color="vehicles_involved",
                title=f"Accident Distribution (Up to {vehicle_limit} Vehicles)"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 2 - SEVERITY
        # =====================================================
        with vehicle_tab2:

            st.subheader("⚠️ Vehicle Involvement vs Accident Severity")


            vehicle_limit = st.slider(
                "Select maximum vehicles involved",
                1,
                max_vehicle,
                max_vehicle,
                key="vehicle_severity_slider"
            )


            data = df[
                df["vehicles_involved"] <= vehicle_limit
            ]


            fig = px.box(
                data,
                x="vehicles_involved",
                y="casualties",
                color="vehicles_involved",
                title="Vehicles Involved vs Casualties"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 3 - CASUALTIES
        # =====================================================
        with vehicle_tab3:

            st.subheader("🚑 Vehicles Involved vs Casualties")


            vehicle_limit = st.slider(
                "Select maximum vehicles involved",
                1,
                max_vehicle,
                max_vehicle,
                key="vehicle_casualty_slider"
            )


            data = df[
                df["vehicles_involved"] <= vehicle_limit
            ]


            casualty = (
                data.groupby(
                    "vehicles_involved"
                )["casualties"]
                .sum()
                .reset_index()
            )


            fig = px.bar(
                casualty,
                x="vehicles_involved",
                y="casualties",
                color="casualties",
                title="Total Casualties by Vehicle Involvement"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 4 - RISK SCORE
        # =====================================================
        with vehicle_tab4:

            st.subheader("📈 Vehicles Involved vs Risk Score")


            vehicle_limit = st.slider(
                "Select maximum vehicles involved",
                1,
                max_vehicle,
                max_vehicle,
                key="vehicle_risk_slider"
            )


            data = df[
                df["vehicles_involved"] <= vehicle_limit
            ]


            fig = px.violin(
                data,
                x="vehicles_involved",
                y="risk_score",
                color="vehicles_involved",
                box=True,
                title="Risk Score Distribution by Vehicle Involvement"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 5 - WEATHER IMPACT
        # =====================================================
        with vehicle_tab5:

            st.subheader("🌦️ Weather Conditions by Vehicle Involvement")


            vehicle_limit = st.slider(
                "Select maximum vehicles involved",
                1,
                max_vehicle,
                max_vehicle,
                key="vehicle_weather_slider"
            )


            data = df[
                df["vehicles_involved"] <= vehicle_limit
            ]


            weather = (
                data.groupby(
                    [
                        "vehicles_involved",
                        "weather"
                    ]
                )
                .size()
                .reset_index(name="Count")
            )


            fig = px.sunburst(
                weather,
                path=[
                    "vehicles_involved",
                    "weather"
                ],
                values="Count",
                title="Weather Impact by Vehicle Involvement"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 6 - ROAD TYPE
        # =====================================================
        with vehicle_tab6:

            st.subheader("🛣️ Road Type by Vehicle Involvement")


            vehicle_limit = st.slider(
                "Select maximum vehicles involved",
                1,
                max_vehicle,
                max_vehicle,
                key="vehicle_road_slider"
            )


            data = df[
                df["vehicles_involved"] <= vehicle_limit
            ]


            road = (
                data.groupby(
                    [
                        "vehicles_involved",
                        "road_type"
                    ]
                )
                .agg(
                    casualties=("casualties","sum"),
                    risk_score=("risk_score","mean")
                )
                .reset_index()
            )


            fig = px.treemap(
                road,
                path=[
                    "vehicles_involved",
                    "road_type"
                ],
                values="casualties",
                color="risk_score",
                title="Road Type Impact by Vehicle Involvement"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        # =====================================================
        # TAB 7 - TRAFFIC DENSITY
        # =====================================================
        with vehicle_tab7:

            st.subheader("🚦 Traffic Density vs Vehicle Involvement")


            vehicle_limit = st.slider(
                "Select maximum vehicles involved",
                1,
                max_vehicle,
                max_vehicle,
                key="vehicle_traffic_slider"
            )


            data = df[
                df["vehicles_involved"] <= vehicle_limit
            ]


            fig = px.density_heatmap(
                data,
                x="vehicles_involved",
                y="traffic_density",
                title="Traffic Density vs Vehicle Involvement"
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )
##########################################################################################################################
elif opt == "Accident Map":
    map_tab = st.tabs(["🗺️ Accident Map"])[0]

    with map_tab:

        st.subheader("🗺️ India Road Accident Map")

        st.markdown("""
        This map displays the geographical distribution of road accidents
        across India using accident locations. The size and color of markers
        represent accident severity and frequency.
        """)


        # Group accident locations
        accident_map = df.groupby(
            ["state", "latitude", "longitude"]
        ).size().reset_index(name="accident_count")


        fig = px.scatter_mapbox(
            accident_map,
            lat="latitude",
            lon="longitude",
            size="accident_count",
            color="accident_count",
            hover_name="state",
            zoom=3.5,
            center={
                "lat": 22.9734,
                "lon": 78.6569
            },
            height=650,
            title="Accident Locations Across India"
        )


        fig.update_layout(
            mapbox_style="open-street-map",
            margin={
                "r":0,
                "t":50,
                "l":0,
                "b":0
            }
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )

    ##################################################################################################################
elif opt == "About":

    st.title("About Road Accident Analysis System")

    st.markdown("""
    The Road Accident Analysis System is a data analytics project developed to
    analyze road accident patterns using the Indian Road Accident Dataset.
    This system performs data processing, exploration, and visualization to
    understand the major factors affecting road accidents.

    The application provides interactive dashboards for analyzing accidents
    based on location, time, weather conditions, road types, accident severity,
    and vehicle involvement.
    """)


    about_tab1, about_tab2, about_tab3, about_tab4, about_tab5 = st.tabs([
        "Project Overview",
        "Objectives",
        "Technology Stack",
        "Dataset Information",
        "Future Scope"
    ])



    # =========================
    # PROJECT OVERVIEW
    # =========================
    with about_tab1:

        st.subheader("Project Overview")

        st.markdown("""
        Road accidents are one of the major causes of injuries and fatalities.
        Analyzing accident data helps identify important patterns and factors
        responsible for accidents.

        This project focuses on analyzing accident records and generating
        meaningful insights through interactive visualizations. The dashboard
        helps users explore accident trends and understand relationships between
        different accident factors.

        The system analyzes:

        - Accident trends
        - Location-based accident patterns
        - Weather impact
        - Road conditions
        - Accident severity
        - Vehicle involvement
        - Risk score analysis
        """)



    # =========================
    # OBJECTIVES
    # =========================
    with about_tab2:

        st.subheader("Project Objectives")

        st.markdown("""
        The main objectives of this project are:

        1. To analyze road accident patterns using real-world accident data.

        2. To identify factors responsible for accident occurrence and severity.

        3. To study the relationship between weather, roads, traffic,
           and accident frequency.

        4. To visualize accident trends using interactive charts.

        5. To provide useful insights for improving road safety strategies.

        6. To support data-driven decision making.
        """)



    # =========================
    # TECHNOLOGY STACK
    # =========================
    with about_tab3:

        st.subheader("Technology Stack")


        col1, col2, col3 = st.columns(3)


        with col1:

            st.info("""
            Programming Language

            Python

            Data Processing

            Pandas
            NumPy
            """)


        with col2:

            st.info("""
            Visualization Tools

            Plotly
            Matplotlib
            Seaborn
            """)


        with col3:

            st.info("""
            Application Development

            Streamlit

            Development Tool

            Visual Studio Code
            """)



    # =========================
    # DATASET INFORMATION
    # =========================
    with about_tab4:

        st.subheader("Dataset Information")


        st.markdown("""
        Dataset Name:

        Indian Road Accident Dataset 2022-2025


        Dataset Size:

        20,000 Accident Records


        Important Features:

        - Accident ID
        - City and State
        - Latitude and Longitude
        - Date and Time
        - Road Type
        - Weather Conditions
        - Visibility
        - Traffic Density
        - Accident Cause
        - Accident Severity
        - Vehicles Involved
        - Casualties
        - Risk Score


        The dataset is processed and cleaned before performing analysis.
        """)



    # =========================
    # FUTURE SCOPE
    # =========================
    with about_tab5:

        st.subheader("Future Scope")


        st.markdown("""
        The project can be further enhanced with advanced features:

        1. Integration of real-time accident data.

        2. Development of Machine Learning models for accident prediction.

        3. Interactive accident location maps using geographical visualization.

        4. Real-time risk monitoring system.

        5. Automated accident warning and alert system.

        6. Integration with traffic management platforms.
        """)



    st.divider()

    st.caption(
        "Developed as a Data Science Project using Python and Streamlit."
    )
################################################################################################################
elif opt=="Query":
    st.title("Ask Query")
    st.write("ask question and answers")
    a=st.chat_input("Ask Question")
    if a:
        url = "https://chatgpt-42.p.rapidapi.com/conversationgpt4-2"

        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": a
                }
            ],
            "system_prompt": "",
            "temperature": 0.9,
            "top_k": 5,
            "top_p": 0.9,
            "max_tokens": 256,
            "web_access": False
        }
        headers = {
            "x-rapidapi-key": "4b2860e8b6mshfd1c7aa091a5abcp1fa192jsn0f79189fb419",
            "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        st.write(response.json()["result"])
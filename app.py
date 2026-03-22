import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# PAGE CONFIG
st.set_page_config(page_title="Dynamic Pricing", layout="wide")

# LOAD DATA
@st.cache_data
def load_data():
    df = pd.read_csv("final_dynamic_pricing_data.csv")
    df = df.dropna(subset=["PriceCategory"])
    return df

df = load_data()

st.markdown("""
<style>

body {
    background: linear-gradient(135deg,#020617,#0f172a);
}

/* KPI CARDS */
.kpi {
    padding:20px;
    border-radius:18px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    border:1px solid rgba(255,255,255,0.1);
    text-align:center;
    color:white;
    position: relative;
    overflow: hidden;
}

/* SHINY EFFECT */
.kpi::before {
    content: "";
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(
        120deg,
        transparent,
        rgba(255,255,255,0.2),
        transparent
    );
    transform: rotate(25deg);
    animation: shine 3s infinite;
}

@keyframes shine {
    0% { transform: translateX(-100%) rotate(25deg); }
    100% { transform: translateX(100%) rotate(25deg); }
}

/* Hover effect */
.kpi:hover {
    transform: scale(1.05);
    transition: 0.3s;
}

h1, h2, h3 {
    color:#e2e8f0;
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("Control Panel")

cat_filter = st.sidebar.multiselect(
    "Price Category",
    df["PriceCategory"].unique(),
    default=df["PriceCategory"].unique()
)

country_filter = st.sidebar.multiselect(
    "Country",
    df["Country"].unique(),
    default=df["Country"].unique()
)

month_filter = st.sidebar.slider("Month", 1, 12, (1, 12))

df = df[
    (df["PriceCategory"].isin(cat_filter)) &
    (df["Country"].isin(country_filter)) &
    (df["Month"].between(month_filter[0], month_filter[1]))
]

# HEADER
st.markdown("# Dynamic Pricing & Revenue Optimization")
st.write("Data-driven pricing system to maximize revenue.")

# KPI
total = df["TotalPrice"].sum()
new = df["NewRevenue"].sum()
lift = new - total
avg = df["UnitPrice"].mean()

c1, c2, c3, c4 = st.columns(4)

c1.markdown(f'<div class="kpi"><h4>Total Revenue</h4><h2>{total:,.0f}</h2></div>', unsafe_allow_html=True)
c2.markdown(f'<div class="kpi"><h4>Optimized Revenue</h4><h2>{new:,.0f}</h2></div>', unsafe_allow_html=True)
c3.markdown(f'<div class="kpi"><h4>Revenue Increase</h4><h2>{lift:,.0f}</h2></div>', unsafe_allow_html=True)
c4.markdown(f'<div class="kpi"><h4>Avg Price</h4><h2>{avg:.2f}</h2></div>', unsafe_allow_html=True)

# INSIGHTS SECTION
st.markdown("## Insights")

col1, col2 = st.columns(2)

# Demand vs Price
with col1:
    filtered = df[df["UnitPrice"] < 50]
    agg = filtered.groupby("UnitPrice")["Quantity"].mean().reset_index()

    fig1 = px.line(
    agg,
    x="UnitPrice",
    y="Quantity",
    title="Demand vs Price Relationship"
)
    st.plotly_chart(fig1, use_container_width=True, key="chart1")

# Category
with col2:
    cat = df.groupby("PriceCategory")["TotalPrice"].sum().reset_index()
    fig2 = px.bar(
    cat,
    x="PriceCategory",
    y="TotalPrice",
    color="PriceCategory",
    title="Revenue by Price Category"
)
    st.plotly_chart(fig2, use_container_width=True, key="chart2")

#  TREND
st.markdown("## Revenue Trend")

time = df.groupby("Month")["TotalPrice"].sum().reset_index()
fig3 = px.area(
    time,
    x="Month",
    y="TotalPrice",
    title="Monthly Revenue Trend"
)

st.plotly_chart(fig3, use_container_width=True, key="chart3")

#  SHARE
st.markdown("## Revenue Share")

pie = df.groupby("PriceCategory")["TotalPrice"].sum().reset_index()
fig4 = px.pie(
    pie,
    names="PriceCategory",
    values="TotalPrice",
    title="Revenue Share Distribution"
)

st.plotly_chart(fig4, use_container_width=True, key="chart4")

# TOP PRODUCTS
st.markdown("## Top Products")

top = (
    df.groupby("StockCode")["TotalPrice"]
    .sum()
    .reset_index()
    .sort_values(by="TotalPrice", ascending=True)
    .tail(10)
)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=top["TotalPrice"],
    y=top["StockCode"],
    mode='markers',
    marker=dict(size=12, color='limegreen', line=dict(width=1, color='white'))
))

for i in range(len(top)):
    fig.add_shape(
        type='line',
        x0=0,
        y0=top["StockCode"].iloc[i],
        x1=top["TotalPrice"].iloc[i],
        y1=top["StockCode"].iloc[i],
        line=dict(color="white", width=2)
    )

fig.update_layout(
    title="Top 10 Revenue Generating Products",
    
    xaxis_title="Revenue (Total Sales)",
    yaxis_title="Product ID (StockCode)",

    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white")
)
st.plotly_chart(fig, use_container_width=True, key="top")

#  DISTRIBUTIONS
st.markdown("## Distribution Analysis")

col1, col2 = st.columns(2)

with col1:
    price_filtered = df[df["UnitPrice"] < df["UnitPrice"].quantile(0.99)]
    fig = px.histogram(
    price_filtered,
    x="UnitPrice",
    nbins=50,
    title="Price Distribution"
)
    st.plotly_chart(fig, use_container_width=True, key="price")

with col2:
    qty_filtered = df[df["Quantity"] < df["Quantity"].quantile(0.99)]
    fig = px.histogram(
    qty_filtered,
    x="Quantity",
    nbins=50,
    title="Demand Distribution"
)
    st.plotly_chart(fig, use_container_width=True, key="qty")


#  SCATTER

st.markdown("## Price vs Demand")

sample = df[
    (df["UnitPrice"] < 100) &
    (df["Quantity"] < df["Quantity"].quantile(0.99))
].sample(2000)

fig = px.scatter(
    sample,
    x="UnitPrice",
    y="Quantity",
    color="PriceCategory",
    opacity=0.6,
    title="Price vs Demand Analysis"
)
st.plotly_chart(fig, use_container_width=True, key="scatter")

#  SIMULATOR
st.markdown("## Pricing Simulator")

price = st.slider("Select Price", 1.0, 50.0, 10.0)

if price > 20:
    rec = price * 0.9
    msg = "Reduce price"
elif price < 5:
    rec = price * 1.1
    msg = "Increase price"
else:
    rec = price
    msg = "Balanced"

st.markdown(f'<div class="kpi"><h3>Recommended: {rec:.2f}</h3><p>{msg}</p></div>', unsafe_allow_html=True)

#  INSIGHTS
st.markdown("## Insights")

st.write("""
- Demand decreases with price increase
- Low price → high volume
- High demand supports higher pricing
""")

#  SOLUTION
st.markdown("## Solution")

st.write("""
Use dynamic pricing:
- Increase price for high demand
- Decrease for low demand
- Optimize continuously
""")

# FOOTER
st.markdown("---")
st.caption("Dynamic Pricing Project")

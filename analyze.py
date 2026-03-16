import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("Pakistan-disaster.csv", encoding="latin1")

# Clean column names
data.columns = data.columns.str.strip()

st.title("Pakistan Disaster Risk Analytics Dashboard")

st.write("Analysis of disaster trends, impacts, and geographic distribution in Pakistan.")

# -------------------------
# Key Metrics
# -------------------------

st.header("Key Statistics")

total_disasters = len(data)
total_deaths = data["Total Deaths"].sum()
total_affected = data["Total Affected"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total Disasters", total_disasters)
col2.metric("Total Deaths", int(total_deaths))
col3.metric("Total People Affected", int(total_affected))

# -------------------------
# Disaster Trends Over Time
# -------------------------

st.header("Disaster Frequency Over Time")

year_counts = data["Start Year"].value_counts().sort_index()

fig1, ax1 = plt.subplots()
year_counts.plot(kind="line", marker="o", ax=ax1)
ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Disasters")

st.pyplot(fig1)

# -------------------------
# Disaster Types
# -------------------------

st.header("Disaster Types in Pakistan")

type_counts = data["Disaster Type"].value_counts()

fig2, ax2 = plt.subplots()
type_counts.plot(kind="bar", ax=ax2)
ax2.set_xlabel("Disaster Type")
ax2.set_ylabel("Number of Events")

st.pyplot(fig2)

# -------------------------
# Deaths by Disaster Type
# -------------------------

st.header("Deaths by Disaster Type")

death_by_type = data.groupby("Disaster Type")["Total Deaths"].sum()

fig3, ax3 = plt.subplots()
death_by_type.plot(kind="bar", ax=ax3)
ax3.set_ylabel("Total Deaths")

st.pyplot(fig3)

# -------------------------
# Economic Damage
# -------------------------

st.header("Economic Damage by Disaster Type")

damage = data.groupby("Disaster Type")["Total Damage ('000 US$)"].sum()

fig4, ax4 = plt.subplots()
damage.plot(kind="bar", ax=ax4)
ax4.set_ylabel("Total Damage ('000 USD)")

st.pyplot(fig4)

# -------------------------
# Disaster Map
# -------------------------

# -------------------------
# Disaster Map
# -------------------------

st.header("Geographic Distribution of Disasters")

map_data = data[["Latitude", "Longitude"]].dropna()

# Rename columns for Streamlit
map_data = map_data.rename(columns={
    "Latitude": "lat",
    "Longitude": "lon"
})

st.map(map_data)

# -------------------------
# Dataset Preview
# -------------------------

st.header("Dataset Preview")

st.dataframe(data.head())

# -------------------------
# Key Insights
# -------------------------

st.header("Key Insights")

st.write("""
• Floods and earthquakes are the most frequent disasters in Pakistan.

• Earthquakes often cause the highest number of deaths.

• Disaster frequency has increased in recent decades.

• Economic losses from disasters are significant and growing.

""")
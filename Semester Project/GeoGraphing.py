import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np
import pandas as pd

covidJulySpike_data = pd.read_csv('Data/July-Total.csv', na_values=['?'], header=0)

# Overall Total Data
Covid_Total = pd.read_csv('Data/Covid-19-Total-Full.csv', na_values=['?'], header=0)
fulltotalfips = Covid_Total['GeoFIPS'].tolist()

# July Data
July_Total = pd.read_csv('Data/July-Total.csv', na_values=['?'], header=0)
July_Total['GeoFIPS'] = July_Total['GeoFIPS'].apply(lambda x: str(x).zfill(1))
July_Total['FIPS'] = July_Total['GeoFIPS']
fips = July_Total['FIPS'].tolist()

# Overall Partial Data
Overall_Total = pd.read_csv('Data/Covid-19 Total.csv', na_values=['?'], header=0)
overallfips = Overall_Total['GeoFIPS'].tolist()
import matplotlib.pyplot as plt

# data to be plotted
# July Specific Data - 1
July_Total_1 = pd.read_csv('Data/July-Total-Cases-1.csv', na_values=['?'], header=0)
x = July_Total_1['percapita_personal_income']
y = July_Total_1['new_cases_per_1000']
plt.scatter(x, y, color='r', alpha=0.5)
plt.show()
# July Specific Data - 2
July_Total_2 = pd.read_csv('Data/July-Total-Cases-2.csv', na_values=['?'], header=0)
x = July_Total_2['percapita_personal_income']
y = July_Total_2['new_cases_per_1000']
plt.scatter(x, y, color='r', alpha=0.5)
plt.show()

x = July_Total['percapita_personal_income']
y = July_Total['new_cases_per_1000']
plt.scatter(x, y, color='r', alpha=0.5)
plt.show()
# plotting

plt.show()

# Total Population per County Mapping
colorscale = ["#030512", "#1d1d3b", "#323268", "#3d4b94", "#3e6ab0",
              "#4989bc", "#60a7c7", "#95C6F0", "#B1D8F4", "#CEEAF9", "#eafcfd"]
values = covidJulySpike_data['Population'].tolist()
endpts = [1000, 5000, 10000, 50000, 100000, 500000, 1000000, 2500000, 5000000]


fig = ff.create_choropleth(
    fips=fips,
    values=values,
    colorscale=colorscale,
    binning_endpoints=endpts,
    round_legend_values=True,
    plot_bgcolor='rgb(11,11,22)',
    paper_bgcolor='rgb(11,11,22)',
    legend_title='Total Population in 2018',
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.05},
    exponent_format=True,
)

fig.layout.template = None
fig.show()

# Total New Cases per County Mapping
values = covidJulySpike_data['new_confirmed'].tolist()
endpts = [1, 50, 100, 200, 400, 750, 1000, 2000, 5000]
colorscale = ["#030512", "#1d1d3b", "#323268", "#3d4b94", "#3e6ab0",
              "#4989bc", "#60a7c7", "#95C6F0", "#B1D8F4", "#CEEAF9", "#eafcfd"]

fig = ff.create_choropleth(
    fips=fips,
    values=values,
    colorscale=colorscale,
    binning_endpoints=endpts,
    round_legend_values=True,
    plot_bgcolor='rgb(11,11,22)',
    paper_bgcolor='rgb(11,11,22)',
    legend_title='Total New Cases in 2020 July',
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.05},
    exponent_format=True,
)

fig.layout.template = None
fig.show()

# Total Covid-19 Cases Mapping
values = Overall_Total['total_cases'].tolist()
endpts = [100, 500, 1000, 2000, 7000, 15000, 21000, 45000, 100000, 300000]
colorscale = ["#030512", "#13142F", "#22234B", "#323268", "#3d4b94",
              "#3e6ab0", "#4989bc", "#60a7c7", "#95C6F0", "#B1D8F4",
              "#CEEAF9", "#eafcfd"]
fig = ff.create_choropleth(
    fips=overallfips,
    values=values,
    colorscale=colorscale,
    binning_endpoints=endpts,
    round_legend_values=False,
    plot_bgcolor='rgb(11,11,22)',
    paper_bgcolor='rgb(11,11,22)',
    legend_title='Total Covid-19 Cases in 2020',
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.1},
)

fig.layout.template = None
fig.show()

# Per capita Personal Income Mapping
values = July_Total['percapita_personal_income'].tolist()
endpts = [30000, 33000, 36000, 40000, 44000, 48000, 52000, 68000, 80000, 150000]
colorscale = ["#030512", "#13142F", "#22234B", "#323268", "#3d4b94",
              "#3e6ab0", "#4989bc", "#60a7c7", "#95C6F0", "#B1D8F4",
              "#CEEAF9", "#eafcfd"]

fig = ff.create_choropleth(
    fips=fips,
    values=values,
    colorscale=colorscale,
    binning_endpoints=endpts,
    round_legend_values=True,
    plot_bgcolor='rgb(11,11,22)',
    paper_bgcolor='rgb(11,11,22)',
    legend_title='Per Capita Personal Income',
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.05},
    exponent_format=True,
)

fig.layout.template = None
fig.show()


# New Cases Per 1000 in July
values = July_Total['new_cases_per_1000'].tolist()
endpts = [0.5, 1, 1.5, 2, 3.0, 4.0, 5.0, 7.0, 10.0, 20.0]
colorscale = ["#030512", "#13142F", "#22234B", "#323268", "#3d4b94",
              "#3e6ab0", "#4989bc", "#60a7c7", "#95C6F0", "#B1D8F4",
              "#CEEAF9", "#eafcfd"]

fig = ff.create_choropleth(
    fips=fips,
    values=values,
    colorscale=colorscale,
    binning_endpoints=endpts,
    round_legend_values=False,
    plot_bgcolor='rgb(11,11,22)',
    paper_bgcolor='rgb(11,11,22)',
    legend_title='New Covid-19 Cases Per 1000 in July',
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.1},
)

fig.layout.template = None
fig.show()

# New Cases Per 1000 in 2020
values = Covid_Total['new_cases_per_1000'].tolist()
endpts = [10.0, 25.0, 32.0, 38.0, 44.0, 50.0, 55.0, 62.0, 80.0, 140.0]
colorscale = ["#eafcfd", "#CEEAF9", "#B1D8F4", "#95C6F0", "#60a7c7",
              "#4989bc", "#3e6ab0", "#3d4b94", "#323268", "#22234B",
              "#13142F", "#030512"]

fig = ff.create_choropleth(
    fips=fulltotalfips,
    values=values,
    colorscale=colorscale,
    binning_endpoints=endpts,
    round_legend_values=False,
    plot_bgcolor='rgb(11,11,22)',
    paper_bgcolor='rgb(11,11,22)',
    legend_title='New Covid-19 Cases Per 1000 in July',
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.1},
)

fig.layout.template = None
fig.show()

import plotly.express as px

# Pulling data from: https://www.270towin.com/states/
places2016 = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI",  "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
pct_GOP2016 = [62.9, 52.9, 49.5, 60.4, 32.8, 44.4, 41.2, 41.9, 49.1, 51.3, 30.1, 59.2, 39.4, 57.2, 51.8, 57.2, 62.5, 58.1, 45.2, 35.3, 33.5, 47.6, 45.4, 58.3, 57.1, 56.5, 60.3, 45.5, 47.2, 41.8, 40.0, 37.5, 50.5, 64.1, 52.1, 65.3, 41.1, 48.8, 39.8, 54.9, 61.5,  61.1, 52.6, 45.9, 32.6, 45.0, 38.2, 68.7, 47.9, 70.1]
pct_DEM2016 = [34.6, 37.7, 45.4, 33.8, 61.6, 47.2, 54.5, 53.4, 47.8, 45.6, 62.3, 27.6, 55.4, 37.9, 42.2, 36.2, 32.7, 38.4, 47.9, 60.5, 60.8, 47.3, 46.9, 39.7, 38, 36.0, 34, 47.9, 47.6, 55, 48.3, 58.8, 46.7, 27.8, 43.5, 28.9, 51.7, 47.6, 55.4, 40.8, 31.7, 34.9, 43.4, 27.8, 61.1, 49.9, 54.4, 26.5, 46.9, 22.5]



difference2016 = []
zip_object = zip(pct_GOP2016, pct_DEM2016)
for list1_i, list2_i in zip_object:
    difference2016.append(list1_i-list2_i)

fig2016 = px.choropleth(\
                    locations = places2016, \
                    locationmode="USA-states", \
                    color = difference2016, \
                    range_color=[-30, 30], \
                    color_continuous_scale=["blue", "white", "red"], \
                    scope="usa")

fig2016.update_layout(
    title_text = '2016 Presidential Election point spreads per state', 
                    )
fig2016.show()
#fig2016
#import 
import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

import warnings
warnings.filterwarnings("ignore")

#___________________________________________________________________________

# SETTING PAGE CONFIGURATIONS
icon = Image.open("airbnb.png")
st.set_page_config(page_title= "AIRBNB ANALYSIS",
                   page_icon= icon,
                   layout= "wide",
                   menu_items={'About': "### This page is created by Desilva!"})

st.markdown("<h1 style='text-align: center; color: #ff5a5f;'>AIRBNB ANALYSIS</h1>", unsafe_allow_html=True)
st.write("")

#____________________________________________________________________________________________________________________________

# CREATING OPTION MENU
selected = option_menu(None, ["HOME","EXPLORE","ABOUT"], 
                       icons=["house","binoculars","file-person"],
                       default_index=0,
                       orientation="horizontal",
                       styles={"container": {"padding": "0!important", "background-color": "#fafafa"},
                               "icon": {"color": "#ff5a5f", "font-size": "20px"},
                               "nav-link": {"font-size": "20px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
                               "nav-link-selected": {"background-color": "#6495ED"}})

##____________________________________________________________________________________________________________________________

df = pd.read_csv("USE YOUR PATH HERE")

#_____________________________________________________________________________________________________________________________

if selected == "HOME":
    st.header("About Airbnb")
    st.markdown(f'''<span style="font-size:20px;"> Airbnb was born in 2007 when two Hosts welcomed three guests to their San Francisco home, 
                and has since grown to over 5 million Hosts who have welcomed over 1.5 billion guest arrivals 
                in almost every country across the globe. Every day, Hosts offer unique stays and experiences that 
                make it possible for guests to connect with communities in a more authentic way.</span>''', unsafe_allow_html=True)

    st.markdown('''<span style="font-size:20px;"> Airbnb connects property owners with guests for short stays, 
                offering hosts a way to earn income. Guests often find Airbnb rentals cheaper and homier than hotels.
                Airbnb Inc operates a platform for hospitality services, allowing users to discover and book unique accommodations worldwide. 
                The company is headquartered in San Francisco, California, US.</span>''', unsafe_allow_html=True)
    
    st.header("About Dataset")
    st.markdown('''<span style="font-size:20px;">The airbnb database is a compilation of vacation home listings 
                and reviews available on Inside AirBnB. This database contains a single collection called listingsAndReviews.</span>''', unsafe_allow_html=True)

#____________________________________________________________________________________________________________________________

if selected == "EXPLORE":

    tab1, tab2, tab3, tab4, tab5,tab6 = st.tabs(["TYPE ANALYSIS","PRICE ANALYSIS","AVAILABILITY ANALYSIS","LOCATION BASED ANALYSIS",
                                             "GEOSPATIAL VISUALIZATION", "TOP CHARTS"])
    
    with tab1:
        st.title("Room Type Analysis")

        col1,col2,col3 = st.columns([5,1,5])
        with col1:
            # Create a select box to choose a country
            country_list = sorted(["ALL COUNTRIES"] + sorted(df["country"].unique()))
            country_1 = st.selectbox("Select the Country", country_list, key="country1")
            # Filter the DataFrame based on the selected country
            if country_1 == "ALL COUNTRIES":
                df_country_1 = df.copy()  # Select all countries
            else:
                df_country_1 = df[df["country"] == country_1]  # Filter based on selected country
            # Reset the index of the filtered DataFrame
            df_country_1.reset_index(drop=True, inplace=True)

            # Group by Room Type
            df_country_1_room = pd.DataFrame(df_country_1.groupby("room_type")[["host_listings_count"]].sum())
            df_country_1_room.reset_index(inplace= True)
            df_country_1_room.index +=1
            st.dataframe(df_country_1_room)

        #------------------------------
            
        with col3:
            # Bar chart - Room Type & Host Listing Count        
            fig_bar_1 = px.bar(df_country_1_room, x='host_listings_count', y= "room_type", title= "Room Type & Host Listing Count",
                    hover_data=["host_listings_count"],color='room_type', width=400, height=500)
            fig_bar_1.update_xaxes(title="Total Host Listing Count")
            fig_bar_1.update_yaxes(title="Room Type")
            st.plotly_chart(fig_bar_1, use_container_width=True) 

        #------------------------------

        col1,col2,col3 = st.columns([3,1,6])
        with col1:
            # Create a select box to choose a Room Type
            room_type_1 = st.selectbox("Select the Room Type", df_country_1["room_type"].unique(), key="room1")
            df_country_1_room = df_country_1[df_country_1["room_type"] == room_type_1]
            # Group by Market
            df_country_1_room_market = pd.DataFrame(df_country_1_room.groupby("market")[["host_listings_count"]].sum())
            df_country_1_room_market.reset_index(inplace= True)
            # Sort the Group by Market
            df_country_1_room_market_sorted = df_country_1_room_market.sort_values(by="host_listings_count", ascending=False)
            df_country_1_room_market_sorted.reset_index(drop=True, inplace=True)
            df_country_1_room_market_sorted.index += 1
            st.dataframe(df_country_1_room_market_sorted)

        #------------------------------
            
        with col3:
            # Bar chart - Market & Host Listing Count
            fig_bar_2 = px.bar(df_country_1_room_market_sorted, x='host_listings_count', y="market", title="Market & Host Listing Count",
                                hover_data=["host_listings_count"],color= "market")
            fig_bar_2.update_xaxes(title="Total Host Listing Count")
            fig_bar_2.update_yaxes(title="Market")
            st.plotly_chart(fig_bar_2, use_container_width=True) 

        #------------------------------

        # Aggregate data to get counts
        df_room_cancellation = df_country_1.groupby(['cancellation_policy', 'room_type']).size().reset_index(name='count')

        # Bar chart - Room Types & Cancellation Policy
        fig_room_cancellation = px.bar(df_room_cancellation, x='cancellation_policy', y='count', color='room_type', 
                    barmode='group', title='Room Types & Cancellation Policy')
        st.plotly_chart(fig_room_cancellation, use_container_width=True)

#____________________________________________________

    with tab2:
        st.title("PRICE ANALYSIS")

        # Scatter Plot - Price and Country
        fig_contry_price = px.scatter(df, x='price', y='country', title='Comparison of Price and Country', color='country')
        st.plotly_chart(fig_contry_price, use_container_width=True)

        #------------------------------

        col1, col2,col3 = st.columns([5,1,5])
        with col1:
            # Create a select box to choose a country
            country_list = sorted(["ALL COUNTRIES"] + sorted(df["country"].unique()))
            country_2 = st.selectbox("Select the Country", country_list, key="country2")
            # Filter the DataFrame based on the selected country
            if country_2 == "ALL COUNTRIES":
                df_country_2 = df.copy()  
            else:
                df_country_2 = df[df["country"] == country_2] 
            # Group by Room Type
            df_country_2_room = pd.DataFrame(df_country_2.groupby("room_type")["price"].mean())
            df_country_2_room.reset_index(inplace= True)
            # Bar Chart - Room Type & Average Price($)
            fig_bar_3 = px.bar(df_country_2_room, x='room_type', y= "price", title= "Room Type & Average Price($)",hover_data=["price"], color= "room_type")
            st.plotly_chart(fig_bar_3, use_container_width=True) 

        #------------------------------

        with col3:
            # Create a select box to choose a Room Type
            room_type_2 = st.selectbox("Select the Room Type",df_country_2["room_type"].unique(), key="room2")
            df_country_2_room= df_country_2[df_country_2["room_type"] == room_type_2]
            df_country_2_room.reset_index(drop= True, inplace= True)
            # Group by Property Type
            df_bar = pd.DataFrame(df_country_2_room.groupby("property_type")["price"].mean())
            df_bar.reset_index(inplace= True)
            # Bar Chart - Property Type & Average Price($)
            fig_bar_4 = px.bar(df_bar, y='property_type', x = "price", title= "Property Type & Average Price($)",hover_data=["price"], color ="price")
            st.plotly_chart(fig_bar_4, use_container_width=True) 

        #------------------------------

        col1, col2,col3 = st.columns([5,1,5])
        with col1:
            # Group by Country   
            country_prices = df_country_2.groupby('country')[['price', 'security_deposit', 'cleaning_fee']].mean()      
            country_prices.reset_index(inplace= True)
            # Bar Chart - Comparison of Price, Security Deposit, and Cleaning Fee by Country
            fig_contry_price = px.bar(country_prices, y='country', x=['price', 'security_deposit', 'cleaning_fee'], 
                                    title='Comparison of Price, Security Deposit, and Cleaning Fee by Country', 
                                    barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow_r)
            st.plotly_chart(fig_contry_price, use_container_width=True)
 
        #------------------------------

        with col3: 
            # Group by Market      
            country_prices_1 = df_country_2.groupby('market')[['price', 'security_deposit', 'cleaning_fee']].mean()      
            country_prices_1.reset_index(inplace= True)
            # Bar Chart - Comparison of Price, Security Deposit, and Cleaning Fee by Market
            fig_con_price_1 = px.bar(country_prices_1, y='market', x=['price', 'security_deposit', 'cleaning_fee'], 
                                    title='Comparison of Price, Security Deposit, and Cleaning Fee by Market', 
                                    barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow_r)
            st.plotly_chart(fig_con_price_1, use_container_width=True)

 #____________________________________________________
       

    with tab3:
        st.title("AVAILABILITY ANALYSIS")
        
        # Create a select box to choose a country
        country_list = sorted(["ALL COUNTRIES"] + sorted(df["country"].unique()))
        country_3 = st.selectbox("Select the Country", country_list, key="country3")
        # Filter the DataFrame based on the selected country
        if country_3 == "ALL COUNTRIES":
            df_country_3 = df.copy()  
        else:
            df_country_3 = df[df["country"] == country_3]  
                
        #------------------------------
        
        col1, col2,col3 = st.columns([5,1,5])
        with col1:
            # Group by Market
            df_country_3_avail = pd.DataFrame(df_country_3.groupby("market")[["bedrooms","beds","bathrooms","accommodates"]].sum())
            df_country_3_avail.reset_index(inplace= True)
            # Bar Chart - Availability Based on Market
            fig_country_4_avail = px.bar(df_country_3_avail, y='market', x=["bedrooms","beds","bathrooms","accommodates"], 
                                        title='Availability Based on Market', barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow_r)
            st.plotly_chart(fig_country_4_avail, use_container_width=True)

        #------------------------------
            
        with col3:
            # Group by Market
            df_market_available= pd.DataFrame(df_country_3.groupby("market")[["availability_30","availability_60","availability_90","availability_365"]].mean())
            df_market_available.reset_index(inplace= True)
            # Bar Chart - Availability Based on Market
            fig_market_available = px.bar(df_market_available, y='market', x=['availability_30', 'availability_60', 'availability_90', "availability_365"], 
                                    title='Availability Based on Market', barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow_r)
            st.plotly_chart(fig_market_available, use_container_width=True) 

        #------------------------------
        # Create a select box to choose a Room Type
        roomtype_3 = st.selectbox("Select the Room Type", df_country_3["room_type"].unique(),key = "room3")
        df_roomtype_3 = df_country_3[df_country_3["room_type"] == roomtype_3]
        # Group by Host Response Time
        df_roomtype_3_avail = pd.DataFrame(df_roomtype_3.groupby("host_response_time")[["availability_30","availability_60","availability_90","availability_365","price"]].sum())
        df_roomtype_3_avail.reset_index(inplace= True)
        # Bar Chart - Availability Based on Host Response Time
        fig_roomtype_3_avail = px.bar(df_roomtype_3_avail, x='host_response_time', 
                                      y=['availability_30', 'availability_60', 'availability_90', "availability_365"], 
        title='Availability Based on Host Response Time', barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow_r)
        st.plotly_chart(fig_roomtype_3_avail, use_container_width=True)

 #____________________________________________________

    with tab4:
        st.title("LOCATION BASED ANALYSIS") 

        # Top 10 Countries based on Price
        top_10_countries = pd.DataFrame(df.groupby("country")[["price"]].mean())
        top_10_countries.reset_index(inplace= True)
        # Bar Chart - Price and country
        fig_top_10_countries = px.bar(top_10_countries, y='country', x='price', title='Price and country',color = 'price') 
        st.plotly_chart(fig_top_10_countries, use_container_width=True)

        #------------------------------

        col1, col2,col3 = st.columns([5,1,5])
        with col1:
            # Count occurrences of 'Yes' and 'No' in the 'host_is_superhost' column
            superhost_counts = df['host_is_superhost'].value_counts().reset_index()
            superhost_counts.columns = ['host_is_superhost', 'Count']

            # Pie Chart - Superhosts
            fig_superhost_pie = px.pie(superhost_counts, values='Count',  names='host_is_superhost',  
                                    title='Distribution of Superhosts (Yes/No)')  
            st.plotly_chart(fig_superhost_pie, use_container_width=True)

        #------------------------------

        with col3:
            # Create a select box to choose a country
            country_list = sorted(["ALL COUNTRIES"] + sorted(df["country"].unique()))
            country_4 = st.selectbox("Select the Country", country_list, key="country4")

            # Filter the DataFrame based on the selected country
            if country_4 == "ALL COUNTRIES":
                df_country_4 = df.copy()  
            else:
                df_country_4 = df[df["country"] == country_4] 

            df_country_4.reset_index(drop=True, inplace=True)

            # Count number of 'yes' superhosts in each market
            df_yes = df_country_4[df_country_4['host_is_superhost'] == 'Yes']
            df_yes_count = df_yes.groupby('country').size().reset_index(name='Yes')

            # Count number of 'no' superhosts in each market
            df_no = df_country_4[df_country_4['host_is_superhost'] == 'No']
            df_no_count = df_no.groupby('country').size().reset_index(name='No')

            # Merge DataFrames
            df_merged = df_yes_count.merge(df_no_count, on='country', how='outer').fillna(0)

            # Bar Chart - Number of Superhosts (Yes/No) in Each Country 
            fig_superhost = px.bar(df_merged, x='country', y=['Yes', 'No'], 
                                    title='Number of Superhosts (Yes/No) in Each Country', 
                                    barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r)
            st.plotly_chart(fig_superhost, use_container_width=True)

        #------------------------------
       
        col1, col2,col3 = st.columns([5,1,5])
        with col1:
            # Scatter Plot - Relation between Minimum Nights and Price
            fig_scatter = px.scatter(df_country_4, x='minimum_nights', y='price', title='Relation between Minimum Nights and Price',  
                                        labels={'minimum_nights': 'Minimum Nights', 'price': 'Price'})
            st.plotly_chart(fig_scatter, use_container_width=True)

        #------------------------------
            
        with col3:
            # Scatter Plot - Relation between Minimum Nights (less than 366) and Price(less than 12000)
            filtered_data = df_country_4[(df_country_4['minimum_nights'] < 366) & (df_country_4['price'] < 12000)]
            fig_scatter_filtered = px.scatter(filtered_data, x='minimum_nights',  y='price',  
                                            title='Relation between Minimum Nights (less than 366) and Price(less than 12000)', 
                                            labels={'minimum_nights': 'Minimum Nights', 'price': 'Price'}) 
            st.plotly_chart(fig_scatter_filtered, use_container_width=True)

 #____________________________________________________

    with tab5:
        st.title("GEOSPATIAL VISUALIZATION")

        # Create a select box to choose a country
        unique_countries = sorted(["ALL COUNTRIES"] + sorted(df["country"].unique()))
        country = st.selectbox("Select the Country", unique_countries, key="country8")

        # Filter the DataFrame based on the selected country
        if country == "ALL COUNTRIES":
            df_selected_country = df.copy() 
        else:
            df_selected_country = df[df["country"] == country]

        df_selected_country.reset_index(drop=True, inplace=True)
        
        # Calculate the center coordinates of the selected city
        center_lat = df_selected_country['latitude'].mean()
        center_lon = df_selected_country['longitude'].mean()

        # Scatter Plot - Geospatial Distribution of Listings
        fig = px.scatter_mapbox(df_selected_country, lat="latitude", lon="longitude", hover_name="name",color='room_type',
                                size_max=15,color_continuous_scale="viridis",height=600,width=600)

        fig.update_layout(mapbox_style="carto-positron") #open-street-map
        fig.update_layout(mapbox=dict(center=dict(lat=center_lat, lon=center_lon)))  # Set the center coordinates
        fig.update_layout(width=1150,height=800,title='Geospatial Distribution of Listings')
        st.plotly_chart(fig)


#____________________________________________________

    with tab6:  
        st.title("TOP CHARTS")

        # Create a select box to choose a country
        unique_countries = sorted(["ALL COUNTRIES"] + sorted(df["country"].unique()))
        country = st.selectbox("Select the Country", unique_countries, key="country9")

        # Filter the DataFrame based on the selected country
        if country == "ALL COUNTRIES":
            df_selected_country = df.copy()  
        else:
            df_selected_country = df[df["country"] == country]  

        # Sort by Price
        df2_t_sorted= df_selected_country.sort_values(by="price")
        df2_t_sorted.reset_index(drop= True, inplace= True)

        # Highest & Lowest Prices
        top_10_highest_prices = df2_t_sorted.nlargest(10, 'price')
        top_10_affortable_prices = df2_t_sorted.nsmallest(10, 'price')

         #------------------------------       

        col1, col2,col3 = st.columns([5,1,5])
        with col1:
            # Bar Chart - Top 10 Costly Hosts
            fig_top_10_price_1= px.bar(top_10_highest_prices, y= "name",  x= "price" ,color= "price",
                                    color_continuous_scale= "greens",
                                    range_color=(0,top_10_highest_prices["price"].max()),
                                    title= "Top 10 Costly Hosts",
                                    hover_data= ["country","minimum_nights","maximum_nights","accommodates","bedrooms","beds"])
            st.plotly_chart(fig_top_10_price_1, use_container_width=True)
        #------------------------------
        with col3:
            # Bar Chart - Top 10 Affortable Hosts
            fig_bottom_10_price_1= px.bar(top_10_affortable_prices, y= "name",  x= "price" ,color= "price",
                                    color_continuous_scale= "reds",
                                    range_color=(0,top_10_affortable_prices["price"].max()),
                                    title= "Top 10 Affortable Hosts",
                                    hover_data= ["country","minimum_nights","maximum_nights","accommodates","bedrooms","beds"])
            st.plotly_chart(fig_bottom_10_price_1, use_container_width=True)

        #------------------------------

        col1, col2,col3 = st.columns([5,1,5])
        with col1:
            # Group by host location (highest)
            df_price_1= pd.DataFrame(top_10_highest_prices.groupby("host_location")["price"].mean())
            df_price_1.reset_index(inplace= True)
            df_price_1.columns= ["host_location", "Avarage_price"]
            # Bar Chart - Highest Price &  Host Location
            fig_price_1= px.bar(df_price_1, x= "Avarage_price", y= "host_location", orientation='h',
                                title= "Highest Price &  Host Location")
            st.plotly_chart(fig_price_1, use_container_width=True)        

        #------------------------------
        with col3:
            # Group by host location (affortable)
            df_price_2= pd.DataFrame(top_10_affortable_prices.groupby("host_location")["price"].mean())
            df_price_2.reset_index(inplace= True)
            df_price_2.columns= ["host_location", "Avarage_price"]
            # Bar Chart - Affortable Price &  Host Location
            fig_price_2= px.bar(df_price_2, x= "Avarage_price", y= "host_location", orientation='h',
                                title= "Affortable Price & Host Location")
            st.plotly_chart(fig_price_2, use_container_width=True)        

#____________________________________________________

if selected == "ABOUT":
        st.header("Approach")

        st.subheader("1. Data Collection:")
        st.write('''From the sample data in MongoDB Atlas, AirBnB Listings Dataset is collected''')
        
        st.subheader("2. Exploratory Data Analysis (EDA):")
        st.write('''Conduct exploratory data analysis to understand the distribution and patterns in the data.''')

        st.subheader("3. Data Cleaning and Preprocessing:")
        st.write('''Collected data is Cleaned and preprocessed by handling missing values,handling data types and outliers.''')
         
        st.subheader("4. Visualization:")
        st.write('''Visualizations are made to represent key metrics and trends. Using tools like Matplotlib, Seaborn, and Plotly for visualizations.''')

        st.subheader("5. Geospatial Analysis:")
        st.write('''Geospatial analysis to understand the geographical distribution of listings.''')

#____________________________________________________END________________________________________________________

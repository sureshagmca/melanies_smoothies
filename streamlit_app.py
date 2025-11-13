# Import python packages
import streamlit as st
# from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(f"My Parents New Healthy Diner ")
st.write(
  """Breakfast Menu
  """
)

st.write(
  """Omega 3 & Blueberry Oatmeal \n
  Kale, Spinach & Rocket Smoothie  \n
  Jard-Boiled Free-Range Egg
  """
)

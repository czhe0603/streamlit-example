import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.preprocessing import MinMaxScaler
import script


location = "200 East 42nd St."
rows = script.return_nearest_scores(location, 1)

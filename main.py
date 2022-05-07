import streamlit as st
import pandas as pd
import os, csv

# streamlit
st.set_page_config(
    page_title='Index Creator',
    page_icon=':anchor:',
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
         'Get Help': 'https://github.com/hirawatt/indexCreator',
         'Report a bug': "https://github.com/hirawatt/indexCreator/issues",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
)
st.title('Index Creator')

@st.experimental_memo
def load_data():
    instruments = pd.read_csv('instruments')
    return instruments

index_path = os.getcwd() + '/indices/'

# Get List of Custom Indices from folder
def custom_indices():
    # Import Custom Indices
    indices_list = os.listdir(index_path)
    return indices_list

# Generate Index Symbols from All Instruments
def index_symbols(instruments):
    st.write(instruments)
    # Select Instrument Exchange
    exchange = st.selectbox('Select Instrument Exchange', instruments.exchange.unique().tolist(), index=3) # index=3 'NSE' is default
    df = instruments[instruments['exchange'] == exchange]
    # Get all Stocks List
    stocks = df[(instruments['instrument_type'] == 'EQ') & (instruments['lot_size'] == 1) & (instruments['tick_size'] == 0.05)]
    st.write(stocks[['name', 'tradingsymbol']].dropna())

    st.subheader('TradingView Price Weighted Index')
    # TV Index from Custom Symbols
    # Select Symbols for Index
    with st.form("symbol_selection_form"):
        st.multiselect('Multiselect', stocks['name'])
        st.form_submit_button("Submit")

# Generate Index Symbols from Custom Indices
def custom_index_symbols():
    # TV Index from Custom Index
    indices_list = custom_indices()
    cIndex = st.sidebar.radio('Select Custom Index', indices_list)
    with open(index_path + cIndex) as f:
        reader = csv.reader(f)
        dfIndex = list(reader)
    symbols_list = dfIndex[0]
    return symbols_list


# Trading View Price Weighted Index
def tv_pw_index(symbols_list):
    symbol = 'NSE:' + '+NSE:'.join(symbols_list)
    return symbol

def main():
    instruments = load_data()
    #index_symbols(instruments)
    constituents = custom_index_symbols()
    st.write(constituents)
    # TV Index from Custom Index/Symbol
    st.info('Paste below Symbol to TradingView')
    symbol = tv_pw_index(constituents)
    st.code(symbol, language='python')


if __name__ == '__main__':
    main()
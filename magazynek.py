import streamlit as st

# Initialize session state for inventory if it doesn't exist
if 'inventory' not in st.session_state:
    st.session_state.inventory = []

st.title('Prosta Aplikacja Magazynowa')

st.write('---')
st.header('Dodaj Produkt')
product_to_add = st.text_input('Nazwa produktu do dodania:', key='add_input')
if st.button('Dodaj Produkt'):
    if product_to_add and product_to_add not in st.session_state.inventory:
        st.session_state.inventory.append(product_to_add)
        st.success(f'Dodano: {product_to_add}')
    elif product_to_add in st.session_state.inventory:
        st.warning(f'Produkt "{product_to_add}" już istnieje w magazynie.')
    else:
        st.warning('Proszę wprowadzić nazwę produktu.')

st.write('---')
st.header('Usuń Produkt')
product_to_remove = st.text_input('Nazwa produktu do usunięcia:', key='remove_input')
if st.button('Usuń Produkt'):
    if product_to_remove in st.session_state.inventory:
        st.session_state.inventory.remove(product_to_remove)
        st.success(f'Usunięto: {product_to_remove}')
    else:
        st.error(f'Produkt "{product_to_remove}" nie znaleziony w magazynie.')

st.write('---')
st.header('Aktualny Magazyn')
if st.session_state.inventory:
    for i, item in enumerate(st.session_state.inventory):
        st.write(f"{i+1}. {item}")
else:
    st.info('Magazyn jest pusty.')

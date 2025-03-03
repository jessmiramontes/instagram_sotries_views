import streamlit as st
from PIL import Image
import pandas as pd

# Función para guardar la información actualizada en la base de datos
def save_data(selected_categories, objeto_principal, emocion_primaria):
    df.at[current_index, 'categoría'] = ', '.join(selected_categories)
    df.at[current_index, 'objeto_principal'] = objeto_principal
    df.at[current_index, 'emocion_primaria'] = emocion_primaria
    df.to_csv('/content/drive/MyDrive/Colab Notebooks/stories_archive/csvs/imagesFINALtoValidate.csv', index=False)
    st.success("Información guardada correctamente")
    go_to_next_image()

# Función para pasar a la siguiente imagen
def go_to_next_image():
    if 'current_index' not in st.session_state:
        st.session_state.current_index = 0
    else:
        st.session_state.current_index += 1
    if st.session_state.current_index >= len(df):
        st.warning("No hay más imágenes.")
    
# Cargar la base de datos
df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/stories_archive/csvs/imagesFINALtoValidate.csv')

# Índice actual de la fila en la base de datos
current_index = 1 # <- AQUÍ: Puedes cambiar el índice inicial según tu necesidad

# Si quieres que el usuario elija el índice de inicio:
index_inicial = st.number_input("Ingresa el índice inicial", min_value=0, max_value=len(df)-1, value=0)
current_index = int(index_inicial)

# Ajusta la ruta a las imágenes
image_path = '/content/drive/MyDrive/Colab Notebooks/stories_archive/' + df.loc[current_index, 'nombre_archivo']
image = Image.open(image_path)
image = image.resize((image.width // 2, image.height // 2))  # Redimensionar la imagen al 50% de su tamaño original
st.image(image, caption='Imagen')

# Mostrar los datos y permitir la edición
objeto_principal = st.text_input("Objeto Principal", df.loc[current_index, 'objeto_principal'])
emocion_primaria = st.text_input("Emoción Primaria", df.loc[current_index, 'emocion_primaria'])

# Mostrar el color dominante desde la base de datos
hex_color = df.loc[current_index, 'color_dominante']
st.text(f"Color Dominante: {hex_color}")
st.markdown(f"<div style='width:50px; height:50px; background-color:{hex_color};'></div>", unsafe_allow_html=True)

# Agregar campo de categoría con selección múltiple
categories = ["Categoría 1", "Categoría 2", "Categoría 3", "Categoría 4", "Categoría 5", "Categoría 6", "Categoría 7", "Categoría 8", "Categoría 9"]
selected_categories = st.multiselect("Selecciona categorías", categories)

# Agregar botón para guardar la información
if st.button("Guardar"):
    save_data(selected_categories, objeto_principal, emocion_primaria)

# Agregar botón para editar la información (guarda y pasa a la siguiente imagen)
if st.button("Editar"):
    save_data(selected_categories, objeto_principal, emocion_primaria)

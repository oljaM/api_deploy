import streamlit as st
from PIL import Image


st.write("""
         # Image Classification
         """
         )

file = st.file_uploader("Upload the image to be classified U0001F447", type=["jpg", "png"])
st.set_option('deprecation.showfileUploaderEncoding', False)


if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)


# update url
#url = 'http://localhost:8080/predict'

# params = {
#    param1 = image
#}

# response = request.get(url, params = params)
#st.text(response.json)

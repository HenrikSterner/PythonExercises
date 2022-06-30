from PIL import Image 
image = Image.open('billede.jpg') # Bemærk billede skal ligge i samme bibliotek
st.image(image, caption='Sunrise by the mountains')
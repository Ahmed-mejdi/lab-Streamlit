import streamlit as st

# Display text using different methods
st.title("Streamlit Tutorial")
st.write('Hello World')

# Input elements
favorite_movie = st.text_input('Favorite Movie?')
st.write(f"Your favorite movie is: {favorite_movie}")

# Button example
is_clicked = st.button("Click Me")
if is_clicked:
    st.write("Button was clicked!")

# Markdown formatting
st.write("## This is a H2 Title!")
st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
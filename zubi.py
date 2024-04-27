import streamlit as st

# Function to display text based on button click
def display_text(text):
    st.write(text)
def set_background_image(image_url):
    # Apply custom CSS to set the background image
    page_bg_img = '''
    <style>
    .stApp {
        background-position: top;
        background-image: url(%s);
        background-size: cover;
    }

    @media (max-width: 768px) {
        /* Adjust background size for mobile devices /
        .stApp {
            background-position: top;
            background-size: contain;
            background-repeat: no-repeat;
        }
    }
    </style>
    ''' % image_url
    st.markdown(page_bg_img, unsafe_allow_html=True)


def main():
    # Set the background image URL
    background_image_url = "https://st5.depositphotos.com/1138869/65602/i/450/depositphotos_656029802-stock-photo-postcard-red-paper-hearts-love.jpg"

    # Set the background image
    set_background_image(background_image_url)

    custom_css = """
       <style>
       body {
           background-color: #4699d4;
           color: #ffffff;
           font-family: Arial, sans-serif;
       }
       select {
           background-color: #000000 !important; / Black background for select box /
           color: #ffffff !important; / White text within select box /
       }
       label {
           color: #ffffff !important; / White color for select box label */
       }
       </style>
       """
    st.markdown(custom_css, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
# Streamlit app
def main():
    st.title("To My Dearest Fiancé...")

    # Define button labels
    button_labels = [
        "Wishing you a very very happy birthday my dearest fiance. May this year bring a lot of happiness into your life and may you get a lot of success ahead.",
        "Allah aapko zindagi ke har Khushi se nawaaze Ameen. Allah aapko aapki mehnat ka ajar aata kare Ameen. Allah aapko tamaan khaabon ko pura karne ki himmat aata kare Ameen. Allah aapke saare gunaahon ku muaaf karde Ameen",
        "You're very very special to me. You're my good morning message and my goodnight message. You're my blush with zero rupees every time I see you I get a million dollars worth blush. You are so special that I can just see you for your entire life and I won't get bored. I JUST LOVE YOU SO MUCH.",
        "I just can write all day you know for you but aapko padhna bhi nai hoga itna  isliye to describe my excitement in a very good way which can grasp your attention. My very first and last desperate prayer will be to get married to you you're so warm+cute+ handsome+ adorable you're just like the man I imagined or I just manifested. You're my herooooooo.",
        "I wish I could be there for you to spend time with you and make good memories but I guess destiny made us be in LDR. and the fact that we never met but we are mad about each other and yes I really want to give this credit to you to make this stupid girl fall for a great man like you. I feel like I'm still in the dream and living the dream  all these moments feel like a beautiful poem. I BEEN SO IN LOVE WITH YOU.",
        "Chaliye ab agar yaha tak aa gaye ho toh sun lijiye. Ke you're not going away from this muskan. Again a very happy birthday babyyyyy."
    ]

    # Loop through buttons and display text based on button click
    button_names = ["Click here zubi", "Ab ye padhiye", "Abhi aur", "This day is very special", "This one's good", "Ok ok last one"]
    for i, label in enumerate(button_names):
        button_clicked = st.button(label)
        if button_clicked:
            display_text(button_labels[i])

if __name__ == "__main__":
    main()

import streamlit as st
import requests
import json
import base64
from PIL import Image
import io
import os
from datetime import datetime

# API Gateway Configuration
API_ENDPOINT = "https://5gu0r7t5d7.execute-api.us-west-2.amazonaws.com/prod/generate"

# Set page configuration
st.set_page_config(
    page_title="AI Watch Face Generator",
    page_icon="⌚",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 20px;
    }
    .title {
        text-align: center;
        color: #2c3e50;
    }
    </style>
    """, unsafe_allow_html=True)

def get_available_metrics(style):
    """Get available metrics based on selected style"""
    base_metrics = ["Time", "Date"]
    style_specific_metrics = {
        "Business": ["Calendar", "Appointments", "Weather", "Battery"],
        "Fitness": ["Heart Rate", "Steps", "Calories", "Distance"],
        "Industrial": ["Temperature", "Humidity", "Pressure", "Battery"],
        "Medical": ["Heart Rate", "Blood Oxygen", "ECG", "Steps"],
        "Cartoon": ["Mood", "Weather", "Pet Status", "Game Score"],
        "Sky": ["Weather", "Temperature", "Sunrise/Sunset", "Moon Phase"]
    }
    return base_metrics + style_specific_metrics.get(style, [])

def generate_watch_face(style, metrics):
    """Generate watch face using API"""
    try:
        response = requests.post(
            API_ENDPOINT,
            json={"style": style, "metrics": metrics},
            timeout=30
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error generating watch face: {response.text}")
            return None
            
    except requests.exceptions.Timeout:
        st.error("Request timed out. Please try again.")
        return None
    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to API. Please check your internet connection.")
        return None
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

def save_generated_image(image_data, style):
    """Save generated image with timestamp"""
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"watch_face_{style.lower()}_{timestamp}.png"
        
        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes))
        
        # Create 'generated' directory if it doesn't exist
        os.makedirs('generated', exist_ok=True)
        filepath = os.path.join('generated', filename)
        
        image.save(filepath)
        return filepath
    except Exception as e:
        st.error(f"Error saving image: {str(e)}")
        return None

def main():
    st.title("⌚ AI Watch Face Generator")
    st.markdown("---")

    # Create two columns for layout
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Design Options")
        
        # Style selection
        style = st.selectbox(
            "Select Watch Face Style",
            ["Business", "Fitness", "Industrial", "Medical", "Cartoon", "Sky"]
        )

        # Style description
        style_descriptions = {
            "Business": "Minimal and elegant design for professionals",
            "Fitness": "Dynamic layout focused on activity tracking",
            "Industrial": "Robust design with industrial elements",
            "Medical": "Clean interface for health monitoring",
            "Cartoon": "Playful and fun animated design",
            "Sky": "Nature-inspired with weather elements"
        }
        st.info(style_descriptions.get(style, ""))

        # Metrics selection
        metrics = st.multiselect(
            "Select Display Metrics",
            get_available_metrics(style)
        )

        # Generate button
        generate_pressed = st.button("Generate Watch Face")

    with col2:
        st.subheader("Preview")
        if generate_pressed:
            if not metrics:
                st.warning("Please select at least one metric!")
                return

            with st.spinner("Generating your watch face..."):
                result = generate_watch_face(style, metrics)
                
                if result and 'image' in result:
                    try:
                        # Save and display the image
                        filepath = save_generated_image(result['image'], style)
                        if filepath:
                            # Display the image with updated parameter
                            image = Image.open(filepath)
                            st.image(image, caption=f"{style} Watch Face", use_container_width=True)
                            
                            # Download button
                            with open(filepath, "rb") as file:
                                st.download_button(
                                    label="Download Watch Face",
                                    data=file,
                                    file_name=os.path.basename(filepath),
                                    mime="image/png"
                                )
                    except Exception as e:
                        st.error(f"Error processing image: {str(e)}")

        else:
            st.info("Click 'Generate Watch Face' to create your design")

        # Display selected metrics
        if metrics:
            st.markdown("### Selected Metrics")
            for metric in metrics:
                st.write(f"- {metric}")

if __name__ == "__main__":
    main()

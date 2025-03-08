#import streamlit
import streamlit as st

# Setting up title and description
st.title("✨ Unit Converter App ✨")
st.markdown("### Converts Length, Weight, Time and Temperature instantly")
st.write("Welcome!! Select a category, enter a value, and get the converted result in real-time.")

# Choosing category
category = st.selectbox("Choose a category", ["Length", "Weight", "Time","Temperature"])

# Function to convert units
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
    
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
    
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9
    return None  # If no valid conversion is selected

# Selecting conversion type based on category
if category == "Length":
    unit = st.selectbox("📏 Select conversion", ["Miles to Kilometers", "Kilometers to Miles"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("⏱️ Select conversion", [
        "Seconds to Minutes", "Minutes to Seconds", 
        "Minutes to Hours", "Hours to Minutes", 
        "Hours to Days", "Days to Hours"
    ])
elif category == "Temperature":
    unit = st.selectbox("🌡️ Select conversion", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
# Taking user input
value = st.number_input("Enter the value to convert")

# Performing conversion when button is clicked
if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"✅ The result is: {result:.2f}")
    else:
        st.error("⚠️ Invalid conversion. Please try again.")

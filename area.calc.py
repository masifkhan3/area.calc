import streamlit as st
import math

# Function to calculate the area of a given shape
def calculate_area(shape, dimensions):
    if shape == 'Circle':
        r = dimensions['radius']
        area = math.pi * (r ** 2)
    elif shape == 'Rectangle':
        l = dimensions['length']
        w = dimensions['width']
        area = l * w
    elif shape == 'Triangle':
        b = dimensions['base']
        h = dimensions['height']
        area = 0.5 * b * h
    elif shape == 'Trapezoid':
        a = dimensions['base1']
        b = dimensions['base2']
        h = dimensions['height']
        area = 0.5 * (a + b) * h
    elif shape == 'Square':
        s = dimensions['side']
        area = s ** 2
    elif shape == 'Parallelogram':
        b = dimensions['base']
        h = dimensions['height']
        area = b * h
    else:
        return "Shape not recognized."
    return area

def main():
    # Setting custom page config for Streamlit
    st.set_page_config(
        page_title="Interactive Area Calculator",
        page_icon="🧮",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Main title with emoji for a modern, colorful effect
    st.markdown("<h1 style='text-align: center; color: #FFA500;'>🧮 Interactive Area Calculator Dashboard</h1>", unsafe_allow_html=True)
    
    # Side panel for developer's name and additional instructions
    st.sidebar.title("Shape Area Calculator")
    st.sidebar.markdown("<h3 style='color: #FF5733;'>Select a shape and provide dimensions:</h3>", unsafe_allow_html=True)
    st.sidebar.markdown("### Developed by: Your Name")

    # Select shape in the sidebar with colored markdown
    shape = st.sidebar.selectbox(
        "Select a shape:",
        ("Circle", "Rectangle", "Triangle", "Trapezoid", "Square", "Parallelogram")
    )

    # Dictionary to store shape dimensions
    dimensions = {}

    # Displaying appropriate input fields for the selected shape with colorful headers
    st.markdown(f"<h2 style='color: #3498DB;'>Calculate the area of a {shape}</h2>", unsafe_allow_html=True)
    
    # Shape-specific input fields with sliders for easy interactivity
    if shape == 'Circle':
        dimensions['radius'] = st.slider("Radius (r):", min_value=0.0, max_value=100.0, step=0.1)

    elif shape == 'Rectangle':
        dimensions['length'] = st.slider("Length (l):", min_value=0.0, max_value=100.0, step=0.1)
        dimensions['width'] = st.slider("Width (w):", min_value=0.0, max_value=100.0, step=0.1)

    elif shape == 'Triangle':
        dimensions['base'] = st.slider("Base (b):", min_value=0.0, max_value=100.0, step=0.1)
        dimensions['height'] = st.slider("Height (h):", min_value=0.0, max_value=100.0, step=0.1)

    elif shape == 'Trapezoid':
        dimensions['base1'] = st.slider("Base 1 (a):", min_value=0.0, max_value=100.0, step=0.1)
        dimensions['base2'] = st.slider("Base 2 (b):", min_value=0.0, max_value=100.0, step=0.1)
        dimensions['height'] = st.slider("Height (h):", min_value=0.0, max_value=100.0, step=0.1)

    elif shape == 'Square':
        dimensions['side'] = st.slider("Side length (s):", min_value=0.0, max_value=100.0, step=0.1)

    elif shape == 'Parallelogram':
        dimensions['base'] = st.slider("Base (b):", min_value=0.0, max_value=100.0, step=0.1)
        dimensions['height'] = st.slider("Height (h):", min_value=0.0, max_value=100.0, step=0.1)

    # Progress bar to simulate calculation
    progress_bar = st.progress(0)
    
    # Calculate button with custom color
    if st.button("🔢 Calculate Area", key='calculate_button'):
        progress_bar.progress(100)  # simulate progress
        area = calculate_area(shape, dimensions)
        st.success(f"🎉 The area of the {shape} is: {area:.2f} square units")
    else:
        progress_bar.progress(0)

    # Using expander for additional information
    with st.expander("Click for more information"):
        st.write("This calculator helps you find the area of different geometric shapes like circles, rectangles, triangles, trapezoids, squares, and parallelograms.")

    # Footer with custom markdown and developer name
    st.markdown("---")
    st.markdown("<h4 style='text-align: center; color: #FF5733;'>Developed by: Your Name</h4>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

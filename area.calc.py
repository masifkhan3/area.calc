import streamlit as st
import math

def calculate_area(shape, dimensions):
    """
    Calculate the area of a given shape based on its dimensions.

    Parameters:
    shape (str): The shape of the area ('circle', 'rectangle', 'triangle', 'trapezoid', 'square', 'parallelogram').
    dimensions (dict): A dictionary containing dimensions of the shape.

    Returns:
    float: The area of the shape.
    """
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
    st.title("Area Calculator for Various Geometric Shapes")

    # Select the shape
    shape = st.selectbox(
        "Select a shape:",
        ("Circle", "Rectangle", "Triangle", "Trapezoid", "Square", "Parallelogram")
    )

    dimensions = {}

    # Input fields based on the selected shape
    if shape == 'Circle':
        dimensions['radius'] = st.number_input("Enter the radius (r):", min_value=0.0, step=0.1)

    elif shape == 'Rectangle':
        dimensions['length'] = st.number_input("Enter the length (l):", min_value=0.0, step=0.1)
        dimensions['width'] = st.number_input("Enter the width (w):", min_value=0.0, step=0.1)

    elif shape == 'Triangle':
        dimensions['base'] = st.number_input("Enter the base (b):", min_value=0.0, step=0.1)
        dimensions['height'] = st.number_input("Enter the height (h):", min_value=0.0, step=0.1)

    elif shape == 'Trapezoid':
        dimensions['base1'] = st.number_input("Enter the length of the first base (a):", min_value=0.0, step=0.1)
        dimensions['base2'] = st.number_input("Enter the length of the second base (b):", min_value=0.0, step=0.1)
        dimensions['height'] = st.number_input("Enter the height (h):", min_value=0.0, step=0.1)

    elif shape == 'Square':
        dimensions['side'] = st.number_input("Enter the side length (s):", min_value=0.0, step=0.1)

    elif shape == 'Parallelogram':
        dimensions['base'] = st.number_input("Enter the base (b):", min_value=0.0, step=0.1)
        dimensions['height'] = st.number_input("Enter the height (h):", min_value=0.0, step=0.1)

    # Button to calculate the area
    if st.button("Calculate Area"):
        area = calculate_area(shape, dimensions)
        st.success(f"The area of the {shape} is: {area:.2f} square units")

if __name__ == "__main__":
    main()

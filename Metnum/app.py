import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk metode Trapezoidal Rule
def trapezoidal_rule(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])
    return integral, x, y

# Fungsi utama aplikasi Streamlit
st.title("Trapezoidal Rule Calculator")
st.write("\nAplikasi ini menghitung integral menggunakan metode Trapezoidal Rule.")

# Input fungsi, batas, dan jumlah subinterval
function_input = st.text_input("Masukkan fungsi f(x):", "np.sin(x)")

a = st.number_input("Masukkan batas bawah (a):", value=0.0, format="%.2f")
b = st.number_input("Masukkan batas atas (b):", value=np.pi, format="%.2f")
n = st.slider("Pilih jumlah subinterval (n):", min_value=1, max_value=100, value=10)

# Mengevaluasi fungsi masukan
try:
    f = lambda x: eval(function_input)
    
    # Hitung integral dan hasilkan data untuk plot
    result, x_values, y_values = trapezoidal_rule(f, a, b, n)

    # Output hasil integral
    st.subheader("Hasil Integral")
    st.write(f"Hasil integral numerik: {result:.6f}")

    # Plot fungsi dan trapezoid
    fig, ax = plt.subplots()
    x_fine = np.linspace(a, b, 500)
    y_fine = f(x_fine)
    ax.plot(x_fine, y_fine, label="f(x)", color="blue")
    ax.fill_between(x_values, 0, y_values, alpha=0.3, step="mid", color="orange", label="Trapezoids")
    ax.scatter(x_values, y_values, color="red", label="Titik")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    ax.grid(True)

    # Tampilkan plot di Streamlit
    st.pyplot(fig)
except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")

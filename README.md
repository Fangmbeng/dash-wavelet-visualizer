# dash-wavelet-visualizer
### Repository Name:  
**dash-wavelet-visualizer**  

### Description:  
This project is a **Dash-based interactive application** that visualizes the **Haar wavelet decomposition** of random data. It allows users to dynamically adjust the decomposition level using a slider and observe how the wavelet transforms affect the data representation.  

### Features:  
- Uses **Dash** for interactive web-based visualization.  
- Implements **Haar wavelet decomposition** with **PyWavelets (pywt)**.  
- Provides a **slider-controlled UI** to adjust the decomposition level.  
- Uses **Plotly** for subplot-based visualization of wavelet coefficients.  

### Dependencies:  
- `dash`  
- `dash_core_components`  
- `dash_html_components`  
- `numpy`  
- `pywt`  
- `plotly`  

### Usage:  
1. Install dependencies:  
   ```bash
   pip install dash numpy pywavelets plotly
   ```
2. Run the script:  
   ```bash
   python app.py
   ```
3. Open the web browser at `http://127.0.0.1:8050/` to interact with the visualization.  

---

💡 **Note:** The code still uses `dash_html_components`, which is deprecated. You may want to replace it with `dash.html` to ensure long-term compatibility. Let me know if you have any improvements! 🚀

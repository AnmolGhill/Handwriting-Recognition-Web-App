# ✍️ Handwriting Recognition Web App

A real-time handwriting recognition web application powered by a custom-trained deep learning model. The AI model was trained on 60,000+ handwriting samples using Google Colab, achieving high accuracy in recognizing handwritten digits and characters.

🔗 **[Live Demo on Render](#)** *(https://penscan.onrender.com)*

---

## ✨ Features

- 🎨 **Interactive Canvas**: Draw directly on the web interface
- 🤖 **Custom AI Model**: Trained on 60,000+ handwriting samples
- ⚡ **Real-time Recognition**: Instant prediction as you write
- 🎯 **High Accuracy**: Deep learning model with optimized performance
- 📱 **Responsive Design**: Works on desktop and mobile devices
- 🚀 **Live Deployment**: Hosted on Render for easy access

---

## 🛠️ Tech Stack

### Frontend
- **HTML5** - Structure and canvas element
- **CSS3** - Modern styling and responsive design
- **JavaScript** - Interactive canvas and API communication

### Backend
- **Python** - Core backend logic
- **Flask/FastAPI** - Web framework for API
- **TensorFlow/PyTorch** - Deep learning framework
- **NumPy** - Numerical computations

### Training
- **Google Colab** - Model training environment
- **Jupyter Notebook** - Experimentation and visualization

### Deployment
- **Render** - Cloud hosting platform

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AnmolGhill/Handwriting-Recognition-Web-App.git
   cd Handwriting-Recognition-Web-App
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the app**
   - Open your browser and navigate to `http://localhost:5000`

---

## 📁 Project Structure

```
Handwriting-Recognition-Web-App/
├── templates/              # HTML templates
├── static/                 # CSS, JS, and static assets
├── app.py                  # Flask/FastAPI application
├── handwriting_model.h5    # Trained model file
├── requirements.txt        # Python dependencies
├── LICENSE                 # MIT License
└── README.md              # Project documentation
```

---

## 🧠 Model Training

The deep learning model was trained using Google Colab with the following specifications:

- **Dataset**: 60,000+ handwritten digit/character images
- **Architecture**: Convolutional Neural Network (CNN)
- **Framework**: TensorFlow/Keras or PyTorch
- **Training Environment**: Google Colab with GPU acceleration

### Dataset Source
The training dataset used is publicly available and consists of handwritten samples. The model was trained from scratch using this data.

---

## 🎯 How It Works

1. **User draws** on the HTML canvas using mouse or touch
2. **Canvas data** is captured and preprocessed
3. **Image sent** to backend Python API
4. **Model predicts** the handwritten character
5. **Result displayed** instantly on the interface

---

## 🌐 Deployment

This application is deployed on **Render** for production use.

### Deploy Your Own

1. Fork this repository
2. Create a new Web Service on [Render](https://render.com)
3. Connect your GitHub repository
4. Set the build command: `pip install -r requirements.txt`
5. Set the start command: `python app.py` or `gunicorn app:app`
6. Deploy!

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Anmol Ghill**
- GitHub: [@AnmolGhill](https://github.com/AnmolGhill)

---

## 🙏 Acknowledgments

- Dataset providers for the handwritten samples
- Google Colab for providing free GPU resources
- TensorFlow/PyTorch community for excellent documentation
- Open source community for inspiration and support

---

## 📞 Support

If you have any questions or issues:
- Open an [Issue](https://github.com/AnmolGhill/Handwriting-Recognition-Web-App/issues)
- Contact via GitHub

---

**Made with ❤️ and AI**
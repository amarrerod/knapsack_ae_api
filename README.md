
# 🎒 Knapsack Autoencoder API - FastAPI + Keras 🚀

Encode and decode variable-sized **0/1 Knapsack Problem** instances (from 50 to 1000 items) using a state-of-the-art **Autoencoder** served via **FastAPI**.

This project combines the flexibility of a custom-trained **Keras Autoencoder**, built with **exhaustive `keras_tuner` optimization** and **learning rate scheduling**, with the speed and simplicity of a FastAPI backend. It even supports reading problem instances directly from the file system.

---

## ✨ Features
* **Autoencoder**:

    * 🧠 **Variable Size Autoencoder** trained for knapsack instances with 50–1000 items.
    * 🔍 **Exhaustive hyperparameter tuning** via `keras_tuner` for optimal architecture.
    * 📉 **Dynamic learning rate scheduling** for better convergence.

* ⚡ **FastAPI-powered API** for quick encode/decode operations.
* 📁 **Filesystem support** to read and process instance files on the fly.
* 🧪 Ready for integration into optimization pipelines or benchmarking tools.
* Docker container available 

---

## 🔧 Endpoints

### `POST /encode`

Encode a knapsack instance to its latent representation.

```json
{
  "size": integer (2N+1),
  "variables": [w0,p0,w1,p1,....,wn-1,pn-1],
}
```

### `POST /decode`

Decode from a latent vector back to an approximate knapsack instance.

### `POST /encode/filename`

Upload a file (e.g., `.kp`) containing the knapsack instance. The expected structure of the file is:

```
N Q

w0 p0
w1 p1
...
wN-1 pN-1
```

---

## 🚀 Getting Started

### Clone the repo

```bash
git clone https://github.com/yourusername/knapsack-autoencoder-api.git
cd knapsack-ae-api
```

### Run the API

```bash
uv run fastapi run app/app.py
```

### Run using Docker

```bash
docker run -d -p 8000:80 amarrerd/knapsack_ae_api:0.0.1
```

---

## 🧠 Model Info

* Encoder/decoder trained using **Keras Functional API**.
* **Latent vector size** dynamically selected via hyperparameter tuning.
* **Trained dataset** includes 100,000+ synthetic knapsack instances.
* **Performance-optimized** using learning rate warmup and cosine decay.

---

## 📁 Example Files

Use the `/test` folder for sample knapsack problem files in supported formats.

---

## 📬 Contact

Feel free to open an issue or PR! Contributions and suggestions are welcome.

---
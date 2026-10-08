# Smart Hostel Room & Bed Allocation System (HMS)

A modern, full-featured web application for managing hostel room and bed allocations, student records, and occupancy analytics.

Built with Python and Streamlit.

---

## 🚀 Features

- **🏠 Live Room & Bed Map**: Real-time visual cards for all hostel rooms and bed statuses (`Full`, `Vacant`, `Partial`).
- **➕ Student Registration**: Easy registration form with validation and optional instant room allotment.
- **🛏️ Allocation Hub**: Seamless matching of unallocated students to vacant beds.
- **👥 Student Roster**: Complete searchable student directory with CSV export.
- **🚪 Bed Vacating**: One-click student checkout and bed release.
- **🔍 Digital Resident Pass**: Instant student lookup with printable verified digital ID badge.
- **📈 Capacity Analytics**: Altair visual charts of occupancy and department distribution.

---

## 🛠️ Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   streamlit run frontend.py
   ```

---

## ☁️ Deployment on Render

This repository is pre-configured for **Render** using `render.yaml`, `requirements.txt`, and `.streamlit/config.toml`.

### Option A: Automatic Blueprint Deployment
1. Push this repository to GitHub.
2. In [Render Dashboard](https://dashboard.render.com), click **New +** > **Blueprint**.
3. Connect your GitHub repository. Render will automatically detect `render.yaml` and configure everything.

### Option B: Manual Web Service Setup
1. In Render Dashboard, click **New +** > **Web Service**.
2. Connect your GitHub repository.
3. Configure settings:
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run frontend.py --server.port $PORT --server.address 0.0.0.0`
4. Click **Create Web Service**.

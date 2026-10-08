# 🏢 Smart Hostel Room & Bed Allocation System

An intuitive, modern hostel management and room/bed allocation system built with Python and Streamlit. This application streamlines hostel operations by offering visual room/bed tracking, automated vacancy management, real-time analytics, student directory management, and dual interfaces (Web GUI & CLI).

---

## ✨ Features

- **📊 Interactive Admin Dashboard**: Real-time KPI metrics displaying total rooms, total beds, occupied beds, available beds, occupancy rate, and unallocated students.
- **🛏️ Live Room Visualizer**: Visual room-by-room and bed-by-bed status cards (Occupied vs. Available) with instant student occupancy details.
- **➕ Student Management**: Register new students with ID, Name, Branch/Course, Academic Year, and Contact Number with validation checks.
- **🎯 Room & Bed Allocation**: Allocate students to available beds across rooms with automated validation preventing double allocation.
- **🚪 Vacate Bed**: Seamless checkout/deallocation mechanism that automatically updates room and bed availability.
- **🔍 Student Search**: Instantly find students and their allocation status by ID or Name.
- **📋 Student Directory**: Tabular view of all registered students with filtering and status indicators.
- **⚙️ Manage Rooms**: Add new rooms with custom bed capacity dynamically.
- **💻 Dual Interface**:
  - **Modern Streamlit Web App** (`frondend.py`)
  - **Terminal / CLI Interactive Menu** (`bachend.py`)

---

## 🛠️ Tech Stack

- **Frontend / UI**: [Streamlit](https://streamlit.io/), Custom CSS & HTML Components
- **Data Handling**: [Pandas](https://pandas.pydata.org/)
- **Core Backend**: Python 3.x
- **Deployment**: [Render](https://render.com/)

---

## 🚀 Getting Started Locally

### 1. Clone the Repository
```bash
git clone https://github.com/dhruv2201p/SMART-HOSTEL-ROOM-BED-ALLOCATION-SYSTEM.git
cd SMART-HOSTEL-ROOM-BED-ALLOCATION-SYSTEM
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Web Application
```bash
streamlit run frondend.py
```
Open your browser and navigate to `http://localhost:8501`.

### 4. (Optional) Run the Terminal CLI Version
```bash
python bachend.py
```

---

## 🌐 Deploy to Render

This project includes configuration ready for 1-click deployment on [Render](https://render.com/).

### Method 1: Using Render Blueprint (Automatic)
1. Go to your [Render Dashboard](https://dashboard.render.com/).
2. Click **New +** and select **Blueprint**.
3. Connect your repository: `https://github.com/dhruv2201p/SMART-HOSTEL-ROOM-BED-ALLOCATION-SYSTEM`.
4. Render will automatically detect [`render.yaml`](./render.yaml) and configure everything.
5. Click **Apply**.

### Method 2: Manual Web Service Setup
1. On [Render Dashboard](https://dashboard.render.com/), click **New +** > **Web Service**.
2. Select your GitHub repository: `SMART-HOSTEL-ROOM-BED-ALLOCATION-SYSTEM`.
3. Configure the following fields:
   - **Name**: `smart-hostel-allocation`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run frondend.py --server.port $PORT --server.address 0.0.0.0`
   - **Plan**: `Free`
4. Click **Deploy Web Service**.

---

## 📁 Project Structure

```plaintext
SMART-HOSTEL-ROOM-BED-ALLOCATION-SYSTEM/
├── .streamlit/
│   └── config.toml     # Streamlit server and cloud settings
├── frondend.py         # Streamlit Web Application (Modern UI, Visualizer, Dashboard)
├── bachend.py          # Terminal CLI Application & Core Logic
├── render.yaml         # Render Blueprint configuration
├── requirements.txt    # Project dependencies
├── .gitignore          # Git ignore file for Python cache & environment files
└── README.md           # Documentation
```

---

## 👤 Author

- **Dhruv Katharotiya** - [dhruv2201p](https://github.com/dhruv2201p)

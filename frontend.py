"""
SMART HOSTEL ROOM & BED ALLOCATION SYSTEM (HMS)
Frontend Web Application powered by Streamlit
"""

import streamlit as st
import pandas as pd
import altair as alt
import json
import time

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Smart Hostel | Room & Bed Allocation",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# Custom Modern CSS (Glassmorphism, Vibrant Dark Aesthetic)
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Main container background gradient */
    .stApp {
        background: radial-gradient(circle at 10% 20%, rgba(20, 26, 40, 1) 0%, rgba(13, 17, 23, 1) 90%);
        color: #e2e8f0;
    }

    /* Custom Header Banner */
    .hero-banner {
        background: linear-gradient(135deg, rgba(37, 99, 235, 0.2) 0%, rgba(139, 92, 246, 0.25) 50%, rgba(236, 72, 153, 0.15) 100%);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 26px 32px;
        margin-bottom: 24px;
        backdrop-filter: blur(16px);
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
    }

    .hero-title {
        font-size: 2.1rem;
        font-weight: 800;
        background: linear-gradient(120deg, #60a5fa, #a78bfa, #f472b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        letter-spacing: -0.5px;
    }

    .hero-subtitle {
        color: #94a3b8;
        font-size: 0.98rem;
        margin-top: 6px;
        margin-bottom: 0px;
    }

    /* Metric Cards */
    .stat-card {
        background: rgba(30, 41, 59, 0.65);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 18px 20px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .stat-card:hover {
        transform: translateY(-2px);
        border-color: rgba(129, 140, 248, 0.4);
    }
    .stat-val {
        font-size: 1.9rem;
        font-weight: 800;
        color: #ffffff;
        margin-top: 4px;
        letter-spacing: -0.5px;
    }
    .stat-lbl {
        color: #94a3b8;
        font-size: 0.82rem;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 0.8px;
    }

    /* Room Cards */
    .room-card {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 18px 20px;
        margin-bottom: 16px;
        backdrop-filter: blur(12px);
    }
    .room-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.06);
        padding-bottom: 8px;
    }
    .room-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #f1f5f9;
    }

    /* Bed slot chips */
    .bed-slot {
        background: rgba(15, 23, 42, 0.8);
        border-radius: 10px;
        padding: 10px 14px;
        margin-bottom: 8px;
        border: 1px solid rgba(255, 255, 255, 0.06);
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .bed-slot.occupied {
        border-left: 4px solid #8b5cf6;
        background: rgba(139, 92, 246, 0.08);
    }
    .bed-slot.available {
        border-left: 4px solid #10b981;
        background: rgba(16, 185, 129, 0.08);
    }

    /* Status Badges */
    .badge-full {
        background: rgba(239, 68, 68, 0.18);
        color: #f87171;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        border: 1px solid rgba(239, 68, 68, 0.3);
    }
    .badge-avail {
        background: rgba(16, 185, 129, 0.18);
        color: #34d399;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        border: 1px solid rgba(16, 185, 129, 0.3);
    }
    .badge-partial {
        background: rgba(245, 158, 11, 0.18);
        color: #fbbf24;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        border: 1px solid rgba(245, 158, 11, 0.3);
    }

    /* Student ID Card */
    .id-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.95) 100%);
        border: 1px solid rgba(139, 92, 246, 0.4);
        border-radius: 20px;
        padding: 24px 28px;
        box-shadow: 0 12px 35px -5px rgba(0, 0, 0, 0.6);
        position: relative;
        overflow: hidden;
    }
    .id-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; height: 5px;
        background: linear-gradient(90deg, #60a5fa, #a78bfa, #f472b6);
    }

    /* Tab enhancements */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(15, 23, 42, 0.6);
        padding: 6px;
        border-radius: 14px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px;
        color: #94a3b8;
        font-weight: 600;
        padding: 8px 18px;
    }
    .stTabs [aria-selected="true"] {
        background: rgba(99, 102, 241, 0.25) !important;
        color: #ffffff !important;
        border: 1px solid rgba(99, 102, 241, 0.4);
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# Default Hostel Data & State Management
# ---------------------------------------------------------
DEFAULT_ROOMS = {
    101: {"total_beds": 2, "beds": [None, None]},
    102: {"total_beds": 2, "beds": [None, None]},
    103: {"total_beds": 3, "beds": [None, None, None]},
    104: {"total_beds": 3, "beds": [None, None, None]},
    105: {"total_beds": 4, "beds": [None, None, None, None]}
}

DEFAULT_STUDENTS = [
    {
        "id": "STU101",
        "name": "Rahul Sharma",
        "course": "Computer Science",
        "year": "2nd Year",
        "contact": "9876543210",
        "room": 101,
        "bed": 1
    },
    {
        "id": "STU102",
        "name": "Priya Patel",
        "course": "AI & Data Science",
        "year": "3rd Year",
        "contact": "9812345678",
        "room": 101,
        "bed": 2
    },
    {
        "id": "STU103",
        "name": "Amit Verma",
        "course": "Mechanical Eng.",
        "year": "1st Year",
        "contact": "9723456789",
        "room": 103,
        "bed": 1
    },
    {
        "id": "STU104",
        "name": "Sneha Kulkarni",
        "course": "Electronics",
        "year": "4th Year",
        "contact": "9988776655",
        "room": 104,
        "bed": 1
    },
    {
        "id": "STU105",
        "name": "Devansh Mehta",
        "course": "Information Tech",
        "year": "2nd Year",
        "contact": "9123456780",
        "room": None,
        "bed": None
    }
]

def initialize_state():
    if "rooms" not in st.session_state:
        # Deep copy initial structure
        st.session_state.rooms = {
            r: {"total_beds": data["total_beds"], "beds": list(data["beds"])}
            for r, data in DEFAULT_ROOMS.items()
        }
        # Populate initial student bed allocations
        for s in DEFAULT_STUDENTS:
            if s["room"] is not None and s["bed"] is not None:
                r_num = s["room"]
                b_idx = s["bed"] - 1
                if r_num in st.session_state.rooms and b_idx < len(st.session_state.rooms[r_num]["beds"]):
                    st.session_state.rooms[r_num]["beds"][b_idx] = s["id"]

    if "students" not in st.session_state:
        st.session_state.students = [dict(s) for s in DEFAULT_STUDENTS]

    if "activity_log" not in st.session_state:
        st.session_state.activity_log = [
            {"time": "Initial Setup", "action": "System loaded with default demo records."}
        ]

initialize_state()


# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------
def get_student_by_id(student_id):
    for s in st.session_state.students:
        if str(s["id"]).strip().upper() == str(student_id).strip().upper():
            return s
    return None

def get_stats():
    rooms = st.session_state.rooms
    students = st.session_state.students
    total_rooms = len(rooms)
    total_beds = sum(r["total_beds"] for r in rooms.values())
    occupied_beds = sum(sum(1 for b in r["beds"] if b is not None) for r in rooms.values())
    available_beds = total_beds - occupied_beds
    allocated_students = sum(1 for s in students if s["room"] is not None)
    unallocated_students = len(students) - allocated_students
    occupancy_pct = (occupied_beds / total_beds * 100) if total_beds > 0 else 0
    return {
        "total_rooms": total_rooms,
        "total_beds": total_beds,
        "occupied_beds": occupied_beds,
        "available_beds": available_beds,
        "total_students": len(students),
        "allocated_students": allocated_students,
        "unallocated_students": unallocated_students,
        "occupancy_pct": occupancy_pct
    }

def allocate_student_to_room(student_id, room_number, preferred_bed=None):
    student = get_student_by_id(student_id)
    if not student:
        return False, "Student not found in registry."
    if student["room"] is not None:
        return False, f"Student is already allocated to Room {student['room']}, Bed {student['bed']}."

    room_number = int(room_number)
    if room_number not in st.session_state.rooms:
        return False, "Selected room does not exist."

    room = st.session_state.rooms[room_number]

    # Bed allocation logic
    chosen_bed_idx = None
    if preferred_bed is not None:
        target_idx = int(preferred_bed) - 1
        if 0 <= target_idx < len(room["beds"]) and room["beds"][target_idx] is None:
            chosen_bed_idx = target_idx
        else:
            return False, f"Bed {preferred_bed} in Room {room_number} is already occupied or invalid."
    else:
        # First available bed
        for i, occupant in enumerate(room["beds"]):
            if occupant is None:
                chosen_bed_idx = i
                break

    if chosen_bed_idx is None:
        return False, f"Room {room_number} has no available beds."

    # Perform allocation
    bed_number = chosen_bed_idx + 1
    room["beds"][chosen_bed_idx] = student["id"]
    student["room"] = room_number
    student["bed"] = bed_number

    st.session_state.activity_log.append({
        "time": time.strftime("%H:%M:%S"),
        "action": f"Allocated {student['name']} ({student['id']}) → Room {room_number}, Bed {bed_number}"
    })
    return True, f"Successfully allocated {student['name']} to Room {room_number}, Bed {bed_number}!"

def vacate_student_bed(student_id):
    student = get_student_by_id(student_id)
    if not student:
        return False, "Student not found in records."
    if student["room"] is None:
        return False, "This student does not currently hold an allocated bed."

    r_num = student["room"]
    b_num = student["bed"]

    if r_num in st.session_state.rooms:
        room = st.session_state.rooms[r_num]
        if b_num is not None and 1 <= b_num <= len(room["beds"]):
            room["beds"][b_num - 1] = None

    student["room"] = None
    student["bed"] = None

    st.session_state.activity_log.append({
        "time": time.strftime("%H:%M:%S"),
        "action": f"Vacated Bed {b_num} in Room {r_num} for {student['name']} ({student['id']})"
    })
    return True, f"Bed {b_num} in Room {r_num} successfully vacated for {student['name']}."


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("""
    <div style="display:flex; align-items:center; gap:12px; margin-bottom:18px;">
        <div style="font-size:2rem; background:linear-gradient(135deg, #6366f1, #06b6d4); padding:8px 12px; border-radius:12px;">🏨</div>
        <div>
            <div style="font-size:1.15rem; font-weight:800; color:#ffffff;">SmartHostel OS</div>
            <div style="font-size:0.75rem; color:#94a3b8; font-weight:600;">HMS ALLOCATION PORTAL</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    stats = get_stats()
    st.markdown("### 📊 Quick Overview")
    st.progress(stats["occupancy_pct"] / 100)
    st.markdown(f"**Occupancy:** `{stats['occupancy_pct']:.1f}%` ({stats['occupied_beds']}/{stats['total_beds']} Beds)")

    c1, c2 = st.columns(2)
    c1.metric("Rooms", stats["total_rooms"])
    c2.metric("Available", stats["available_beds"])

    st.markdown("---")
    st.markdown("### ⚙️ System Controls")

    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("🔄 Reset Demo", use_container_width=True, help="Reset to initial sample data"):
            st.session_state.rooms = {
                r: {"total_beds": data["total_beds"], "beds": list(data["beds"])}
                for r, data in DEFAULT_ROOMS.items()
            }
            st.session_state.students = [dict(s) for s in DEFAULT_STUDENTS]
            for s in DEFAULT_STUDENTS:
                if s["room"] is not None and s["bed"] is not None:
                    st.session_state.rooms[s["room"]]["beds"][s["bed"] - 1] = s["id"]
            st.session_state.activity_log = [{"time": time.strftime("%H:%M:%S"), "action": "Reset to default demo dataset."}]
            st.toast("System reset to sample dataset!", icon="🔄")
            st.rerun()

    with col_btn2:
        if st.button("🧹 Clear All", use_container_width=True, help="Clear all students & allocations"):
            st.session_state.rooms = {
                101: {"total_beds": 2, "beds": [None, None]},
                102: {"total_beds": 2, "beds": [None, None]},
                103: {"total_beds": 3, "beds": [None, None, None]},
                104: {"total_beds": 3, "beds": [None, None, None]},
                105: {"total_beds": 4, "beds": [None, None, None, None]}
            }
            st.session_state.students = []
            st.session_state.activity_log = [{"time": time.strftime("%H:%M:%S"), "action": "All student and bed records cleared."}]
            st.toast("All hostel data cleared!", icon="🧹")
            st.rerun()

    st.markdown("---")
    st.markdown("### 📜 Recent Log")
    if st.session_state.activity_log:
        for entry in reversed(st.session_state.activity_log[-4:]):
            st.caption(f"**{entry['time']}**: {entry['action']}")


# ---------------------------------------------------------
# Top Hero Banner
# ---------------------------------------------------------
st.markdown("""
<div class="hero-banner">
    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
        <div>
            <h1 class="hero-title">Smart Hostel Allocation System</h1>
            <p class="hero-subtitle">Comprehensive Room & Bed Management • Real-time Availability • Intelligent Student Assignment</p>
        </div>
        <div style="background:rgba(255,255,255,0.06); padding:8px 16px; border-radius:12px; border:1px solid rgba(255,255,255,0.1); text-align:right;">
            <div style="font-size:0.75rem; color:#94a3b8; font-weight:600; text-transform:uppercase;">Status</div>
            <div style="font-size:0.95rem; font-weight:700; color:#34d399;">● System Active</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# KPI Metric Row
# ---------------------------------------------------------
stats = get_stats()
kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

with kpi1:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-lbl">Total Rooms</div>
        <div class="stat-val" style="color:#60a5fa;">{stats['total_rooms']}</div>
        <div style="font-size:0.75rem; color:#94a3b8; margin-top:2px;">Configured Wings</div>
    </div>
    """, unsafe_allow_html=True)

with kpi2:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-lbl">Total Capacity</div>
        <div class="stat-val" style="color:#a78bfa;">{stats['total_beds']} Beds</div>
        <div style="font-size:0.75rem; color:#94a3b8; margin-top:2px;">Available hostel slots</div>
    </div>
    """, unsafe_allow_html=True)

with kpi3:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-lbl">Occupied Beds</div>
        <div class="stat-val" style="color:#f472b6;">{stats['occupied_beds']}</div>
        <div style="font-size:0.75rem; color:#94a3b8; margin-top:2px;">{stats['allocated_students']} Students Housed</div>
    </div>
    """, unsafe_allow_html=True)

with kpi4:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-lbl">Available Beds</div>
        <div class="stat-val" style="color:#34d399;">{stats['available_beds']}</div>
        <div style="font-size:0.75rem; color:#94a3b8; margin-top:2px;">Open for immediate allotment</div>
    </div>
    """, unsafe_allow_html=True)

with kpi5:
    pct_color = "#34d399" if stats["occupancy_pct"] < 60 else ("#fbbf24" if stats["occupancy_pct"] < 85 else "#f87171")
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-lbl">Occupancy Rate</div>
        <div class="stat-val" style="color:{pct_color};">{stats['occupancy_pct']:.1f}%</div>
        <div style="font-size:0.75rem; color:#94a3b8; margin-top:2px;">Capacity utilization</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)


# ---------------------------------------------------------
# Main Navigation Tabs
# ---------------------------------------------------------
tab_overview, tab_add, tab_alloc, tab_students, tab_vacate, tab_search, tab_analytics = st.tabs([
    "🏠 Live Room Grid",
    "➕ Add Student",
    "🛏️ Allocate Bed",
    "👥 Student Roster",
    "🚪 Vacate Bed",
    "🔍 Student Lookup",
    "📈 Analytics & Reports"
])


# =========================================================
# TAB 1: LIVE ROOM GRID & BED MAP
# =========================================================
with tab_overview:
    st.markdown("### 🛏️ Live Room & Bed Availability Map")
    st.markdown("Real-time visual map of all hostel rooms, bed statuses, and registered occupants.")

    # Filter controls
    col_f1, col_f2 = st.columns([2, 1])
    with col_f1:
        status_filter = st.radio(
            "Filter Rooms by Status:",
            ["All Rooms", "Available Rooms Only", "Fully Occupied Rooms"],
            horizontal=True
        )
    with col_f2:
        search_room_str = st.text_input("Quick Find Room Number:", placeholder="e.g. 101, 105")

    # Render Room Cards
    room_cols = st.columns(3)
    col_idx = 0

    rooms_dict = st.session_state.rooms

    for room_num, room_info in rooms_dict.items():
        # Search filter
        if search_room_str.strip() and str(room_num) not in search_room_str:
            continue

        total_b = room_info["total_beds"]
        occupied_b = sum(1 for b in room_info["beds"] if b is not None)
        avail_b = total_b - occupied_b

        if status_filter == "Available Rooms Only" and avail_b == 0:
            continue
        if status_filter == "Fully Occupied Rooms" and avail_b > 0:
            continue

        target_col = room_cols[col_idx % 3]
        col_idx += 1

        with target_col:
            # Status Badge Calculation
            if avail_b == 0:
                badge_html = '<span class="badge-full">FULL</span>'
            elif occupied_b == 0:
                badge_html = '<span class="badge-avail">VACANT</span>'
            else:
                badge_html = f'<span class="badge-partial">{avail_b} LEFT</span>'

            card_html = f"""
            <div class="room-card">
                <div class="room-header">
                    <div>
                        <span class="room-title">Room {room_num}</span>
                        <div style="font-size:0.8rem; color:#94a3b8;">{total_b}-Bed Capacity</div>
                    </div>
                    <div>{badge_html}</div>
                </div>
            """

            for bed_idx, occupant_id in enumerate(room_info["beds"]):
                bed_num = bed_idx + 1
                if occupant_id:
                    occupant = get_student_by_id(occupant_id)
                    occupant_name = occupant["name"] if occupant else occupant_id
                    occupant_branch = occupant["course"] if occupant else ""
                    card_html += f"""
                    <div class="bed-slot occupied">
                        <div>
                            <div style="font-size:0.85rem; font-weight:700; color:#e2e8f0;">
                                🛏️ Bed #{bed_num} <span style="font-size:0.75rem; color:#c084fc; font-weight:600;">(Occupied)</span>
                            </div>
                            <div style="font-size:0.78rem; color:#cbd5e1; margin-top:2px;">
                                {occupant_name} <span style="color:#94a3b8;">({occupant_id})</span>
                            </div>
                            <div style="font-size:0.72rem; color:#94a3b8;">{occupant_branch}</div>
                        </div>
                    </div>
                    """
                else:
                    card_html += f"""
                    <div class="bed-slot available">
                        <div>
                            <div style="font-size:0.85rem; font-weight:700; color:#34d399;">
                                🛏️ Bed #{bed_num} <span style="font-size:0.75rem; color:#10b981;">(Available)</span>
                            </div>
                            <div style="font-size:0.78rem; color:#94a3b8; margin-top:2px;">
                                Ready for allocation
                            </div>
                        </div>
                    </div>
                    """

            card_html += "</div>"
            st.markdown(card_html, unsafe_allow_html=True)


# =========================================================
# TAB 2: ADD STUDENT
# =========================================================
with tab_add:
    st.markdown("### ➕ Student Registration Portal")
    st.markdown("Register a new student into the hostel database with optional direct room allotment.")

    with st.form("add_student_form", clear_on_submit=True):
        col_s1, col_s2 = st.columns(2)

        with col_s1:
            st_id = st.text_input("Student Registration ID *", placeholder="e.g. STU106, 2026BCS045").strip()
            st_name = st.text_input("Full Name *", placeholder="e.g. Rohan Gupta").strip()
            st_course = st.selectbox(
                "Course / Branch *",
                [
                    "Computer Science & Engineering",
                    "AI & Data Science",
                    "Information Technology",
                    "Mechanical Engineering",
                    "Electrical & Electronics",
                    "Civil Engineering",
                    "Biotechnology",
                    "Business Administration",
                    "Other"
                ]
            )

        with col_s2:
            st_year = st.selectbox(
                "Academic Year *",
                ["1st Year", "2nd Year", "3rd Year", "4th Year", "Post Graduate"]
            )
            st_contact = st.text_input("Contact Number *", placeholder="e.g. 9876543210").strip()

            direct_allocate = st.checkbox("Allocate Room Immediately Upon Registration")
            selected_direct_room = None
            if direct_allocate:
                avail_room_choices = [
                    r for r, d in st.session_state.rooms.items()
                    if sum(1 for b in d["beds"] if b is None) > 0
                ]
                if avail_room_choices:
                    selected_direct_room = st.selectbox("Select Available Room:", avail_room_choices)
                else:
                    st.warning("All rooms are currently full! Cannot auto-allocate.")

        submit_student = st.form_submit_button("Register Student", use_container_width=True)

        if submit_student:
            if not st_id:
                st.error("Student ID cannot be empty!")
            elif get_student_by_id(st_id) is not None:
                st.error(f"Student ID '{st_id}' already exists in the registry!")
            elif not st_name:
                st.error("Student name cannot be empty!")
            elif not st_contact:
                st.error("Contact number cannot be empty!")
            else:
                new_student = {
                    "id": st_id.upper(),
                    "name": st_name,
                    "course": st_course,
                    "year": st_year,
                    "contact": st_contact,
                    "room": None,
                    "bed": None
                }
                st.session_state.students.append(new_student)
                st.session_state.activity_log.append({
                    "time": time.strftime("%H:%M:%S"),
                    "action": f"Registered student {st_name} ({st_id.upper()})"
                })

                if direct_allocate and selected_direct_room:
                    ok, msg = allocate_student_to_room(st_id.upper(), selected_direct_room)
                    if ok:
                        st.success(f"Student {st_name} registered AND {msg}")
                    else:
                        st.warning(f"Student registered, but allocation failed: {msg}")
                else:
                    st.success(f"Student {st_name} ({st_id.upper()}) successfully registered!")
                st.balloons()
                st.rerun()


# =========================================================
# TAB 3: ALLOCATE ROOM & BED
# =========================================================
with tab_alloc:
    st.markdown("### 🛏️ Room & Bed Allocation Hub")
    st.markdown("Assign unallocated registered students to vacant rooms and bed numbers.")

    unallocated_students = [s for s in st.session_state.students if s["room"] is None]

    if not unallocated_students:
        st.info("🎉 All registered students currently have allocated rooms & beds! Use the 'Add Student' tab to enroll new candidates.")
    else:
        col_al1, col_al2 = st.columns([1, 1])

        with col_al1:
            st.markdown("#### 1. Select Student")
            student_options = {
                f"{s['id']} - {s['name']} ({s['course']})": s['id']
                for s in unallocated_students
            }
            selected_label = st.selectbox("Choose Candidate for Allotment:", list(student_options.keys()))
            selected_sid = student_options[selected_label]
            selected_student_obj = get_student_by_id(selected_sid)

            if selected_student_obj:
                st.markdown(f"""
                <div style="background:rgba(15,23,42,0.6); padding:14px 18px; border-radius:12px; border:1px solid rgba(255,255,255,0.06); margin-top:8px;">
                    <div style="font-weight:700; color:#f8fafc; font-size:1.05rem;">{selected_student_obj['name']}</div>
                    <div style="font-size:0.85rem; color:#94a3b8; margin-top:2px;">ID: <span style="color:#60a5fa;">{selected_student_obj['id']}</span> | Year: {selected_student_obj['year']}</div>
                    <div style="font-size:0.85rem; color:#94a3b8;">Department: {selected_student_obj['course']}</div>
                    <div style="font-size:0.85rem; color:#94a3b8;">Phone: {selected_student_obj['contact']}</div>
                </div>
                """, unsafe_allow_html=True)

        with col_al2:
            st.markdown("#### 2. Select Room & Bed")

            available_rooms_map = {}
            for r_num, r_data in st.session_state.rooms.items():
                open_beds = [idx + 1 for idx, b in enumerate(r_data["beds"]) if b is None]
                if open_beds:
                    available_rooms_map[r_num] = open_beds

            if not available_rooms_map:
                st.error("No rooms have available beds! Please vacate beds or register more rooms.")
            else:
                chosen_room = st.selectbox(
                    "Choose Room:",
                    list(available_rooms_map.keys()),
                    format_func=lambda r: f"Room {r} ({len(available_rooms_map[r])} beds open)"
                )

                bed_options = ["Auto-assign next available"] + [f"Bed #{b}" for b in available_rooms_map[chosen_room]]
                chosen_bed_sel = st.selectbox("Preferred Bed Slot:", bed_options)

                pref_bed_num = None
                if chosen_bed_sel != "Auto-assign next available":
                    pref_bed_num = int(chosen_bed_sel.replace("Bed #", "").strip())

                st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

                if st.button("🚀 Confirm Room & Bed Allotment", use_container_width=True, type="primary"):
                    success, message = allocate_student_to_room(selected_sid, chosen_room, pref_bed_num)
                    if success:
                        st.success(message)
                        st.toast("Room allocation saved successfully!", icon="✅")
                        time.sleep(0.5)
                        st.rerun()
                    else:
                        st.error(message)


# =========================================================
# TAB 4: STUDENT ROSTER & ALLOCATED RECORDS
# =========================================================
with tab_students:
    st.markdown("### 👥 Student Directory & Allocation Roster")

    if not st.session_state.students:
        st.info("No students enrolled yet. Add students using the 'Add Student' tab or reset to demo data in the sidebar.")
    else:
        # Filter controls
        filter_col1, filter_col2, filter_col3 = st.columns([2, 1, 1])
        with filter_col1:
            roster_search = st.text_input("🔍 Search by Name, ID, or Branch:", placeholder="Type to filter...")
        with filter_col2:
            status_filter_roster = st.selectbox("Allocation Status:", ["All", "Allocated Only", "Unallocated Only"])
        with filter_col3:
            export_mode = st.selectbox("Actions:", ["View Table", "Export CSV"])

        # Filter students
        filtered_list = []
        for s in st.session_state.students:
            # Status filter
            if status_filter_roster == "Allocated Only" and s["room"] is None:
                continue
            if status_filter_roster == "Unallocated Only" and s["room"] is not None:
                continue
            # Text search
            query = roster_search.strip().lower()
            if query:
                if (query not in s["id"].lower() and
                    query not in s["name"].lower() and
                    query not in s["course"].lower() and
                    query not in str(s.get("room", "")).lower()):
                    continue
            filtered_list.append(s)

        df_students = pd.DataFrame([
            {
                "Student ID": s["id"],
                "Full Name": s["name"],
                "Course/Branch": s["course"],
                "Academic Year": s["year"],
                "Contact Number": s["contact"],
                "Room": f"Room {s['room']}" if s["room"] is not None else "—",
                "Bed": f"Bed {s['bed']}" if s["bed"] is not None else "—",
                "Status": "Allocated ✅" if s["room"] is not None else "Pending Allotment ⏳"
            }
            for s in filtered_list
        ])

        if export_mode == "Export CSV":
            csv_data = df_students.to_csv(index=False).encode('utf-8')
            st.download_button(
                "📥 Download Student Roster (CSV)",
                data=csv_data,
                file_name="hostel_students_allocation.csv",
                mime="text/csv",
                use_container_width=True
            )

        st.dataframe(
            df_students,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Student ID": st.column_config.TextColumn(width="small"),
                "Full Name": st.column_config.TextColumn(width="medium"),
                "Status": st.column_config.TextColumn(width="small"),
            }
        )

        st.markdown(f"Showing **{len(filtered_list)}** of **{len(st.session_state.students)}** students.")


# =========================================================
# TAB 5: VACATE BED
# =========================================================
with tab_vacate:
    st.markdown("### 🚪 Bed Vacating & Checkout Portal")
    st.markdown("Process student room checkouts and release bed allocations back to the available pool.")

    allocated_students = [s for s in st.session_state.students if s["room"] is not None]

    if not allocated_students:
        st.info("No students are currently allocated to any rooms.")
    else:
        v_col1, v_col2 = st.columns([1, 1])

        with v_col1:
            st.markdown("#### Select Resident to Vacate")
            vacate_dict = {
                f"{s['id']} - {s['name']} (Room {s['room']}, Bed {s['bed']})": s['id']
                for s in allocated_students
            }
            chosen_vacate_label = st.selectbox("Choose Student:", list(vacate_dict.keys()))
            vacate_sid = vacate_dict[chosen_vacate_label]
            target_student = get_student_by_id(vacate_sid)

        with v_col2:
            st.markdown("#### Checkout Summary")
            if target_student:
                st.markdown(f"""
                <div style="background:rgba(239, 68, 68, 0.08); border:1px solid rgba(239, 68, 68, 0.3); border-radius:14px; padding:18px;">
                    <div style="font-size:1.1rem; font-weight:700; color:#fca5a5;">⚠️ Confirm Bed Vacating</div>
                    <div style="margin-top:8px; font-size:0.9rem; color:#e2e8f0;">
                        <b>Resident:</b> {target_student['name']} ({target_student['id']})<br>
                        <b>Current Allotment:</b> Room {target_student['room']} • Bed #{target_student['bed']}<br>
                        <b>Course:</b> {target_student['course']} ({target_student['year']})
                    </div>
                    <div style="margin-top:10px; font-size:0.8rem; color:#f87171;">
                        Action will immediately release Bed #{target_student['bed']} in Room {target_student['room']} as available.
                    </div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
                if st.button("Confirm & Vacate Bed", type="primary", use_container_width=True):
                    ok, msg = vacate_student_bed(vacate_sid)
                    if ok:
                        st.success(msg)
                        st.toast("Bed vacated successfully!", icon="🚪")
                        time.sleep(0.5)
                        st.rerun()
                    else:
                        st.error(msg)


# =========================================================
# TAB 6: STUDENT LOOKUP & DIGITAL ID CARD
# =========================================================
with tab_search:
    st.markdown("### 🔍 Student Search & Digital Resident Pass")
    st.markdown("Lookup individual student profile and generate a verified digital hostel badge.")

    if not st.session_state.students:
        st.info("No students registered yet.")
    else:
        student_id_list = [f"{s['id']} - {s['name']}" for s in st.session_state.students]
        search_query = st.selectbox("Select or Type Student:", student_id_list)

        if search_query:
            query_id = search_query.split(" - ")[0].strip()
            student_rec = get_student_by_id(query_id)

            if student_rec:
                col_c1, col_c2 = st.columns([1.2, 1])

                with col_c1:
                    # Digital Resident ID Pass
                    is_allocated = student_rec["room"] is not None
                    room_badge = f"Room {student_rec['room']} • Bed #{student_rec['bed']}" if is_allocated else "Not Allocated (Waitlisted)"
                    badge_style = "color:#34d399; background:rgba(16,185,129,0.15);" if is_allocated else "color:#fbbf24; background:rgba(245,158,11,0.15);"

                    st.markdown(f"""
                    <div class="id-card">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <div style="font-size:0.75rem; letter-spacing:1px; font-weight:800; color:#a78bfa; text-transform:uppercase;">
                                SMART HOSTEL RESIDENT PASS
                            </div>
                            <div style="font-size:0.75rem; padding:3px 10px; border-radius:12px; font-weight:700; {badge_style}">
                                {'ACTIVE RESIDENT' if is_allocated else 'WAITLISTED'}
                            </div>
                        </div>

                        <div style="display:flex; gap:20px; align-items:center; margin-top:20px;">
                            <div style="width:75px; height:75px; border-radius:50%; background:linear-gradient(135deg, #6366f1, #ec4899); display:flex; align-items:center; justify-content:center; font-size:2rem; box-shadow:0 4px 15px rgba(99,102,241,0.4);">
                                👤
                            </div>
                            <div>
                                <div style="font-size:1.4rem; font-weight:800; color:#ffffff;">{student_rec['name']}</div>
                                <div style="font-size:0.85rem; color:#94a3b8; font-weight:600;">ID: {student_rec['id']}</div>
                            </div>
                        </div>

                        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:12px; margin-top:22px; padding-top:16px; border-top:1px solid rgba(255,255,255,0.08);">
                            <div>
                                <div style="font-size:0.72rem; color:#94a3b8; text-transform:uppercase; font-weight:600;">Department</div>
                                <div style="font-size:0.9rem; font-weight:600; color:#e2e8f0;">{student_rec['course']}</div>
                            </div>
                            <div>
                                <div style="font-size:0.72rem; color:#94a3b8; text-transform:uppercase; font-weight:600;">Year of Study</div>
                                <div style="font-size:0.9rem; font-weight:600; color:#e2e8f0;">{student_rec['year']}</div>
                            </div>
                            <div>
                                <div style="font-size:0.72rem; color:#94a3b8; text-transform:uppercase; font-weight:600;">Hostel Room & Bed</div>
                                <div style="font-size:0.95rem; font-weight:700; color:#60a5fa;">{room_badge}</div>
                            </div>
                            <div>
                                <div style="font-size:0.72rem; color:#94a3b8; text-transform:uppercase; font-weight:600;">Emergency Contact</div>
                                <div style="font-size:0.9rem; font-weight:600; color:#e2e8f0;">📞 {student_rec['contact']}</div>
                            </div>
                        </div>

                        <div style="margin-top:18px; padding-top:12px; border-top:1px dashed rgba(255,255,255,0.1); font-size:0.7rem; color:#64748b; display:flex; justify-content:space-between;">
                            <span>SmartHostel Management System Verified</span>
                            <span>Session 2026-27</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                with col_c2:
                    st.markdown("#### Quick Actions")
                    if is_allocated:
                        if st.button("🚪 Vacate This Bed Now", use_container_width=True):
                            ok, msg = vacate_student_bed(student_rec["id"])
                            if ok:
                                st.success(msg)
                                st.rerun()
                    else:
                        st.info("Student currently has no bed assigned. Go to the 'Allocate Bed' tab to assign a room.")


# =========================================================
# TAB 7: ANALYTICS & HOSTEL SUMMARY
# =========================================================
with tab_analytics:
    st.markdown("### 📈 Hostel Analytics & Capacity Intelligence")

    stats = get_stats()

    # Room Occupancy Chart Data
    room_chart_data = []
    for r_num, r_data in st.session_state.rooms.items():
        occ = sum(1 for b in r_data["beds"] if b is not None)
        tot = r_data["total_beds"]
        room_chart_data.append({
            "Room": f"Room {r_num}",
            "Occupied": occ,
            "Available": tot - occ,
            "Total": tot
        })

    df_rooms = pd.DataFrame(room_chart_data)

    c_chart1, c_chart2 = st.columns(2)

    with c_chart1:
        st.markdown("#### Bed Distribution by Room")
        df_melt = pd.melt(df_rooms, id_vars=["Room"], value_vars=["Occupied", "Available"], var_name="Status", value_name="Beds")
        chart = alt.Chart(df_melt).mark_bar(cornerRadius=6).encode(
            x=alt.X('Room:N', title='Room Number'),
            y=alt.Y('Beds:Q', title='Number of Beds'),
            color=alt.Color('Status:N', scale=alt.Scale(domain=['Occupied', 'Available'], range=['#8b5cf6', '#10b981'])),
            tooltip=['Room', 'Status', 'Beds']
        ).properties(height=320)
        st.altair_chart(chart, use_container_width=True)

    with c_chart2:
        st.markdown("#### Department Distribution")
        if st.session_state.students:
            dept_counts = pd.DataFrame([s["course"] for s in st.session_state.students], columns=["Department"]).value_counts().reset_index()
            dept_counts.columns = ["Department", "Students"]
            chart_dept = alt.Chart(dept_counts).mark_bar(cornerRadius=6).encode(
                y=alt.Y('Department:N', sort='-x', title=''),
                x=alt.X('Students:Q', title='Count'),
                color=alt.value('#38bdf8'),
                tooltip=['Department', 'Students']
            ).properties(height=320)
            st.altair_chart(chart_dept, use_container_width=True)
        else:
            st.info("No student data available to graph.")

    st.markdown("---")
    st.markdown("#### 📥 System Backup & Export")
    export_json_data = json.dumps({
        "rooms": st.session_state.rooms,
        "students": st.session_state.students,
        "exported_at": time.strftime("%Y-%m-%d %H:%M:%S")
    }, indent=2)

    st.download_button(
        "💾 Download Complete Hostel State (JSON)",
        data=export_json_data,
        file_name="hostel_backup.json",
        mime="application/json"
    )

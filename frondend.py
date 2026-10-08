import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Smart Hostel Allocation System",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# Custom Styling (CSS)
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Main container background & padding */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Hero Header */
    .hero-banner {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 18px;
        padding: 26px 32px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.4);
    }
    .hero-title {
        font-size: 2.1rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.02em;
        background: linear-gradient(90deg, #38bdf8 0%, #818cf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-subtitle {
        font-size: 0.98rem;
        color: #94a3b8;
        margin-top: 6px;
        margin-bottom: 0px;
    }

    /* Metric Cards */
    .stat-card {
        background: rgba(30, 41, 59, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 18px 20px;
        text-align: left;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .stat-card:hover {
        transform: translateY(-2px);
        border-color: rgba(99, 102, 241, 0.4);
    }
    .stat-label {
        font-size: 0.82rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #94a3b8;
        margin-bottom: 4px;
    }
    .stat-value {
        font-size: 1.85rem;
        font-weight: 800;
        color: #f8fafc;
        line-height: 1.2;
    }
    .stat-subtext {
        font-size: 0.8rem;
        margin-top: 4px;
        color: #64748b;
    }

    /* Room Cards */
    .room-container {
        background: #182234;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 16px;
        margin-bottom: 16px;
    }
    .room-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
        padding-bottom: 8px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    }
    .room-number {
        font-size: 1.15rem;
        font-weight: 700;
        color: #f1f5f9;
    }

    /* Bed chips */
    .bed-badge {
        display: inline-block;
        border-radius: 8px;
        padding: 6px 12px;
        font-size: 0.8rem;
        font-weight: 600;
        margin: 4px 6px 4px 0;
    }
    .bed-badge-available {
        background: rgba(16, 185, 129, 0.15);
        color: #34d399;
        border: 1px solid rgba(16, 185, 129, 0.3);
    }
    .bed-badge-occupied {
        background: rgba(239, 68, 68, 0.15);
        color: #f87171;
        border: 1px solid rgba(239, 68, 68, 0.3);
    }

    /* Student details card */
    .student-card {
        background: #1e293b;
        border: 1px solid rgba(255, 255, 255, 0.09);
        border-radius: 14px;
        padding: 20px;
        margin-top: 15px;
    }

    /* Status Pills */
    .status-pill {
        padding: 3px 10px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        display: inline-block;
    }
    .status-available {
        background-color: rgba(16, 185, 129, 0.2);
        color: #10b981;
    }
    .status-full {
        background-color: rgba(239, 68, 68, 0.2);
        color: #ef4444;
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# State Initialization (In-Memory Session Persistence)
# ---------------------------------------------------------
if "rooms" not in st.session_state:
    st.session_state.rooms = {
        101: {"total_beds": 2, "beds": ["STU-101", None]},
        102: {"total_beds": 2, "beds": ["STU-102", None]},
        103: {"total_beds": 3, "beds": [None, None, None]},
        104: {"total_beds": 3, "beds": [None, None, None]},
        105: {"total_beds": 4, "beds": [None, None, None, None]}
    }

if "students" not in st.session_state:
    st.session_state.students = [
        {
            "id": "STU-101",
            "name": "Aarav Sharma",
            "course": "Computer Engineering",
            "year": "2nd Year",
            "contact": "9876543210",
            "room": 101,
            "bed": 1
        },
        {
            "id": "STU-102",
            "name": "Priya Patel",
            "course": "Information Technology",
            "year": "1st Year",
            "contact": "9876543211",
            "room": 102,
            "bed": 1
        },
        {
            "id": "STU-103",
            "name": "Rohan Mehta",
            "course": "Mechanical Engineering",
            "year": "3rd Year",
            "contact": "9876543212",
            "room": None,
            "bed": None
        }
    ]


# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------
def get_student_by_id(student_id):
    for s in st.session_state.students:
        if s["id"] == student_id:
            return s
    return None

def compute_hostel_metrics():
    total_rooms = len(st.session_state.rooms)
    total_beds = sum(r["total_beds"] for r in st.session_state.rooms.values())
    occupied_beds = sum(
        sum(1 for bed in r["beds"] if bed is not None)
        for r in st.session_state.rooms.values()
    )
    available_beds = total_beds - occupied_beds
    allocated_students = sum(1 for s in st.session_state.students if s["room"] is not None)
    unallocated_students = len(st.session_state.students) - allocated_students
    occupancy_pct = (occupied_beds / total_beds * 100) if total_beds > 0 else 0

    return {
        "total_rooms": total_rooms,
        "total_beds": total_beds,
        "occupied_beds": occupied_beds,
        "available_beds": available_beds,
        "allocated_students": allocated_students,
        "unallocated_students": unallocated_students,
        "occupancy_pct": occupancy_pct
    }


# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("### 🏢 Hostel Admin Portal")
    st.caption("Smart Room & Bed Allocation Engine")
    st.divider()

    menu_option = st.radio(
        "Navigation",
        [
            "📊 Dashboard & Summary",
            "🛏️ Live Room Visualizer",
            "➕ Add New Student",
            "🎯 Allocate Room & Bed",
            "🚪 Vacate Bed",
            "🔍 Search Student",
            "📋 Student Directory",
            "⚙️ Manage Rooms"
        ],
        index=0
    )

    st.divider()
    metrics = compute_hostel_metrics()
    st.markdown(f"**Quick Stats:**")
    st.progress(metrics["occupancy_pct"] / 100.0)
    st.caption(f"Occupancy Rate: **{metrics['occupancy_pct']:.1f}%** ({metrics['occupied_beds']}/{metrics['total_beds']} Beds)")
    st.caption(f"Unallocated Students: **{metrics['unallocated_students']}**")


# ---------------------------------------------------------
# Top Hero Banner
# ---------------------------------------------------------
st.markdown("""
<div class="hero-banner">
    <div class="hero-title">🏢 Smart Hostel Room & Bed Allocation</div>
    <div class="hero-subtitle">Real-time room occupancy tracking, smart student-to-bed allocation, and dormitory management.</div>
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# PAGE 1: Dashboard & Summary
# ---------------------------------------------------------
if menu_option == "📊 Dashboard & Summary":
    st.subheader("Hostel Overview & Key Metrics")
    m = compute_hostel_metrics()

    # 4 Top Metric Cards
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-label">Total Rooms</div>
            <div class="stat-value">{m['total_rooms']}</div>
            <div class="stat-subtext">Active wings & floors</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-label">Total Beds</div>
            <div class="stat-value">{m['total_beds']}</div>
            <div class="stat-subtext">Hostel capacity</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-label">Occupied Beds</div>
            <div class="stat-value" style="color: #f87171;">{m['occupied_beds']}</div>
            <div class="stat-subtext">{m['occupancy_pct']:.1f}% Occupancy</div>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-label">Available Beds</div>
            <div class="stat-value" style="color: #34d399;">{m['available_beds']}</div>
            <div class="stat-subtext">Ready for allocation</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Secondary row: Student stats & quick actions
    col_left, col_right = st.columns([1.2, 1])

    with col_left:
        st.markdown("#### 🛏️ Room Availability Breakdown")
        room_data = []
        for r_num, r_info in sorted(st.session_state.rooms.items()):
            occ = sum(1 for b in r_info["beds"] if b is not None)
            avail = r_info["total_beds"] - occ
            status = "FULL" if avail == 0 else "AVAILABLE"
            room_data.append({
                "Room": f"Room {r_num}",
                "Total Beds": r_info["total_beds"],
                "Occupied": occ,
                "Available": avail,
                "Status": status
            })

        df_rooms = pd.DataFrame(room_data)
        st.dataframe(
            df_rooms,
            use_container_width=True,
            hide_index=True
        )

    with col_right:
        st.markdown("#### 👥 Student Roster Summary")
        st.info(f"**Total Registered Students:** {len(st.session_state.students)}")
        st.success(f"**Allocated Students:** {m['allocated_students']}")
        if m['unallocated_students'] > 0:
            st.warning(f"**Students Awaiting Beds:** {m['unallocated_students']}")
        else:
            st.caption("All registered students currently have an allocated bed.")

        # Quick visual of occupied rooms
        st.markdown("##### Overall Bed Occupancy")
        st.progress(m["occupancy_pct"] / 100.0)
        st.caption(f"{m['occupied_beds']} of {m['total_beds']} total beds occupied across {m['total_rooms']} rooms.")


# ---------------------------------------------------------
# PAGE 2: Live Room Visualizer
# ---------------------------------------------------------
elif menu_option == "🛏️ Live Room Visualizer":
    st.subheader("Interactive Room & Bed Floor Visualizer")
    st.caption("Inspect bed occupancy per room. Green slots represent available beds; red slots indicate occupied beds.")

    cols = st.columns(2)
    rooms_sorted = sorted(st.session_state.rooms.items())

    for idx, (r_num, r_info) in enumerate(rooms_sorted):
        col = cols[idx % 2]
        occupied_count = sum(1 for b in r_info["beds"] if b is not None)
        avail_count = r_info["total_beds"] - occupied_count
        status_text = "FULL" if avail_count == 0 else f"{avail_count} Bed(s) Available"
        status_class = "status-full" if avail_count == 0 else "status-available"

        with col:
            with st.container():
                st.markdown(f"""
                <div class="room-container">
                    <div class="room-header">
                        <span class="room-number">🚪 Room {r_num}</span>
                        <span class="status-pill {status_class}">{status_text}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Show bed pills
                bed_cols = st.columns(len(r_info["beds"]))
                for b_idx, bed_occupant in enumerate(r_info["beds"]):
                    bed_number = b_idx + 1
                    with bed_cols[b_idx]:
                        if bed_occupant is None:
                            st.button(
                                f"🛏️ Bed {bed_number}\n(Available)",
                                key=f"vis_avail_{r_num}_{bed_number}",
                                disabled=True,
                                use_container_width=True
                            )
                        else:
                            student = get_student_by_id(bed_occupant)
                            s_name = student["name"] if student else bed_occupant
                            st.button(
                                f"👤 Bed {bed_number}\n{s_name[:10]}..",
                                key=f"vis_occ_{r_num}_{bed_number}",
                                help=f"Occupied by: {s_name} ({bed_occupant})",
                                use_container_width=True
                            )
            st.markdown("<br>", unsafe_allow_html=True)


# ---------------------------------------------------------
# PAGE 3: Add New Student
# ---------------------------------------------------------
elif menu_option == "➕ Add New Student":
    st.subheader("Register a New Student")
    st.caption("Enroll a new student into the hostel registry.")

    with st.form("add_student_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            student_id = st.text_input("Student ID *", placeholder="e.g. STU-104").strip()
            student_name = st.text_input("Full Name *", placeholder="e.g. Ananya Sen").strip()
            course = st.text_input("Course / Branch *", placeholder="e.g. Computer Science").strip()
        with col2:
            year = st.selectbox(
                "Academic Year *",
                ["1st Year", "2nd Year", "3rd Year", "4th Year", "Postgraduate"]
            )
            contact = st.text_input("Contact Number *", placeholder="e.g. 9876543219").strip()

        submitted = st.form_submit_button("➕ Register Student", use_container_width=True)

        if submitted:
            # Validations
            if not student_id or not student_name or not course or not contact:
                st.error("Please fill in all required fields!")
            elif any(s["id"].lower() == student_id.lower() for s in st.session_state.students):
                st.error(f"Student ID '{student_id}' already exists! Please use a unique ID.")
            else:
                new_student = {
                    "id": student_id,
                    "name": student_name,
                    "course": course,
                    "year": year,
                    "contact": contact,
                    "room": None,
                    "bed": None
                }
                st.session_state.students.append(new_student)
                st.success(f"Student **{student_name}** ({student_id}) registered successfully!")
                st.info("You can now assign a room and bed using the 'Allocate Room & Bed' tab.")


# ---------------------------------------------------------
# PAGE 4: Allocate Room & Bed
# ---------------------------------------------------------
elif menu_option == "🎯 Allocate Room & Bed":
    st.subheader("Assign Room & Bed to Student")
    st.caption("Match registered students with available hostel beds.")

    # Find unallocated students
    unallocated = [s for s in st.session_state.students if s["room"] is None]

    if not unallocated:
        st.info("🎉 All registered students currently have beds assigned!")
    else:
        # Create student dropdown options
        student_options = {
            f"{s['id']} - {s['name']} ({s['course']})": s
            for s in unallocated
        }

        selected_label = st.selectbox(
            "Select Student for Allocation:",
            options=list(student_options.keys())
        )
        selected_student = student_options[selected_label]

        # Find rooms with at least one free bed
        available_rooms = {
            r_num: r_info for r_num, r_info in st.session_state.rooms.items()
            if any(b is None for b in r_info["beds"])
        }

        if not available_rooms:
            st.error("⚠️ All rooms are currently full! No beds available for allocation.")
        else:
            col_r, col_b = st.columns(2)

            with col_r:
                room_choices = sorted(list(available_rooms.keys()))
                selected_room = st.selectbox(
                    "Select Room:",
                    options=room_choices,
                    format_func=lambda r: f"Room {r} ({sum(1 for b in available_rooms[r]['beds'] if b is None)} free beds)"
                )

            with col_b:
                # Find available beds in the selected room
                room_beds = available_rooms[selected_room]["beds"]
                free_bed_indices = [
                    idx + 1 for idx, b in enumerate(room_beds) if b is None
                ]
                selected_bed = st.selectbox(
                    "Select Bed Number:",
                    options=free_bed_indices,
                    format_func=lambda b: f"Bed #{b}"
                )

            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("🚀 Confirm Room & Bed Allocation", type="primary", use_container_width=True):
                # Update room bed
                st.session_state.rooms[selected_room]["beds"][selected_bed - 1] = selected_student["id"]

                # Update student object
                selected_student["room"] = selected_room
                selected_student["bed"] = selected_bed

                st.success(
                    f"✅ Successfully allocated **Room {selected_room}**, **Bed {selected_bed}** to "
                    f"**{selected_student['name']}** ({selected_student['id']})!"
                )
                st.rerun()


# ---------------------------------------------------------
# PAGE 5: Vacate Bed
# ---------------------------------------------------------
elif menu_option == "🚪 Vacate Bed":
    st.subheader("Vacate an Occupied Bed")
    st.caption("Release an assigned bed back to the hostel pool.")

    allocated_students = [s for s in st.session_state.students if s["room"] is not None]

    if not allocated_students:
        st.info("No students are currently occupying beds.")
    else:
        student_vacate_options = {
            f"{s['id']} - {s['name']} (Room {s['room']}, Bed {s['bed']})": s
            for s in allocated_students
        }

        selected_vacate_label = st.selectbox(
            "Select Student to Vacate:",
            options=list(student_vacate_options.keys())
        )
        student_to_vacate = student_vacate_options[selected_vacate_label]

        st.warning(
            f"Are you sure you want to release **Bed {student_to_vacate['bed']}** "
            f"in **Room {student_to_vacate['room']}** occupied by **{student_to_vacate['name']}**?"
        )

        if st.button("🚪 Vacate Bed Now", type="secondary", use_container_width=True):
            r_num = student_to_vacate["room"]
            b_num = student_to_vacate["bed"]

            # Clear bed
            if r_num in st.session_state.rooms:
                st.session_state.rooms[r_num]["beds"][b_num - 1] = None

            # Clear student allocation
            student_to_vacate["room"] = None
            student_to_vacate["bed"] = None

            st.success(f"Bed {b_num} in Room {r_num} is now available again!")
            st.rerun()


# ---------------------------------------------------------
# PAGE 6: Search Student
# ---------------------------------------------------------
elif menu_option == "🔍 Search Student":
    st.subheader("Student Lookup & Details")
    st.caption("Search student records by ID, Name, or Branch.")

    search_query = st.text_input("Enter Student ID or Name:", placeholder="e.g. STU-101 or Aarav").strip().lower()

    if search_query:
        matches = [
            s for s in st.session_state.students
            if search_query in s["id"].lower()
            or search_query in s["name"].lower()
            or search_query in s["course"].lower()
        ]

        if not matches:
            st.error(f"No student found matching '{search_query}'.")
        else:
            st.success(f"Found {len(matches)} matching student(s):")
            for s in matches:
                with st.container():
                    c_info, c_alloc = st.columns([2, 1])
                    with c_info:
                        st.markdown(f"### 👤 {s['name']}")
                        st.write(f"**Student ID:** `{s['id']}`")
                        st.write(f"**Course/Branch:** {s['course']}")
                        st.write(f"**Year:** {s['year']}")
                        st.write(f"**Contact:** {s['contact']}")
                    with c_alloc:
                        st.markdown("#### Allocation Status")
                        if s["room"] is not None:
                            st.success(f"🏠 **Room:** {s['room']}\n\n🛏️ **Bed:** {s['bed']}")
                        else:
                            st.warning("⚠️ **Not Allocated**\n\nAwaiting bed assignment.")
                    st.divider()
    else:
        st.info("Type a student ID or name above to view complete details.")


# ---------------------------------------------------------
# PAGE 7: Student Directory
# ---------------------------------------------------------
elif menu_option == "📋 Student Directory":
    st.subheader("Student Master Directory")
    st.caption("Complete list of registered students with allocation statuses.")

    filter_choice = st.radio(
        "Filter List:",
        ["All Students", "Allocated Only", "Unallocated Only"],
        horizontal=True
    )

    if filter_choice == "Allocated Only":
        display_list = [s for s in st.session_state.students if s["room"] is not None]
    elif filter_choice == "Unallocated Only":
        display_list = [s for s in st.session_state.students if s["room"] is None]
    else:
        display_list = st.session_state.students

    if not display_list:
        st.info("No students found matching current filter.")
    else:
        formatted_data = []
        for s in display_list:
            formatted_data.append({
                "Student ID": s["id"],
                "Full Name": s["name"],
                "Course": s["course"],
                "Academic Year": s["year"],
                "Contact": s["contact"],
                "Room": f"Room {s['room']}" if s["room"] else "—",
                "Bed": f"Bed {s['bed']}" if s["bed"] else "—",
                "Status": "Allocated" if s["room"] else "Pending"
            })

        df = pd.DataFrame(formatted_data)
        st.dataframe(df, use_container_width=True, hide_index=True)

        # Export to CSV
        csv_data = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Student Directory (CSV)",
            data=csv_data,
            file_name="hostel_students_allocation.csv",
            mime="text/csv"
        )


# ---------------------------------------------------------
# PAGE 8: Manage Rooms
# ---------------------------------------------------------
elif menu_option == "⚙️ Manage Rooms":
    st.subheader("Hostel Room & Inventory Configuration")
    st.caption("Add new rooms and manage room bed capacities.")

    col_add, col_list = st.columns([1, 1.2])

    with col_add:
        st.markdown("#### ➕ Add New Room")
        with st.form("add_room_form"):
            new_room_no = st.number_input("Room Number", min_value=101, max_value=999, step=1, value=106)
            new_bed_count = st.number_input("Bed Capacity", min_value=1, max_value=10, step=1, value=2)

            add_room_btn = st.form_submit_button("Add Room to Inventory", use_container_width=True)
            if add_room_btn:
                if new_room_no in st.session_state.rooms:
                    st.error(f"Room {new_room_no} already exists!")
                else:
                    st.session_state.rooms[new_room_no] = {
                        "total_beds": int(new_bed_count),
                        "beds": [None] * int(new_bed_count)
                    }
                    st.success(f"Room {new_room_no} with {new_bed_count} beds added successfully!")
                    st.rerun()

    with col_list:
        st.markdown("#### 🏢 Current Room Inventory")
        inv_data = []
        for r_no, r_val in sorted(st.session_state.rooms.items()):
            occ = sum(1 for b in r_val["beds"] if b is not None)
            inv_data.append({
                "Room Number": r_no,
                "Total Capacity": r_val["total_beds"],
                "Occupied Beds": occ,
                "Available Beds": r_val["total_beds"] - occ
            })
        st.dataframe(pd.DataFrame(inv_data), use_container_width=True, hide_index=True)

import streamlit as st
import json
from email_handler import save_email

st.set_page_config(page_title="Sydney Events", layout="wide")

# Custom Clean CSS
st.markdown("""
    <style>
        html, body {
            background-color: #f9fafb;
            font-family: 'Segoe UI', sans-serif;
        }
        .event-card {
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
        }
        .event-title {
            font-size: 1.4rem;
            font-weight: 600;
            color: #1a202c;
            margin-bottom: 0.4rem;
        }
        .event-meta {
            font-size: 0.95rem;
            color: #4a5568;
            margin-bottom: 1rem;
        }
        .event-desc {
            font-size: 0.95rem;
            color: #2d3748;
            margin-bottom: 1rem;
        }
        .ticket-btn {
            background-color: #3b82f6;
            color: white;
            padding: 0.55rem 1.2rem;
            border-radius: 6px;
            border: none;
            font-size: 0.95rem;
            font-weight: 500;
            transition: background-color 0.2s ease;
        }
        .ticket-btn:hover {
            background-color: #2563eb;
        }
        .stTextInput > div > div > input {
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h2 style='text-align: center; color: #1f2937;'>Sydney City Events</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1rem; color: #6b7280;'>A curated list of upcoming events in Sydney. Updated regularly.</p>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar
st.sidebar.header("Filter Events")
category = st.sidebar.selectbox("Category", ["All", "Music", "Tech", "Art", "Business"])
date_filter = st.sidebar.selectbox("Date", ["All", "This Week", "This Month"])

# Load data
def load_events():
    with open("event_data.json", "r") as f:
        return json.load(f)

events = load_events()

# Render each event (without image)
for event in events:
    if category != "All" and category.lower() not in event["title"].lower():
        continue

    with st.container():
        st.markdown('<div class="event-card">', unsafe_allow_html=True)

        st.markdown(f'<div class="event-title">{event["title"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="event-meta">📍 {event["location"]} | 🗓️ {event["date_time"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="event-desc">{event["description"]}</div>', unsafe_allow_html=True)

        with st.expander("Reserve / Get Tickets"):
            email = st.text_input("Your Email", key=f"email-{event['title']}")
            opt_in = st.checkbox("I agree to receive updates", key=f"opt-{event['title']}")

            if st.button("Get Tickets", key=f"submit-{event['title']}"):
                if email and opt_in:
                    save_email(email)
                    st.success("Redirecting you to the event page...")
                    st.markdown(f"<a href='{event['link']}' target='_blank' class='ticket-btn'>Go to Event Page</a>", unsafe_allow_html=True)
                else:
                    st.warning("Please enter your email and agree to updates.")

        st.markdown('</div>', unsafe_allow_html=True)

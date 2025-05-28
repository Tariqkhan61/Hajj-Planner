import streamlit as st

# --- HajjTrip Class ---
class HajjTrip:
    def __init__(self, budget, family_members):
        self.budget = budget
        self.family_members = family_members
        self.Hajj_cost_per_person = 1200000  # Corrected Cost of Hajj per person in PKR
        self.total_cost = self.Hajj_cost_per_person * self.family_members
        self.is_sufficient = self.budget >= self.total_cost

    def plan_trip(self):
        if self.is_sufficient:
            st.success(f"🎉 Congratulations! You can perform Hajj with your family of {self.family_members}.")
        else:
            st.error(f"🚨 Unfortunately, you do not have enough budget to perform Hajj with your family of {self.family_members}.")
        st.info(f"👉 Total Hajj Cost: {self.total_cost:,.0f} PKR")

# --- Streamlit UI ---
st.markdown("<h1 style='color: green;'>🕋 Hajj Trip Planner🕌</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: orange;'>Plan Your Blessed Journey</h2>", unsafe_allow_html=True)

# --- User Input ---
budget = st.number_input("Enter Your Budget (PKR)", min_value=0)
family_members = st.number_input("Enter Number of Family Members", min_value=1, step=1)

# --- Button to Check Feasibility ---
if st.button("Check Feasibility"):
    hajj_trip = HajjTrip(budget, family_members)
    hajj_trip.plan_trip()

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>🟧 It is made with ❤️‍🩹 <strong style='font-size: 30px; color: purple;'>Muhammad Tariq MahboobⓂ️</strong></p>", unsafe_allow_html=True)
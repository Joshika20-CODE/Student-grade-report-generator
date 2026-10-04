import streamlit as st

st.set_page_config(
    page_title="Student Grade Report",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Grade Report Generator")
st.write("Enter student details and marks to generate the report.")

# Student details
name = st.text_input("Student Name")
register_no = st.text_input("Register Number")

st.subheader("📚 Enter Marks")

tamil = st.number_input("Tamil", min_value=0, max_value=100, value=0)
english = st.number_input("English", min_value=0, max_value=100, value=0)
maths = st.number_input("Mathematics", min_value=0, max_value=100, value=0)
science = st.number_input("Science", min_value=0, max_value=100, value=0)
computer = st.number_input("Computer Science", min_value=0, max_value=100, value=0)

if st.button("Generate Grade Report"):

    marks = [tamil, english, maths, science, computer]

    total = sum(marks)
    average = total / len(marks)

    # Grade calculation
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    # Result
    if all(mark >= 35 for mark in marks):
        result = "PASS ✅"
    else:
        result = "FAIL ❌"

    st.success("Grade Report Generated!")

    st.subheader("📋 Student Grade Report")

    st.write("**Student Name:**", name)
    st.write("**Register Number:**", register_no)

    st.write("---")

    st.write("**Tamil:**", tamil)
    st.write("**English:**", english)
    st.write("**Mathematics:**", maths)
    st.write("**Science:**", science)
    st.write("**Computer Science:**", computer)

    st.write("---")

    st.write("### 📊 Result Summary")
    st.write("**Total Marks:**", total, "/ 500")
    st.write("**Average:**", round(average, 2), "%")
    st.write("**Grade:**", grade)
    st.write("**Result:**", result)
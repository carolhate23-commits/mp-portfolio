import streamlit as st

st.markdown("""<style>
[data-testid="stSidebar"] {
    background-color:pink;
}
[data-testid="stSidebar"] * {
    color: black;
}
.stApp {
   background-color:lightblue;
}  

.main {
    text-align: center;
}
img {
    border-radius: 50%;
}
.title {
    font-size: 40px;
    font-weight: bold;
}
.subtitle {
    font-size: 20px;
    color: gray;
}
.box {
    background-color: #f0f2f6;
    padding: 15px;
    border-radius: 10px;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

st.title("🧑‍💻 :green[About Me]")

st.write(""" 
I am a Computer Science Student at DEBESMSCAT I enjoy creating a basic Graphic design 
""")
st.subheader("🎓:red[Education]")
st.write("- Bachelor of Science in Computer Science")
st.write("- 3rd year student at DEBESMSCAT")
st.subheader("🎯:red[Goals]")
st.write("- My goal is to finish my studies And improve my skills in programming ")
st.write("- I want to build a Web App")

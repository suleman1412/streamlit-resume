from pathlib import Path
import streamlit as st
from PIL import Image



# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Suleman Karigar"
PAGE_ICON = ":wave:"
NAME = "Suleman Karigar"
DESCRIPTION = """
Data Engineer skilled in Python, database management and building pipelines based on business requirement.
"""
EMAIL = "sulemanhsk01@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/sulemankarigar",
    "GitHub": "https://github.com/suleman1412",
    "Twitter": "https://twitter.com/suletexh",
}
PROJECTS = {
    "🏆 Schipol Airport Stats - Designed to provide a clear picture of aviation activity at Schiphol Airport": "https://aeroatlas.streamlit.app",
    "🏆 Reddit Video Downloader Bot - A reddit bot downloads the video and provides a downloadable link for the user. ": "https://github.com/suleman1412/reddit-video-downloader-bot",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="centered")


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic,width=None)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button( 
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))

for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].markdown(f"<div style='text-align: center;'><a href='{link}'>{platform}</a></div>", unsafe_allow_html=True)
    

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✅ Strong hands-on experience and knowledge in Python and SQL
- ✅ Good understanding of statistical principles and their respective applications
- ✅ Excellent team-player and displaying strong sense of initiative on tasks
"""
)
# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Pandas, Numpy, Scikit-learn), SQL, C/C++
- 🗄️ Databases: Postgres, Snowflake, BigQuery, DuckDB
- 🛠️ Tools: MageAI, Talend

"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Programmer Analyst Trainee | Cognizant**")
st.write("06/2023 - Present")
st.write(
    """
- ► Developed and optimized over 50 customized data feeds using Snowflake and Talend ETL.
- ► Implemented reusable Talend job components, driving a 30% productivity gain in feed development cycles.
- ► Collaborated with business analysts to identify client requirements and leveraged Talend ETL tool to design and develop integrated data feeds, reports, and extracts from on-premises and cloud data sources.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Engineering Intern | Cognizant**")
st.write("01/2023 - 05/2023")
st.write(
    """
- ► Successfully completed an intensive internship program, demonstrating proficiency in Python, SQL, and Microsoft Azure
- ► Leveraged newfound skills to optimize database queries and automate data processing.
- ► Applied SQL fundamentals to support database management.
- ► Acquired foundational knowledge of Microsoft Azure, applying principles to successfully complete a COVID capstone project.
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")






with st.sidebar:
    # --- Reach out to me ---
    st.sidebar.header("📩 Contact Me")
    contact_form = f"""
    <form action="https://formsubmit.co/sulemanhsk01@gmail.com" method="POST">
    <div class="contact-form">
    <input type="hidden" name="_captcha" value="false">
    <div class='name'><input type="text" name="name" placeholder="Your name" required style="width: 100%;"></div>
    <div class='mail'><input type="email" name="email" placeholder="Your email" required style="width: 100%;"></div>
    <div class='message'><textarea name="message" placeholder="Your message here" required style="width: 100%;"></textarea></div>
    <div class='button'><button type="submit"> 📨 Send</button></div>
    </div>
    </form>
    """
    st.sidebar.markdown(contact_form,unsafe_allow_html=True)
   
import streamlit as st
import base64
from PIL import Image
import io

# Page configuration
st.set_page_config(
    page_title="Samarth - Digital Portfolio",
    page_icon="🧑‍💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for impressive styling and effects
def load_css():
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    /* Global Styles */
    .main {
        padding-top: 2rem;
    }
    
    /* Hero Section with Gradient Background */
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 4rem 2rem;
        border-radius: 20px;
        margin-bottom: 3rem;
        text-align: center;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }
    
    .hero-title {
        font-family: 'Inter', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        color: white;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .hero-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.5rem;
        color: rgba(255,255,255,0.9);
        margin-bottom: 2rem;
    }
    
    /* Animated Button */
    .cta-button {
        display: inline-block;
        padding: 12px 30px;
        background: rgba(255,255,255,0.2);
        color: #000000;
        text-decoration: none;
        border-radius: 50px;
        font-weight: 600;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.3);
        transition: all 0.3s ease;
    }
    
    .cta-button:hover {
        background: rgba(255,255,255,0.3);
        transform: translateY(-2px);
        color: #000000;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        text-decoration: underline;
    }
    
    /* Project Cards with Hover Effects */
    .project-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        border: 1px solid rgba(0,0,0,0.05);
        height: 100%;
    }
    
    .project-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
    }
    
    .project-title {
        font-family: 'Inter', sans-serif;
        font-size: 1.5rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 1rem;
    }
    
    .project-description {
        color: #7f8c8d;
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }
    
    /* Tech Stack Tags */
    .tech-tag {
        display: inline-block;
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        margin: 2px;
        font-weight: 500;
    }
    
    /* Blur Effect Container */
    .blur-container {
        backdrop-filter: blur(10px);
        background: rgba(255,255,255,0.8);
        border-radius: 15px;
        padding: 2rem;
        border: 1px solid rgba(255,255,255,0.3);
    }
    
    /* Navigation Pills */
    .nav-pills {
        display: flex;
        justify-content: center;
        margin: 2rem 0;
        gap: 1rem;
    }
    
    .nav-pill {
        padding: 10px 20px;
        background: #f8f9fa;
        border-radius: 25px;
        cursor: pointer;
        transition: all 0.3s ease;
        border: none;
        color: #495057;
        font-weight: 500;
    }
    
    .nav-pill.active {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
    }
    
    /* Skills Progress Bars */
    .skill-item {
        margin-bottom: 1.5rem;
    }
    
    .skill-name {
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: #2c3e50;
    }
    
    .skill-bar {
        background: #ecf0f1;
        height: 10px;
        border-radius: 10px;
        overflow: hidden;
    }
    
    .skill-progress {
        height: 100%;
        background: linear-gradient(90deg, #667eea, #764ba2);
        border-radius: 10px;
        animation: fillBar 2s ease-in-out;
    }
    
    @keyframes fillBar {
        from { width: 0; }
        to { width: var(--width); }
    }
    
    /* Contact Section */
    .contact-section {
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
        color: white;
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-top: 3rem;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        .hero-subtitle {
            font-size: 1.2rem;
        }
    }
    
    /* Hide Streamlit Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Function to convert image to base64 for embedding
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# Navigation
def create_navigation():
    st.markdown("""
        <style>
            .fixed-nav {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                z-index: 100;
                background-color: #222222;  /* Or any color you want */
                padding: 5px;
                box-shadow: 0 2px 4px rgba(0,0,0,.1);
            }
            .nav-pills {
                display: flex;
                justify-content: center;
                gap: 15px;
            }
            .nav-pill {
                padding: 8px 16px;
                border: none;
                background-color: #f0f2f6;
                border-radius: 50px;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            .nav-pill:hover, .nav-pill.active {
                background-color: #007bff;
                color: white;
            }
            .content-spacer {
                height: 60px; /* Adjust this value to the height of your navbar */
            }
        </style>
        
        <div class="fixed-nav">
            <div class="nav-pills">
                <a href="#home" style = "color:black;text-decoration:none;"class="nav-pill active" id="nav-home">Home</a>
                <a href="#featured-projects" style = "color:black;text-decoration:none;"class="nav-pill" id="nav-projects">Projects</a>
                <a href="#technical-skills" style = "color:black;text-decoration:none;"class="nav-pill" id="nav-skills">Skills</a>
                <a href="#about-me" style = "color:black;text-decoration:none;"class="nav-pill" id="nav-contact">About Me</a>            
                <a href="#lets-connect" style = "color:black;text-decoration:none;"class="nav-pill" id="nav-contact">Contact</a>
            </div>
        </div>
        <div class="content-spacer"></div>
        
        <script>
            document.querySelectorAll('.nav-pill').forEach(pill => {
                pill.addEventListener('click', function(event) {
                    event.preventDefault(); // Prevents the default anchor jump
                    
                    // Your existing logic for removing and adding the active class
                    document.querySelectorAll('.nav-pill').forEach(p => {
                        p.classList.remove('active');
                    });
                    event.target.classList.add('active');
                    
                    // Your existing scroll logic
                    const sectionId = this.getAttribute('href').substring(1);
                    const section = document.getElementById(sectionId);
                    
                    if (section) {
                        const headerOffset = 60;
                        const elementPosition = section.getBoundingClientRect().top;
                        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                        
                        window.scrollTo({
                            top: offsetPosition,
                            behavior: "smooth"
                        });
                    }
                });
            });
        </script>
    """, unsafe_allow_html=True)

# Hero Section
def create_hero_section():
    st.markdown("""
    <div class="hero-section" id="home">
        <h1 class="hero-title">Hi, I'm Samarth!</h1>
        <p class="hero-subtitle">Prospective Data Scientist</p>
        <a href="#featured-projects" style = "color:black;text-decoration:none;" class="cta-button">View My Work</a>
    </div>
    """, unsafe_allow_html=True)

# Projects Section
def create_projects_section():
    st.markdown("<h2 style='text-align: center; margin: 3rem 0 2rem 0; font-size: 2.5rem; color: #2c3e50;'>Featured Projects</h2>", unsafe_allow_html=True)
    
    # Sample project data
    projects = [
        {
            "title": "AI-Powered Web Scraper",
            "description": "Built a intelligent web scraping tool using Python, BeautifulSoup, and machine learning to automatically extract and categorize data from various websites.",
            "tech_stack": ["Python", "BeautifulSoup", "Pandas", "Scikit-learn"],
            "github_link": "https://github.com/yourusername/project1"
        },
        {
            "title": "Real-Time Data Dashboard",
            "description": "Created an interactive dashboard using Streamlit and Plotly to visualize real-time financial data with advanced filtering and analysis capabilities.",
            "tech_stack": ["Streamlit", "Plotly", "PostgreSQL", "APIs"],
            "github_link": "https://github.com/yourusername/project2"
        },
        {
            "title": "Machine Learning Classifier",
            "description": "Developed a multi-class classification model achieving 95% accuracy for predicting customer behavior using ensemble methods and feature engineering.",
            "tech_stack": ["Python", "TensorFlow", "Pandas", "NumPy"],
            "github_link": "https://github.com/yourusername/project3"
        }
    ]
    
    # Create project cards in columns
    cols = st.columns(len(projects))
    for idx, project in enumerate(projects):
        with cols[idx]:
            tech_tags = "".join([f'<span class="tech-tag">{tech}</span>' for tech in project["tech_stack"]])
            
            st.markdown(f"""
            <div class="project-card">
                <h3 class="project-title">{project['title']}</h3>
                <p class="project-description">{project['description']}</p>
                <div style="margin-bottom: 1rem;">
                    {tech_tags}
                </div>
                <a href="{project['github_link']}" target="_blank" style="
                    display: inline-block;
                    padding: 8px 16px;
                    background: linear-gradient(45deg, #667eea, #764ba2);
                    color: white;
                    text-decoration: none;
                    border-radius: 25px;
                    font-size: 0.9rem;
                    font-weight: 500;
                ">View Project</a>
            </div>
            """, unsafe_allow_html=True)

# Skills Section with Progress Bars
def create_skills_section():
    st.markdown("<h2 style='text-align: center; margin: 3rem 0 2rem 0; font-size: 2.5rem; color: #2c3e50;'>Technical Skills</h2>", unsafe_allow_html=True)
    
    skills = {
        "Python": 90,
        "Data Analysis": 85,
        "Machine Learning": 80,
        "Web Development": 75,
        "SQL": 85,
        "Git/GitHub": 80
    }
    
    col1, col2 = st.columns(2)
    
    skill_items = list(skills.items())
    mid_point = len(skill_items) // 2
    
    with col1:
        for skill, level in skill_items[:mid_point]:
            st.markdown(f"""
            <div class="skill-item">
                <div class="skill-name">{skill}</div>
                <div class="skill-bar">
                    <div class="skill-progress" style="--width: {level}%; width: {level}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        for skill, level in skill_items[mid_point:]:
            st.markdown(f"""
            <div class="skill-item">
                <div class="skill-name">{skill}</div>
                <div class="skill-bar">
                    <div class="skill-progress" style="--width: {level}%; width: {level}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# Contact Section
def create_contact_section():
    st.markdown("""
    <div class="contact-section" id="contact">
        <h2 style="margin-bottom: 1rem; font-size: 2.5rem;">Let's Connect</h2>
        <p style="font-size: 1.2rem; margin-bottom: 2rem; opacity: 0.9;">
            Interested in collaborating or have a project in mind?
        </p>
        <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;">
            <a href="mailto:samsrinivas678@gmail.com" style="color: white; text-decoration: none; font-size: 1.1rem;">
                📧 Email
            </a>
            <a href="https://linkedin.com/in/yourprofile" style="color: white; text-decoration: none; font-size: 1.1rem;">
                💼 LinkedIn
            </a>
            <a href="https://github.com/Sam-ProgStack" style="color: white; text-decoration: none; font-size: 1.1rem;">
                🐙 GitHub
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
def create_about_me_section():
    st.markdown("""
    <div class = "about-me-section" id = "about">
        <h2 style="margin-bottom: 1rem; align-items: center; font-size:2.5rem;">About Me</h2>
        <h4 style="margin-bottom: 1rem; font-size:2.5rem;">My Motive</h4>

        <p style="font-size:1.2rem; margin-bottom:2rem; opacity:0.9;">
            I want to help the world through research in automation using AI and Machine Learning.
        </p>
    </div>
                
                
                """, unsafe_allow_html=True)
# Interactive Features
def add_interactive_elements():
    # Floating particles effect
    st.markdown("""
    <script>
    // Add floating particles animation
    function createParticles() {
        const container = document.querySelector('.main');
        if (!container) return;
        
        for (let i = 0; i < 20; i++) {
            const particle = document.createElement('div');
            particle.style.cssText = `
                position: fixed;
                width: 4px;
                height: 4px;
                background: linear-gradient(45deg, #667eea, #764ba2);
                border-radius: 50%;
                pointer-events: none;
                opacity: 0.6;
                animation: float ${5 + Math.random() * 10}s infinite linear;
                left: ${Math.random() * 100}%;
                top: 100%;
                z-index: -1;
            `;
            container.appendChild(particle);
        }
    }
    
    // CSS for particle animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes float {
            0% {
                transform: translateY(0) rotate(0deg);
                opacity: 0.6;
            }
            100% {
                transform: translateY(-100vh) rotate(360deg);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
    
    // Initialize particles
    setTimeout(createParticles, 1000);
    </script>
    """, unsafe_allow_html=True)

# Main App
def main():
    # Load custom CSS
    load_css()
    
    # Add interactive elements
    add_interactive_elements()
    
    # Create navigation
    create_navigation()
    
    # Create hero section
    create_hero_section()
    
    # Create projects section
    create_projects_section()
    
    # Create skills section
    create_skills_section()
    
    create_about_me_section()
    # Create contact section
    create_contact_section()
    
    # Add some spacing at the bottom
    st.markdown("<br><br>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
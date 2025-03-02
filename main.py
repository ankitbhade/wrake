import streamlit as st
from wrake import wrake_website
from wrake import split_dom_content
from wrake import extract_body_content
from wrake import clean_body_content
from parse import parse_with_ollama
import pathlib

# Set page configuration
st.set_page_config(
    page_title="wrake - the web rake",
    page_icon="🍁",
    layout="wide"
)

# Load external CSS
def load_css(css_file):
    with open(css_file) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the CSS file
css_path = pathlib.Path(__file__).parent / "static" / "styles.css"
load_css(css_path)

# Header
st.title("🍁 wrake - the web rake")
st.markdown("<p style='text-align: center; color: #B0B0B0; margin-bottom: 2rem;'>AI web scraper to rake leaves of data in the vast forest of the web</p>", unsafe_allow_html=True)

# Main content
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    url = st.text_input("", placeholder="Enter website URL...")

    if st.button("wrake it"):
        with st.spinner("Wraking the website..."):
            result = wrake_website(url)
            body_content = extract_body_content(result)
            cleaned_content = clean_body_content(body_content)
            st.session_state.dom_content = cleaned_content
            
            st.markdown("<div class='status-message success'>✅ Website content extracted successfully!</div>", unsafe_allow_html=True)

if "dom_content" in st.session_state:
    st.markdown("---")
    
    # Two-column layout for content and parsing
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🍂 Extracted Pile")
        with st.expander("View DOM Content", expanded=True):
            st.text_area("", st.session_state.dom_content, height=400)
    
    with col2:
        st.markdown("### 🍂 Wrake Leaves")
        parse_description = st.text_area("", placeholder="Describe what information you want to extract...", height=150)

        if st.button("Ask wrake 🔍"):
            if parse_description:
                with st.spinner("Wraking your query..."):
                    dom_chunks = split_dom_content(st.session_state.dom_content)
                    parsed_result = parse_with_ollama(dom_chunks, parse_description)
                    
                    if parsed_result.strip():
                        st.markdown("<div class='status-message success'>🍁 Wraked leaves</div>", unsafe_allow_html=True)
                        st.markdown("""
                        <div class="parsed-results">
                            {}
                        </div>
                        """.format(parsed_result.replace('\n', '<br>')), unsafe_allow_html=True)
                    else:
                        st.markdown("<div class='status-message warning'>ℹ️ No matching information found</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='status-message warning'>⚠️ Please describe what information you want to extract</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")

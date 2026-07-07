import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load API environment keys if using a .env file locally
load_dotenv()

st.set_page_config(page_title="AI Lecture Workspace", page_icon="🎙️", layout="wide")

st.title("🎙️ AI-Powered Lecture & Meeting Summarizer")
st.caption("Phase 1 Production Prototype — Powered by Groq Ultra-Low Latency Inference")
st.write("---")

# Initialize Client safely
api_key = os.environ.get("GROQ_API_KEY") or st.sidebar.text_input("Enter Groq API Key:", type="password")

if not api_key:
    st.info("💡 Please provide a Groq API Key in the sidebar or via environment variables to run the engine.")
else:
    client = Groq(api_key=api_key)
    
    # UI Layout Split
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📤 Upload Audio Content")
        uploaded_file = st.file_uploader(
            "Select lecture or meeting recording", 
            type=["mp3", "wav", "m4a", "ogg", "flac"]
        )
        
        # Audio Player Preview if file is detected
        if uploaded_file:
            st.audio(uploaded_file, format=f"audio/{uploaded_file.type.split('/')[-1]}")
            
    with col2:
        st.subheader("⚡ Processing Diagnostics")
        if uploaded_file and st.button("🔥 Generate Academic Summary"):
            try:
                with st.spinner("Step 1: Uploading buffer & running ASR Transcription..."):
                    # Pass tuple with format (filename, binary_stream) directly to api
                    transcription = client.audio.transcriptions.create(
                        file=(uploaded_file.name, uploaded_file.read()),
                        model="whisper-large-v3-turbo",
                        response_format="json",
                        temperature=0.0
                    )
                
                raw_text = transcription.text
                st.success("✅ Speech-To-Text pipeline succeeded!")
                
                with st.spinner("Step 2: Formatting text structures using LLM context maps..."):
                    # Structured Prompt Engineering Layer
                    prompt = f"""
                    You are an elite academic editor. Convert the following rough transcript into highly structured markdown notes.
                    
                    Follow this structural blueprint exactly:
                    ## 📋 Overall Context Summary
                    Provide a detailed 3-paragraph executive overview.
                    
                    ## 🔑 Core Technical Concepts
                    * **Concept Name**: Direct, rigorous definition and details from the text.
                    
                    ## 📝 Step-by-Step Task Checklist & Deadlines
                    * [ ] Actionable task mentioned in the audio.
                    """
                    
                    completion = client.chat.completions.create(
                        messages=[
                            {"role": "system", "content": prompt},
                            {"role": "user", "content": raw_text}
                        ],
                        model="llama-3.3-70b-versatile", # High intelligence reasoning model
                        temperature=0.3
                    )
                
                final_notes = completion.choices[0].message.content
                
                # Render results dynamically in a tabular/workspace layout
                st.write("---")
                st.subheader("📝 Generated Output Workspace")
                
                tab1, tab2 = st.tabs(["✨ AI Structured Notes", "📜 Raw Transcript Line-by-Line"])
                with tab1:
                    st.markdown(final_notes)
                with tab2:
                    st.text_area("Verbatim Text Output", value=raw_text, height=400)
                    
            except Exception as e:
                st.error(f"Execution failed down the pipeline: {str(e)}")
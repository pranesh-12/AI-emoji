#!/usr/bin/env python3
"""
Emoji Translator AI - Streamlit Web Interface
Interactive web UI for emoji translation with real-time preview
"""

import streamlit as st
import json
import os
from datetime import datetime
from translator import EmojiTranslator

# Configure Streamlit page
st.set_page_config(
    page_title="Emoji Translator AI",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #FF6B6B;
        font-size: 3em;
        margin-bottom: 20px;
    }
    .translation-box {
        background-color: #F0F8FF;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #4CAF50;
        margin: 10px 0;
    }
    .original-text {
        background-color: #FFF8DC;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #FFD700;
        margin: 10px 0;
    }
    .stats-container {
        background-color: #F5F5F5;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'translation_history' not in st.session_state:
    st.session_state.translation_history = []
if 'translator' not in st.session_state:
    st.session_state.translator = EmojiTranslator()

def add_to_history(original: str, translated: str, settings: dict):
    """Add translation to history."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {
        'timestamp': timestamp,
        'original': original,
        'translated': translated,
        'settings': settings
    }
    st.session_state.translation_history.insert(0, entry)
    # Keep only last 10 entries
    if len(st.session_state.translation_history) > 10:
        st.session_state.translation_history = st.session_state.translation_history[:10]

def export_history():
    """Export translation history to JSON."""
    if st.session_state.translation_history:
        return json.dumps(st.session_state.translation_history, indent=2, ensure_ascii=False)
    return None

def main():
    # Header
    st.markdown('<h1 class="main-header"> Emoji Translator AI </h1>', unsafe_allow_html=True)
    st.markdown("Transform your text with smart emoji translation!")
    
    # Sidebar for settings
    with st.sidebar:
        st.header(" Translation Settings")
        
        # Density control
        density = st.select_slider(
            "Emoji Density",
            options=['light', 'medium', 'heavy'],
            value='medium',
            help="Controls how many emojis get added to your text"
        )
        
        # Mode selection
        mode = st.radio(
            "Translation Mode",
            ['append', 'replace'],
            help="Append: keep original word + emoji | Replace: emoji only"
        )
        
        # Style selection
        style = st.selectbox(
            "Output Style",
            ['fun', 'professional', 'meme'],
            help="Choose the tone and emoji selection style"
        )
        
        # Sentiment option
        add_sentiment = st.checkbox(
            "Add Sentiment Emoji",
            help="Append emotion-based emoji at the end"
        )
        
        # Custom emoji file upload
        st.subheader(" Custom Emojis")
        uploaded_file = st.file_uploader(
            "Upload custom emoji mappings (JSON)",
            type=['json'],
            help="Upload a JSON file with custom emoji mappings"
        )
        
        if uploaded_file:
            try:
                custom_emojis = json.load(uploaded_file)
                # Create temporary file and load into translator
                temp_path = "temp_custom_emojis.json"
                with open(temp_path, 'w', encoding='utf-8') as f:
                    json.dump(custom_emojis, f, ensure_ascii=False, indent=2)
                st.session_state.translator = EmojiTranslator(custom_emoji_file=temp_path)
                st.success("Custom emojis loaded! ")
                os.remove(temp_path)  # Clean up
            except Exception as e:
                st.error(f"Error loading custom emojis: {e}")
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader(" Enter Your Text")
        
        # Text input
        input_text = st.text_area(
            "Type your message here:",
            height=150,
            placeholder="Enter the text you want to translate with emojis..."
        )
        
        # Real-time translation
        if input_text:
            settings = {
                'density': density,
                'mode': mode,
                'style': style,
                'add_sentiment': add_sentiment
            }
            
            translated_text = st.session_state.translator.translate(
                text=input_text,
                density=density,
                mode=mode,
                style=style,
                add_sentiment=add_sentiment
            )
            
            # Display results
            st.subheader(" Translation Result")
            
            # Original text
            st.markdown('<div class="original-text">', unsafe_allow_html=True)
            st.markdown(f"**Original:** {input_text}")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Translated text
            st.markdown('<div class="translation-box">', unsafe_allow_html=True)
            st.markdown(f"**Translated:** {translated_text}")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Statistics
            original_length = len(input_text)
            translated_length = len(translated_text)
            emoji_count = translated_length - original_length
            
            st.markdown('<div class="stats-container">', unsafe_allow_html=True)
            col_stat1, col_stat2, col_stat3 = st.columns(3)
            with col_stat1:
                st.metric("Original Length", original_length)
            with col_stat2:
                st.metric("Translated Length", translated_length)
            with col_stat3:
                st.metric("Emojis Added", f"~{emoji_count}")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Action buttons
            button_col1, button_col2, button_col3 = st.columns(3)
            
            with button_col1:
                if st.button(" Save to History"):
                    add_to_history(input_text, translated_text, settings)
                    st.success("Added to history! ")
            
            with button_col2:
                if st.button(" Copy Result"):
                    st.write("Copy the result from the box above")
                    
            with button_col3:
                # Download as text file
                if st.download_button(
                    label=" Download .txt",
                    data=f"Original: {input_text}\n\nTranslated: {translated_text}\n\nSettings: {settings}",
                    file_name=f"emoji_translation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain"
                ):
                    st.success("Downloaded! ")
    
    with col2:
        st.subheader(" Style Preview")
        
        # Show example translations for different styles
        example_text = "I love coffee in the morning"
        
        st.write("**Example:** 'I love coffee in the morning'")
        
        for example_style in ['fun', 'professional', 'meme']:
            example_result = st.session_state.translator.translate(
                text=example_text,
                density='medium',
                mode='append',
                style=example_style,
                add_sentiment=False
            )
            
            if example_style == style:
                st.markdown(f"**{example_style.title()}** (current): {example_result}")
            else:
                st.write(f"**{example_style.title()}**: {example_result}")
        
        # Emoji map info
        st.subheader(" Emoji Database")
        total_words = len(st.session_state.translator.emoji_map)
        total_phrases = len(st.session_state.translator.phrase_patterns)
        
        st.info(f"""
         **{total_words}** individual words  
         **{total_phrases}** phrase patterns  
         **3** output styles  
         **2** translation modes
        """)
    
    # History section
    if st.session_state.translation_history:
        st.subheader(" Translation History")
        
        # Export history button
        col_export1, col_export2, col_export3 = st.columns([1, 1, 2])
        with col_export1:
            if st.button(" Clear History"):
                st.session_state.translation_history = []
                st.success("History cleared!")
                st.experimental_rerun()
        
        with col_export2:
            history_json = export_history()
            if history_json:
                st.download_button(
                    label=" Export JSON",
                    data=history_json,
                    file_name=f"emoji_translation_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json"
                )
        
        # Display history
        for i, entry in enumerate(st.session_state.translation_history):
            with st.expander(f"{entry['timestamp']} - {entry['original'][:50]}..."):
                st.write(f"**Original:** {entry['original']}")
                st.write(f"**Translated:** {entry['translated']}")
                st.write(f"**Settings:** {entry['settings']}")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.8em;'>
        Built with  using Streamlit | Emoji Translator AI v1.0
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

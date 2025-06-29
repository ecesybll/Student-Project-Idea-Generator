"""
Helper functions for the Student Project Generator application.
"""
import os
import json
import base64
import logging
from datetime import datetime
from typing import Dict, Any, List, Optional, Union, Tuple
import pandas as pd
from PIL import Image
import io
import streamlit as st

from config.settings import AppConfig
from config.constants import COMPLEXITY_DESCRIPTIONS

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def validate_input(text: str) -> Tuple[bool, Optional[str]]:
    """
    Validate user input text.
    
    Args:
        text (str): Text to validate
        
    Returns:
        Tuple[bool, Optional[str]]: (is_valid, error_message)
    """
    if not text or len(text.strip()) < AppConfig.MIN_TEXT_LENGTH:
        return False, AppConfig.ERROR_MESSAGES["input_too_short"].format(min_length=AppConfig.MIN_TEXT_LENGTH)
    
    if len(text) > AppConfig.MAX_TEXT_LENGTH:
        return False, AppConfig.ERROR_MESSAGES["input_too_long"].format(max_length=AppConfig.MAX_TEXT_LENGTH)
    
    return True, None

def validate_file(file) -> Tuple[bool, Optional[str]]:
    """
    Validate uploaded file.
    
    Args:
        file: File object from st.file_uploader
        
    Returns:
        Tuple[bool, Optional[str]]: (is_valid, error_message)
    """
    if file is None:
        return True, None  # File is optional
    
    # Check file size
    if file.size > AppConfig.MAX_FILE_SIZE:
        max_size_mb = AppConfig.MAX_FILE_SIZE / (1024 * 1024)
        return False, AppConfig.ERROR_MESSAGES["file_too_large"].format(max_size=max_size_mb)
    
    # Check file extension
    file_ext = file.name.split('.')[-1].lower() if '.' in file.name else ''
    if file_ext not in AppConfig.ALLOWED_EXTENSIONS:
        return False, AppConfig.ERROR_MESSAGES["invalid_file_type"].format(
            allowed_types=', '.join(AppConfig.ALLOWED_EXTENSIONS)
        )
    
    return True, None

def create_project_prompt(user_inputs: Dict[str, Any]) -> str:
    """
    Create a comprehensive prompt for the Gemini API based on user inputs.
    
    Args:
        user_inputs (Dict[str, Any]): Dictionary of user inputs
        
    Returns:
        str: Formatted prompt for Gemini API
        
    Following clean code principles:
    - All magic strings moved to constants
    - Clear separation of data extraction and prompt generation
    """
    # Extract user inputs
    categories = user_inputs.get('categories', [])
    difficulty = user_inputs.get('difficulty', '')
    project_type = user_inputs.get('project_type', '')
    interests = user_inputs.get('interests', [])
    keywords = user_inputs.get('keywords', '')
    timeline = user_inputs.get('timeline', 0)
    complexity = user_inputs.get('complexity', 0)
    detailed_info = user_inputs.get('detailed_info', '')
    
    # Get complexity description from constants
    complexity_desc = COMPLEXITY_DESCRIPTIONS.get(complexity, "Not specified")
    
    # Format the comprehensive prompt in English
    prompt = f"""
You are a senior software architect, project manager, and technical mentor with 15+ years of experience. You need to create not just a project idea, but a complete project guide and implementation plan for students. Your response should be professional, detailed, and actionable.

## Student Profile and Needs:
- **Detailed Project Description:** {detailed_info if detailed_info else 'The student is looking for a general project idea'}
- **Targeted Categories:** {', '.join(categories) if categories else 'Open'}
- **Areas of Interest:** {', '.join(interests) if interests else 'Various technologies'}
- **Keywords:** {keywords if keywords else 'Innovative solutions'}
- **Difficulty Level:** {difficulty if difficulty else 'Appropriate level'}
- **Project Type:** {project_type if project_type else 'Flexible'}
- **Timeline:** {timeline} weeks
- **Complexity:** {complexity}/10 ({complexity_desc})

## CREATE A COMPREHENSIVE PROJECT GUIDE:

Follow the format below and fill in each section as detailed as possible:

# 🚀 [Creative and Catchy Project Title]

## 📋 Project Overview

### 🎯 Problem Statement and Solution
- What real-world problem does it solve?
- How is it different from existing solutions?
- Why is this project important and valuable?

### 🌟 Project Vision
- Long-term goal of the project
- Success criteria
- Achievements upon project completion

## 🎯 Detailed Project Objectives

### Main Objectives:
- [ ] [Objective 1 - Specific and measurable]
- [ ] [Objective 2 - Specific and measurable]
- [ ] [Objective 3 - Specific and measurable]

### Secondary Objectives:
- [ ] [Bonus feature 1]
- [ ] [Bonus feature 2]

## 👥 Target Audience and Use Cases

### Primary Users:
- **Profile:** [Detailed user profile]
- **Needs:** [User needs]
- **Usage Frequency:** [How often will they use it]

### Use Cases:
1. **Scenario 1:** [Detailed use case]
2. **Scenario 2:** [Detailed use case]
3. **Scenario 3:** [Detailed use case]

## 🏗️ Technical Architecture and Technology Stack

### Recommended Technologies:

#### Frontend:
- **Main Technology:** [Technology name]
- **Why this technology:** [Detailed explanation]
- **Alternatives:** [Other options]

#### Backend:
- **Main Technology:** [Technology name]
- **Why this technology:** [Detailed explanation]
- **Alternatives:** [Other options]

#### Database:
- **Main Technology:** [Technology name]
- **Why this technology:** [Detailed explanation]
- **Data model:** [Basic data structure]

#### Additional Tools and Services:
- **Development Tools:** [IDE, Version Control, etc.]
- **Deployment:** [Hosting, CI/CD]
- **Monitoring:** [Analytics, error tracking]

## 📋 Feature List and Functional Requirements

### Core Features (MVP):
1. **[Feature 1]**
   - Description: [Detailed description]
   - Technical requirements: [Technical details]
   - Acceptance criteria: [Testable criteria]

2. **[Feature 2]**
   - Description: [Detailed description]
   - Technical requirements: [Technical details]
   - Acceptance criteria: [Testable criteria]

### Advanced Features:
1. **[Advanced Feature 1]**
   - Description: [Detailed description]
   - Prerequisites: [Which core features are required]

## 🗓️ Detailed Development Roadmap

### Phase 1: Planning and Setup (**Weeks 1-{timeline//4}:**)
- [ ] Project setup and development environment preparation
- [ ] Technical research and technology selection
- [ ] Project structure and architecture design
- [ ] Database design and modeling
- [ ] UI/UX wireframes and mockups

**Deliverables:**
- Project setup documentation
- Technical specification document
- Database schema
- UI mockups

### Phase 2: Core Development ({timeline//2} weeks)
**Weeks {timeline//4 + 1}-{timeline//2 + timeline//4}:**
- [ ] Backend API development
- [ ] Database integration
- [ ] Basic frontend interface
- [ ] User authentication system
- [ ] Basic CRUD operations

**Deliverables:**
- Working MVP version
- API documentation
- Basic test scenarios

### Phase 3: Feature Development ({timeline//4} weeks)
**Weeks {timeline//2 + timeline//4 + 1}-{timeline - timeline//4}:**
- [ ] Advanced features
- [ ] User experience improvements
- [ ] Performance optimizations
- [ ] Security testing
- [ ] Responsive design

**Deliverables:**
- Fully featured application
- Performance test reports
- Security analysis

### Phase 4: Testing and Deployment ({timeline//4} weeks)
**Weeks {timeline - timeline//4 + 1}-{timeline}:**
- [ ] Comprehensive test scenarios
- [ ] Bug fixes
- [ ] Deployment preparation
- [ ] Complete documentation
- [ ] User guide preparation

**Deliverables:**
- Production-ready application
- Complete documentation
- User guide
- Presentation materials

## 📚 Comprehensive Learning Resources

### Core Concepts:
- **Resources for [Technology 1]:**
  - Official documentation: [Link]
  - Recommended courses: [Course names]
  - Practice projects: [Sample projects]

### Advanced Topics:
- **Architecture and Design:**
  - Clean Architecture
  - Design Patterns
  - SOLID Principles

### Practical Resources:
- GitHub repositories: [Sample projects]
- YouTube channels: [Recommended channels]
- Blog posts: [Useful blog posts]
- Books: [Recommended books]

## ⚠️ Potential Challenges and Solutions

### Technical Challenges:
1. **[Challenge 1]**
   - Problem: [Detailed explanation]
   - Solution: [Recommended solution]
   - Alternative: [Plan B]

### Time Management:
- **Risk:** [Potential cause of delay]
- **Precaution:** [Preventive measures]

## 🎯 Success Metrics and Evaluation

### Technical Metrics:
- [ ] Code quality (Code coverage, linting)
- [ ] Performance (Load time, response time)
- [ ] Security (Vulnerability scanning)

### User Experience:
- [ ] Usability testing
- [ ] User feedback
- [ ] Accessibility standards

## 🚀 Future Improvements and Release Plan

### Version 2.0 Features:
- [Future feature 1]
- [Future feature 2]

### Scalability:
- [Growth plan]
- [Technical improvements]

## 💡 Bonus Tips and Recommendations

### During Development:
- Using Git and branch strategy
- Code review process
- Continuous Integration/Deployment

### For Portfolio:
- Preparing a demo video
- GitHub README optimization
- LinkedIn sharing strategy

---

**Note:** This project guide is a template. 

**Important:** For any issues encountered during project development, actively use Stack Overflow, GitHub Issues, and relevant community forums. Don't hesitate to seek mentorship and code review from experienced developers.
"""
    
    return prompt

def create_chat_prompt(message: str, project_context: str = None) -> str:
    """
    Create a comprehensive prompt for chat interactions.
    
    Args:
        message (str): User's chat message
        project_context (str, optional): Context from previously generated project
        
    Returns:
        str: Formatted prompt for chat
    """
    if project_context:
        prompt = f"""
You are an experienced software development mentor and project consultant with 15+ years of industry experience, specializing in guiding students on technical topics.

## Project Context:
You have previously created the following detailed project guide:

{project_context}

## Student Question:
"{message}"

## Response Format and Expectations:

Answer this question in English, in the context of the above project. Your response should meet these criteria:

### 1. Comprehensive and Detailed:
- Do not give only short answers, explain the topic in depth
- Add examples and code snippets (when necessary)
- Mention alternative approaches as well

### 2. Practical and Actionable:
- Provide step-by-step instructions
- Specify which tools to use
- Explain potential issues and solutions

### 3. Educational:
- Explain why you recommend this approach
- Teach relevant concepts and terminology
- Suggest additional learning resources

### 4. Motivational:
- Use a positive and supportive tone
- Give confidence that the student can succeed
- Explain how to overcome challenges

### 5. Structured:
- Use headings and subheadings
- Use bullet points and numbered lists
- Emphasize important points

For technical terms, provide the English equivalent in parentheses when necessary. At the end of your response, suggest related follow-up questions the student can ask for more information.

**Important:** Your response should be at least 200 words and truly cover the topic in depth. Do not give superficial answers.
"""
    else:
        prompt = f"""
You are an experienced software development mentor and project consultant with 15+ years of industry experience, specializing in guiding students on technical topics.

## Student Question:
"{message}"

## Response Format and Expectations:

Answer this question in English. Your response should meet these criteria:

### 1. Comprehensive and Detailed:
- Do not give only short answers, explain the topic in depth
- Add examples and code snippets (when necessary)
- Mention different approaches and options

### 2. Practical and Actionable:
- Provide step-by-step instructions
- Specify which tools and technologies to use
- Guide from beginner to advanced level

### 3. Educational:
- Explain core concepts
- State why you recommend these approaches
- Teach relevant terminology
- Suggest additional learning resources

### 4. Motivational:
- Use a positive and supportive tone
- Give confidence that the student can succeed
- Break down complex topics into simple steps

### 5. Structured:
- Use headings and subheadings
- Use bullet points and numbered lists
- Emphasize important points in **bold**

### 6. Project-Oriented:
- If possible, suggest project ideas
- Give examples of real-world applications
- Offer portfolio development suggestions

For technical terms, provide the English equivalent in parentheses when necessary. At the end of your response, suggest related follow-up questions the student can ask for more information.

**Important:** Your response should be at least 250 words and truly cover the topic in depth. Do not give superficial answers; always be detailed and educational.
"""
    
    return prompt

def save_project(project_data: Dict[str, Any], file_path: str = "saved_projects.json") -> bool:
    """
    Save project data to a JSON file.
    
    Args:
        project_data (Dict[str, Any]): Project data to save
        file_path (str, optional): Path to save the file
        
    Returns:
        bool: True if saved successfully, False otherwise
    """
    try:
        # Add timestamp
        project_data["timestamp"] = datetime.now().isoformat()
        
        # Load existing projects if file exists
        existing_projects = []
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                existing_projects = json.load(f)
        
        # Append new project
        existing_projects.append(project_data)
        
        # Save back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(existing_projects, f, ensure_ascii=False, indent=2)
        
        return True
    except Exception as e:
        logger.error(f"Error saving project: {e}")
        return False

def load_saved_projects(file_path: str = "saved_projects.json") -> List[Dict[str, Any]]:
    """
    Load saved projects from a JSON file.
    
    Args:
        file_path (str, optional): Path to the JSON file
        
    Returns:
        List[Dict[str, Any]]: List of saved projects
    """
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    except Exception as e:
        logger.error(f"Error loading saved projects: {e}")
        return []

def export_to_markdown(project_data: Dict[str, Any], file_path: str = None) -> Optional[str]:
    """
    Export project data to a Markdown file.
    
    Args:
        project_data (Dict[str, Any]): Project data to export
        file_path (str, optional): Path to save the file
        
    Returns:
        Optional[str]: Path to the saved file or None if failed
    """
    try:
        content = project_data.get("content", "")
        title = project_data.get("title", "Project Suggestion")
        
        if not file_path:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_path = f"{title.replace(' ', '_')}_{timestamp}.md"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return file_path
    except Exception as e:
        logger.error(f"Error exporting to markdown: {e}")
        return None

def export_to_pdf(project_data: Dict[str, Any], file_path: str = None) -> Optional[str]:
    """
    Export project data to a PDF file.
    
    Args:
        project_data (Dict[str, Any]): Project data to export
        file_path (str, optional): Path to save the file
        
    Returns:
        Optional[str]: Path to the saved file or None if failed
    """
    try:
        # This is a placeholder - in a real implementation, you would use a PDF library
        # such as reportlab, fpdf, or weasyprint to convert the content to PDF
        content = project_data.get("content", "")
        title = project_data.get("title", "Project Suggestion")
        
        if not file_path:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_path = f"{title.replace(' ', '_')}_{timestamp}.pdf"
        
        # Placeholder for PDF generation
        # For now, just save as markdown
        return export_to_markdown(project_data, file_path.replace('.pdf', '.md'))
    except Exception as e:
        logger.error(f"Error exporting to PDF: {e}")
        return None

def extract_title_from_content(content: str) -> str:
    """
    Extract the project title from the generated content.
    
    Args:
        content (str): Generated project content
        
    Returns:
        str: Extracted title or default title
    """
    try:
        # Look for a title in the format "### 1. Project Title" followed by text
        import re
        title_match = re.search(r'#+\s*1\.\s*Project\s*Title\s*\n+([^\n#]+)', content)
        if title_match:
            return title_match.group(1).strip()
        
        # Alternative: look for the first heading
        heading_match = re.search(r'#+\s*([^\n#]+)', content)
        if heading_match:
            return heading_match.group(1).strip()
        
        return "Project Suggestion"
    except Exception as e:
        logger.error(f"Error extracting title: {e}")
        return "Project Suggestion"

def get_download_link(content: str, filename: str, text: str) -> str:
    """
    Generate a download link for a string content.
    
    Args:
        content (str): Content to download
        filename (str): Name of the file to download
        text (str): Text to display for the download link
        
    Returns:
        str: HTML string with the download link
    """
    b64 = base64.b64encode(content.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">{text}</a>'
    return href

def apply_custom_css() -> None:
    """Apply custom CSS to the Streamlit app."""
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #0D47A1;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #E3F2FD;
        padding-bottom: 0.3rem;
    }
    .info-box {
        background-color: #E3F2FD;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #1E88E5;
        margin-bottom: 1rem;
    }
    .success-box {
        background-color: #E8F5E9;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #43A047;
        margin-bottom: 1rem;
    }
    .warning-box {
        background-color: #FFF8E1;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #FFA000;
        margin-bottom: 1rem;
    }
    .error-box {
        background-color: #FFEBEE;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #E53935;
        margin-bottom: 1rem;
    }
    .stButton>button {
        background-color: #1E88E5;
        color: white;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        border: none;
        font-weight: bold;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #0D47A1;
    }
    .stButton>button:focus {
        outline: none;
        box-shadow: 0 0 0 2px rgba(30, 136, 229, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)

def display_info_box(text: str) -> None:
    """Display an info box with custom styling."""
    st.markdown(f'<div class="info-box">{text}</div>', unsafe_allow_html=True)

def display_success_box(text: str) -> None:
    """Display a success box with custom styling."""
    st.markdown(f'<div class="success-box">{text}</div>', unsafe_allow_html=True)

def display_warning_box(text: str) -> None:
    """Display a warning box with custom styling."""
    st.markdown(f'<div class="warning-box">{text}</div>', unsafe_allow_html=True)

def display_error_box(text: str) -> None:
    """Display an error box with custom styling."""
    st.markdown(f'<div class="error-box">{text}</div>', unsafe_allow_html=True) 
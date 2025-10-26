# Policy AIX User Guide

## Getting Started

Welcome to Policy AIX, an AI-powered policy research platform that helps you explore datasets, conduct research, and generate comprehensive reports. This guide will walk you through the key features and how to use them effectively.

**Main Platform**: All functionality is accessible through the main explore page at `http://localhost:3000/data/explore`

---

## 1. Registration & Sign-In Process

### How to Register or Sign In

1. **Locate the Person Icon**: Look for the **person icon** (👤) in the top-right corner of the header
2. **Click to Sign In**: Click the person icon to access the sign-in page at `http://localhost:3000/sign-in?callbackUrl=/data/explore`
3. **Choose Your Option**:
   - **New Users**: Click "Register" to create an account with your email address
   - **Existing Users**: Enter your email and password to sign in
4. **Email Verification**: New users will receive a confirmation email - check your inbox and click the verification link
5. **Automatic Redirect**: After successful sign-in, you'll be automatically redirected to the **Explore page** (`/data/explore`)

### Registration Benefits
- Access to personalized collections and favorites
- Ability to save and organize datasets
- Full access to AI chatbot features
- Report generation capabilities

---

## 2. Main Explore Page - Your Complete Research Platform

### Overview
The main explore page at `http://localhost:3000/data/explore` is your complete research platform containing:

- **Interactive Map**: Real-time data visualization with multiple layers
- **Dataset Browser**: Comprehensive library of policy and environmental datasets
- **AI Research Chatbot**: Intelligent assistant for data analysis and research
- **Report Generation**: Professional report creation tools

### Page Layout & Architecture

#### **Left Sidebar - Dataset Navigation**
The sidebar provides access to different dataset categories:

#### **Center - Interactive Map**
- **Real-time Visualization**: Live data from Google Earth Engine
- **Multiple Layers**: Toggle between different datasets
- **Interactive Features**: Click for data popups, zoom, and pan
- **Layer Management**: Add/remove datasets from the map view
- **Basemap Controls**: Switch between different map styles
- **Drawing Tools**: Create custom areas of interest

#### **Right Side - AI Chatbot Panel**
- **Floating AI Button**: Triggers the chatbot interface
- **Research Assistant**: AI-powered data analysis and insights
- **Dataset Integration**: Connect datasets as context for research

### Adding Data as Context Using Tokens

#### **Dataset Token System**
1. **Type @ Symbol**: In the chatbot input field, type `@` followed by a dataset name
2. **Select from Dropdown**: Choose from the suggested dataset list
3. **Token Creation**: The dataset appears as a token (e.g., `@Solar Irradiance Data`)
4. **Automatic Map Activation**: Selected datasets automatically appear on the map
5. **Context Integration**: The chatbot can now reference this data in responses

#### **Data Sources**
- **User Uploads**: Personal datasets uploaded through "My Data"
- **Platform Datasets**: Curated datasets from Resource Watch
- **Connected APIs**: Real-time data from external sources
- **Research Collections**: Specialized datasets for policy analysis

---

## 3. AI Research Chatbot - Your Intelligent Assistant

### Chatbot Interface Overview

The AI chatbot is a sophisticated research assistant that appears as a floating panel on the right side of the explore page. It features a modern, dark-themed interface with glass-morphism effects and professional styling.

### How to Access the Chatbot

#### **AI Button Activation**
1. **Locate the AI Button**: Look for the floating **"AI"** button in the bottom-right corner
2. **Button Appearance**: 
   - Transparent background with white border
   - AI icon (favicon) + "AI" text
   - Glowing turquoise hover effect (`#4effd0`)
   - Positioned fixed at bottom-right (20px from bottom, 8px from right)
3. **Click to Open**: Click the AI button to open the chatbot panel
4. **Button Behavior**: The AI button disappears when the chatbot is open and reappears when closed

### Chatbot Panel Interface

#### **Panel Specifications**
- **Dimensions**: 465px wide × Full viewport height (minus 75px margin)
- **Position**: Fixed, top-right corner (55px from top, 8px from right)
- **Background**: Dark semi-transparent (`rgba(30, 30, 30, 0.85)`) with backdrop blur
- **Styling**: Rounded corners (12px), subtle border, professional shadow
- **Z-index**: 9999 (high priority overlay)

#### **Panel Components**

**1. Close Button (X)**
- **Location**: Bottom-right corner of the panel
- **Appearance**: 48px × 48px rounded button
- **Styling**: Semi-transparent white background with border
- **Hover Effect**: Scales to 110% with enhanced border
- **Function**: Closes the chatbot and shows the AI button again

**2. Messages Area**
- **Layout**: Scrollable container for conversation history
- **Styling**: Clean, professional message bubbles
- **Message Types**:
  - **User Messages**: Right-aligned, white background (`rgba(255, 255, 255, 0.15)`)
  - **Assistant Messages**: Left-aligned, subtle background (`rgba(255, 255, 255, 0.08)`)
  - **System Messages**: Italic, left border accent for status updates
  - **Error Messages**: Red background (`rgba(239, 68, 68, 0.1)`) with red border

**3. Input Area**
- **Height**: 180px minimum (expandable textarea)
- **Styling**: White border, semi-transparent background
- **Font**: 18px Inter font, light weight (300)
- **Placeholder**: Subtle white text for guidance
- **Focus Effect**: Enhanced border and background on focus

**4. Action Buttons**
- **Send Button (→)**: 32px × 32px, sends your message
- **Clear Button (🗑️)**: 24px × 24px, clears conversation history
- **Upload Button (•)**: 24px × 24px, uploads files for analysis
- **Styling**: Semi-transparent white backgrounds with subtle borders

### Dataset Integration System

#### **Token-Based Context System**
The chatbot uses an innovative token system to integrate datasets as research context:

**1. Dataset Selection Process**
- **Type @ Symbol**: In the input field, type `@` followed by dataset name
- **Dropdown Appears**: Shows filtered list of available datasets
- **Search Filtering**: Continue typing to narrow down options
- **Select Dataset**: Click on desired dataset from dropdown

**2. Token Display**
- **Visual Tokens**: Selected datasets appear as removable tokens above input
- **Token Styling**: Small rounded badges with dataset names
- **Remove Function**: Click "×" on token to remove dataset from context
- **Token Colors**: Semi-transparent white background with subtle borders

**3. Automatic Map Integration**
- **Map Activation**: Selected datasets automatically appear on the map
- **Layer Management**: Tokens trigger Redux actions to add/remove map layers
- **Visual Feedback**: Map updates in real-time as you add/remove datasets

#### **File Upload System**
- **Supported Formats**: PDF, DOC, DOCX, TXT, CSV, XLSX, XLS
- **Multiple Files**: Can upload multiple files simultaneously
- **File Tokens**: Uploaded files appear as tokens alongside dataset tokens
- **Integration**: Files become part of the research context for AI analysis

### Research Capabilities

#### **What the Chatbot Can Do**

**Policy Analysis**:
- Analyze policy documents, regulations, and frameworks
- Compare different policy approaches and their implications
- Identify gaps and opportunities in current policies

**Data Interpretation**:
- Explain complex datasets and their real-world implications
- Translate technical data into actionable insights
- Identify patterns and trends in data

**Stakeholder Mapping**:
- Identify key stakeholders and their roles in policy implementation
- Analyze stakeholder influence and engagement strategies
- Map stakeholder relationships and dependencies

**Cost-Benefit Analysis**:
- Compare different policy options and interventions
- Analyze financial implications and resource requirements
- Evaluate return on investment for policy initiatives

**Geographic Analysis**:
- Focus on specific regions (especially Arequipa, Peru)
- Analyze spatial patterns and geographic variations
- Provide location-specific recommendations

#### **Response Types**

**Comprehensive Research Reports**:
- Detailed analysis with tables, charts, and insights
- Executive summaries with key findings
- Professional formatting with proper citations

**Interactive Data Tables**:
- Stakeholder analysis tables
- Cost-benefit comparison matrices
- Implementation timeline tables

**Data Visualizations**:
- Charts and graphs embedded in responses
- Geographic visualizations of findings
- Trend analysis charts

**Implementation Strategies**:
- Actionable recommendations
- Step-by-step implementation guides
- Risk assessment and mitigation strategies

### Data Pipeline Integration

#### **Real-Time Data Flow**
The chatbot integrates with a sophisticated data pipeline:

**1. Data Sources**
- **Google Earth Engine (GEE)**: Live satellite and environmental data
- **Resource Watch API**: Curated datasets and metadata
- **User Uploads**: Personal documents and datasets
- **Web Research**: Current information from authoritative sources

**2. Processing Pipeline**
- **API Layer**: Resource Watch API (`api.resourcewatch.org`) processes requests
- **Service Layer**: Frontend services (`dataset.ts`, `layer.js`, `query.js`) handle data
- **State Management**: Redux store manages application state
- **Visualization**: Mapbox GL + Deck.gl render interactive maps

**3. AI Processing**
- **Vector Search**: Semantic search through document database
- **Context Retrieval**: Relevant information extracted for responses
- **Response Generation**: AI processes context to generate insights
- **Source Attribution**: Proper citations and data references

### WebSocket Communication

#### **Real-Time Features**
- **Connection**: WebSocket connection to `ws://localhost:5029/ws`
- **Live Updates**: Real-time status messages and streaming responses
- **Token Usage**: Live tracking of AI processing tokens
- **Dataset Integration**: Map layer activation via WebSocket events

#### **Message Types**
- **agentStart**: Research phase beginning notifications
- **agentUpdate**: Progress updates during processing
- **agentCompleted**: Research phase completion
- **chatResponse**: Final AI responses with analysis
- **streamResponse**: Streaming content for long responses

---

## 4. Report Generation - Professional Documentation

### How to Generate Reports

#### **Step-by-Step Process**

1. **Conduct Research**: Use the chatbot to explore your topic and gather insights
2. **Access Report Tool**: Click on the **REPORT** menu in the header
3. **Select "Create New Report"**: Choose this option from the dropdown
4. **Automatic Processing**: The system analyzes your conversation history
5. **AI Generation**: Gemini AI processes the research data and generates a comprehensive report
6. **Review & Download**: Access your report on the dashboard page

#### **Report Generation Flow**
```
User Research → Chatbot Analysis → Report Menu → Gemini AI → Professional Report → Download Options
```

#### **Report Structure**

**8-Section Professional Reports**:
1. **Executive Summary**: 4-5 paragraph overview of key findings
2. **Electricity Access Gaps**: Analysis of coverage disparities
3. **Coverage Analysis**: Interactive charts showing district-level data
4. **Social Impact**: Assessment of electrification benefits
5. **Barriers & Regulations**: Policy and implementation challenges
6. **Stakeholder Analysis**: Key players and their roles
7. **Prioritization Table**: District rankings and recommendations
8. **References**: Complete source citations and data attribution

#### **Expected Output**

**Content Features**:
- **Professional Formatting**: Clean, executive-ready presentation
- **Interactive Charts**: Horizontal bar charts for data visualization
- **Comprehensive Tables**: District baseline data, cost-benefit analysis
- **Download Options**: PDF and Word document formats
- **Mobile Responsive**: Optimized for all device types

**Download Capabilities**:
- **PDF Generation**: Print-ready reports with proper formatting
- **Word Documents**: Editable format for further customization
- **Print Functionality**: Direct printing from the browser
- **Share Options**: Easy sharing via email or collaboration tools

#### **Data Integration**
- **RAG Context**: Incorporates data from the vector database
- **Web Research**: Includes current information from authoritative sources
- **Dataset References**: Links to original data sources
- **Arequipa Focus**: Specialized analysis for Peruvian districts

---

## 5. Data Pipeline & Technical Architecture

### Understanding the Data Flow

The Policy AIX platform operates on a sophisticated data pipeline that processes information from multiple sources in real-time:

#### **Data Sources**
- **Google Earth Engine (GEE)**: Live satellite data including TROPOMI NO₂ atmospheric chemistry
- **Resource Watch API**: Curated environmental and policy datasets
- **User Uploads**: Personal documents and datasets
- **Web Research**: Current information from authoritative sources

#### **Processing Pipeline**
1. **API Layer**: Resource Watch API (`api.resourcewatch.org`) handles data requests
2. **Service Layer**: Frontend services manage data fetching and processing
3. **State Management**: Redux store maintains application state
4. **Visualization**: Mapbox GL + Deck.gl render interactive maps
5. **AI Processing**: Vector search and context retrieval for intelligent responses

#### **Real-Time Features**
- **Live Data**: Satellite imagery and environmental data updated in real-time
- **Interactive Maps**: Click for data popups, zoom, and pan functionality
- **Layer Management**: Add/remove datasets dynamically
- **Responsive Design**: Optimized for desktop and mobile devices

### Complete Data Flow Diagram

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   DATA SOURCE   │    │   API LAYER     │    │  FRONTEND APP   │    │   MAP RENDER    │
│                 │    │                 │    │                 │    │                 │
│ ┌─────────────┐ │    │ ┌─────────────┐ │    │ ┌─────────────┐ │    │ ┌─────────────┐ │
│ │Google Earth │ │    │ │ResourceWatch│ │    │ │Next.js React│ │    │ │Mapbox GL +  │ │
│ │Engine (GEE) │ │    │ │API          │ │    │ │App          │ │    │ │Deck.gl      │ │
│ │             │ │    │ │             │ │    │ │             │ │    │ │             │ │
│ │TROPOMI NO₂  │ │    │ │api.resource │ │    │ │Redux State  │ │    │ │Tile Layers  │ │
│ │Satellite    │ │    │ │watch.org    │ │    │ │Management   │ │    │ │Color Mapping│ │
│ │Data         │ │    │ │             │ │    │ │             │ │    │ │             │ │
│ └─────────────┘ │    │ └─────────────┘ │    │ └─────────────┘ │    │ └─────────────┘ │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │                       │
         ▼                       ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   DATA STORAGE  │    │   API ENDPOINTS │    │   SERVICE LAYER │    │   VISUALIZATION │
│                 │    │                 │    │                 │    │                 │
│ • Raster Tiles  │    │ • /v1/dataset   │    │ • dataset.ts    │    │ • Map Component │
│ • Time Series   │    │ • /v1/layer     │    │ • layer.js      │    │ • Layer Manager │
│ • Metadata      │    │ • /v1/widget    │    │ • query.js      │    │ • GEE Provider  │
│ • SQL Queries   │    │ • /v1/query     │    │ • widget.ts     │    │ • Tile Renderer │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
```

### API Call Sequence

#### **Dataset Loading Process**
1. **Dataset Metadata Request**: `GET /v1/dataset/{id}` with metadata, vocabulary, and layer info
2. **Widget Data Request**: `GET /v1/widget/{id}` for display configuration
3. **Layer Configuration Request**: `GET /v1/dataset/{id}/layer` for map rendering specs
4. **Data Query Request**: `GET /v1/query/{id}` with SQL queries for actual data

#### **Frontend Data Processing**
```
User Action → Redux Actions → Service Calls → State Update → Map Render
     │              │              │              │              │
     ▼              ▼              ▼              ▼              ▼
Select Dataset → fetchDatasets → fetchDataset → setDatasets → Tile Loading
Click Map → setViewport → fetchLayer → setViewport → Color Mapping
Zoom/Pan → setMapLayers → fetchQuery → setMapLayers → Interaction
```

---

## Tips for Effective Use

### **Best Practices**

#### **Getting Started**
- **Start with the Map**: Explore the interactive map to understand available datasets
- **Use the Sidebar**: Browse different dataset categories to find relevant information
- **Begin with Simple Questions**: Start with broad questions, then narrow down based on responses

#### **Chatbot Optimization**
- **Use Dataset Tokens**: Always add relevant datasets as context using the `@` symbol
- **Upload Supporting Documents**: Include PDFs, spreadsheets, or other relevant files
- **Ask Follow-up Questions**: Build on previous responses for deeper analysis
- **Save Important Conversations**: Use the clear button sparingly to maintain context

#### **Data Exploration**
- **Combine Multiple Datasets**: Use several datasets together for comprehensive analysis
- **Check Map Layers**: Ensure selected datasets are visible on the map
- **Use Filters**: Narrow down datasets by topics, data types, and time periods
- **Explore Collections**: Organize related datasets for easier access

#### **Report Generation**
- **Build Rich Context**: Have substantial conversations before generating reports
- **Include Multiple Perspectives**: Ask about different aspects of your research topic
- **Review Sources**: Always check the references section for data credibility
- **Download and Share**: Use the download options to save and distribute reports

### **Troubleshooting**

#### **Common Issues**
- **Chatbot Not Responding**: Check your internet connection and try refreshing the page
- **Datasets Not Loading**: Verify you're logged in and have proper permissions
- **Map Not Updating**: Clear your browser cache and reload the page
- **Report Generation Fails**: Ensure you have sufficient conversation history

#### **Getting Help**
- **Dataset Descriptions**: Click on dataset cards for detailed information
- **Chatbot Guidance**: Ask the chatbot for help with specific features
- **Documentation**: Refer to this guide for detailed feature explanations
- **Technical Support**: Contact support for technical issues

### **Advanced Features**

#### **Power User Tips**
- **Keyboard Shortcuts**: Use Enter to send messages, Escape to close panels
- **Multiple Tabs**: Open multiple browser tabs for different research sessions
- **Data Export**: Use the map's data export features for further analysis
- **Custom Collections**: Create themed collections for specific research projects

#### **Integration Capabilities**
- **API Access**: The platform provides API endpoints for custom integrations
- **Data Export**: Export datasets in various formats (CSV, JSON, etc.)
- **Embedding**: Embed maps and visualizations in external websites
- **Collaboration**: Share collections and reports with team members

---

*This platform is designed to make policy research accessible, efficient, and comprehensive. The sophisticated data pipeline ensures you have access to the most current information, while the AI chatbot provides intelligent analysis and insights. Start exploring to discover the full potential of AI-powered policy analysis.*

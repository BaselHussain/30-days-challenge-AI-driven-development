# Role: Principal Python AI Systems Engineer  
**Mission:** Deliver a lean, production-ready **PDF Academic Assistant Agent** using OpenAgents SDK + Gemini backend.

### 1. CORE OBJECTIVE  
Construct a focused agent that:  
- Extracts full text from any uploaded PDF  
- Produces a clear, well-structured study summary  
- Generates high-quality mixed-format quizzes **exclusively from the raw original PDF text** (summary must never be used as quiz source)  

**Stack Overview**  
- UI Framework: Streamlit  
- LLM: Gemini (accessed via OpenAgents SDK OpenAI-compatible endpoint)  
- PDF Processing: pypdf  
- Orchestration: Context7 MCP server (already active)  
- Runtime: Gemini CLI environment (fully pre-configured)

### 2. STRICT COMPLIANCE RULES  
1. **Zero-Bloat Policy**  
   - No extra features, logging, comments, or abstractions  
   - Only allowed libraries: `openagents`, `streamlit`, `pypdf`, `python-dotenv`  

2. **Gemini Endpoint Configuration (Mandatory)**  
   - Base URL: `https://generativelanguage.googleapis.com/v1beta/openai/`  
   - Auth: `GEMINI_API_KEY` environment variable  
   - Model: `gemini-2.0-flash`  
   - Model class: `OpenaiChatCompletionModel` (exact OpenAgents SDK implementation)  

3. **Context7 MCP Requirement**  
   - All operations run under pre-configured `context7` server  
   - **Before any code is written**, you must execute `get-library-docs` or `resolve-library-id` on `openagents` to verify current SDK syntax  
   - Any syntax mismatch → stop and re-query docs  

4. **Package Management**  
   - Exclusive use of **uv**  
   - Only permitted dependencies listed above  

### 3. EXACT FILE STRUCTURE (NO EXCEPTIONS)  
├── app.py          # Streamlit frontend & runtime entrypoint
├── agent.py        # Agent setup, model initialization, tool binding
├── tools.py        # PDF text extraction + SDK-compliant tool wrapper
├── pyproject.toml  # uv dependency declaration
└── .env            # API key storage

### 4. IMPLEMENTATION PHASES  

**PHASE 1 – SDK VALIDATION (Required First Step)**  
- Invoke `get-library-docs` on `openagents`  
- Confirm precise syntax for tool decorators, Agent creation, and model attachment  

**PHASE 2 – tools.py**  
- Implement single function: `extract_pdf_text(file_bytes: bytes) -> str` using pypdf  
- Apply correct OpenAgents SDK tool decorator/class exactly as verified  

**PHASE 3 – agent.py**  
- Create OpenAI-compatible client with Gemini base URL  
- Load `GEMINI_API_KEY` from environment  
- Instantiate `OpenaiChatCompletionModel(model="gemini-2.0-flash")`  
- Register extraction tool using verified SDK method  
- System prompt:  
  > "You are a precise academic assistant. Summarize PDFs accurately and generate quizzes using only the complete original text."  

**PHASE 4 – app.py**  
- Single PDF uploader  
- "Generate Summary" → extract → agent call → display formatted summary  
- "Generate Quiz" (enabled post-summary) → agent call with full raw text → 8–12 mixed questions (MCQ + True/False + Fill-in-the-blank)  
- Interactive answer checking  
- Non-streaming responses only  

**PHASE 5 – Supporting Files**  
- `.env` template containing `GEMINI_API_KEY=`  
- `pyproject.toml` with exact uv-compatible dependency list  

### 5. ACCEPTANCE CRITERIA  
- PDF upload → instant accurate summary  
- Quiz button produces 8–12 correct, varied questions sourced **only from original full text**  
- No pseudocode, no placeholders  
- Runs immediately with valid API key  

**Deliver now:** Complete, clean, fully functional code for every file listed above, 100% compliant with verified OpenAgents SDK syntax and Context7 MCP environment.
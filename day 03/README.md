# TASK 3

### What new improvements were introduced in Gemini 3.0?

- **Maximizes reasoning depth**  
  The model may take significantly longer to reach a first token, but the output will be more carefully reasoned (Deep Think mode).

- **Granular control over multimodal vision processing**  
  Introduces the `media_resolution` parameter. Higher resolutions improve the model’s ability to read fine text or identify small details, but increase token usage and latency.

- **Gemini 3 Pro Image**  
  Generate and edit images from text prompts. It uses reasoning to “think” through a prompt and can retrieve real-time data (e.g., current weather forecasts or live stock charts).

### How does Gemini 3.0 improve coding & automation workflows?

- **Richer, production-ready code**  
  Improved frontend quality and UI components; excels at zero-shot tasks such as simulating OS interfaces or creating interactive 3D games/visualizations in a single prompt.

- **Strict multimodal function calling with thought signatures**  
  Ensures seamless multi-turn reasoning; supports parallel tool calls (e.g., querying weather in multiple cities) and real-time Google Search integration.

- **End-to-end autonomous workflows**  
  Handles complete tasks (e.g., inbox organization via Gmail, travel booking) with granular controls like `thinking_level: "high"` for complex reasoning and default temperature 1.0 to prevent looping.

### How does Gemini 3.0 improve multimodal understanding?

- **1M+ token context window**  
  Processes entire videos, large PDFs, or full code repositories alongside text in a single prompt.

- **New `media_resolution` parameter**  
  - **High** – detailed OCR (1120 tokens/image)  
  - **Medium** – optimized for PDFs (560 tokens)  
  - **Low** – fastest processing for speed-critical tasks.

### Name any two developer tools introduced with Gemini 3.0

- **Google Antigravity**  
  A revolutionary agentic development platform that lets AI agents autonomously plan, code, test, and deploy full applications from natural language prompts.

- **Client-Side Bash Tool** (new with Gemini 3.0)  
  Enables secure local execution of shell commands, filesystem operations, and multi-language prototyping directly within agentic flows.
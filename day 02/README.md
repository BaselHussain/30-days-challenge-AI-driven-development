# 📁 Part A — Theory (Short Questions) 

## 1. Nine Pillars Understanding 

**Q:** Why is using AI Development Agents (like Gemini CLI) for repetitive setup tasks better for your growth as a system architect?  

**A:** Using AI Development Agents (like Gemini CLI) for repetitive tasks is better for our growth because it allows us to focus on system design, architecture, and complex problem-solving instead of manual, time-consuming work. The AI agents don’t replace your skills; they amplify them, letting you spend more time on architectural principles rather than trivial coding tasks.  

**Q:** Explain how the Nine Pillars of AIDD help a developer grow into an M-Shaped Developer.  

**A:** The M-Shaped developer isn’t about being good at everything. It’s about having deep expertise in a few domains while being broadly competent in others, augmented by AI. The Nine Pillars of AI-Driven Development help a developer become M-shaped by combining deep expertise in their core area with broad skills across other domains. AI agents and Markdown as code let you handle tasks outside your main expertise quickly. MCP and AI-first IDEs simplify tools and reduce mental load, while a universal Linux environment and cloud deployment make your skills portable. Test-driven and specification-driven development ensure quality, and composable skills let you leverage domain knowledge without mastering everything. Together, these pillars let you work confidently across multiple areas while staying strong in your specialty.  

---

## 2. Vibe Coding vs Specification-Driven Development 

**Q:** Why does Vibe Coding usually create problems after one week?  

**A:** In Vibe Coding, there are no clear specifications, so in the future you may misunderstand how things work or are expected to work, and other developers can also get confused. Many bugs appear when modifying or extending the code, making it messy and hard to understand. Edge cases are often overlooked, so new bugs emerge after a week or sometime later.  

**Q:** How would Specification-Driven Development prevent those problems?  

**A:** In Specification-Driven Development, all specifications are clearly documented. This ensures clarity for future development, and other developers can understand the workflow by reading the spec file. When modifying or extending code, you first update the spec file and then the code, keeping both aligned. Including all scenarios and edge cases in the spec reduces the chances of hidden bugs.  

---

## 3. Architecture Thinking 

**Q:** How does architecture-first thinking change the role of a developer in AIDD?  

**A:** Architecture-first thinking shifts a developer’s role from just writing code to designing and orchestrating entire systems. Developers focus on how components, AI agents, and workflows interact, ensuring scalability, maintainability, and integration across domains.  

**Q:** Explain why developers must think in layers and systems instead of raw code.  

**A:** Developers need to think in layers and systems instead of just raw code because big apps are like LEGO sets—each piece must fit together, or the whole thing breaks. You don’t focus on raw code because AI agents handle it; instead, you concentrate on system design.  

---

# 📁 Part B — Practical Task (Screenshot Required) 

**CLI PROMPT:** Create a `GEMINI.md` file in the root and generate a 1-paragraph specification for an email validation function.  
**Requirements:** Must contain “@”, must have a valid domain (e.g., .com, .org), should return clear error messages.  

**Generated 1-paragraph specification:**  
The email validation function should accept a string as input and return a boolean indicating whether the email is valid, along with an array of error messages if validation fails. A valid email address must contain a "@" symbol and a domain with a valid top-level domain (e.g., ".com", ".org", ".net"). If the email is invalid, the function should provide clear and specific error messages, such as "Email must contain @" if the "@" symbol is missing, or "Invalid domain" if the domain is malformed or uses an unsupported TLD.  

---

# 📁 Part C — Multiple Choice Questions 

**1. What is the main purpose of Spec-Driven Development?**  
A. Make coding faster  
B. Clear requirements before coding begins ✅  
C. Remove developers  
D. Avoid documentation  

**2. What is the biggest mindset shift in AI-Driven Development?**  
A. Writing more code manually  
B. Thinking in systems and clear instructions ✅  
C. Memorizing more syntax  
D. Working without any tools  

**3. Biggest failure of Vibe Coding?**  
A. AI stops responding  
B. Architecture becomes hard to extend ✅  
C. Code runs slow  
D. Fewer comments written  

**4. Main advantage of using AI CLI agents (like Gemini CLI)?**  
A. They replace the developer completely  
B. Handle repetitive tasks so dev focuses on design & problem-solving ✅  
C. Make coding faster but less reliable  
D. Make coding optional  

**5. What defines an M-Shaped Developer?**  
A. Knows little about everything  
B. Deep in only one field  
C. Deep skills in multiple related domains ✅  
D. Works without AI tools  

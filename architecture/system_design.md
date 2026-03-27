# System Architecture

## Flow

User Input  
→ Lead Agent  
→ Recommendation Agent (RAG)  
→ Sales Agent  
→ Compliance Agent  
→ Final Output  

## RAG Layer

- Vector DB stores:
  - Policies
  - Claims docs
  - FAQs

## Key Design

- Agents are modular
- Each agent has:
  - Prompt
  - LLM call
  - Output schema

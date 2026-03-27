
# AI Multi-Agent Insurtech System

This project demonstrates a production-style AI system using:

- Multi-agent architecture  
- LLM APIs  
- RAG (Retrieval Augmented Generation)  
- Evaluation pipelines  

## Key Idea

Instead of a single prompt, the system uses specialized agents:

- Lead Qualification Agent  
- Policy Recommendation Agent  
- Sales Agent  
- Claims Agent  
- Compliance Agent  

## Architecture

User → Lead Agent → Recommendation (RAG) → Sales → Compliance → Output  

## Why This Matters

Most AI demos stop at prompting.  
This system focuses on:
- Structured agent design  
- Grounded responses (RAG)  
- Measurable evaluation  

## Key Files

- `agents.md` → Full system design  
- `prompts/` → Real prompts per agent
- `architecture/` - System design and architecture
- `evaluation/` → Metrics & evaluation logic  
- `src/` → Example LLM API usage  

## Tech Stack

- Python  
- LLM APIs (OpenAI/Claude)  
- Vector DB (conceptual)  

## Author

Vidhu Sood

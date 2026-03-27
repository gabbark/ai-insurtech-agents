#  Agents.md — Insurtech AI Platform

## A. Overview

This platform uses multiple AI agents to automate insurance customer journeys across:
- Lead qualification
- Policy recommendation
- Customer support
- Claims assistance

The system is designed using LLM APIs + RAG for factual grounding.


## B. Agent Architecture

###  1. Lead Qualification Agent
- Role: Identify user intent and qualification level
- Input: User query / chat / form data
- Output: Structured profile (age, need, intent, budget)


###  2. Policy Recommendation Agent
- Role: Recommend best insurance policies
- Input: User profile + insurer data (via RAG)
- Output: Top 3 policies with reasoning



###  3. Conversational Sales Agent
- Role: Persuade and convert users
- Input: Recommendations + objections
- Output: Personalized pitch / responses



###  4. Claims Assistance Agent
- Role: Guide users through claims process
- Input: Policy + claim scenario
- Output: Step-by-step instructions



###  5. Compliance & Validation Agent
- Role: Ensure regulatory correctness
- Input: Generated response
- Output: Approved / flagged response



## C. Agent Communication Flow

User → Lead Qualification Agent  
User → Policy Recommendation Agent (via RAG)  
User → Sales Agent  
User → Compliance Agent  
User → Final Response  



## D. Tools & Data Access

### Shared Tools:
- LLM API (text generation)
- Vector Database (policy wordings, exclusions, inclusions,claim docs, FAQs)
- CRM (user data,catalogue data, historical data)
- Policy Database (insurer APIs, PAS APIs)

### Agent-specific Access:

Lead Agent:
- CRM
- Basic LLM classification

Recommendation Agent:
- Vector DB (RAG)
- Policy APIs

Sales Agent:
- LLM (high creativity)

Claims Agent:
- RAG (claims docs)

Compliance Agent:
- Rule engine + LLM



## E. Prompting Strategy

Each agent uses a specialized system prompt:

For example: Recommendation Agent

"You are an insurance advisor. Recommend policies based only on retrieved documents. Do not hallucinate. Provide reasoning."


## F. Constraints

- No hallucinated policy details
- Must cite source (RAG)
- Follow IRDAI compliance guidelines
- Maintain professional tone



## G. Failure Handling

- If confidence < threshold → fallback to human agent
- If RAG returns no data → ask clarification
- If compliance fails → regenerate response



## H. Logging & Observability

Track:
- Prompt + response
- Latency
- Token usage
- Errors
- User feedback


## I. Evaluation Hooks

Each agent output is evaluated on:
- Accuracy
- Relevance
- Compliance
- Conversion effectiveness


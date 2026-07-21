# Enterprise Knowledge Assistant

An AI-powered assistant that helps employees find reliable project knowledge stored in Confluence.

## Problem Statement

Enterprise knowledge is often distributed across Confluence pages and understood primarily by individual subject-matter experts. Employees may struggle to locate reliable project information without interrupting members of other teams. This creates knowledge silos, slows onboarding, and increases the time required to make informed decisions.

## Proposed Solution

The Enterprise Knowledge Assistant will use Retrieval-Augmented Generation (RAG) to answer employee questions using relevant content retrieved from Confluence. Grounding responses in retrieved enterprise knowledge is intended to make existing information easier to discover while reducing dependence on individual subject-matter experts.

## Current Scope

The initial version is planned to support:

- Loading documents from Confluence.
- Splitting documents into retrieval-friendly chunks.
- Generating and storing vector embeddings in Chroma.
- Retrieving relevant chunks for an employee's question.
- Generating an answer grounded in the retrieved context.
- Exposing the question-answering workflow through a REST API.

## High-Level Architecture

```text
Confluence
    |
Document Loader
    |
Text Splitter
    |
Embedding Model
    |
Chroma Vector Store
    |
Retriever <- User Question
    |
Large Language Model
    |
FastAPI REST API
```

## Planned Technology Stack

| Area | Technology |
| --- | --- |
| Language | Python |
| API framework | FastAPI |
| RAG framework | LangChain |
| Vector database | Chroma |
| Knowledge source | Confluence |

### Later Phases

- LangGraph for stateful workflows.
- PostgreSQL for persistent application data.
- Docker for reproducible packaging and deployment.
- DeepEval for RAG evaluation.
- LangSmith for tracing and observability.
- Authentication and authorization.
- Continuous integration and deployment.

## Project Status

The project is currently in the foundation phase. The repository structure and initial project documentation are being established; the RAG pipeline and API have not yet been implemented.

## Local Setup

To be added after the development environment and initial dependencies are defined.

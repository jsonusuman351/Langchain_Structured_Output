# ⚙️ Mastering Structured Output with LangChain

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python) ![LangChain](https://img.shields.io/badge/LangChain-0086CB?style=for-the-badge&logo=langchain) ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai) ![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic)

Welcome to this hands-on guide for taming the output of Large Language Models! By default, LLMs produce unstructured text, which is great for conversation but difficult to use in downstream systems like databases, APIs, or AI agents. This repository explores how to force LLMs to return clean, predictable, and structured data (like JSON) using LangChain.

This collection of scripts is a deep dive into the `with_structured_output` method, showcasing how to define a desired data schema using powerful Python libraries.

---

### 🤔 Why Do We Need Structured Output?

LLMs are creative, but software systems are not. To make AI applications reliable, we need predictable data formats. Structured output is essential for:

-   **Data Extraction**: Reliably pulling specific information from a block of text (e.g., extracting user details from a query).
-   **API Building**: Ensuring the LLM's response can be directly used to call another API or service without messy parsing.
-   **AI Agents & Function Calling**: Providing tools and functions to an AI agent in a format it can understand and execute.
-   **Database Integration**: Formatting LLM output so it can be directly inserted into a database table.

---

### ✨ Core Concepts Demonstrated

This repository explores the three primary methods for defining a data schema with LangChain's `with_structured_output` method:

1.  **TypedDict**:
    -   A simple and direct way to define a dictionary's structure with type hints.
    -   Ideal for straightforward cases where you just need a dictionary with specific keys and value types. The output is a standard Python `dict`.

2.  **Pydantic**:
    -   The most powerful and recommended approach. Pydantic models not only define the structure but also perform **data validation**, coercion, and can handle default values and optional fields.
    -   It returns a Pydantic model **object**, which allows for cleaner code and attribute access (e.g., `result.name` instead of `result['name']`).

3.  **JSON Schema**:
    -   A language-agnostic standard for defining the structure of JSON data.
    -   This method is perfect for multi-language environments or when the required data schema is already defined in JSON Schema format. The output is a Python `dict`.

This collection of scripts also explores **JSON Mode and Function Calling**, the underlying mechanisms that models like OpenAI, Gemini, and Claude use to produce structured data.

---

### 🛠️ Tech Stack

-   **Core Framework**: LangChain
-   **LLM Provider**: OpenAI
-   **Data Validation & Schemas**: Pydantic, TypedDict
-   **Core Libraries**: `langchain-core`, `langchain-openai`, `python-dotenv`

---

### ⚙️ Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/jsonusuman351/Langchain_Structured_Output.git](https://github.com/jsonusuman351/Langchain_Structured_Output.git)
    cd Langchain_Structured_Output
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # It is recommended to use Python 3.10 or higher
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Environment Variables:**
    -   Create a file named `.env` in the root directory.
    -   Add your OpenAI API key to this file:
        ```env
        OPENAI_API_KEY="your-openai-api-key"
        ```

---

### 🚀 Usage Guide

Each script in this repository demonstrates how to extract structured information from a sample sentence using a different schema definition method.

-   **Using Pydantic for Validation and Object Output:**
    *This is the most robust method.*
    ```bash
    python with_structured_output_pydantic.py
    ```

-   **Using TypedDict for Simple Dictionary Output:**
    *A lightweight and straightforward approach.*
    ```bash
    python with_structured_output_typeddict.py
    ```

-   **Using JSON Schema for Language-Agnostic Definitions:**
    *Ideal for cross-platform compatibility.*
    ```bash
    python with_structured_output_json.py
    ```

**Example Output (from `with_structured_output_pydantic.py`):**
```
Person(name='Suman', age=24)
<class '__main__.Person'>
```

---

### 🔬 A Tour of the Structuring Methods

This repository is organized by the schema definition technique, allowing you to compare each approach directly.

<details>
<summary>Click to view the code layout</summary>

```
Langchain_Structured_Output/
│
├── with_structured_output_pydantic.py  # Recommended: Uses Pydantic for robust validation
├── with_structured_output_typeddict.py # Simple: Uses Python's built-in TypedDict
├── with_structured_output_json.py    # Flexible: Uses a standard JSON Schema file
│
├── Pydantic.py                         # Defines the Pydantic model
├── typeddict.py                        # Defines the TypedDict model
├── json_schema.json                    # Contains the JSON Schema definition
│
├── requirements.txt
├── .env                                # (Need to create this for your API key)
└── README.md
```
</details>

---

---
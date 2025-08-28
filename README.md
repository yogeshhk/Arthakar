# **अर्थकार (Arthakar) \- Your AI Financial Assistant**

**अर्थकार** (Arthakar) is a sophisticated, AI-powered financial assistant designed to empower users with deep insights into the world of finance. It leverages a powerful stack of modern AI technologies to provide comprehensive equity research, portfolio analysis, and actionable buy/sell recommendations.

## **Why Arthakar? The Ikigai of Finance and AI**

The financial world is awash with data, from real-time market feeds and complex financial reports to the ever-flowing stream of social media sentiment. For an individual investor or even a seasoned analyst, manually processing this deluge of information is a herculean task. This is where the synergy of **Finance \+ AI** finds its purpose, its *ikigai*.

* **Passion & Mission (What you love & what the world needs):** We are passionate about democratizing financial knowledge. The world needs accessible, unbiased, and intelligent tools to navigate the complexities of financial markets. Arthakar is built to be that tool.  
* **Vocation & Profession (What you are good at & what you can be paid for):** By harnessing the power of Large Language Models and agentic workflows, we can perform tasks that traditionally required teams of analysts. This creates a powerful, efficient, and scalable solution for financial intelligence.

Arthakar is born from this intersection, providing a clear path through the noise and empowering users to make informed financial decisions.

## **What Can Arthakar Do?**

Arthakar is designed to be a comprehensive financial assistant with three core capabilities:

1. **Equity Research:** Conduct in-depth research on any publicly traded company. Arthakar can parse annual reports, analyze financial statements, and summarize key findings to give you a complete picture of a company's health.  
2. **Portfolio Analysis:** Analyze your existing investment portfolio. Arthakar can assess your asset allocation, identify areas of risk, and provide insights into the overall performance of your investments.  
3. **Buy/Sell Recommendations:** Get intelligent, data-driven recommendations. By synthesizing market data, news sentiment, and fundamental analysis, Arthakar can suggest potential buying opportunities or recommend selling certain assets.

## **How Does It Work? The Tech Stack**

Arthakar is built on a foundation of cutting-edge, open-source technologies, ensuring transparency, flexibility, and power.

* **Agent Workflow Modeling (LangGraph):** At its core, Arthakar uses LangGraph to create a sophisticated, stateful multi-agent system. This allows for complex financial analysis tasks to be broken down into logical steps, with different specialized agents handling each part of the process, from data gathering to final analysis and recommendation.  
* **Live Data Integration (MCP \- Market & Community Pulse):** To make informed decisions, access to real-time information is crucial. We've conceptualized a toolset called **MCP** which will be responsible for fetching live stock quotes, financial news, and social media feeds, providing the agent with the most current data.  
* **Document Parsing & Structuring (Docling):** Financial reports are often dense and unstructured. A conceptual toolset named **Docling** will be used to parse these documents (like PDFs of annual reports) and convert them into structured JSON, making the data easily accessible for our AI agents.  
* **Graph-Based RAG (LlamaIndex):** For deep, context-aware analysis, Arthakar utilizes LlamaIndex to build knowledge graphs from the structured data. This allows for a powerful Graph RAG (Retrieval-Augmented Generation) approach, where the LLM can query the interconnected data to uncover non-obvious insights and relationships.  
* **Core Intelligence (Groq API & Open-Source LLMs):** The brain of the operation is a fast, open-source Large Language Model like Llama 3, served via the ultra-low-latency Groq API. This ensures that analysis is not only intelligent but also delivered in near real-time.

### **System Architecture**

\[User Query\] \-\> \[Main Agent (LangGraph)\]  
                     |  
                     |--- 1\. Task Decomposition \---  
                     |  
       \-------------------------------------------------  
      |                         |                       |  
\[Research Agent\]        \[Data Fetcher Agent\]    \[Analysis Agent\]  
      |                         |                       |  
      |--- (Docling) \-\> \[Parse Reports\] |--- (MCP) \-\> \[Get Live Data\]   |--- (LlamaIndex) \-\> \[Graph RAG\]  
      |                         |                       |  
      |--- \[Summarize\]         |--- \[Get News/Social\]   |--- \[Synthesize & Recommend\]  
      |                         |                       |  
       \-------------------------------------------------  
                     |  
                     |--- 2\. Synthesize Results \---  
                     |  
              \[Final Response\]

## **Getting Started**

### **Prerequisites**

* Python 3.9+  
* Groq API Key  
* Access to financial data APIs (e.g., Alpha Vantage, Financial Modeling Prep)

### **Installation**

1. **Clone the repository:**  
   git clone https://github.com/your-username/arthakar.git  
   cd arthakar

2. **Install dependencies:**  
   pip install \-r requirements.txt

3. Set up environment variables:  
   Create a .env file in the root directory and add your API keys:  
   GROQ\_API\_KEY="your\_groq\_api\_key"  
   FINANCIAL\_DATA\_API\_KEY="your\_financial\_data\_api\_key"

### **Running the Assistant**

You can interact with the Arthakar agent through the command line:

python main.py "Provide a detailed analysis of NVIDIA's latest quarterly report and give a buy or sell recommendation."

## **Contributing**

We welcome contributions from the community\! If you'd like to contribute, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## **License**

This project is licensed under the MIT License \- see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.

## **Disclaimer**

Arthakar is an AI-powered assistant and is intended for informational purposes only. It is not financial advice. Please consult with a qualified financial advisor before making any investment decisions.
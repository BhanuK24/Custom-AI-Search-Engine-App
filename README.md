# 🌐 Custom Exa AI Search Engine

A custom AI-powered search engine built in Python using the [Exa API](https://exa.com).  
This project provides an interactive web interface with [Streamlit](https://streamlit.io/), allowing users to perform intelligent keyword searches across the web, optionally filtering results by popular website domains.


---

## **Features**

- **Keyword Search:** Search any topic and get relevant results.  
- **Domain Filtering:** Filter results by popular websites such as YouTube, TikTok, GitHub, Reddit, and more.  
- **Automatic Domain Detection:** Detects if a query mentions a popular site and filters results automatically.  
- **Interactive Web Interface:** Built with Streamlit for a clean and user-friendly experience.  
- **Clickable Results:** Search results are displayed as clickable links.  
- **Secure API Key Handling:** API keys are loaded from environment variables (`.env`) to keep them private.

---

## **Setup Instructions**

1. **Clone the repository**

```
git clone https://github.com/YOUR_USERNAME/exa-search-engine.git
cd exa-search-engine
```
2. Install dependencies

```
pip install streamlit exa_py python-dotenv
```

3. Create a .env file in the project folder and add your Exa API key:

```
EXA_API_KEY=your_actual_api_key_here
```
Make sure .env is included in .gitignore to prevent exposing your API key.


4. Run the app

```
streamlit run search_app.py
```
A browser window will open with the interactive search interface.

---


## **Usage**

1. Enter your search query in the input box.  
2. Optionally, select a popular website from the dropdown to filter results.  
3. Click the **Search** button to display clickable search results.  
4. If no site is selected, the search engine returns the most relevant results from any domain.

---

## **Tech Stack**

- Python 3.x  
- Exa API  
- Streamlit  
- python-dotenv

---

## **Screenshots**
![Search Interface 1](https://github.com/user-attachments/assets/6455ec88-0c12-4f37-ab59-d56d350cad0e)
![Search Interface 2](https://github.com/user-attachments/assets/cac7e9ea-df60-42f8-8ce3-7bf57b47fdad)
![Search Interface 3](https://github.com/user-attachments/assets/773927d0-2e0d-49e7-b3a6-aa14106c4705)


---

## **Contributing**

Contributions are welcome! Please open an issue or submit a pull request with improvements or new features.


---

## **License**

This project is open-source and available under the MIT License.

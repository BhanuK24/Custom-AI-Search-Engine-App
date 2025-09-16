import os
from dotenv import load_dotenv
from exa_py import Exa
import streamlit as st

# Load environment variables from .env
load_dotenv()
EXA_API_KEY = os.getenv("EXA_API_KEY")

# Initialize Exa
exa = Exa(EXA_API_KEY)


# Popular sites mapping
popular_sites = {
    "youtube": "https://www.youtube.com",
    "tiktok": "https://www.tiktok.com",
    "reddit": "https://www.reddit.com",
    "twitter": "https://x.com",  # Twitter/X
    "github": "https://github.com",
    "medium": "https://medium.com",
    "amazon": "https://www.amazon.com",
    "wikipedia": "https://www.wikipedia.org",
    "stack overflow": "https://stackoverflow.com",
    "linkedin": "https://www.linkedin.com",
    "facebook": "https://www.facebook.com",
    "instagram": "https://www.instagram.com",
    "quora": "https://www.quora.com",
    "pinterest": "https://www.pinterest.com",
    "imdb": "https://www.imdb.com",
    "spotify": "https://www.spotify.com",
    "netflix": "https://www.netflix.com",  
    "cnn": "https://www.cnn.com",
    "bbc": "https://www.bbc.com",
    "nytimes": "https://www.nytimes.com",
    "the verge": "https://www.theverge.com",
    "huffpost": "https://www.huffpost.com",
    "techcrunch": "https://techcrunch.com",
    "forbes": "https://www.forbes.com",
    "the guardian": "https://www.theguardian.com",
    "washington post": "https://www.washingtonpost.com",
    "yahoo": "https://www.yahoo.com",
    "bing": "https://www.bing.com",
    "duckduckgo": "https://duckduckgo.com",
    "etsy": "https://www.etsy.com",
    "ebay": "https://www.ebay.com",
    "tripadvisor": "https://www.tripadvisor.com",
    "airbnb": "https://www.airbnb.com",
    "craigslist": "https://www.craigslist.org",
    "udemy": "https://www.udemy.com",
    "coursera": "https://www.coursera.org",
    "khan academy": "https://www.khanacademy.org",
    "walmart": "https://www.walmart.com",
    "target": "https://www.target.com",
    "best buy": "https://www.bestbuy.com",
    "costco": "https://www.costco.com"

}

# -----------------------
# STREAMLIT UI
# -----------------------
st.set_page_config(page_title="Exa Search Engine", layout="centered")
st.title("🌐 Custom Exa Search Engine")
st.write("Search any query and optionally filter by popular sites!")

# Query input
# Query input
query = st.text_input("Enter your search query:")

# Optional dropdown for popular site filter
selected_site = st.selectbox(
    "Select a popular site to filter results (optional):",
    ["None"] + list(popular_sites.keys())
)

# Search button
if st.button("Search") and query:
    query_lower = query.lower()

    # Determine domain filter
    include_domains = None
    if selected_site != "None":
        include_domains = [popular_sites[selected_site]]
    else:
        # Auto-detect from query keywords if no selection is made
        for keyword, domain in popular_sites.items():
            if keyword.lower() in query_lower and domain is not None:
                include_domains = [domain]
                break

    # Prepare search
    search_args = {
        "query": query,
        "num_results": 10,
        "type": "keyword"
    }
    if include_domains:
        search_args["include_domains"] = include_domains

    # Perform search
    response = exa.search(**search_args)

    # Display results
    st.subheader("Results:")
    if response.results:
        for result in response.results:
            st.markdown(f"- [{result.title}]({result.url})")
    else:
        st.write("No results found. Try a different query.")
from datetime import date
import time
import pandas as pd
import streamlit as st
from streamlit import spinner

import get_content
import visualisation
import quantitative_analyse
import nlp_analysis
from guardian import GuardianArticle

def main():
    if 'list_of_all_articles' not in st.session_state:
        st.session_state.list_of_all_articles = []
    if 'fetch_articles_clicked' not in st.session_state:
        st.session_state.fetch_articles_clicked = False
    list_of_all_articles = st.session_state.list_of_all_articles

    st.title("Manloi's Project :sunflower:")
    st.markdown(f"This application was developed as part of a Python Programming Language Course. It serves as a comprehensive tool for analyzing and visualizing articles from **The Guardian**. The app offers various analytical features, including:\n- Quantitative Analysis\n- Keyword Analysis (Natural Language Processing)\n- Sentiment Analysis (Natural Language Processing)\n- Word Mention\n\nThese tools aim to help you gain deeper insights into the content of articles published by The Guardian. Please note that this project is intended solely for educational purposes.")
    # Sidebar
    st.logo("https://avatars.githubusercontent.com/u/164318?s=200&v=4")

    folder_path = "Manloi_project/guardian_articles"
    api_key = "e3574d33-be67-451d-bde6-ce32ffa11f78"
    api_endpoint = 'http://content.guardianapis.com/search'

    # Side Bar
    st.sidebar.header("Please choose a time period.")
    start_date = st.sidebar.date_input("Start Date", date(2024,10,1))
    end_date = st.sidebar.date_input("End Date", date(2024,10,31))
    st.write("Start the program by choosing a time period.")

    if start_date > end_date:
        st.sidebar.error("Start Date must be before End Date.")

    if end_date >= date.today():
        st.sidebar.error("End Date must be before today.")

    else:
        fetch_button = st.sidebar.button("Fetch Articles", key="fetch_articles_button", disabled=st.session_state.fetch_articles_clicked)
        if fetch_button:
            st.session_state.fetch_articles_clicked = True
            print("button pressed")
            with st.spinner('Downloading the articles...'):
                list_of_all_articles = []
                get_content.import_data_from_TheGuardian(api_key, api_endpoint, start_date, end_date, folder_path)
                get_content.get_readable_articles(list_of_all_articles, folder_path, GuardianArticle, start_date, end_date)
            st.session_state.list_of_all_articles = list_of_all_articles
            st.success(f"Fetched {len(list_of_all_articles)} articles from {start_date} to {end_date}")
        if not list_of_all_articles:
            st.error("No articles fetched. Please fetch articles before proceeding.")
            return

    if list_of_all_articles:
        list_section_count = []
        quantitative_analyse.count_articles_per_section_per_day(list_of_all_articles, list_section_count)
        date_section_counts = visualisation.parse_data(list_section_count, start_date, end_date)
        days, sections, y_values, section_totals = visualisation.prepare_data_for_stackplot(date_section_counts)
        fig = visualisation.plot_stackplot_poo(days, sections, y_values, section_totals)
        st.subheader("Quantitative Analysis")
        st.pyplot(fig)

        tab1, tab2, tab3 = st.tabs(["Keyword Analysis","Sentiment Analysis","Word Mention"])
        with tab1:
            st.subheader("Keyword Analysis")
            sections_to_include = ["World news","US news","Football","Opinion","Australia news","Sport","UK news","Business","Music","Environment","Film","Society","Politics","Life and style","Books","Television & radio","Stage","Art and design","Food","Culture","Technology","Media","Science","Global development"]
            selected_section = st.selectbox("Select a section for Keyword Analysis:", options=sections_to_include)
            if st.button("Submit", key="keyword_analysis_button"):
                with st.spinner(f"Performing keyword analysis on the following section: **{selected_section}**"):
                    keywords = nlp_analysis.extract_keywords_from_section(list_of_all_articles, selected_section, 10)
                fig = visualisation.wordcloud_poo(keywords)
                st.pyplot(fig)
                fig = visualisation.plot_keywords_poo(keywords,selected_section,start_date, end_date,10)
                st.pyplot(fig)
            else:
                st.warning("Please select a section to start the analysis.")
        with tab2:
            st.subheader("Sentiment Analysis :smiley::neutral_face::anguished:")
            sections_to_include = ["World news", "US news", "Football", "Opinion", "Australia news", "Sport", "UK news",
                                   "Business", "Music", "Environment", "Film", "Society", "Politics", "Life and style",
                                   "Books", "Television & radio", "Stage", "Art and design", "Food", "Culture",
                                   "Technology", "Media", "Science", "Global development"]
            selected_section = st.selectbox("Select a section for Sentiment Analysis:", options=sections_to_include)
            if st.button("Submit", key="sentiment_analysis_button"):
                with st.spinner(f"Performing sentiment analysis on the following section: **{selected_section}**"):
                    sentiment_result = nlp_analysis.analyse_sentiment_by_section(list_of_all_articles,selected_section)
                    fig = visualisation.visualise_sentiment_pie_chart_poo(sentiment_result,selected_section)
                st.pyplot(fig)
        with tab3:
            st.subheader("Word Mention :mag:")
            st.markdown("Here, you can explore all articles that mention a specific word or term. This feature is particularly useful for identifying content related to a topic of interest.")
            word_to_find = st.text_input("Enter a word", max_chars=20, help="Please enter a word with only letter. No space and no special characters like !#$%&'()*+,-./:;<=>?@[]^_`{|}~")
            if st.button("Submit", key="find_word_articles_button"):
                with spinner(f"Finding articles with the mention of **{word_to_find}**"):
                    filtered_articles = nlp_analysis.find_articles_containing_a_word(list_of_all_articles, word_to_find)
                    df = pd.DataFrame(filtered_articles)
                if df.empty:
                    st.warning(f"No articles found containing the word '{word_to_find}'.")
                else:
                    st.success(f"Found {len(df)} articles containing the word '{word_to_find}'.")
                    st.table(df)


    if st.sidebar.button("Restart Program"):
        st.session_state.clear()
        st.rerun()

if __name__ == '__main__':
    main()
# charts/visualizations.py
import plotly.express as px
import pandas as pd

def top_authors_chart(author_counts, plot_theme):
    top_authors_df = author_counts.head(10).reset_index()
    top_authors_df.columns = ['Author', 'Book Count']

    fig = px.bar(
        top_authors_df,
        x='Author',
        y='Book Count',
        title='Top 10 Authors by Number of Bestseller Books',
        color='Author',
        text='Book Count',
        template=plot_theme,
        hover_data={'Author': True, 'Book Count': True}
    )
    fig.update_traces(textposition='outside')
    fig.update_layout(
        xaxis_title="Author",
        yaxis_title="No. of Books",
        showlegend=False,
        title_x=0.3
    )
    return fig

def avg_rating_by_genre_chart(df, avg_rating_by_genre, plot_theme):
    avg_rating_df = avg_rating_by_genre.reset_index()
    avg_rating_df.columns = ['Genre', 'Average Rating']

    # Merge avg price for hover
    avg_price_by_genre = df.groupby("Genre")["Price"].mean().reset_index()
    avg_price_by_genre.columns = ['Genre', 'Avg Price']
    avg_rating_df = avg_rating_df.merge(avg_price_by_genre, on='Genre')

    fig = px.bar(
        avg_rating_df,
        x='Genre',
        y='Average Rating',
        color='Genre',
        text='Average Rating',
        template=plot_theme,
        hover_data={
            'Genre': True,
            'Average Rating': ':.2f',
            'Avg Price': ':.2f'
        }
    )
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig.update_layout(
        xaxis_title="Genre",
        yaxis_title="Average Rating",
        showlegend=False,
        title_x=0.3
    )
    return fig
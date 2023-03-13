# IMDB_viz_python

Welcome everyone and thank you for visiting the `IMDB_Viz_python` project repository!

If you love great movies and need some help figuring out which one to watch next, then you've come to the right place as our app is exactly what you need!


To read more about our wonderful app, feel free to jump over to one of the sections below or continue scrolling down.

- [Motivation and Purpose](#motivation-and-purpose)
- [Dashboard Description](#dashboard-description)
- [Usage](#usage)
- [Installation](#installation)
- [Contributing](#contributing)
- [Description of the data](#description-of-the-data)
- [License](#license)


## Motivation and Purpose

Choosing a good movie to watch can be a struggle sometimes and there's almost nothing worse than realizing you just spent 2 hours sitting through a horrible movie that you didn't enjoy one bit. Our user-friendly and accessible dashboard aims to help movie enthusiasts avoid this problem by helping them discover and explore new movies based on their movie watching preferences. In addition, our dashboard uses a vast database of movies to provide users with information on ratings, runtimes, and movie numbers presented through engaging visuals based on various metrics they can select via an interactive and intuitive interface. Please check out [Proposal](https://github.com/UBC-MDS/IMDB_Viz_R/blob/main/reports/proposal.md) of our R version.

## Dashboard Description

Our dashboard contains a landing page that recommends 3 movies for users based on their preferences. Users can use drop-down lists on the left-side of the page to select multiple genres, and actors of interest, as well as sliders to indicate the minimum Gross Revenue, release year range, and runtime range they prefer. The thumbnail, title, and a short summary are shown for each of the 3 movies in the main panel of the page.

Our dashboard also contains 3 additional tabs each containing a reactive plot to help users visualize their movie preferences based on the same filters applied on the `Top 3 Movie Recommendation page`:

- `Ratings by Genre`: A boxplot that shows the distribution of IMDB ratings by selected genres
- `Runtimes by Genre`: A boxplot that shows the distribution of runtime by selected genres
- `Movies by Genre`: A bar chart that shows the number of movies by selected genres

The boxplots and bar chart are coloured by genres and will update as the user varies their selections via the drop-down lists and sliders on the left-side of the page.

This dashboard is aimed at providing users with an easy-to-use and efficient way to find and select the movies they'll love.

## Usage

## Installation


## Contributing

Interested in contributing? Check out the [contributing guidelines](https://github.com/louiewang820/IMDB_viz_python/blob/main/CONTRIBUTING.md). Please note that this project is released with a [Code of Conduct](https://github.com/louiewang820/IMDB_viz_python/blob/main/CODE_OF_CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## Description of the data

For the dashboard, we're sourcing the data from Kaggle, which is a well-known platform for data science and machine learning projects. It can be accessed [here](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows). The dataset contains 1000 observations of movie data with a compressive set of features. Some of the key features are the movie's title (Series_Title), the certificate issued (Certificate), release year (Released_Year), runtime (Runtime), genre (Genre), IMDB rating (IMDB_Rating), meta score (Meta_score), director (Director), star power (Star1, Star2, Star3, Star4), number of votes (No_of_votes), and box office earnings (Gross). The dataset also contains a summary of the movie (Overview) which allows the users to quickly understand if the story is something they would prefer or not.


## License

`IMDB_Viz_python` was created by Gaoxiang Wang. It is licensed under the terms of the MIT license.

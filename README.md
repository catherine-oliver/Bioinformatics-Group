# COVID-19 Vaccine Dashboard

## Purpose

The purpose of our COVID-19 dashboard is to help make information about the vaccine more publically available and easy to understand. As well, the dashboard will serve as a way to upload and save an image of your COVID-19 vaccine card for easy retrieval and back-up storage.

## Usage

In future releases, we plan to have our application hosted on a server, however it is running locally for now. To run the application, first clone the git repository:

```
git clone https://github.com/catherine-oliver/Bioinformatics-Group.git
```

Next, navigate into the bioi-group-project-front-end directory and run the following command:

```
npm run serve
```

Now the application can be accessed from the url **localhost:8080**

## Functionality
### General Information

The general information page contains a summary of what the COVID-19 vaccine is and how it generates immunity within our bodies. We have included data from peer-reviewed sources, as well as a video from Simple Explained (https://www.youtube.com/channel/UCnxrdFPXJMeHru_b4Q_vTPQ) which can help make sense of the scientific jargon surrounding the COVID-19 vaccine. Additionally, we have a section discussing the safety of the vaccine supported by peer-reviewed literature. 

### Vaccine Data Visualization

This section will be added in the future and will allow users to visualize current vaccine data from the United States.

### Vaccine Card Storage

This section will be added in the future and will allow users to create an account tied to their vaccine card. Once their accound has been created, the users can log in and view their vaccine card image.


## Release Notes
### 06/24/2020
- Updated README Documentation with description of application
- Created Vue project structure for front-end
- Configured Vue router and application landing page
- Created the General Information Page and populated it with data
- Created a Flask Project for future back-end API
- Configured mySQL database for future storage of vaccine card and vaccine data

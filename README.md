# BikeShare Data Analysis Project
---

## Project Details

Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

---

## The Datasets

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

- **Start Time** (e.g., 2017-01-01 00:07:57)
- **End Time** (e.g., 2017-01-01 00:20:53)
- **Trip Duration** (in seconds - e.g., 776)
- **Start Station** (e.g., Broadway & Barry Ave)
- **End Station** (e.g., Sedgwick St & North Ave)
- **User Type** (Subscriber or Customer)

The **Chicago** and **New York City** files also have the following two columns:

- **Gender**
- **Birth Year**

The original files are much larger and messier, and you don't need to download them, but they can be accessed here if you'd like to see them ([Chicago](https://www.example.com), [New York City](https://www.example.com), [Washington](https://www.example.com)). Some data wrangling has been performed to condense these files to the above core six columns.

---

## Statistics Computed

### Popular Times of Travel
- Most common month
- Most common day of week
- Most common hour of day

### Popular Stations and Trip
- Most common start station
- Most common end station
- Most common trip from start to end (i.e., most frequent combination of start station and end station)

### Trip Duration
- Total travel time
- Average travel time

### User Info
- Counts of each user type
- Counts of each gender (only available for NYC and Chicago)
- Earliest, most recent, most common year of birth (only available for NYC and Chicago)

---

## Software Needs

- **Python 3**, **NumPy**, and **pandas** installed using Anaconda.
- A text editor, like **Sublime** or **Atom**.
- A terminal application (**Terminal** on Mac and Linux or **Cygwin** on Windows).

---

## About the Project

This project explores BikeShare data from three different cities. It uses data from CSV files to compute statistics for these cities and takes user inputs to create an interactive experience.

---

## Built With

- **Python**
- **Pandas**
- **Numpy**
- **Pycharm** (IDE)

---

## Files Used

- `chicago.csv`
- `new_york_city.csv`
- `washington.csv`

---

## Credits

This project was completed as part of the **Udacity Programming for Data Science Nanodegree Program**.

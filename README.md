# Image-Web-Scraping-Python
This repo contains the materials for image scrapping from Google Image Search

## Setup
1. Git clone this project.
```
git clone https://github.com/evanyeohboonkhai/Image-Web-Scraping-Python.git
```

2.  Download Anaconda from this [site](https://www.anaconda.com/products/individual) which is a toolkit that equips you to work with thousands of open-source packages and libraries.

3. Create a conda environment that has all the required libraries installed and activate it
```
cd Image-Web-Scraping-Python
conda env create -f environment.yml
```
 
4. Activate the environment
![image](https://user-images.githubusercontent.com/59526258/148317050-5280fc4f-c653-4f83-945d-36b847c9e938.png)
 ```
 conda activate web_scrapping
 ```
## Usage  
1. Copy paste the command into terminal
```
python web_scrap.py
```
2. Key in the keyword that you would to search. Example:`test kit positive`
![image](https://user-images.githubusercontent.com/59526258/148317264-2874d060-7ca8-4e96-b06e-b79e8b141cff.png)

3. You scrapped image should be in `scrapped_img` folder. If the script successfully compute, it will shown as the image below: 
![image](https://user-images.githubusercontent.com/59526258/148317487-ac780809-2ea0-43f7-bcd1-4b9a0fcbff11.png)

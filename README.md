# **Database_Analysis**

database_analysis is a reporting tool that analyzes and prints out reports based on data in a news database. It is a Python program that uses psql to solve the problems.

database_analysis can answer the following three questions:  
  1) What are the most popular three articles of all time?  
  2) Who are the most popular article authors of all time?  
  3) On which days did more than 1% of requests lead to errors?

## **Setup**
Make sure you have both [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) installed. In addition, if you do not have a Mac or Linux operating system, install the [Git Bash](https://git-scm.com/downloads) terminal system.

In order to get the correct VM configuration, download and unzip [this](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) file. Put this file in the Downloads folder of your computer.

Finally, download the data ([newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)) and unzip the following file. Ensure that the data and the program (Esther_Database_Analysis.py) are in the vagrant directory and the terminal path is set to vagrant directory.

## **Running the program**
Once you have everything set up, you can run Vagrant with the following commands in the terminal.

```
$ cd Downloads/FSND-Virtual-Machine  
$ cd vagrant/  
$ vagrant up  
$ vagrant ssh  
```
Set up the news database by loading the site's data into your local database with the command.

```
psql -d news -f newsdata.sql
```
Finally, you can run the program by exiting psql (\q) and inputting the following command

```
python Esther_Database_Analysis.py
```

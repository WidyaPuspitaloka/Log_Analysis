# Log Analysis - FSND Project 3

This is the source code for the Log Analysis project, the third project of Full Stack Nanodegree Programme in Udacity. This project is made by Widya A. Puspitaloka.

This project was created to write a reporting tool that prints out reports based on the data provided in the large database (will not take any input from the user). The data is provided by Udacity. This reporting tool is a Python program using the psycopg2 module to connect to the database, use SQL queries to analyze the log data, and print out the answers to some questions. This project act as an internal reporting tool for a newspaper site that will use information from the database to discover what kind of articles the site's readers like. The database contains newspaper articles, as well as the web server log for the site.

The provided database includes three tables:

* The authors table includes information about the authors of articles.
* The articles table includes the articles themselves.
* The log table includes one entry for each time a user has accessed the site.

The project answered these following questions:

* Most popular three articles of all time.
* Most popular article authors of all time.
* Days on which more than 1% of requests lead to errors.

### Tools
You'll need database software (provided by a Linux virtual machine) and the data to analyze
1. Python 3
2. [Vagrant](https://www.vagrantup.com/downloads.html)
3. [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
4. [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), the SQL script file with all the data

### Setup
* Download and isntall Python 3 (if you have not already)
* Download and install [vagrant](https://www.vagrantup.com/downloads.html) (the link is provided by Udacity)
* Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) (the link is provided by Udacity)
* Clone or download, then unzip VM configuration, [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm ) provided by Udacity
* Download [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from the Udacity course page. Put this file into the `vagrant` directory, which is shared with your virtual machine.
* Clone or download [this `Log_Analysis` repository](https://github.com/WidyaPuspitaloka/Log_Analysis.git) into `vagrant` directory

### Usage
Starting virtual machine that will give you the PostgreSQL database and support software needed for this project
* From your terminal, go to a new directory containing the VM files
* Inside, you will find another directory called `vagrant`. Change directory to the `vagrant` directory
* Inside the vagrant subdirectory, run the command `vagrant up` to download the Linux operating system and install it
* Then, to log in to the installed Linux VM, run `vagrant ssh`
* Inside the VM, change directory to `/vagrant` and you can look around with `ls` command.

Loading the data
* To load the `newsdata.sql` data, cd into `vagrant` directory inside the VM and use the command `psql -d news -f newsdata.sql`
* Once you have the data loaded into your database, connect to your database using `psql -d news` and you can explore the tables using the `\dt` and `\d` table commands and `select` statements

Running the script
* Inside the `vagrant` directory in the VM, cd into `Log_Analysis-master`
* Run `$ python3 log_analysis.py` to execute the program and to see the result


### License
This project is released under the [MIT License](https://opensource.org/licenses/MIT)

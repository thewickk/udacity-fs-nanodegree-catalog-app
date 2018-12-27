# Udacity_FSND_Project_Two: Item Catalog App

### This is the Item Catalog Application Project from the Udacity Full Stack Web Developer Nanodegree Program
## Project overview:
* Develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

## Purpose of this project:
* Using the Python Flask framework, this application implements CRUD (create, read, write, and delete) operations to create a dynamic RESTful web application that additionally utilizes Googles API to integrate OAuth2 authentication.

## Software Requirements (These will all be automatically installed via the requirements.txt file in the start-up script)
* Python 3.7.1
* certifi==2018.11.29
* chardet==3.0.4
* Click==7.0
* dominate==2.3.5
* Flask==1.0.2
* Flask-Bootstrap==3.3.7.1
* httplib2==0.12.0
* idna==2.8
* itsdangerous==1.1.0
* Jinja2==2.10
* MarkupSafe==1.1.0
* oauth2client==4.1.3
* pyasn1==0.4.4
* pyasn1-modules==0.2.2
* requests==2.21.0
* rsa==4.0
* six==1.12.0
* SQLAlchemy==1.2.15
* urllib3==1.24.1
* visitor==0.1.3
* Werkzeug==0.14.1

## Instructions For Installing Vagrant Virtual Machine

**These instructions, and the Vagrant VM are courtesy of [Udacity.com](https://www.udacity.com) and their [Full Stack Web Developer Nanodegree Program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)**

* **Install VirtualBox:**
VirtualBox is the software that actually runs the virtual machine. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

* **Install Vagrant:**
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Install the version for your operating system.

**Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.**

* **Install the Vagrant VM:**
There are a couple of different ways you can download the VM configuration.

You can download and unzip this file: [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.

Alternately, you can use Github to fork and clone the repository [https://github.com/udacity/fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm).

Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with **cd**. Inside, you will find another directory called vagrant. Change directory to the vagrant directory:
```bash
cd /vagrant
```

## Instructions for starting the Virtual Machine, connecting to the database, and running the Python file

* **Start the virtual machine**
From your terminal, inside the vagrant subdirectory, run the command **vagrant up**. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

When vagrant up is finished running, you will get your shell prompt back. At this point, you can run **vagrant ssh** to log in to your newly installed Linux VM!

## **Important!** *Python 3.7.1 is required in order for this application to run*
### **Please follow these steps to automate the installation and configuration of the Python 3.7.1 environment and launch the application:**

## Step 1:
### Move into the catalog directory that contains the application
```bash
cd /vagrant/catalog/
```

## Step 2:
### Clone the git repository containing the project files:
```bash
git clone https://github.com/thewickk/Udacity_FSND_Project_Two.git
```

## Step 3:
### Move the project files into the current catalog directory and remove unneeded folders and files:
```bash
cp -R ./Udacity_FSND_Project_Two/* ./ && rm -rf Udacity_FSND_Project_Two && rm README.txt
```

## Step 2:
### Make the automated startup script executable:
```bash
chmod +x init.sh
```

## Step 3:
### Run the startup script to automate the Python 3.7.1 installation and launch the app on port 5000
**(Please note this startup script will take several minutes to complete)**
```bash
source init.sh
```

## You can now access the application via your web browser at
**http://localhost:5000/**


## To exit the vagrant environment and kill the running vagrant processes, exit out of the current vagrant terminal and terminate the vagrant environment:
```bash
exit
vagrant halt
```

# Notes and Troubleshooting:
* This app has been tested to work in Chrome and Firefox ONLY. This application could exhibit undesirable behaviors or possibly not work at all in other web browsers
* If you experience a blank screen after authenticating with your Google account and are not redirected to the home page, please delete your browsing history, quit out of your web browser application and relaunch. This should flush any stored credentials and allow a new Google log in to happen.

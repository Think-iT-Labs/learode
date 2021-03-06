# Learode: Learn by coding

Learode is a portmanteau made by the words Learn and Code, referring to the goal of the project: The user will receive a reading list made by resources about the languages used in his Github contributions.

## Getting Started
### Prerequisites
 - Nginx
 - MongoDB v3.4.3
 - Python 3.6
 - Python modules
	 - requests==2.13.0
	 - pymongo==3.5.1
	 - eve==0.7.4
	 - flask==0.12
	 - github-flask==3.1.7
	 - flask_cors==3.0.3
 - ReactJS dependencies: 
	 - axios: ^ 0.16.2 
	 - postcss: ^ 6.0.12
	 - postcss-cssnext: ^ 3.0.2
	 - query-string: ^ 5.0.1
	 - react: ^ 15.6.1
	 - react-dom: ^ 15.6.1
	 - react-form: ^ 2.1.5
    	 - react-modal-bootstrap: ^ 1.1.1
	 - react-toolbox: ^ 2.0.0-beta.12
	 - style-loader: ^ 0.18.2
	 - webpack: ^ 3.6.0
	 - webpack-dev-server: ^ 2.8.2
 - ReactJS dev dependencies:
	 - css-loader:^ 0.28.7 
	 - node-sass: ^ 4.5.3 
	 - postcss-load-config: ^ 1.2.0
	 - postcss-loader: ^ 2.0.6
	 - sass-loader: ^ 6.0.6
	 - webpack: ^ 3.6.0

### Preparing the database

    $ sudo service mongod start
    $ python3.6 /API/prepare_database.py 

### Running

    $ python3.6 /API/run.py
    $ cd /ReactUI
    $ npm start

### Using Learode dev version

**Deprecated**

 1. Connect to the host and port of ReactJS (default is localhost:8080)
 2. Enter the username in the textfield in the navbar
 3. Click on "Go"
 4. Wait for the "Success" print in the API console
 5. Reload the page and re-enter your username
 6. Click on Go for the result

PS: You need 2 scans at least to have access to the past reading list display option available in the navbar.

## Built With

* [ReactJS](https://facebook.github.io/react/)
* [Python](https://www.python.org/)
* [Eve](http://python-eve.org/)

## Authors

* **Ghaith Limam** - *Initial work* - [SynergySINE](https://github.com/SynergySINE)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Tip of the hat to the Think.iT team



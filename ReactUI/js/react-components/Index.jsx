import React from 'react';
import axios from 'axios';
import App from './App.jsx';
import queryString from 'query-string';


const urlForLogin = `http://localhost:5000/login`
const urlForCheck = `http://localhost:5000/check/`


class Index extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            connected: false,
            username: ''
        }
    }
    componentWillMount() {
        this.setState({
            username: queryString.parse(location.search)['login']
        })

        if (username != '') {
            this.setState({
                connected: verifyToken(this.state.username)
            })
        }
    }

    verifyToken(username) {
        axios.get(urlForCheck + username)
            .then(function(response) {
                console.log(response);
                if (response['response'] == 200) {
                    return true
                }
                else {
                    return false
                }
            })
            .catch(function(error) {
                console.log(error);
            });
    }

    render() {

        return (
            <div>
            {this.state.connected ? <App username={this.state.username}></App> :
                <div className="container">
	                <div className="row">
		                <form className="form-signin mg-btm">
                    	<h3 className="heading-desc">
		                Login to Learode</h3>
		                <div className="social-box">
			                <div className="row mg-btm">
                             <div className="col-md-12">
                                <a href={urlForLogin} className="btn btn-primary btn-block">
                                  <i className="icon-github"></i>    Login with Github
                                </a>
			                </div>
			                </div>
			
		                </div>

                      </form>
	                </div>
                </div>
            }
            </div>
        );
    }
}

export default Index;

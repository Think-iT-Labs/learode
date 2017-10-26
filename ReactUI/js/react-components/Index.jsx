import React from 'react';
import axios from 'axios';
import App from './App.jsx';
import queryString from 'query-string';


const urlForLogin = `http://localhost:5000/login`
var urlForCheck = user => `http://localhost:5000/check/${user}`


class Index extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            connected: false,
            username: ''
        }
        this.verifyToken = this.verifyToken.bind(this)
    }


    verifyToken(user) {
        axios.get(urlForCheck(user))
            .then((response) => {
                if (response['data']['response'] == 200) {
                    this.setState({
                        username: user,
                        connected: true
                    }, function() {
                        console.log(this.state.connected);
                        console.log(this.state.username);
                    });
                    return true
                } else {
                    return false
                }
            })
            .catch(function(error) {
                console.log(error);
            });
    }

    componentWillMount() {
        var user = queryString.parse(location.search)['login'];
        this.verifyToken(user)
    }

    render() {

        return (
            <div>
                {this.state.connected ?
                <App username={this.state.username}></App> :
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

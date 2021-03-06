import React from 'react';
import axios from 'axios';
import App from './App.jsx';

import queryString from 'query-string';


const urlForLogin = `/api/login`
var urlForCheck = user => `/api/check/${user}`


class Index extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            connected: false,
            username: '',
            loading: false,
            loginbox:true
        }
        this.verifyToken = this.verifyToken.bind(this)
    }


    verifyToken(user) {
        this.setState({
            loading:true,
            loginbox:false
        })
        axios.get(urlForCheck(user))
            .then((response) => {
                if (response['data']['response'] == 200) {
                    this.setState({
                        username: user,
                        connected: true,
                        loading: false
                    }, function() {
                        console.log("connected");
                    });
                    return true
                } else {
                    this.setState({
                        loading:false,
                        loginbox:true
                    })
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
            <nav className="navbar navbar-expand-lg navbar-dark bg-navbar fixed-top">
            <div className="container">
                <a className="navbar-brand super-text animated fadeIn" href="#">Learode: Learn by Coding !</a>
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon"></span>
            </button>

            </div>
            </nav>
            <div className="container">
            {this.state.connected ?
                <App username={this.state.username}></App> : ''}
            {this.state.loginbox ?
                <div className="container animated fadeInRight">
                    <div className="row">
                        <form className="form-signin mg-btm">
                            <h3 className="heading-desc text-center">
                                Login to Learode</h3>
                            <div className="social-box">
                                <p className="text-center">Learode would need your authorization to check your repos (both private and public !) to see what language you've been using.</p>
                                <p className="text-center">Click away!</p>
                                <div className="row mg-btm">
                                    <div className="col-md-12">
                                        <a href={urlForLogin} className="btn btn-primary btn-block btn-github">
                                              <img src="../../pics/git.png" height="42" width="42"/> Login with Github
                                            </a>
                                    </div>
                                </div>
                            </div>
                        </form>
                    </div>
                </div> : '' }
            {this.state.loading ?
            <div className="loader-container">
		<div className="loader"></div>
	    </div> : ''}
            </div>
            <footer className="py-5 bg-footer footer">
            <div className="container">
                <p className="m-0 text-center copyright-text">Copyright &copy; Learode 2017</p>
            </div>
            </footer>
        </div>
        );
    }
}

export default Index;

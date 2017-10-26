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
            <nav className="navbar navbar-expand-lg navbar-dark bg-learode fixed-top">
            <div className="container">
                <a className="navbar-brand" href="#">Learode: Learn by Coding !</a>
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon"></span>
            </button>
                <div className="collapse navbar-collapse" id="navbarResponsive">

                </div>
            </div>
            </nav>
            <div className="container">
            <h1>H</h1>
            <h2>h</h2>
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
                                        <a href={urlForLogin} className="btn btn-primary btn-block btn-github">
                                              <img src="../../pics/git.png" height="42" width="42"/> Login with Github
                                            </a>
                                    </div>
                                </div>

                            </div>

                        </form>
                    </div>
                </div>
                }
            </div>
            <footer className="py-5 bg-learode footer">
            <div className="container">
                <p className="m-0 text-center text-black">Copyright &copy; Learode 2017</p>
            </div>
            </footer>
        </div>
        );
    }
}

export default Index;

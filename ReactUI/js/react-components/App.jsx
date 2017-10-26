import React from 'react';
import axios from 'axios';
import Learode from './learode.jsx';
//import DrawerTest from './drawer.jsx'; TODO: Drawer feature 

class App extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            username: this.props.username,
            operation: "new",
            oppositelistname: "last reading list",
            fetched: true
        }
    }


    switchMode() {
        if (this.state.operation == "new") {
            this.setState({
                operation: "last",
                oppositelistname: "new reading list",
                fetched: true
            })


        } else if (this.state.operation == "last") {
            this.setState({
                operation: "new",
                oppositelistname: "last reading list",
                fetched: true
            })
        }
    }

    
    /*fetchUsername(un) {
        this.setState({
            username: this.refs.un.value,
            fetched: true
        });
    }*/


    manualGitScan() {
        axios.get('http://127.0.0.1:5000/scan/' + this.state.username)
            .then(function(response) {
                console.log(response);
            })
            .catch(function(error) {
                console.log(error);
            });
    }


    renderContent() {
        if (this.state.fetched == true) {
            this.state.fetched = false
            return true
        } else {
            return false
        }
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
                <ul className="navbar-nav ml-auto">
                    <li className="nav-item">
                        <a className="nav-link" href="#" onClick={()=> this.switchMode()}>Switch to {this.state.oppositelistname}</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="#" onClick={()=> this.manualGitScan()}>Rescan Github</a>
                    </li>
                </ul>
                </div>
            </div>
            </nav>
            <div className="container">
            <h1>H</h1>
            <h2>h</h2>
            {this.renderContent() ?
            <div className='app'>
                <Learode operation={this.state.operation} username={this.state.username}></Learode>
            </div>: ""}
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

export default App;

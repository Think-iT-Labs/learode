import React from 'react';
import axios from 'axios';
import {
  Modal,
  ModalHeader,
  ModalTitle,
  ModalClose,
  ModalBody,
  ModalFooter
} from 'react-modal-bootstrap';

import Learode from './learode.jsx';
import AddResourceForm from './add_resource_form.jsx';


var urlForScan = user => `/api/scan/${user}`
var urlForLogout = user => `/api/logout/${user}`

class App extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            username: this.props.username,
            operation: "new",
            oppositelistname: "last reading list",
            fetched: true,
            isOpen: false,
            isSubOpen: false,
	        allow: true
        }
        this.openModal = this.openModal.bind(this)
        this.hideModal = this.hideModal.bind(this);
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

    manualGitScan() {
	this.setState({
		allow: false
	})
        axios.get(urlForScan(this.state.username))
            .then(response => {
                this.setState({
			fetched:true,
			allow: true
		})
            })
            .catch(function(error) {
                console.log(error);
            });
    }

    logout(){
        axios.get(urlForLogout(this.state.username))
            .then((response) => {
                this.setState({
                        username: '',
                        connected: false,
                        allow: false
                    });
            })
            .catch(function(error) {
                console.log(error);
            })
    }

  openModal(){
    this.setState({
      isOpen: true
    });
  }

  hideModal(){
    this.setState({
      isOpen: false,
      fetched: true
    });
  }

    renderContent() {
        if (this.state.fetched == true && this.state.allow == true) {
            this.state.fetched = false
            return true
        } else {
            return false
        }
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
                <div className="collapse navbar-collapse" id="navbarResponsive">
                <ul className="navbar-nav ml-auto">
                    <li className="nav-item">
                        <a className="nav-link" href="#" onClick={()=> this.openModal()}>Add new resource</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="#" onClick={()=> this.switchMode()}>Switch to {this.state.oppositelistname}</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="#" onClick={()=> this.manualGitScan()}>Rescan Github</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="#" onClick={()=> this.logout()}>Log out</a>
                    </li>
                </ul>
                </div>
            </div>
            </nav>
            <div className="container">

            <h1>H</h1>
            <h2>h</h2>

            <Modal isOpen={this.state.isOpen} size='modal-lg' onRequestHide={this.hideModal}>
              <ModalHeader>
                <ModalClose onClick={this.hideModal}/>
                <ModalTitle>Add new resource</ModalTitle>
              </ModalHeader>
              <ModalBody>

              <AddResourceForm username={this.state.username}/>

              </ModalBody>
              <ModalFooter>
                <button className='btn btn-default' onClick={this.hideModal}>
                  Close
                </button>
              </ModalFooter>
            </Modal>
            {this.renderContent() ?
            <div className='app'>
                <Learode operation={this.state.operation} username={this.state.username}></Learode>
            </div> : <div className="loader-container">
		<div className="loader"></div>
	    </div>}
            
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

export default App;

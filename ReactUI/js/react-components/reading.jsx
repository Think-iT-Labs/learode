import React, { Component } from 'react';
import axios from 'axios';

const urlForResource = resource =>
    `/api/resource/read/${resource}`

class Reading extends Component {
    constructor(props) {
        super(props)
        this.setRead = this.setRead.bind(this)
        this.checkRead = this.checkRead.bind(this)
    }

    setRead(){ 
        let data = {
            "read_by": this.props.username
        }
        axios.post(urlForResource(this.props.item.res_id), data)
        .then(response => console.log(response))
        .catch(error => console.log(error))

    }

    checkRead(){
        for(var i = 0; i < this.props.item.read_by.length; i++) {
            if(this.props.item.read_by[i] == this.props.username)
                return true;
        }
        return false;
    }

    render() {
        return (
    <div>
        {this.checkRead() == false ?
        <div className="row animated fadeInRight">
        <div className="col-lg-12 portfolio-item">
            <div className="card-learode">
                <div className="card-image-frame">
                    <span className="card-helper"></span><img className="card-image" src={"pics/"+this.props.item.language+".png"} alt="" />
                </div>
                <div className="card-body">
                    <h4 className="card-title">
                        <a href="#">{this.props.item.title}</a>
                    </h4>
                    <p className="card-text">Language: {this.props.item.language}</p>
                <p className="card-text">Difficulty level: {this.props.item.level}</p>
                    <p className="card-text">URL: <a href={this.props.item.url}>Click here</a></p>
                </div>
		<div className="col-lg-3 portfolio-item card-read">
		    <a href='#' className="btn btn-primary btn-success" onClick={this.setRead}><img src="../../pics/tick.gif" height="20" width="20"></img> Read</a>
		</div>
            </div>
        </div>
        </div> : ''}
    </div>
        )
    }
};

export default Reading;

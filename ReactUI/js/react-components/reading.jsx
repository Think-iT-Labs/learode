import React, { Component } from 'react';
import Link from 'react-toolbox/lib/link';

class Reading extends Component {
    constructor(props) {
        super(props)
    }



    render() {
        return (
    <div>
        <div className="row">
        <div className="col-lg-12 portfolio-item">
            <div className="card-learode">
                <a href="#"><img className="card-img-learode" src={"pics/"+this.props.item.language+".png"} alt="" /></a>
                <div className="card-body">
                    <h4 className="card-title">
                        <a href="#">{this.props.item.title}</a>
                    </h4>
                    <p className="card-text">Language: {this.props.item.language}</p>
                <p className="card-text">Difficulty level: {this.props.item.level}</p>
                    <p className="card-text">URL: <a href={this.props.item.url}>Click here</a></p>
                </div>
		<div className="col-lg-3 portfolio-item card-read">
		    <a href="#" className="btn btn-primary btn-success"><img src="../../pics/tick.gif" height="20" width="20"></img> Read</a>
		</div>
            </div>
        </div>
        </div>
    </div>
        )
    }
};

export default Reading;

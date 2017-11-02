import React, {Component} from 'react';
import Reading from './reading.jsx';

var urlForUsername = username =>
    `/api/user/${username}`

class Learode extends Component {

    constructor(props) {
        super(props)
        this.state = {
            requestFailed: false,
            learodeData: false
        }
        this.getIndex = this.getIndex.bind(this)
    }

    getIndex(value, arr, prop) {
        for(var i = 0; i < arr.length; i++) {
            if(arr[i] === value) {
                return i;
            }
        }
        return -1; 
    }

    componentDidMount() {
        fetch(urlForUsername(this.props.username))
            .then(response => {
                if (!response.ok) {
                    throw Error("Network request failed")
                }
                return response
            })
            .then(d => d.json())
            .then(d => {
                this.setState({
                    learodeData: d
                })
            }, () => {
                this.setState({
                    requestFailed: true
                })
            })
    }


    render() {
        if (this.state.requestFailed) return <p>Failed!</p>
        if (!this.state.learodeData) return <p>Loading...</p>
        let renderedItems = []
        if (this.props.operation == "new") {
            this.state.learodeData.new_reading_list.map(item => {
                renderedItems.push(
                    <Reading item={item} username={this.props.username}></Reading>
                )
            })
        } else if (this.props.operation == "last") {
            this.state.learodeData.last_reading_list.map(item => {
                renderedItems.push(
                    <Reading item={item} username={this.props.username}></Reading>
                )
            })
        };
        return (
            <div> {renderedItems} </div>
        )
    }
}

export default Learode;

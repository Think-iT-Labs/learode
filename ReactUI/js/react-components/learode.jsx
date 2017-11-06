import React, {Component} from 'react';
import axios from 'axios';
import Reading from './reading.jsx';

var urlForUsername = username =>
    `/api/user/${username}`

class Learode extends Component {

    constructor(props) {
        super(props)
        this.state = {
            requestFailed: false,
            learodeData: null
        }
        this.getIndex = this.getIndex.bind(this)
        this.componentWillMount = this.componentWillMount.bind(this)
    }

    getIndex(value, arr, prop) {
        for(var i = 0; i < arr.length; i++) {
            if(arr[i] === value) {
                return i;
            }
        }
        return -1; 
    }

    componentWillMount() {
        axios.get(urlForUsername(this.props.username), {'headers':{'accept':'application/json'}})
        .then(response =>
            this.setState({
                learodeData: response['data']
            })
        )
        .catch(error =>
            this.setState({
                requestFailed: true
            })
        )
    }


    render() {
        if (this.state.requestFailed) return <p>Failed!</p>
        if (!this.state.learodeData) return <p>Loading...</p>
        let renderedItems = []
        console.log(this.state.learodeData)
        if (this.props.operation == "new") {
            this.state.learodeData.new_reading_list.map(item => {
            if (this.getIndex(this.props.username, item.read_by) == -1) {
                renderedItems.push(
                    <Reading item={item} username={this.props.username}></Reading>
                )}
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

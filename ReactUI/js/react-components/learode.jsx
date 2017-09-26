import React, {Component} from 'react';
import Reading from './reading.jsx';

const urlForUsername = username =>
	`http://127.0.0.1:5000/user/${username}`

class Learode extends Component {

	constructor(props) {
		super(props)
		this.state = {
			requestFailed: false,
			learodeData: false
		}
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
			this.state.learodeData.new_reading_list.map(function(item) {
				renderedItems.push(
					<Reading item={item}></Reading>
				)
			})
		} else if (this.props.operation == "last") {
			this.state.learodeData.last_reading_list.map(function(item) {
				renderedItems.push(
					<Reading item={item}></Reading>
				)
			})
		};
		console.log(renderedItems[1])
		return (
			<div> {renderedItems} </div>
		)
	}
}

export default Learode;

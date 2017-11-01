import React from 'react';
import axios from 'axios';

const urlForResource = `http://127.0.0.1:5000/resource`
const urlForSeq = `http://127.0.0.1:5000/seq`

class AddResourceForm extends React.Component {

    constructor( props ) {
      super( props );
      this.state = {};
      this.updateState = this.updateState.bind(this);
      this.submitForm = this.submitForm.bind(this);
    }

    updateState(e) {
      name = e.target.name
      console.log(name)
      this.setState({[e.target.name]: e.target.value}, 
      console.log(this.state));
    }

    submitForm(){
        let data = {}
        this.forceUpdate()
        axios.get(urlForSeq)
        .then(response => (
            data = {
                "res_id": response['data']['seq'],
                "title": this.state.title,
                "url": this.state.url,
                "language": this.state.language,
                "level":this.state.level
            },
            console.log(data),
            axios.post(urlForResource, data)
            .then(response => console.log(response))
            .catch(errors => console.log(errors))
        ))
        .catch(errors => console.log(errors));
    }

    render() {
      return (
        <div>
         <form className="form-basic" onSubmit={this.submitForm}>

            <div className="form-title-row">
                <h1>Add new resource</h1>
            </div>
            <div className="form-row">
                <label>
                    <span>Title</span>
                    <input type="text" name="title" onChange = {this.updateState}/>
                </label>
            </div>

            <div className="form-row">
                <label>
                    <span>Programming Language</span>
                    <input type="text" name="language" onChange = {this.updateState}/>
                </label>
            </div>

            <div className="form-row">
                <label>
                    <span>URL</span>
                    <input type="text" name="url" onChange = {this.updateState}/>
                </label>
            </div>


            <div className="form-row">
                <label><span>Level</span></label>
                <div className="form-radio-buttons">

                    <div>
                        <label>
                            <input type="radio" name="skill" value="beginner" onChange = {this.updateState}/>
                            <span>Beginner</span>
                        </label>
                    </div>

                    <div>
                        <label>
                            <input type="radio" name="skill" value="intermediate" onChange = {this.updateState} />
                            <span>Intermediate</span>
                        </label>
                    </div>

                    <div>
                        <label>
                            <input type="radio" name="skill" value="advanced" onChange = {this.updateState}/>
                            <span>Advanced</span>
                        </label>
                    </div>

                </div>
            </div>

            <div className="form-row">
                <button type="submit">Submit</button>
            </div>

        </form>
        </div>
      );
    }
  }

export default AddResourceForm;

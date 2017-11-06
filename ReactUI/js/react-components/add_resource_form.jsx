import React from 'react';
import axios from 'axios';

const urlForResource = `/api/resource`
const urlForSeq = `/api/seq`

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
        axios.get(urlForSeq)
        .then(response => (
            data = {
                "res_id": response['data']['seq'],
                "title": this.state.title,
                "url": this.state.url,
                "language": this.state.language,
                "level": this.state.level,
		"read_by":[],
		"created_by": this.props.username
            },
            axios.post(urlForResource, data, {headers:{"Content-Type":"application/json"}})
            .then(response => console.log(response),console.log(data))
            .catch(errors => console.log(errors))
        ))
        .catch(errors => console.log(errors));
    }

    render() {
      return (
        <div>
         <form className="form-basic" onSubmit={this.submitForm}>

            <div className="form-row">
                <label>
                    <span>Title</span>
                    <input type="text" name="title" onChange = {this.updateState}/>
                </label>
            </div>

            <div className="form-row">
                <label>
                    <span>Programming Language</span>
                    <select onChange = {this.updateState}>
		                <option value="csharp">C#</option>
                        <option value="c">C</option>
                        <option value="c++">C++</option>
                        <option value="perl">Perl</option>
		                <option value="ruby">Ruby</option>
                        <option value="python">Python</option>
                        <option value="javascript">Javascript</option>
                        <option value="html">HTML</option>
		                <option value="css">CSS</option>
                    </select>
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
                            <input type="radio" name="level" value="beginner" onChange = {this.updateState}/>
                            <span>Beginner</span>
                        </label>
                    </div>

                    <div>
                        <label>
                            <input type="radio" name="level" value="intermediate" onChange = {this.updateState} />
                            <span>Intermediate</span>
                        </label>
                    </div>

                    <div>
                        <label>
                            <input type="radio" name="level" value="advanced" onChange = {this.updateState}/>
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

//WIP: Drawer feature still not implemented

import React from 'react';
import Button from 'react-toolbox/lib/button';
import Drawer from 'react-toolbox/lib/drawer';
import Input from 'react-toolbox/lib/input';
import Checkbox from 'react-toolbox/lib/checkbox';
import { RadioGroup, RadioButton } from 'react-toolbox/lib/radio';

class DrawerTest extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            active:false
        }
    }

  handleToggle() {
    this.setState({active: !this.state.active});
  };
  handleChange()
	{
	
}
  render () {
    return (
      <div>
        <Button label='Show Drawer' raised accent onClick={() => this.handleToggle()} />
        <Drawer active={this.state.active} onOverlayClick={() => this.handleToggle()}>
          <h1>This is your Drawer.</h1>
          <h2>This is your drawer. </h2>	
	<Input type='text' label='Github Username' name='gitusername' value={this.state.name}  maxLength={16 } /> 
	  <div>
	<p>Python:</p>
	<RadioGroup name='pythonlevel' value={this.state.value} onChange={() => this.handleChange}>
        <RadioButton label='Beginner' value='beginner'/>
        <RadioButton label='Intermediate' value='intermediate'/>
        <RadioButton label='Expert' value='expert'/>
	</RadioGroup>
	<p>Javascript:</p>
	<RadioGroup name='jslevel' value={this.state.value} onChange={() => this.handleChange}>
        <RadioButton label='Beginner' value='beginner'/>
        <RadioButton label='Intermediate' value='intermediate'/>
        <RadioButton label='Expert' value='expert'/>
	</RadioGroup>
	<p>HTML:</p>
	<RadioGroup name='htmllevel' value={this.state.value} onChange={() => this.handleChange}>
        <RadioButton label='Beginner' value='beginner'/>
        <RadioButton label='Intermediate' value='intermediate'/>
        <RadioButton label='Expert' value='expert'/>
	</RadioGroup>	
	
</div>
        </Drawer>
      </div>
    );
  }
}

export default DrawerTest;

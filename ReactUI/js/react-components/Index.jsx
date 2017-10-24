import React from 'react';
import App from './App.jsx';

class Index extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            connected: false,
            username: '',
            client_id: 'a2dfecffbb39b5f749fb'
        }
    }

    //OAuthLogin() {}

    render() {
        return (
            <div>
            {this.state.connected ? <App></App> :
                <html>
                  <head>
                  </head>
                  <body>
                    <p>
                      We're going to now talk to the GitHub API. Ready?
                      <br/>
                      <a className="btn-auth btn-github large" href={'https://github.com/login/oauth/authorize?scope=user:email,repo&client_id=' + this.state.client_id}>Click here to begin!</a>
                    </p>
                  </body>
                </html>
            }
            </div>
        );
    }
}

export default Index;

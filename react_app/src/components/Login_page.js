import React from 'react';
import {Alert} from 'react-bootstrap'

import image1 from './image_user_1.png'

import Login_page_1 from "./Login_page_1.js";
import Login_page_2 from "./Login_page_2.js";

class Login_page extends React.Component {

  render() {
  	return(
    	<div className="App">


            <Alert variant={"primary"}>
                <h1> Messagerie </h1>
            </Alert>

    		<div class="login-page-images-aligner-1">
	    		<img alt="jsp" src={image1} class="image-user-1" />
    			<div class="login-page-images-aligner-2">
		    		<h2> Se connecter </h2>
		    	</div>
	    	</div>
	    	<Login_page_1 />
    		<div class="login-page-images-aligner-1">
	    		<img alt="jsp" src={image1} class="image-user-2" />
    			<div class="login-page-images-aligner-2">
	    			<h2> S'inscrire </h2>
	    		</div>
	    	</div>
    		<Login_page_2 />
    	</div>
    	)
    }
}

export default Login_page;





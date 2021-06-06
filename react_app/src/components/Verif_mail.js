import React from 'react';
import {Redirect} from 'react-router-dom';

import image1 from './image_logoff_1.png'
import image2 from './fleche_retour_1.png'

import {Alert,Button,Navbar,Nav,Form} from 'react-bootstrap'

import Verif_mail_1 from "./Verif_mail_1.js";
import Verif_mail_2 from "./Verif_mail_2.js";

class Verif_mail extends React.Component {
    constructor(){
        super()
        this.state = {
            rediriger_acceuil:false
        }
    }

    retourAcceuilHandler = (e) => {
        e.preventDefault()
        console.log("nique")
        this.setState({rediriger_acceuil:true})
    }

  render() {
    const {rediriger_acceuil} = this.state
    if (rediriger_acceuil === true) {
        if (localStorage.getItem("logged") === "true"){ return <Redirect to="/page_principale" /> }
        else { return <Redirect to="/" /> }
    }
  	return(
    	<div className="App">
            <>
              <Navbar bg="dark" variant="dark">
                <Nav className="mr-auto">
                    <Button variant="outline-dark" onClick={this.retourAcceuilHandler}> <img alt="jsp" src={image2} class="image-log-off" /> </Button>   
                </Nav>
                <Form inline>
                  <Button variant="outline-info" onClick={this.deconnectionHandler}> <img alt="jsp" src={image1} class="image-log-off" /> </Button>                  
                </Form>
              </Navbar>
            </>

            <Alert variant={"primary"}>
                <h1> Gérer la vérification de son adresse mail </h1>
            </Alert>



            <Alert variant={"info"}>
                <h2> Envoyer un nouvel email de confirmation </h2>
            </Alert>

            <Verif_mail_1/>


            <Alert variant={"info"}>
                <h2> Vérifier son adresse mail </h2>
            </Alert>
    		
            <Verif_mail_2 />

    	</div>
    	)
    }
}

export default Verif_mail;





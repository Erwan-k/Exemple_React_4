import React from 'react';
import {Redirect} from 'react-router-dom';

import image1 from './image_logoff_1.png'
import image2 from './fleche_retour_1.png'

import {Alert,Button,Navbar,Nav,Form} from 'react-bootstrap'

import Gestion_mdp_1 from "./Gestion_mdp_1.js";
import Gestion_mdp_2 from "./Gestion_mdp_2.js";
import Gestion_mdp_3 from "./Gestion_mdp_3.js";

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
                <h1> Gérer la modification de son mot de passe </h1>
            </Alert>

            <Alert variant={"info"}>
                <h2> Demander un code pour modifier son mot de passe </h2>
            </Alert>

            <Gestion_mdp_1/>


            <Alert variant={"info"}>
                <h2> Changer son mot de passe à l'aide d'un code </h2>
            </Alert>
    		
            <Gestion_mdp_2 />

            <Alert variant={"info"}>
                <h2> Changer son mot de passe à l'aide du mot de passe actuel </h2>
            </Alert>
            
            <Gestion_mdp_3 />
            


    	</div>
    	)
    }
}

export default Verif_mail;





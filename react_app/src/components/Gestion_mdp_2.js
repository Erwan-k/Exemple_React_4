import React from 'react';
import axios from 'axios';

import {Button, Form, Col, Row} from 'react-bootstrap'

class Gestion_mdp_2 extends React.Component {
	constructor(){
		super()
		this.state = {
			adresse_mail:"",
			code:"",
			nouveau_mdp:"",
			message_retour_api:""
		}
	}

	changeHandler = (e) => {
		this.setState({[e.target.name]: e.target.value})
	}

	submitHandler = (e) => {
		e.preventDefault()
        axios.post('http://127.0.0.1:1201/connexion5',{adresse_mail:this.state.adresse_mail,code:this.state.code,nouveau_mdp:this.state.nouveau_mdp})
            .then(response => {
                if(response.status === 200){
                    this.setState({"message_retour_api":response.data.retour})
                    if (response.data.retour === "ok"){
                        this.setState({"adresse_mail":""})
                        this.setState({"code":""})
                        this.setState({"nouveau_mdp":""})
                                                      }
                                           }
                              }
                  ).catch(error => {console.log(error)})
	}



	render(){
		const {adresse_mail,code,nouveau_mdp,message_retour_api} = this.state
	  	return(
	    	<div class="bloc-changer-mdp-avec-actuel">
		    	<div class="bloc-changer-mdp-avec-actuel-2">

		            <Form onSubmit={this.submitHandler}>
		              
		              <Form.Group as={Row} controlId="formHorizontalEmail">
		                <Form.Label column sm={2}>
		                  Email
		                </Form.Label>
		                <Col sm={10}>
		                  <Form.Control type="email" placeholder="Email" name="adresse_mail"  value={adresse_mail} onChange={this.changeHandler}/>
		                </Col>
		              </Form.Group>
		              
		              <Form.Group as={Row} controlId="formHorizontalEmail">
		                <Form.Label column sm={2}>
		                  Code
		                </Form.Label>
		                <Col sm={10}>
		                  <Form.Control type="text" placeholder="Mot de passe actuel" name="code"  value={code} onChange={this.changeHandler}/>
		                </Col>
		              </Form.Group>
		              
		              <Form.Group as={Row} controlId="formHorizontalEmail">
		                <Form.Label column sm={2}>
		                  Nouveau mot de passe
		                </Form.Label>
		                <Col sm={10}>
		                  <Form.Control type="text" placeholder="Nouveau mot de passe" name="nouveau_mdp"  value={nouveau_mdp} onChange={this.changeHandler}/>
		                </Col>
		              </Form.Group>

		              <Form.Group as={Row}>
		                <Col sm={{ span: 10, offset: 2 }}>
		                  <Button type="submit">Changer son mot de passe</Button>
		                </Col>
		              </Form.Group>
		            
		            </Form>

	    		{message_retour_api}

	    		</div>
	    	</div>
	    	)
    }
}

export default Gestion_mdp_2;